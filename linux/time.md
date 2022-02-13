# Determine which time sync daemon is running
```
ps -ef | grep -E '(chrony|ntp|timesyncd)'
```

# timedatectl
Current settings of the system clock, including whether network time synchronization is active
```
timedatectl status
```

Enable synchronization with a public NTP server
```
timedatectl set-ntp true
systemctl status systemd-timesyncd
```

```
timedatectl set-time "2022-02-04 19:30:00"
```
# timesyncd.conf
/etc/systemd/timesyncd.conf