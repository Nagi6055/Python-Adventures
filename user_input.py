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

w = float(input("Enter your width: "))
l = float(input("Enter your lenght: "))

A = w * l 

#to add a subscript 2 -> make sure numlock is on, hold alt, then type 0178 on Windows
print(f"The area is: {A}cm")


#----------------------------------------------------Exercises 2-----------------------------------------------------------#

#Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many woud you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")



