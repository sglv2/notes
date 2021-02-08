# Verifiy certificate was signed by a root CA
```
openssl verify -verbose -show_chain -CAfile root-ca.pem some.crt
```

# Verify that certificate and key match
```
openssl rsa -in some.key -noout -modulus| openssl md5
openssl x509 -in some.crt -noout -modulus| openssl md5
```