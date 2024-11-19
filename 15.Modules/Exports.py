user_data = [
    {
        "name": "John",
        "paid": True,
        "status": "Premium"
    },
    {
        "name": "Rose",
        "paid": False,
        "status": "Premium"
    },
    {
        "name": "Jane",
        "paid": True,
        "status": "Wild"
    },
    {
        "name": "Dave",
        "paid": False,
        "status": "Beyound"
    }
]


def getBeyound(users):
    for user in users:
        if user["status"] == "Beyound":
            print(user["name"] + " is Beyound!")