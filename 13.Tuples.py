new_tuple = ("John",)

print(new_tuple[0])

new_list = list(new_tuple)
new_list[0] = 11
new_tuple = tuple(new_list)

print(new_tuple[0])

other_tuple = (2044, "Leonard", "Hallowen", 505)

new_tuple += other_tuple

new_list = list(new_tuple)
new_list.remove("Leonard")
new_tuple = tuple(new_list)

(lucky_number, singularity, *holiday) = new_tuple

print(new_tuple)

print("The year of singularity is " + str(singularity))
print("You lucky number is " + str(lucky_number))
print(f"Today in {holiday[0]} we have up to {holiday[1]} contestant in the candy hunt!")