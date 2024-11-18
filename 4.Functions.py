def hi_name(name):
    print("Hi " + name)

def valid_name(name):
    if name == "Kayle":
        hi_name(name)
        return True
    return False

def check_name(name):
    isValid = valid_name(name)
    if isValid:
        print(name + " is a valid name")
    else:
        print(name + " is not a valid name")

check_name("Kayle")
check_name("Nancy")
