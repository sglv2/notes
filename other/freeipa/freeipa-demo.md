# Network
```
docker network create --subnet=172.18.0.0/16 freeipa
```

# FreeIPA server
Master
```
docker run --name freeipa-1 -it \
    -h freeipa1.example.local \
    -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
    -v /opt/ipa1:/data \
    -p 80:80  -p 88:88 -p 389:389 -p 443:443 -p 464:464 -p 636:636 \
    -p 88:88/udp -p 464:464/udp \
    --sysctl net.ipv6.conf.all.disable_ipv6=0 \
    --net freeipa \
    --ip 172.18.0.101 \
    --add-host freeipa2.example.local:172.18.0.102 \
    --add-host freeipa3.example.local:172.18.0.103 \
    docker.io/freeipa/freeipa-server:fedora-33 \
    ipa-server-install \
    --realm=EXAMPLE.LOCAL \
    --ds-password=The-directory-server-password \
    --admin-password=The-admin-password \
    --no-host-dns --no-ntp \
    --hostname freeipa1.example.local \
    --ip-address=172.18.0.101
```
Replica
```
docker run --name freeipa-2 -it \
    -h freeipa2.example.local \
    -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
    -v /opt/ipa2:/data \
    --sysctl net.ipv6.conf.all.disable_ipv6=0 \
    --net freeipa \
    --ip 172.18.0.102 \
    --add-host freeipa1.example.local:172.18.0.101 \
    --add-host freeipa3.example.local:172.18.0.103 \
    docker.io/freeipa/freeipa-server:fedora-33 \
    ipa-replica-install \
    --domain example.local \
    --server freeipa1.example.local \
    --admin-password=The-admin-password \
    --hostname freeipa2.example.local \
    --ip-address=172.18.0.102
    --no-host-dns \
    --no-ntp \
    --setup-ca
```