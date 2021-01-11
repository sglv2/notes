## id
Print user and group information for the specified USERNAME, or (when USERNAME omitted) for the current user.
```
id username
```
get uid
```
id -u
```
get real name
```
id -nu
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

## ipcs
ipcs shows information on the inter-process communication facilities for which the calling process has read access.  
By default it  shows  information  about  all  three  resources shared memory segments, message queues, and semaphore arrays.

## lsblk

## lsof
The ‘lsof’ command will provide the number of open files associated with a process.

## lsns
List namespaces for a process
```
sudo lsns -p 23029
```
List namespaces of type `net`
```
sudo lsns -t net
```

# last
List of last logged in users for the last 7 days
```
sudo last -iw --since -7days
```

# lastb
List of bad login attempts for the last 7 days
```
sudo lastb -iw -s -7days
```

## lshw
Hardware Info
```
sudo lshw
```

## passwd
* `-e` Immediately expire an account's password. This in effect can force a user to change their password at the user's next login.
* `-l` lock a named account
* `-S` status
* `-u` unlock

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