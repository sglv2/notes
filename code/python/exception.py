l = [1, 2, 3, 4, 5]
try:
    print(l[10])
except IndexError:
    print('IndexError')

try:
    print(l[1])
except IndexError:
    print('IndexError')
else:
    print('Something else')
finally:
    print('Step that is always executed')

import traceback

try:
    value = l[10]
except:
    traceback.print_exc()
