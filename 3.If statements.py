a = 90
b = 500

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("A") if a > b else print("=") if a == b else print("B")

passwordValid = True

if passwordValid:
    print("Password is valid")
    passwordValid = False

if passwordValid != True:
    print("Password is reseted")