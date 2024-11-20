def abstractc():
    pass

def plus(x, y):
    return print(x + y)

abstractc = plus

abstractc_variable = abstractc

abstractc(2,3)

abstractc_variable(5,8)

def say_hi():
    print("Hi")

def do_something(func):
    def inner():
        func()
        print("Do something.")
    return inner

abstractc = do_something(say_hi)

abstractc()

abstractc_variable(3,6)