# Intro
In order to simplify the examples, I'll use `${CMD}` whenever a command name must be provided.

This can be set prior to running the examples.

E.g. `export CMD=containerd-shim` or `export CMD=bash`

Multiple commands can be provided `export CMD=containerd-shim,bash`

# Top Consumers
To sort by memory use `--sort=-%mem`

## Top 5 consumers for the entire system
```
ps -eo pid,ppid,uid,%cpu,%mem,vsz,etime,comm --sort=-%cpu | head -5
```

## Top consumers for a specific command
```
ps -C ${CMD} -o pid,ppid,uid,%cpu,%mem,vsz,etime,args --sort=-%cpu
```

## Top consumers which are child processes for specific command
Note: `pgrep` expects a pattern, therefore the comma will be replaced with a pipe `|`.

```
ps --ppid $(pgrep -d ',' $(echo "${CMD}"| sed 's/,/|/g')) \
  -o pid,%cpu,%mem,vsz,etime,args --sort=-%cpu
```

## Process tree
```
pstree -sp ${PID}
```

# Namespaces
## List namespaces
```
lsns
```
List a specific type (`cgroup`, `ipc`, `mnt`, `net`, `pid`, `user`, `uts`)
```
lsns -t pid
```
## Run program with namespaces of other processes
Replace `<target-pid>` with the pid of the target process before running the following.
```
sudo nsenter -a -t <target-pid> sh
```

### pid
List processes running in namespace.
```
sudo nsenter -m -p -t <target-pid> ps -ef
```

### net
List routes
```
sudo nsenter -n -t <target-pid> ip r
```