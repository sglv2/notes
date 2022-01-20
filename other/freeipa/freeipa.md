# ipa
Run `kinit <user>`
## user-add
Add user
```
ipa user-add <username> --first <first name> --last <first name>
```
## user-find
Search for an user
```
ipa user-find --login <username>
ipa user-find --last <last name>
```
## user-mod
Set a temporary password for an user
```
ipa user-mod <username> --password
```

## Certificates
### Renew IPA service certificates
```
for s in "krbtgt" "ldap" "HTTP";do
  ipa-getcert list -t \
    | grep "principal name: ${s}/" -B 11 \
    | head -1 \
    | cut -f2 -d"'" \
    | xargs -I % ipa-getcert resubmit -i %
done
```

### Generate CSR and certificate
```
cat <<EOF > cert.cnf
[req]
distinguished_name = req_distinguished_name
prompt = no
[req_distinguished_name]
C = MU
ST = Sunny
L = Quatre Cocos
O = Coconut
CN = qc.example.local
EOF

openssl req -new -newkey rsa:2048 -nodes -keyout cert.key -out cert.csr -config cert.cnf

ipa cert-request --principal=host/qc.example.local@EXAMPLE.LOCAL --add cert.csr
```