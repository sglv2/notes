#!/bin/bash
# Prerequisite: Transfer files downloaded using kubeadm-download.sh to /opt on the target machine

TOOLS_DOWNLOAD_DIR=/opt/k8s-tools
IMG_DOWNLOAD_DIR=/opt/k8s-images
BIN_DIR=/usr/local/bin
DEP_DOWNLOAD_DIR=/opt/k8s-dependencies

# Load modules
lsmod | grep br_netfilter || bash -c "echo br_netfilter | tee /etc/modules-load.d/k8s.conf"
lsmod | grep overlay || bash -c "echo overlay | tee /etc/modules-load.d/containerd.conf"

modprobe overlay
modprobe br_netfilter

# Let iptables see bridged traffic
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sysctl -w net.ipv4.ip_forward=1



# Install kubectl, kubelet and kubeadm
pushd ${TOOLS_DOWNLOAD_DIR}


for t in "kubectl" "kubelet" "kubeadm";do sudo install -o root -g root -m 0755 ${t} /usr/local/bin/${t};done

# Extract CRI, containerd, CNI files
tar --no-overwrite-dir -C / -xzf cri-containerd-cni-*-linux-amd64.tar.gz
systemctl daemon-reload
systemctl start containerd

popd

# Load container images required for k8s cluster setup
pushd ${IMG_DOWNLOAD_DIR}

for image in $(ls *.gz); do 
  ctr -n k8s.io image import ${image}
done

popd

# Dependencies
dpkg -i ${DEP_DOWNLOAD_DIR}/*.deb

export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl get nodes

# kubelet
pushd ${TOOLS_DOWNLOAD_DIR}

mkdir -p /etc/systemd/system/kubelet.service.d

cat kubelet.service | sed "s:/usr/bin:${BIN_DIR}:g" | tee /etc/systemd/system/kubelet.service

cat 10-kubeadm.conf | sed "s:/usr/bin:${BIN_DIR}:g" | tee /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

systemctl enable --now containerd
systemctl enable --now kubelet

popd