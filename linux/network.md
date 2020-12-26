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