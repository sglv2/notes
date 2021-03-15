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