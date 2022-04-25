import logging
import traceback

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

l = [1, 2, 3, 4, 5]
try:
    print(l[10])
except IndexError:
    log.error('IndexError')

try:
    print(l[1])
except IndexError:
    log.error('IndexError')
finally:
    print('Step that is always executed')

try:
    value = l[10]
except:
    traceback.print_exc()
