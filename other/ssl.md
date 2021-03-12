# openssl
## Verifiy certificate was signed by a root CA
```
openssl verify -verbose -show_chain -CAfile root-ca.pem some.crt
```

## Verify that certificate and key match
```
openssl rsa -in some.key -noout -modulus| openssl md5
openssl x509 -in some.crt -noout -modulus| openssl md5
```

## Export certificates
```
export target="<host>" && \
  for port in $(nmap -p 443 ${target} | grep " open " | cut -d "/" -f 1); do \
  echo checking on port: $port && \
  echo | openssl s_client -showcerts -connect ${target}:$port \
 ;done > ${target}.$(date +%FT%H%M%S)
```