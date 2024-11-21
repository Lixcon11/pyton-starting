
def say_next_fruit_to_buy(it):
    global limit
    if limit != 0:
        print(next(it))
        limit -= 1
        print(f"Limit remaining: {limit}")
    else:
        print("Maximum fruits have been bought. The ones that reaim will be put on the next buy list. Which are:")
        try:
            while True:
                fruit = next(it)
                buy_next_time.append(fruit)
                print(fruit)
        except StopIteration:
            pass
         


fruit_list = ["banana", "tomato", "cherry", "pumpkin", "watermelon"]
buy_next_time = []
limit = 4
iterable = iter(fruit_list)

say_next_fruit_to_buy(iterable)
say_next_fruit_to_buy(iterable)
say_next_fruit_to_buy(iterable)
say_next_fruit_to_buy(iterable)
say_next_fruit_to_buy(iterable)