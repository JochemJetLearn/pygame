data = {}

print("Welcome to the World Database!")

while True:
    print("Choose an option:\n 1. New country \n 2. Get capital\n 3. Get all countries\n 4. Remove country\n 5. Exit")
    while True:
        try:
            opt = int(input("Please choose an option (1-5): "))
            break
        except:
            print("Please only type numbers. (im bad at letters)")
    if opt == 1:
        country = input("Enter country: ")
        capital = input("Enter capital: ")
        data[country] = capital
        print(f"Added {country} with capital {capital}.")
    elif opt == 2:
        country = input("Enter country: ")
        if country in data:
            print(f"Capital of {country} is {data[country]}.")
    elif opt == 3:
        for i in data:
            print(f"Country: {i}, Capital: {data[i]}")
    elif opt == 4:
        country = input("Enter country to remove: ")
        if country in data:
            del data[country]
            print(f"Removed {country}.")
        else:
            print(f"{country} not found in database.")
    elif opt == 5:
        print("Exiting app...")
        break
    else:
        print("Please only choose a number between 1-5.")