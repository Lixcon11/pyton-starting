names = ["Julia", "Clark", "Ben", "Rajka"]

for name in names:
    print(name)
    if len(name) < 4:
        print("Short name founded! Now it's letters!")
        for letter in name:
            print(letter)
        break

def counter(number):
    print("Lets count to " + str(number))
    for number in range(number):
        print (number+1)
    print("Finished!")

def inverse_counter(number):
    print("Lets count to " + str(number) + " backwards")
    for number in range(number, 0, -1):
        print (number)
    print("Finished!")

counter(10)

inverse_counter(10)