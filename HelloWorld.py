from math import *
from question import Question
import os



# print("Hello World")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# character_name = "John"
# character_age = 35
# print("There once was a man named " + character_name + ", ")
# print("he was "  + str(character_age) + " years old.")

# print(character_name.lower())
# print(character_name.upper())
# print(character_name.upper().isupper())
# print(character_name.islower())
# print(len(character_name))
# print(character_name[0])
# print(character_name[1])
# print(character_name[2])
# print(character_name[3])
# print(character_name.index("h"))
# print(character_name.replace("John", "Mike"))

# print(3*(4.567+5))
# print(10%3)

# print(abs(-5))
# print(pow(2,3))
# print(max(2,3))
# print(min(2,3))
# print(round(2.567))

# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(36))

# name = input("How are you? Please enter your name: ")
# age = input("Please enter your age: ")

# print(name + ", it is a pleasure to meet you! You are "+str(age)+" years old.")

# num_1 = input("Enter your first number: ")
# num_2 = input("Enter your second number: ")
# result = float(num_1)+ float(num_2)
# print(result)

# friends = ["Tom", "Jill", "Jack", "Tony", "Jim", "Toby"]
# lucky_numbers = [1, 45, 423, 98, 90, 100]
# print(friends)
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[2:5])
# friends.extend(lucky_numbers)
# print(friends)

# friends.append("Creed")
# print(friends)

# friends.insert(1,"Kelly")
# print(friends)

# friends.remove("Jim")
# print(friends)

# friends.pop()
# print(friends)

# print(friends.index("Toby"))

# print(friends.count("Toby"))

# lucky_numbers.sort()
# print(lucky_numbers)

# lucky_numbers.reverse()
# print(lucky_numbers)

# friends2 = friends.copy()
# print(friends2)

# friends.clear()
# print(friends)

# coordinates = (4,5)
# print(coordinates[1])


# def say_hi():
#     select = input("Select 1 to say Hello or 2 to say Adios Amigo!")

#     if select == "1":
#        return print("Hello!!!!!")
#     else:
#         return print("Adios Amigo!")

# say_hi()

# def fizzBuzz():
#     num = int(input("Please enter a FizzBuzz Number: "))
#     for i in range(1, num+1):
#         if(i%5==0 and i%3==0):
#             print("FizzBuzz")
#         elif i%5 == 0:
#             print("Buzz")
#         elif i%3 == 0:
#             print ("Fizz")
#         else:
#             print(i)

# fizzBuzz()

# num1 = float(input("Enter num1: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter num2: "))

# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "/":
#     print(num1/num2)
# elif op == "*":
#     print(num1*num2)
# else:
#     print("What the hell are you doing?")

# monthConversions = {
#     "Jan":"January",
#     "Feb":"February",
#     "Mar":"March",
#     "Apr":"April",
#     "May":"May",
#     "Jun":"June",
#     "Jul":"July",
#     "Aug":"August",
#     "Sep":"September",
#     "Oct":"October",
#     "Nov":"November",
#     "Dec":"December"   
# }

# print(monthConversions.get("Luv", "Not a valid key"))

# i = 1
# while i <= 10:
#     print(i)
#     i+=1

# print("Done with loop")

# secret_word = "giraffe"
# guess = input("What is the secret word???")
# guess_count = 0
# guess_limit = 5

# while guess_count < guess_limit:
#     if guess != secret_word:
#         guess = input("Try again :(")
#         guess_count += 1
#     else: guess_count = 5
 
# print("Congratulations!! The secret word was \"Giraffe\"")

# print(2**3)

# def powerRaiser(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result*base_num
#     return result
        
# print(powerRaiser(2,4))

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# # print(number_grid[2][2])

# for row in number_grid:
#     for column in row:
#         print(column)

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#            if letter.isupper():
#                 translation = translation + "G"
#            else:
#                 translation = translation + "g"

#         else:
#             translation = translation + letter
#     return translation
            
# print(translate("To Be or not to Be"))

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")

# text_file = open("test.txt", "r")
# print(text_file.readlines())
# text_file.close()

# employee_file = open("test1.txt","w")
# employee_file.write("\nI just wrote this!")
# print(employee_file.readlines())
# employee_file.close()

# os.remove("test1.txt")


class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else: 
            return False

# question_prompts = [
#     "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n",
#     "What color are bananas?\n(a) Red\n(b) Yellow\n(c) Orange\n",
#     "What color are oranges?\n(a) Red\n(b) Purple\n(c) Orange\n"

# ]

# questions = [
#     Question (question_prompts[0], "a"),
#     Question (question_prompts[1], "b"),
#     Question (question_prompts[2], "c")

# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score+=1
#     print("You got "+str(score)+" out of "+str(len(questions))+ " right.")
    

# run_test(questions)


