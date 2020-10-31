## Config
* List information regarding to the current context
```
kubectl config view --minify
```

* Change default namespace
```
kubectl config set-context --current --namespace ${NAMESPACE}
```

## Events
* List all warnings
```
kubectl get -A ev | egrep "Warning"
```

* List specific events
```
kubectl get -A ev | grep -i -E 'Backoff|Conflict|Failed|Invalid|NotReady|Rebooted|OOM|Unhealthy'
```

## Nodes
* List condition reasons for the nodes
```
kubectl get node -o jsonpath='{range .items[*]}{.metadata.name}{" "}{..reason}{"\n"}{end}'
```

* List capacity and allocated resources for nodes.
```
kubectl describe node| grep -A 7 -E 'Allocated|Hostname'
```

## RBAC
List (cluster) role bindings, referenced roles and subjects for all namespaces.
```
kubectl get rolebinding,clusterrolebinding -A \
  -o jsonpath='{range .items[*]}{.kind}{","}{.metadata.name}{","}{.metadata.namespace}{","}{.roleRef.kind}{","}{.roleRef.name}{","}{range .subjects[*]}{.kind}{","}{.name}{","}{.namespace}{"\n"}{end}'
```

## DNS
### List endpoints for kube-dns
```
kubectl -n kube-system get ep kube-dns
```
### Resolve an address
```
kubectl run debug-pod --rm -it --restart=Never \
  --image=docker.io/alpine:3.12 \
  --command -- nslookup kubernetes.default.svc.cluster.local
```
### Check connectivity with DNS service
Same as above(debug pod), using `--command -- nc -uzv kube-dns.kube-system 53`

### Check kube-proxy logs
```
kubectl logs -n kube-system -fl k8s-app=kube-proxy
```

### Check resolv.conf
```
kubectl run debug-pod --rm -it --restart=Never \
  --image=docker.io/alpine:3.12 \
  --command -- cat /etc/resolv.conf
```

## API Server
### Check connectivity with API server
Debug pod with `--command -- nc -zv kubernetes.default 443`

## Pods

* Get `name,namespace,hostIP,ready,restartCount,containerID` sorted by number of restarts (descending).
```
kubectl get po -o jsonpath='{range .items[*]}{.metadata.name}{","}{.metadata.namespace}{","}{.status.hostIP}{","}{range .status.containerStatuses[*]}{.ready}{","}{.restartCount}{","}{.containerID}{"\n"}{end}{end}'| sort -rt',' -k5
```
The `containerID` can be used to determine the process on the node
```
ps -f --ppid $(pgrep -f ${CONTAINER_ID})
```

* Get all running pods in the namespace
```
kubectl get pods --field-selector=status.phase=Running
```

* Get limits for the pods
```
kubectl get pods --field-selector=status.phase=Running -o jsonpath='{range .items[*]}{ ..metadata.name }{","}{ ..limits.cpu }{","}{ ..limits.memory }{"\n"}{end}'
```

* Get images used in the pods
```
kubectl get pods --field-selector=status.phase=Running -o jsonpath='{range .items[*]}{ ..metadata.name }{" "}{ ..image }{"\n"}{end}'
```

## Logs
Get logs for the last 10 minutes, with timestamps and a prefix containing the pod and container name.
```
kubectl logs -f --since=10m --timestamps --prefix deploy/${DEPLOYMENT}
```

Get logs using a selector
```
kubectl logs -l ${KEY}=${VALUE}
```

## Generate Load
Pod using 1 CPU (1000m)
```
kubectl run --image=serbangilvitu/kube-stress stress-cpu -- --cpu 1
```

Pod using 1GiB RAM
```
kubectl run --image=serbangilvitu/kube-stress stress-mem -- --vm 1 --vm-bytes 1G
```

## Deployments
### 

## Configmaps
* Get data with newlines instead of `\n`
```
kubectl get cm ${CONFIGMAP} -o json| jq '.data'| sed 's/\\n/\n/g'
```

## Secrets
* Decoding secrets
```
kubectl get secret ${SECRET} -o jsonpath='{.data.token}'| base64 --decode
```