# Kirill Kaminskyi M9P4.py 10/15/2026


#input
do_program = input("Do you want to do this program? ")
do_program = do_program.lower()

total_tuition_owned = 0

#function
def school(code: str, tuition: float):
    if code == "I":
        tuition = 250
    elif code == "O":
        tuition = 550

    return tuition

#process + outputs
while do_program == "yes":
    student_name = input("Enter your student last name: ")
    credit_hours = float(input("Enter your credit hours: "))
    district_code = input("Enter your district code: ").upper()

    total_payments = school(district_code, credit_hours)

    tuition_owned = credit_hours * total_payments

    total_tuition_owned = total_tuition_owned + tuition_owned

    print(f"{"Last name:":<20} {"Tuition owned:":<20}")
    print(f"{student_name:<20} ${tuition_owned:<20,.2f}")

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()


#final output
print()
print(f"Total tuition owned: ${total_tuition_owned:,.2f}")

