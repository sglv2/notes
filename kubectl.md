# Intro
## Aliases
kubectl will be used extensively, so in order to avoid repetition, the following aliases are applied
```
alias k='kubectl'
alias ka='kubectl apply -f'
alias kd='kubectl describe'
alias kg='kubectl get'
alias kns='kubectl config set-context --current --namespace'
```

# Identifying problems
## Events
```
kg -A events| egrep -i "(Failed|Rebooted|NodeNotReady|HostPortConflict)"
```
