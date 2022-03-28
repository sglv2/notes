# variables - general

pets = ['cat', 'dog', 'snake']
x, y, z = pets
print(x, y, z)

print(str('Hello'))
print(int(99))
print(float(3.14))
print(list(('cat', 'bird', 'snake')))
print(tuple(('cat', 'bird', 'snake')))
print(range(6))
print(dict(type='car', color='blue'))
print(set(('cat', 'bird', 'snake')))
print(frozenset(('cat', 'bird', 'snake')))
print(bool(True))
print(bytes(5))
print(bytearray(5))


# Cast
def cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


print(cast('5', int))  # returns 5
print(cast('5.5', int))  # returns None

# Strings
s = '''This is a 
multiline 
string spanning 3 lines'''
print(s)

print(f'line substring was found: {"line" in s}')
print(f'Slice between index 0 and 4: {s[0:4]}')
print(f'Slice between index 4 to the end: {s[4:]}')
print(f'{"one".upper()} {"TWO".lower()} {"  a  ".strip()}')
print('Split string by newline', s.split("\n"))
print(f'{"1".isdigit()} {"1".isalnum()} {"1".isalpha()}')
# Encoding
s = 'Malmö'
print(s.encode().decode())  # default is utf-8
print(s.encode(encoding='utf-8').decode())
print(s.encode(encoding='ascii', errors='namereplace'))
print(s.encode(encoding='ascii', errors='replace'))
"""
'backslashreplace' uses a backslash instead of the character that could not be encoded
'ignore' ignores the characters that cannot be encoded
'namereplace' replaces the character with a text explaining the character
'strict' Default, raises an error on failure
'replace' replaces the character with a questionmark
'xmlcharrefreplace' replaces the character with an xml character
"""

# Lists
l = [0, 10, 20, 30, 40, 50, 60, 70, 80]
print(f'l[1:]={l[1:]}')
print(f'l[1:2]={l[1:2]}')
print(f'l[2:-1]={l[2:-1]}')
print(f'every 3rd item={l[::3]}')
print(f'6 to 3={l[6:3:-1]}')
print(f'last 3={l[-3:]}')
exit(1)
print(f'len(l)={len(l)}')
l.append(100)
l.insert(1, 5)
print(l)
l.extend([110, 120])
print(l)
l.pop(1)
print(l)
sum = 0
for x in l:
    sum = sum + x
print(sum)
for i in range(len(l)):
    print(l[i])

# List comprehension
[print(x + 1) for x in l]
l2 = [x for x in l if x % 30 == 0]
l2.sort(reverse=True)
print(l2)
l3 = l2.copy()
l3.sort()
print(l2 + l3)

# Tuples
t1 = (1, 21, 31, 41)
l4 = list(t1)
l4[0] = 11
t2 = tuple(l4)
print(t2)

# Set
set1 = {22, 32, 42}
set1.add(52)
set2 = set1.union({62, 72})
set0 = {32, 55, 42, 66}
[print(x + 1) for x in set1]
## Get the intersection of 2 sets
set3 = set1.copy()
print('intersection')
print(set3.intersection(set0))
set3.intersection_update(set0)
print(set3)
## Get the difference of 2 sets
print('difference')
set4 = set1.copy()
print(set4.symmetric_difference(set0))
set4.symmetric_difference_update(set0)
print(set4)

## Other set functions
print(set1.isdisjoint(set0))
print({52}.issubset(set1))
print(set1.issuperset({52}))

# Dictionary
d = {
    "k1": "v11",
    "k2": "v2",
    "k3": "v3"
}
d.update({"k1": "v1"})
print(d)
print(f'')
print(f'len(d)={len(d)}')
print(f'd["k1"]={d["k1"]}')
print(f'd.get("k1")={d.get("k1")}')
print(f'd.items()={d.items()}')
print(f'Key exists: "k1" in d={"k1" in d}')
d.pop("k3")
print(d)
## print values
print('for x in d:')
for x in d:
    print(x)
print('for x in d.values():')
for x in d.values():
    print(x)
## print keys
print('for x in d.keys():')
for x in d.keys():
    print(x)
## print items
for x, y in d.items():
    print(x, y)
## copy dict
d2 = d.copy()
d3 = dict(d)
print(d2)
print(d3)
## nested
d4 = {
    'k1': 10
}
d5 = {
    'e1': d4
}
print(d5['e1']['k1'])
## fromkeys
d6 = dict.fromkeys(('k1', 'k2'), 0)
print(d6)