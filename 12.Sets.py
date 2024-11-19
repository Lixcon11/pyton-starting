perks = { "couch", "bed", "bathroom", "kitchen", "garaje" }

if "kitchen" in perks:
    print("Look at this amazing kitchen!")

if not "laundry" in perks:
    print("You can use the public laundry the street next door!")

perks.add("jacuzzi")

if "bed" and "couch" in perks:
    print("You seem to have both a bed and a couch perks, we will trade them for the amazing sofa bed!")
    perks.remove("bed")
    perks.remove("couch")
    perks.add("sofa bed")

for perk in perks:
    print(perk)

deluxe = {"TV", "swimming pool", "garden", "garaje"}

print("Lucky! Here is the new list of perks after adding the deluxe package! The following perks will be not added again because you have them already:")

for perk in perks.intersection(deluxe):
    print(perk)

perks = perks.union(deluxe)
print("This is your new upadted list of perks!")
for perk in perks:
    print(perk)