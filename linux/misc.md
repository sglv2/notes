## date

Get yesterday's date
```
date --date="yesterday" +%Y-%m-%d
```
Get timestamp
```
date +%s
```
Get date from timestap
```
date -d @<timestamp>
```

## dumpe2fs
Filesystem information
```
sudo dumpe2fs -h /dev/sda1
```

## findmnt
Test /etc/fstab configuration
```
sudo findmnt --verbose --verify
```
List filesystems in "df" format
```
findmnt -t notmpfs,nosquashfs,novfat,noiso9660,notracefs -D
findmnt -t ext4 -D
```

List by device
```
findmnt -S /dev/vda1
```

## fmt
Format output, e.g. for a width of 120 columns.
```
ps -ef | fmt -w 120
```

## fusermount
```
fusermount -u /mnt/fuse
```

## id
Print user and group information for the specified USERNAME, or (when USERNAME omitted) for the current user.
```
id username
```
* get uid
```
id -u
```
* get real name
```
id -nu
```
* list of groups
```
id -nG
```

## hostnamectl
Set hostname
```
hostnamectl set-hostname 'myhost'
```

Check if running in a computer or vm
```
hostnamectl | grep 'Chassis'
```

## history
Delete all history
```
history -c
```
Delete specific command
```
delete -d 5
```

## httping
```
httping -c4 -l -g https://example.com
```

## ipcs
ipcs shows information on the inter-process communication facilities for which the calling process has read access.  
By default it  shows  information  about  all  three  resources shared memory segments, message queues, and semaphore arrays.

## jq
* Decode JWT token
```
export JWT="<token>"
jq -R 'split(".") | .[0],.[1] | @base64d | fromjson' <<< $(printf "${JWT}") | jq '.'
```

## last
List of last logged in users for the last 7 days
```
sudo last -iw --since -7days
```

## lastb
List of bad login attempts for the last 7 days
```
sudo lastb -iw -s -7days
```

## lsblk
Exclude RAM, loop, ROM devices
```
lsblk --exclude 1,7,11
```

## lsof
List of open files
* filtered by pid
```
lsof -p <pid>
```
* filtered by command
```
lsof -c <command>
```
* filtered by user
```
lsof -u <user>
```
* filtered by directory
```
lsof +D <path-to-dir>
```

Combining filters with `-a` (AND)
```
lsof -p <pid> -u <user> -a
```
## lsmod
Show the status of modules in the Linux Kernel
```
lsmod
```

## lsns
List namespaces for a process
```
sudo lsns -p <pid>
```
List namespaces of type `net`
```
sudo lsns -t net
```

## lshw
Hardware Info
```
sudo lshw
```

## modeprobe
Show module dependencies
```
modprobe --show-depends <module>
```

## patch
```
printf "first line" > ~/sample.txt
cp ~/sample.txt /tmp/sample.txt
printf "\nsecond line" >> /tmp/sample.txt

diff /tmp/sample.txt ~/sample.txt > sample.patch
patch ~/sample.txt sample.patch
```

## passwd
* `-e` Immediately expire an account's password. This in effect can force a user to change their password at the user's next login.
* `-l` lock a named account
* `-S` status
* `-u` unlock

## rsync
```
rsync -auv dir1/ dir2/
rsync -auv dir1/ <user>@<host>:/dir1/
```

## sipcalc
IP subnet calculator
```
sipcalc 10.0.0.0/28
```

## ssh-keygen
Fingerprint key
```
ssh-keygen -lf ~/.ssh/id_ecdsa
```

## sshfs

## sudo
* `-E` preserve environment
* `-l` If no command is specified, list the allowed (and forbidden) commands for the invoking user
* `-i`  Run the shell specified by the target user's password database entry as a login shell.  This means that login-specific resource files such as .profile, .bash_profile or .login will be read by the shell
* `-u` user

## tar
Create a tar.gz archive
```
tar -zcvf tar-archive-name.tar.gz source-folder-name
```
Extract a tar.gz compressed archive
```
tar -zxvf tar-archive-name.tar.gz source-folder-name
```
To preserve permissions
Use -p flag

## timeout
Run a command with a time limit
```
timeout 5 top
timeout --preserve-status 3 top
```
If the command reaches the time limit without `--preserve-status`, the exit code is 124