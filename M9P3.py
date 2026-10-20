# Kirill Kaminskyi M9P3.py 10/15/2026

#input
do_program = input("Do you want to do this program? ")
do_program = do_program.lower()

number_of_entries = 0

#function
def road_trip(travel: float, fuel: float ):
    travel_fuel = travel / fuel

    return travel_fuel

#process + outputs
while do_program == "yes":

    destination_city = input("Enter the destination city: ")
    miles_traveled =  float(input("Miles traveled: "))
    gallons_used = float(input("Gallons used: "))

    miles_per_gallon = road_trip(miles_traveled, gallons_used)

    print(f'{"Destination City:":<20} {"Distance in miles:":<20} {"Mpg:":<20}')
    print(f"{destination_city:<20} {miles_traveled:<20,.2f} {miles_per_gallon:<20,.2f}")

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()

    number_of_entries += 1

#final output
print()
print(f"Number of entries made: {number_of_entries}")