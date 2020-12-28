# ldapsearch
Search for user `someuser`
```
ldapsearch -x -b "cn=someuser,cn=users,cn=accounts,dc=example,dc=com"
```
Search for user `someuser`, list only `uid` and `cn`
```
ldapsearch -x -b "cn=someuser,cn=users,cn=accounts,dc=example,dc=com" uid cn
```