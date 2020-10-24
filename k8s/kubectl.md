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

## Events
List all warnings
```
kg -A ev | egrep "Warning"
```

List specific events
```
kg -A ev | egrep "Warning"
kg -A ev | egrep -i "(Backoff|Conflict|Failed|Invalid|NotReady|Rebooted|OOM|Unhealthy)"
```
