# Arbitrary arguments
def sum1(*args) -> int:
    n = 0
    for i in range(len(args)):
        print(args[i])
        n = n + args[i]
    return n


print(sum1(10, 22, 33))


# Keword Arguments
def sum2(**kwargs):
    n = 0
    for k in kwargs.keys():
        print(f'{k}->{kwargs[k]}')


sum2(p1='v1', p2='v2', p3='v3')

# Lambda
double = lambda x: 2 * x
print(double(10))

## map - transform elements into new values
m = map(lambda x: x * x, range(5))
for e in m:
    print(e)

## filter - filter elements matching a condition
numbers = [10, 12, 20, 22, 34, 48]
num_ending_in_2 = filter(lambda x: x % 10 == 2, numbers)
print(f'{list(num_ending_in_2)=}')

## reduce
from functools import reduce

sum10 = reduce(lambda x, y: x + y, range(10))
print(f'{sum10=}')
