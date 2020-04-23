# from math import *

# print("Hello world")

# print("     /|")
# print("    / |")
# print("   /  |")
# print("  /__ |")

# character_name = "John"
# character_age = 50.578833
# is_male = False
# print("There once was a man named "+character_name+",")
# print("he was 70 years old.")

# character_name = "Mike"
# print("He really liked the name "+character_name+",")
# print("but didn't like being ",character_age)


# # Working with strings

# phrase = "Giraffe Academy"
# print("Giraffe\nAcademy")
# print("Giraffe\"Academy")#scape
# print(phrase + "is cool")
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper()) #verification
# print(phrase.upper().isupper())
# print(len(phrase)) #how many 
# print(phrase[0]) #grab a specific character
# print(phrase.index("G")) #specific character
# # print(phrase.index("z")) #error
# print(phrase.replace("Giraffe", "Elephant"))

# # Working with numbers

# print(-2)
# print(5.9)
# print(3 + 4.5)
# print(3 * (4 + 5) )
# print(10 % 3)
# my_num = 5
# print(my_num)
# print(str(my_num)+" my favorite number")
# my_num = -5
# print(abs(my_num))
# print(pow(3,2))
# print(max(4, 6))
# print(min(4,6))

# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(3.7))

# #Getting input from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello "+name+"! You are "+age)

# # Build basic calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# #result = num1 + num2 #string concatenation ERROR
# result = int(num1) + int(num2) #doesn't work with float
# result = float(num1) + float(num2)

# print(result)

# Mad Libs Game

# print("Roses are red")
# print("Violets are blue")
# print("I love you")

# color = input("Enter a color:")
# plural_noun = input("Enter a plural noun:")
# food = input("Enter a food:")

# # print("Roses are {color}")
# # print("{plural noun} are blue")
# # print("I love {food}")

# print("Roses are "+color)
# print(plural_noun+" are blue")
# print("I love "+food)

# List

# friends = ["Kevin", "Karen", "Jim", "Toby", "Oscar"]

# # friends = ["Kevin", 2, False]

# print(friends)
# print(friends[-1]) #back of the list
# print(friends[1:])
# print(friends[1:3])
# friends[1] = 'Mike'
# print(friends[1])

#List functions
# 
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends.extend(lucky_numbers)
# print(friends)
# friends.append("Creed")
# print(friends)
# friends.insert(1, "Kelly")
# print(friends)
# friends.remove("Jim")
# print(friends)
# friends.pop()
# print(friends)
# print(friends.index("Kevin"))
# friends.sort()
# print(friends)
# lucky_numbers.reverse()
# print(lucky_numbers)
# friends2 = friends.copy()
# print(friends2)
# friends.clear()
# print(friends)

#Tuples

# coordinates = (4, 5) #for data that never change
# # coordinates = [ (4, 5), (6, 5), (4, 1)] #list of tuples
# # coordinates[1] = 10 #don't do this
# print(coordinates[1])

# #Functions 

# def say_hi(name, age):
#     print("Hello "+name+" you are "+str(age) )
# print("Top")
# say_hi("Ann", 12)
# say_hi("Tim", 45)
# print("Bottom")

# def cube(num):
#    return num * num * num

# result = cube(3)
# print(result)

# # If statements

# is_male = False
# is_tall = False

# # if is_male and is_tall:
# if is_male or is_tall:
#     print("You are a male or tall")
# elif is_male and not(is_tall):
#     print("You are a short male")
# else:
#     print("You are neither male nor tall")

# #If statements using comparison

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(3, 4, 5))

#Calculator 

# num1 = float(input("Enter first number:"))
# op = input("Enter first operator:")
# num2 = float(input("Enter second number:"))

# if op == '+':
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '/':
#     print(num1/num2)
# elif op == '*':
#     print(num1 * num2)
# elif op == '%':
#     print(num1 % num2)
# else:
#     print("Invalid operator")

# Dictionary

# month_conversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(month_conversions['Nov'])
# print(month_conversions.get("Dec", "Not valid key"))

# #While loops

# i = 1

# while i <= 10:
#     print(i)
#     i += 2
# print("Done with loop")

# Building a guessing game

# secret_word = 'giraffe'
# guess = ''
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if  guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if not(out_of_guesses):
#     print("You win!")
# else:
#     print("Out of guesses, You lose!")

# For 

# for letter in "Giraffe Academy":
#     print(letter)

# friends = ["Jim", "Karen", "Kevin"]

# for friend in friends:
#     print(friend)

# for index in range(10):
#     print(index)

# for index in range(3,10):
#     print(index)

# for index in range(len(friends)):
#     print(friends[index])

# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("not first")

# # Exponent function

# print(2**3)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in  range(pow_num):
#         result = result *  base_num
#     return result

# print(raise_to_power(2, 3))
# base_num = int(input("Enter base number: "))
# pow_num = int(input("Enter power number: "))
# print(raise_to_power(base_num, pow_num))

# 2D Lists

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ] 

# print(number_grid[0][0])

# print(number_grid[0])

# for row in number_grid:
#     # print(row)
#     for col in row:
#         print(col)

# Build a translator

# Giraffe language
# vowels -> g
# dog -> dgg

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))

#Comments

'''
Comment
Comment
'''

# print("Comments are fun")

#Try expect

# try:
#     value = 10 / 0 #error
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

# Reding files

#r+ read and write
#a append new information
#r read
#write
# employee_file = open("employees.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readlines())
# print(employee_file.readline())
# print(employee_file.readlines()[1])

# for employee in employee_file.readlines():
#     print(employee)

# employee_file.close()

# employee_file = open("employees.txt", "a")
# employee_file.write("\nTobias - Human resources")
# employee_file.write("\nKelly - Customer service")

# employee_file = open("index.html", "w")

# employee_file.write("<p> Welcome!</p>")

#Modules

# import useful_tools
# import docx

# print(useful_tools.roll_dice(10))

#Class and objects

# from Student import Student

# student1 = Student("Jim", "Business", 3.1, False)
# student2 = Student("Kim", "Art", 2.1, True)

# print(student1.name)
# print(student2.name)

# from Question import Question

# question_prompts = [
#         "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#         "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#         "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got "+str(score) + "/" + str(len(questions)) + "correct")

# run_test(questions)


#Object functions

# from Student import Student

# student1 = Student("Jim", "Business", 3.5, False)
# student2 = Student("Kim", "Art", 2.1, True)

# print(student1.on_honor_roll())

# from Chef import Chef
# from ChineseChef import ChineseChef

# myChef = Chef()
# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()

#Python interpretor