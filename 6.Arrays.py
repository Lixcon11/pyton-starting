assistance_name = lambda ticket: ticket[3][1]
has_assistance = lambda ticket: ticket[3][2]
check_assistants = lambda: print("Valid assists list: " + str(valid_assitances))

def new_assistance(ticket): 
    ticket[3][1] = valid_assitances[0]
    valid_assitances.pop(0)

def assistance_check(ticket):
    if has_assistance(ticket):
        print("You are suposed to have a assistant while the flight, checking name.")
        name = assistance_name(ticket)
        if name in valid_assitances:
            print("Your assistant named " + name + " is avaible for the flight.")
        else:
            print("Your assistant named " + name + " is not avaible for the flight. A new assistant while be chosen for you.")
            new_assistance(ticket)
            name = assistance_name(ticket)
            print("You have a new assistant named " + name + ", enjoy the flight")

    else:
        print("You are not suposed to have a assistant while the flight.")

valid_assitances = ["Kim", "Nala", "Lara"]

ticket_array = ["Tom", "Lucy", 4874, [55, "Julia", True]]

check_assistants()

assistance_check(ticket_array)

check_assistants()