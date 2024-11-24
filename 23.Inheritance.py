class BaseTier:
    power_level = 40000

class Breath:
    _aspect = "Breath"
    aspect_lore = "the embodiment of freedom"

class Mage:
    _class = "Mage"
    class_lore = "guides and benefits the others by"

god_stats = dict(fly = True, __str__ = lambda self: f"{self.name} is a {self._class} of {self._aspect} is known to {self.class_lore} being {self.aspect_lore}.")

mage_of_breath = type("GodTier", (BaseTier, Breath, Mage), god_stats)

john = mage_of_breath()

john.name = "John"

print(john.power_level)
print(john._aspect)
print(john.fly)
print(john)