#write a program to check if a person is eligible to vote the person must be a kenyan,ugandan,tanzanian and above 18years.
nationality =input("Enter your nationality(kenyan,ugandan,tanzanian):")
age =int(input("Enter your age:"))
if(nationality=="Kenyan" or "Ugandan" or "Tanzanian")and age>=18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")    