```
kubectl apply -f rbac.yaml
```
To do a quick test:
* in one terminal
```
kubectl run event-viewer --rm -it \
    --restart=Never \
    --image=docker.io/alpine:3.12 \
    --serviceaccount=event-viewer \
    --command -- ash -c "while true;do sleep 10; done"
```
* in another terminal
```
kubectl cp $(which kubectl) event-viewer:/usr/local/bin/kubectl
kubectl exec -it event-viewer -- kubectl get events -w
```