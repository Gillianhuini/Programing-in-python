#Create a Python program that prompts the user to enter a list of names• After receiving the input, the program should sort the names in alphabetical order, remove any duplicates, and then display the final sorted list• Additionally, count and print the total number of names entered by the user.
# Prompt the user to enter names separated by spaces
names = input("Enter names separated by spaces: ").split()
unique_sorted_names = sorted(set(names))
print("Sorted names:", unique_sorted_names)
print("Total names entered:", len(names))