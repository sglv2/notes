import logging

log = logging.getLogger(__name__)

l = [1, 2, 3, 4, 5]
try:
    print(l[10])
except IndexError:
    log.error('IndexError')


try:
    print(l[1])
except IndexError:
    log.error('IndexError')
else:
    log.error('Something else')
finally:
    print('Step that is always executed')

import traceback

try:
    value = l[10]
except:
    traceback.print_exc()
