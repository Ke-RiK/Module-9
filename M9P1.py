# Kirill Kaminskyi M9P1.py 10/14/2026

#input
do_program = input("Do you want to do this program? ")
do_program = do_program.lower()

total_extended_price = 0

#function
def compute_total(qty: int , unit_price: float):
    ext_price = unit_price * qty

    if ext_price > 10000:
        discount = 0.10
        total_discount = ext_price * discount
        total = ext_price - total_discount
    else:
        total = ext_price

    return total, ext_price

#process and output
while do_program == "yes":

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))


    final_total, extended_price = compute_total(quantity, price)

    total_extended_price += final_total

    print(f'{"Quantity:":<20} {"Price:":<20} {"Total:":<20}')
    print(f"{quantity:<20} ${price:<20,.2f} ${final_total:<20,.2f}")

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()

#final output
print()
print(f"Total extended price: ${total_extended_price:,.2f}")