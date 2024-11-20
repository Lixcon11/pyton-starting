def print_kwargs(a, b, c):
    print(a, b, c)

kwargs = {
    "a": 1000,
    "b": 0,
    "c": 100
}

print_kwargs(**kwargs)

def greet(**names):
        print(names)

greet(first="Alice", second="Bob")

print(dict(first="Alice", second="Bob"))

def print_args(a, b, c):
    print(a, b, c)

args_one = {10, True, "M"}
args_two = (10, True, "M")
args_three = [10, True, "M"]

print_args(*args_one)
print_args(*args_two)
print_args(*args_three)

def hello(*names):
        print(names)

hello("Jonh", "Dave")