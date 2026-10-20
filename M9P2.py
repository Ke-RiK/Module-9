# Kirill Kaminskyi M9P2.py 10/15/2026

#input
do_program = input("Do you want to do this program? ")
do_program = do_program.lower()

number_of_players_entered = 0

#function
def games_result(hits: float, at_bats: float ):
    batting = hits / at_bats

    return batting

#process + outputs
while do_program == "yes":
    player_last_name = input("Enter player last name: ")
    number_of_hits = int(input("Enter number of hits: "))
    number_of_at_bats = int(input("Enter number of at-bats: "))

    batting_average = games_result(number_of_hits, number_of_at_bats)

    print(f"{"Last name:":<20} {"Batting average:":<20}")
    print(f"{player_last_name:<20} {batting_average:<20,.3f}")

    number_of_players_entered += 1

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()

#final output
print()
print(f"Number of players entered: {number_of_players_entered}")