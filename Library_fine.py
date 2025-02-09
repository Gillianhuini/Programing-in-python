# User input
book_id = input("Enter Book ID: ")
due_date = int(input("Enter Due Date (as day of the month): "))
return_date = int(input("Enter Return Date (as day of the month): "))

# to Calculate the days overdue
overdue_days = return_date - due_date
if overdue_days < 0:
    overdue_days = 0

# to Determine the fine per day
if overdue_days == 0:
    fine_per_day = 0
elif overdue_days <= 7:
    fine_per_day = 20
elif overdue_days <= 14:
    fine_per_day = 50
else:
    fine_per_day = 100 

# to Calculate the total fine 
fine_amount = overdue_days * fine_per_day

# Display results
print("Book ID:", book_id)
print("Due Date:", due_date)
print("Return Date:", return_date)
print("Days Overdue:", overdue_days)
print("Fine Amount: Ksh", fine_amount)