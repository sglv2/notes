## List processes using TCP or UDP sockets
```
ss -tulpn
```
### Alternative 1: netstat
Use `netstat` instead of `ss` in the command above.

## List processes using TCP sockets with an ESTABLISHED state
Listening
```
ss state listening -pt
```

Established
```
ss state established -pt
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
## List processes listening on specific ports
Source or destination port is 22
```
ss -pt '( dport = :22 or sport = :22 )'
ss -pt '( dport = :ssh or sport = :ssh )'
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