# Kirill Kaminskyi M9P4.py 10/15/2026

#input
do_program = input("Do you want to do this program? ")
do_program = do_program.lower()

total_gross_pay = 0

#function
def money(code, pay_rate: float ):
    if code == "L":
        pay_rate = 25
    elif code == "A":
        pay_rate = 30
    elif code == "J":
        pay_rate = 50
    return pay_rate

#process + outputs
while do_program == "yes":
    last_name = input("Enter your last name: ")
    job_code = input("Enter your job code: ").upper()
    hours_worked =  float(input("Enter your hours worked: "))

    hours_rate = money(job_code, hours_worked)

    if hours_worked > 40:
        gross_pay = (40 * hours_worked) + (hours_rate - 40) * (hours_worked * 1.5)
    else :
        gross_pay = hours_worked * hours_rate


    print(f"{"Last name:":<20} {"Gross Pay:":<20}")
    print(f"{last_name:<20} ${gross_pay:<20,.2f}")

    total_gross_pay += gross_pay

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()

#final output
print()
print(f"Total gross pay: ${total_gross_pay:,.2f}")