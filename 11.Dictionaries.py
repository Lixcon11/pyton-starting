unique_car = {
    "color": "blue",
    "exclusive": True,
    "speed": 280,
    "co2/h": 0,
    "country": "Germany",
    "perks": ["AC", "AI", "Airbag premium", "Bottle holder"]
}

unique_car["perks"].append("TV")

print("The perks of the car are: ")
for perk in unique_car["perks"]:
    print(perk)

unique_car["price"] = 65000

unique_car.update({"co2/h": 10})

unique_car["color"] = "red"

unique_car.pop("exclusive")

print(unique_car)

def car(price, color, country): 
    return dict(price = price, color = color, country = country)

new_car = car(10000, "red", "France")

print(new_car)
