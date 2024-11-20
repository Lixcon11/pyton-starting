def plus(x: int, y: int) -> int:
    return x + y

x: int = 10
y: int = 25

print(plus(x, y))

def hello(name: str, male: bool) -> str:
    return f"Hi { 'mister' if male else 'miss'} {name}"

name: str = "John"
gender: str = "male"

print(hello(name, True if gender == "male" else False))