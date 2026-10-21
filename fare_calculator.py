

# Travel Fare Calculator (Enhanced)
FARE_RATE = 14

# Validate passenger name
name = input("Enter passenger name: ").strip()

while name == "":
    print("Error: Name cannot be empty.")
    name = input("Enter passenger name: ").strip()

# Validate distance
while True:
    distance = input("Enter distance (km): ")

    try:
        distance = float(distance)

        if distance > 0:
            break
        else:
            print("Error: Distance must be greater than 0.")

    except ValueError:
        print("Error: Enter a valid number.")

# Validate passengers
while True:
    passengers = input("Enter number of passengers: ")

    if passengers.isdigit() and int(passengers) > 0:
        passengers = int(passengers)
        break
    else:
        print("Error: Enter a positive whole number.")

# Calculate fare
total_fare = distance * FARE_RATE * passengers

# Display results
print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
