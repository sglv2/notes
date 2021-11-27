#!/bin/bash
kubeadm init
# kubeadm init --control-plane-endpoint <internal-ip> --node-name <internal-ip> --service-cidr <service-cidr> --pod-network-cidr <pod-cidr>

export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl get nodes

# /etc/kubernetes/pki

# kubelet
# pushd ${TOOLS_DOWNLOAD_DIR}

# mkdir -p /etc/systemd/system/kubelet.service.d

# cat kubelet.service | sed "s:/usr/bin:${BIN_DIR}:g" | tee /etc/systemd/system/kubelet.service

# cat 10-kubeadm.conf | sed "s:/usr/bin:${BIN_DIR}:g" | tee /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

# cat << EOF > /etc/systemd/system/kubelet.service.d/0-containerd.conf
# [Service]
# Environment="KUBELET_EXTRA_ARGS=--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"
# EOF

# systemctl enable --now kubelet

# popd