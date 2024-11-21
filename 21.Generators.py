def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

#regular function equivalent
def fib_two(limit):
    x = []
    a, b = 0, 1
    while b < limit:
        x.append(b)
        a, b = b, a + b
    return iter(x)

x = list(fib(200))
y = list(fib_two(200))

print(x)
print(y)

generator_exp = (i + 2 for i in range(10) if i % 4 == 0)

for i in generator_exp:
    print(i)

def stateful_generator():
    value = yield  # Receive a value from outside
    while True:
        value = yield value * 2

gen = stateful_generator()
next(gen)          # Start the generator
print(gen.send(10)) 
print(gen.send(20))