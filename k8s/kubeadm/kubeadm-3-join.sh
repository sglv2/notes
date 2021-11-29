#! /bin/bash

# Obtain the certificate key by running the following on an existing master
# kubeadm certs certificate-key
read -p 'CERTIFICATE_KEY=' CERTIFICATE_KEY

kubeadm join <master-1>:6443 --token <token> \
	--discovery-token-ca-cert-hash sha256:<hash> \
	--control-plane \
	--certificate-key ${CERTIFICATE_KEY}