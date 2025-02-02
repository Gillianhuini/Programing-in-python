#write a program to check if a person is eligible to vote the person must be a kenyan,ugandan,tanzanian and above 18years.
# Get the user's nationality as input 
nationality =input("Enter your nationality(kenyan,ugandan,tanzanian):")
#Get the user's age as input and convert it to an integer
age =int(input("Enter your age:"))
# Check if the nationality is valid and if the person is 18 or older
if(nationality=="Kenyan" or "Ugandan" or "Tanzanian")and age>=18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")    
