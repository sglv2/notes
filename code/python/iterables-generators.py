# To avoid loading a list in memory, a generator is used - which returns an iterable object

# Generator example
def generate_first_n(n):
    i = 1
    while i <= n:
        yield i * 10
        i += 1


# sum function accepts an iterable
print(sum(generate_first_n(5)))
for v in generate_first_n(5):
    print(v)

for i, v in enumerate(generate_first_n(5)):
    print(f'index={i} value={v}')


# Iterator
# You have to implement __iter__() and __next__() methods
class OddNumbers:
    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        x = self.n
        self.n += 2
        return x


odd = OddNumbers()
it = iter(odd)

print(next(it))
print(next(it))
