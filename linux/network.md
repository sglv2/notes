# Interfaces
List network interfaces in a compact format
```
ip -br a
ip -br address list
```

# Routes
## List routes
```
ip r
ip route list
```
### Alternative 1: netstat
```
netstat -r
```
## Tracing routes
```
nmap -sn --traceroute $IP
```

# Connectivity
TCP
```
IP=8.8.8.8; PORT=443; nc -zv ${IP} ${PORT} || echo "Failed to connect to ${IP}:${PORT}"
```

For UDP add the `-u` flag to nc.

# Connections
## List processes using TCP or UDP sockets
```
ss -tulpn
```
### Alternative 1: netstat
Use `netstat` instead of `ss` in the command above.

## List processes using TCP sockets with an specific state
```
ss state established -pt
ss state connected -pt # All the states except for listen and closed
```
### Alternative 1 : netstat
Use `netstat` instead of `ss` in the commands above.

### Alternative 2 : lsof
Established
```
lsof -i -s TCP:ESTABLISHED
```

Not established
```
lsof -i -s TCP:^ESTABLISHED
```
## List processes using TCP sockets, including timer information
```
ss -optn
```

## List processes using specific ports
Source or destination port is 22
```
ss -pt dport :22 or sport :22
ss -pt dport :ssh or sport :ssh
ss -pt dst :22 or src :22
```
### Alternative 1 : netstat
Use `netstat` instead of `ss` in the commands above.

### Alternative 2 : lsof
Source or destination port is 22
```
lsof -i :22
```
Source or destination port is in range 1-1024
```
lsof -i :1-1024
```

## List processes connecting to a specific IP address
Using `1.1.1.1` as an example IP address
```
ss -pt dst 1.1.1.1 or src 1.1.1.1
```

### Alternative 1 : lsof
```
lsof -i @1.1.1.1
```

## Check open ports
Check common ports
```
nmap -T4 -Pn <ip-address>
```
Check if ports in range 1-1024 are open for `<ip-address>`
```
nmap -T4 -Pn -p 1-1024 <ip-address>
```

# DNS
## resolvectl
Get details about the uplink DNS servers currently in use.
```
resolvectl status
```

# Firewalls
## firewalld
Check the status of the firewalld service
```
systemctl status firewalld.service
```

List ports
```
firewall-cmd --list-ports
```

Permanently add port
```
firewall-cmd --permanent --zone=public --add-port=<port-number>/tcp
```

Permanently remove port
```
firewall-cmd --permanent --zone=public --remove-port=<port-number>/tcp
```

Reload configuration
```
firewall-cmd --reload
```

List zones
```
firewall-cmd --list-all-zones
```

# Traffic Analysis
## tcpdump
List of devices from which you can capture traffic
```
tcpdump -D
```

Capture on all devices, do not convert addresses to names
```
tcpdump -i any -n
```

```
tcpdump -i any port 53 -n
tcpdump -i any src port 53 -n
tcpdump -i any dst port 53 -n
```

Write capture to pcap file
```
tcpdump -i any port 53 -w dns.pcap -v
```
Read pcap file
```
tcpdump -r dns.pcap
```

Traffic for a particular host
```
tcpdump host duckduckgo.com -i any -n
tcpdump "host duckduckgo.com and port 443" -i any -n
```

Source and destination networks
```
tcpdump -i any -n "src net 192.168.0.0/16 and not dst net 10.0.0.0/8
```

Filter on TCP flags
```
tcpdump -i any  "tcp[tcpflags] & tcp-ack !=0"
```

## tcptrace
Analyze pcap output
```
tcptrace file.pcap
```

## ngrep
grep on network traffic

## tcpspy
Logs traffic to syslog
```
sudo tcpspy
```

## tcpreplay
Replay pcap file
```
tcpreplay -i eth0 -tK --loop 1 --unique-ip file.pcap
```

## wireshark
### TLS
```
export SSLKEYLOGFILE=~/keylogfile
```
In Wireshark, go to Edit->Preferences->Protocols->TLS, set the same value for
secret logfilename.

# NetworkManager
## Show active connections
```
nmcli con show --active
```

# Check own IP
```
dig +short myip.opendns.com @resolver1.opendns.com
```
or
```
curl https://checkip.amazonaws.com
```