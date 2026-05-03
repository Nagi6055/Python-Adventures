"""
Project Name: Variables
File Name: variable.py
Author: Nagi
Date: 5/1/2026

Description:
    Variable = A container for a value (string, integer, float, boolean)
    A variable beaves as if it was the value it contains.
"""

#The variable is first_name and its assigned the value you give after the equal sign
#This is all the variables created as Strings
first_name = "Nagilynn"
food = "Sushi"
email = "Nagilynn@moondrop.com"

#Test my first use of a variable - first_name
print(first_name)

#You can use the f-string (formatted string literals) if you want to include a text Ex: print(f"text {variable}")
print(f"Hello {first_name}")

#Testing second use of a variable - food
print(f"You like {food}")

#Testing third Variable created - email
print(f"Your email is: {email}")

#-------------------------------------------------------------------------------------------

#Integers - is a whole number
#This is variables created as integers
age = 25
quantity = 3
num_of_students = 30 


#Testing first use of the integer variable - age
print(f"You are {age} years old")

#Testing second use of the integer variable - quantity
print(f"You are buying {quantity} items")

#Testing third use of the integer variable - num_of_students
print(f"Your class has {num_of_students} students")

#Integers can be use in arithmatic but not strings
#Float - Floating point number pretty much numbers with decibles

#This is variables created as floats
price = 10.99
gpa = 3.2
distance = 5.5

#Testing first use of the float variable - price
print(f"The price is ${price}")

#Testing second use of the float variable - age
print(f"Your gpa is: {gpa}")

#Testing third use of the float variable - distance
print(f"You ran {distance}km")

#-------------------------------------------------------------------------------------------

#Boolean - can be a condition of true or false

#This is variables created as booleans
is_student = True
for_sale = False
is_online = True

#Testing first use of boolean variable - 
print(f"Are you a student?: {is_student}")

#Usually not done directly but more internally like using if/else statements
if is_student:
    print("You are a student.")
else:
    print("You are NOT a student.")
#It will print you are a student because the variable is True

#Testing second use of boolean variable - for_sale
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

#Testing third use of boolean variable - is_online
if is_online:
    print("You are online")
else:
    print("You are offline")