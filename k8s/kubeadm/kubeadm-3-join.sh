#! /bin/bash
kubeadm join <master-1>:6443 --token <token> \
	--discovery-token-ca-cert-hash sha256:<hash>