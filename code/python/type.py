# variables
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
