#!/bin/bash
# https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
# https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#without-internet-connection

TOOLS_DOWNLOAD_DIR=/opt/k8s-tools
DEP_DOWNLOAD_DIR=/opt/k8s-dependencies
IMG_DOWNLOAD_DIR=/opt/k8s-images
export PATH=${TOOLS_DOWNLOAD_DIR}:${PATH}
# Make sure that the br_netfilter module is loaded
lsmod | grep br_netfilter || bash -c "echo br_netfilter | tee /etc/modules-load.d/k8s.conf"
lsmod | grep overlay || bash -c "echo overlay | tee /etc/modules-load.d/containerd.conf"


modprobe overlay
modprobe br_netfilter

# Download dependencies
mkdir -p ${DEP_DOWNLOAD_DIR}
pushd ${DEP_DOWNLOAD_DIR}
curl -LO http://mirrors.kernel.org/ubuntu/pool/main/libs/libseccomp/libseccomp2_2.5.1-1ubuntu1~20.04.1_amd64.deb
# dpkg -i libseccomp2*
popd

# Download tools
mkdir -p ${TOOLS_DOWNLOAD_DIR}
pushd ${TOOLS_DOWNLOAD_DIR}
RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
ARCH="amd64"
curl -L --remote-name-all https://storage.googleapis.com/kubernetes-release/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet,kubectl}
chmod +x {kubeadm,kubelet,kubectl}

RELEASE_VERSION="v0.4.0"
curl -sSLO "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubelet/lib/systemd/system/kubelet.service" 
#| sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | tee /etc/systemd/system/kubelet.service
#mkdir -p /etc/systemd/system/kubelet.service.d
curl -sSLO "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubeadm/10-kubeadm.conf" 
#| sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | tee /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

# Download containerd
# https://github.com/containerd/containerd/blob/main/docs/cri/installation.md
# https://github.com/containerd/containerd/releases
CONTAINERD_VERSION='1.5.8'
wget https://github.com/containerd/containerd/releases/download/v${CONTAINERD_VERSION}/cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz
wget https://github.com/containerd/containerd/releases/download/v${CONTAINERD_VERSION}/cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz.sha256sum
sha256sum --check cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz.sha256sum
tar --no-overwrite-dir -C / -xzf cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz
systemctl daemon-reload
systemctl start containerd

cat << EOF > 0-containerd.conf
# /etc/systemd/system/kubelet.service.d/0-containerd.conf
[Service]
Environment="KUBELET_EXTRA_ARGS=--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"
EOF

popd

# Images
mkdir -p ${IMG_DOWNLOAD_DIR}
pushd ${IMG_DOWNLOAD_DIR}
kubeadm config images list > kubeadm-images.list
for image in $(cat kubeadm-images.list); do 
  ctr image pull ${image}
  ctr image export $(printf ${image}| tr ':/' '__') ${image}
done

popd