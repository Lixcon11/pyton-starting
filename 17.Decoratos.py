def hello_user(func):
    def greetings():
        print("Hello user.")
        func()
        print("It's a pleasure.")
    return greetings

@hello_user
def hi_back():
    print("Hi back.")

hi_back()