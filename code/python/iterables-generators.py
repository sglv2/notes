# To avoid loading a list in memory, a generator is used - which returns an iterable object

# Generator example
def generate_first_n(n):
    i = 1
    while i <= n:
        yield i
        i += 1


# sum function accepts an iterable
print(sum(generate_first_n(5)))
for i in generate_first_n(5):
    print(i)
