import time
import hashlib
import pickle

cache_items = {}


def has_expired(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def cached(duration=60):
    def _cached(function):
        def __cached(*args, **kw):
            key = compute_key(function, args, kw)
            if (
                    key in cache_items and
                    not has_expired(cache_items[key], duration)
            ):
                print('found in cache')
                return cache_items[key]['value']
            else:
                print('not found in cache, executing function')
            result = function(*args, **kw)
            cache_items[key] = {
                'value': result,
                'time': time.time()
            }
            return result

        return __cached

    return _cached


@cached()
def pow_cached(x, y):
    return pow(x, y)


print(pow_cached(2, 10))
print(pow_cached(2, 10))
print(pow_cached(2, 10))