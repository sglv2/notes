#!/bin/bash

kubeadm init
# kubeadm init --control-plane-endpoint <load-balancer-ip> --node-name <internal-ip> --service-cidr <service-cidr> --pod-network-cidr <pod-cidr>
