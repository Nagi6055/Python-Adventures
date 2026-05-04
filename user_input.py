"""
Project Name: User Input
File Name: user_input.py
Author: Nagi
Date: 5/4/2026

Description: This program will be taking the user inputs using a prompt for them to answer then we will e doing some exercises.
    input() = A function that prompts the user to enter data
                Returns the entered data as a string 
"""

#A prompt is needed, so we need to tell the user what we need to type in. We can also make a variable with the user input.
name = input("What is your name?: ")
age = int(input("How old are you?: "))

#This will help make the user input age from str to int or you can make the typecast to the user input
#age = int(age)
#adds age by one
age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")

#----------------------------------------------------Exercises 1-----------------------------------------------------------#

#Exercise 1 Rectangle Area Calculation 

#We will take the users input and turn them into floats
w = float(input("Enter your width: "))
l = float(input("Enter your lenght: "))

#The equation for finding the Area
A = w * l 

#to add a subscript 2 -> make sure numlock is on, hold alt, then type 0178 on Windows
#This will print the statement with the answer for the area.
print(f"The area is: {A}cm")


#----------------------------------------------------Exercises 2-----------------------------------------------------------#

#Exercise 2 Shopping Cart Program

#Will be getting the user input in different types
#as a str
item = input("What item would you like to buy?: ")
#as a float
price = float(input("What is the price?: "))
#as a int
quantity = int(input("How many woud you like?: "))

#This code is the equation to get the total of the price with quantity
total = price * quantity

#Will pretty much repeat what the customer has inputed 
print(f"You have bought {quantity} x {item}/s")
#Printing out the total
print(f"Your total is: ${total}")



