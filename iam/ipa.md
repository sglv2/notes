# ipa
## Kerberos
Obtain and cache Kerberos ticket-granting ticket
```
kinit <user>
```
List cached Kerberos tickets
```
klist
```
## DNS
Search for DNS zones
```
ipa dnszone-find --pkey-only
ipa dnszone-find --raw
```
## role-find
Show all roles
```
ipa role-find
```

# user
## user-add
Add user
```
ipa user-add <username> --first <first-name> --last <last-name>
```

## user-find
Find user
```
ipa user-find
ipa user-find <pattern>
```

# ipa-backup
```
ipa-backup --online --data
```