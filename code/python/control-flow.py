a = 1
b = 2
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('>')

if a <= b: print('<=')
print('>') if a > b else print('<=')
print('>') if a > b else print('<') if a < b else print('=')
