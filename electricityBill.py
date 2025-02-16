# user inputs
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))

#  charges per unit
if units_consumed <= 199:
    charge_per_unit = 1.20
elif units_consumed < 400:
    charge_per_unit = 1.50
elif units_consumed < 600:
    charge_per_unit = 1.80
else:
    charge_per_unit = 2.00

# total bill before surcharge
total_bill = units_consumed * charge_per_unit

if total_bill > 400:
    surcharge = 0.15 * total_bill 
    total_bill += surcharge

if total_bill < 100:
    total_bill = 100

#printing the results
print("\nElectricity Bill")
print("Customer ID      :", customer_id)
print("Customer Name    :", customer_name)
print("Units Consumed   :", units_consumed)
print("Charges per Unit :", charge_per_unit)
print("Total Amount to Pay: Ksh", round(total_bill, 2))