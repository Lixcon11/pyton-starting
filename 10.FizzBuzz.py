def FizzBuzz(numbers):
    new_list = []
    for number in range(1, numbers+1):
        element = ""
        if number % 3 == 0:
            element += "Fizz"
        if number % 5 == 0:
            element += "Buzz"
        if element == "":
            element = str(number)
        new_list.append(element)
    return new_list

print(FizzBuzz(20))