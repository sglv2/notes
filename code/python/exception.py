import logging

log = logging.getLogger(__name__)

def log_error(message):
    log.error(f'[{__name__}] {message}')


l = [1, 2, 3, 4, 5]
try:
    print(l[10])
except IndexError:
    log_error('IndexError')

try:
    print(l[1])
except IndexError:
    log_error('IndexError')
else:
    log_error('Something else')
finally:
    print('Step that is always executed')

import traceback

try:
    value = l[10]
except:
    traceback.print_exc()
