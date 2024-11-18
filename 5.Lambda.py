multiply = lambda x, y: x * y

stock_value = 214

margin = 0.95

taxes = 0.75

cut = 60

benefits = lambda: multiply(multiply(stock_value, margin), taxes) - cut

actions_number = 200

total_benefits = lambda: multiply(actions_number, benefits())

print ("The total benefits are " + str(total_benefits()) + "$")