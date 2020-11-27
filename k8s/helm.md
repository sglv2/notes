# ls
List releases in namespace
```
helm ls
helm ls -n ${NAMESPACE}
helm ls -n default
```

# repo
## add
```
helm repo add <url>
```

```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

## ls
List repos
```
helm repo ls
```

# search
## hub
Searches the hub https://hub.helm.sh/ which now redirects to https://artifacthub.io/
```
helm search hub ${KEYWORD}
helm search hub redis
```

## repo
Search repositories for a keyword in charts
```
helm search repo ${KEYWORD}
helm search repo redis
```