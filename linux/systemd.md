# Check which init system you're using
```
cat /proc/1/comm
sudo stat /proc/1/exe
stat /sbin/init

```

# journalctl
Display last 100 records and follow
```
journalctl -n 100 -f
```

Logs since last boot
```
journalctl -b
```

Logs between 2 intervals specified in UTC time
```
journalctl --utc --since "2021-01-29 19:00" --until "2021-01-30 15:00"
```

Logs related to a user
```
journalctl -r _UID=$(id -u someuser)
```

Logs related to an application
```
journalctl -r $(which containerd)
```
Logs related to a service
```
journalctl -ru cups.service
```

# systemctl
## Get list of services
```
systemctl list-units -t service
```
## Enable and start
```
systemctl enable --now example.service
```

# systemd-analyze
Determine how long it took for processes to start
```
systemd-analyze blame
systemd-analyze blame --user
```