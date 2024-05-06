# Getting input from the user

name = input("What is your name? ")
print("Hello", name)

# get input as number
wage = float(input("How much do you earn per hour? "))
hours = float(input("How many hours do you work per week? ")) 
weeklyWage = (wage * hours)  
# Perform some operation with the input
print(f"Your weekly Wage is: $ {weeklyWage}")
 