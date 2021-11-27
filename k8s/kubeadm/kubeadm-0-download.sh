#!/bin/bash
# https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
# https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#without-internet-connection

TOOLS_DOWNLOAD_DIR=/opt/k8s-tools
DEP_DOWNLOAD_DIR=/opt/k8s-dependencies
IMG_DOWNLOAD_DIR=/opt/k8s-images
export PATH=${TOOLS_DOWNLOAD_DIR}:${PATH}

CONTAINERD_VERSION='1.5.8'
TEMPLATES_VERSION="v0.4.0"

lsmod | grep br_netfilter || bash -c "echo br_netfilter | tee /etc/modules-load.d/k8s.conf"
lsmod | grep overlay || bash -c "echo overlay | tee /etc/modules-load.d/containerd.conf"


modprobe overlay
modprobe br_netfilter

# Download dependencies
mkdir -p ${DEP_DOWNLOAD_DIR}
pushd ${DEP_DOWNLOAD_DIR}

curl -sLO http://mirrors.kernel.org/ubuntu/pool/main/s/socat/socat_1.7.3.3-2_amd64.deb
curl -sLO http://mirrors.kernel.org/ubuntu/pool/main/c/conntrack-tools/conntrack_1.4.5-2_amd64.deb

popd

# Download tools
mkdir -p ${TOOLS_DOWNLOAD_DIR}
pushd ${TOOLS_DOWNLOAD_DIR}
RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
ARCH="amd64"
curl -L --remote-name-all https://storage.googleapis.com/kubernetes-release/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet,kubectl}
chmod +x {kubeadm,kubelet,kubectl}

curl -sSLO "https://raw.githubusercontent.com/kubernetes/release/${TEMPLATES_VERSION}/cmd/kubepkg/templates/latest/deb/kubelet/lib/systemd/system/kubelet.service" 

curl -sSLO "https://raw.githubusercontent.com/kubernetes/release/${TEMPLATES_VERSION}/cmd/kubepkg/templates/latest/deb/kubeadm/10-kubeadm.conf" 

# Download containerd
# https://github.com/containerd/containerd/blob/main/docs/cri/installation.md
# https://github.com/containerd/containerd/releases
wget https://github.com/containerd/containerd/releases/download/v${CONTAINERD_VERSION}/cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz
wget https://github.com/containerd/containerd/releases/download/v${CONTAINERD_VERSION}/cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz.sha256sum
sha256sum --check cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz.sha256sum
tar --no-overwrite-dir -C / -xzf cri-containerd-cni-${CONTAINERD_VERSION}-linux-amd64.tar.gz
systemctl daemon-reload
systemctl start containerd

popd

# Images
mkdir -p ${IMG_DOWNLOAD_DIR}
pushd ${IMG_DOWNLOAD_DIR}
kubeadm config images list > kubeadm-images.list
for image in $(cat kubeadm-images.list); do 
  ctr image pull ${image}
  ctr image export $(printf ${image}| tr ':/' '__').tar.gz ${image}
done

popd