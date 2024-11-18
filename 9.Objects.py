class MyUniqueTicket:
    name = "Kyle"
    number = 16518
    class_type = "Unique"
    is_premium = True
    privileges = ["Suite", "Assistant", "Bar", "Laundry"]

    def __str__(self):
        return f"{self.name}({self.class_type})"


def ticket_info(ticket): 
    print("Username: " + str(ticket.name))
    print("Unique ID: " + str(ticket.number))
    print("Class type: " + str(ticket.class_type))
    if not ticket.privileges:
        print("Privileges: None")
    else:
        privilege_count = ""
        for privilege in ticket.privileges:
            privilege_count += privilege + ", "
        privilege_count = privilege_count[:len(privilege_count)-2]
        print("Privileges: " + privilege_count)
    if ticket.is_premium:
        print("You are premium!")
    else:
        print("You are standard.")
 
my_ticket = MyUniqueTicket()

ticket_info(my_ticket)

class Ticket:
    def __init__(self, name, number, class_type, is_premium, privileges):
        self.name = name
        self.number = number
        self.class_type = class_type
        self.is_premium = is_premium
        self.privileges = privileges
    
    def __str__(self):
        return f"{self.name}({self.class_type})"


john_ticket = Ticket("John", 4, "Wind", True, ["Rewind", "Cruise Ship", "Blue Pijamas"])

ticket_info(john_ticket)

def tell_a_joke():
    print("Why don't ghosts ever throw parties? Because they can't handle the boos!")

john_ticket.tell_a_joke = tell_a_joke

john_ticket.tell_a_joke()

print(my_ticket)
print(john_ticket)