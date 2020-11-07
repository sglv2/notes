## List processes using TCP or UDP sockets with an ESTABLISHED state
Listening
```
ss state listening -ptu
```

Established
```
ss state established -pt
```

### Alternative 1 : lsof
Established
```
lsof -i -s TCP:ESTABLISHED
```

Not established
```
lsof -i -s TCP:^ESTABLISHED
```