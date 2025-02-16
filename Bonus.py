 #user input for salary and years of service
salary = float(input("Enter your salary:"))
years_of_service =(int(input("Enter your years of service:")))
# bonus percentage based on years of service
if years_of_service > 10:
    bonus_percentge = 10
elif years_of_service >= 6 and years_of_service <= 10:
    bonus_percentage = 8
else:
    bonus_percentage = 5
# calculating bonus 
bonus_amount = (bonus_percentage / 100) * salary
total_amount = salary + bonus_amount
#printing the bonus amount
print("your net bonus amount is:",bonus_amount)
print("TotalAmount:", total_amount)