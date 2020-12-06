# get
download all hooks for a named release
```
helm get hooks
```

download the manifest for a named release
```
helm get manifest
```

download the notes for a named release
```
helm get notes
```

download the values file for a named release
```
helm get values
```

# history

# install
Install a chart
```
helm install ${RELEASE_NAME} ${CHART_NAME} \
  -n ${K8S_NAMESPACE} \
  -f ${VALUE_FILE} \
  --version ${CHART_VERSION}
```

# ls
List releases in namespace
```
helm ls
helm ls -n ${K8S_NAMESPACE}
helm ls -n default
```

# repo
## add
```
helm repo add <url>
```

```
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
```

## ls
List repos
```
helm repo ls
```

# pull
Download a chart from a repository and (optionally) unpack it in local directory
```
helm pull ${CHART_NAME} --version ${VERSION}
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

# rollback

# show
```
helm show chart ${CHART_NAME}
helm show chart bitnami/redis
```
```
helm show readme ${CHART_NAME}
helm show readme bitnami/redis
```
```
helm show values ${CHART_NAME}
helm show values bitnami/redis
```

# upgrade
Upgrades a chart
```
helm upgrade ${RELEASE_NAME} ${CHART_NAME} \
  -n ${K8S_NAMESPACE} \
  -f ${VALUE_FILE} \
  --version ${CHART_VERSION}
```
## Reusing and resetting values during an upgrade
### --reuse-values
When upgrading, reuse the last release's values.


### --reset-values
When upgrading, reset the last release's values.