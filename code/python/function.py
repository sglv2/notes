# Arbitrary arguments
def sum1(*args):
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