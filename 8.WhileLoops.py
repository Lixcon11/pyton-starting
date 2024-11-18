number = 0
odd_numbers = 0

while number < 1000:
    print(number)
    if number % 2 != 0:
        odd_numbers += 1
    number += 1
    if odd_numbers > 4:
        break
