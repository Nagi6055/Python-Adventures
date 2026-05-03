"""
Project Name: Type Casting
File Name: type_casting.py
Author: Nagi
Date:5/3/2026

Description:
    Typecasting = the process of converting a variable from one data to another.
                    str(), int(), float(), bool()
"""
#This is our lis of different types of variables
name = "Nagilynn"
age = 25
gpa = 3.2
is_student = True

#You could get the data type of a variable or a value by using the type function, then pass in a value or variale.
#if you just type the following you wont get an output

type(name)

#To get and output you must do this:
#First type you will get str
print(type(name))

#Second type you will get int
print(type(age))

#Third type you will get float
print(type(gpa))

#Fourth type you will get bool
print(type(is_student))

#Using these type cast functions you can convert from one data type to another.

#converting gpa to integer
#reassigning gpa -> use int function to type cast to an integer -> then pass in my gpa
gpa = int(gpa)
print(gpa)

#converting age to float
#age = float(age)
#print(age)

#converting age to a string (make sure to comment the last code to run the next part)
age = str(age)
print(age)
#when running this code it will look like a int but its actually a string
#Proof:
print(type(age))

#this will make a difference because if we add 1 to age we will get an error because age is a str not an int now
#but if we make 1 a str we will get 25.01 or 251 if we comment out the flat code part
age += '1'

print(age)

#converting name to a bool
name = bool(name)
print(name)

#if we change the name we will keep getting true but if the variable is empty it will give False
#can be use to check if someone inputs their name which gives True but if they dont give their name we can get false
