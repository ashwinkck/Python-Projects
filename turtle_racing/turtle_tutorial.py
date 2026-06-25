def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the no of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input should be a number.... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("The input should in between (2 - 10)")


racers = get_number_of_racers()
print(racers)