"""
Project Name: Madlibs
File Name: madlibs_game.py
Author: Nagi
Date: 5/6/2026

Description:
    Madlibs Game - word game where you create a story by filling in the blanks with random words.

"""
#Listing all the variables with the option where users can input their answers 
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

#This will print sentences (the story) with the answer that the user has given
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
