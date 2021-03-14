# FreeIPA server
```
docker run --name freeipa-server-container -ti \
    -h ipa.example.test --read-only \
    -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
    -v /opt/ipa:/data:Z \
    -p 80:80 -p 443:443 -p 389:389 -p 636:636 -p 88:88 -p 464:464 \
    -p 88:88/udp -p 464:464/udp -p 123:123/udp \
    --sysctl net.ipv6.conf.all.disable_ipv6=0 \
    docker.io/freeipa/freeipa-server:fedora-33 \
    --realm=EXAMPLE.TEST \
    --ds-password=The-directory-server-password \
    --admin-password=The-admin-password
```