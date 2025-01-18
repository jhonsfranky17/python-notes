# this is my first python program
# print("Hello guys!")
# print("I like Biriyani") 

# variables and types

# strings
# first_name = "Franklin"
# food = "Biriyani"
# email = "franklinjettyjohnson6@gmail.com"

# print(first_name)
# print(f"Hello {first_name}")
# print(f"I like {food}")
# print(f"My email is {email}")

# integers
# age = 24 
# print(f"I am {age} years old")

# float
# price = 10.99

# print(f"The price is {price}")

# boolean
# is_student = True

# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")

# typecasting - the process of converting a variable from one data type to another
# str(), int(), float(), bool()

# name = "Franklin Jetty Johnson"
# age = 24
# gpa = 3.2
# is_student = True

# age = str(age)
# age += "1"

# print(type(age))
# print(age)

# input() = A funtion that prompts the user to enter data. Returns the enteres data as a string

# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) # typecasting entered string type to int

# age += 1

# print(f"Hello {name}")
# print("Happy Birthday!")
# print(f"You are {age} years old")

# built-in math functions

# x = 3.14
# y = -1
# z = 5

# result = round(x) # rounds off to the nearest integer
# result = abs(y) # returns the value without sign
# result = pow(x, 3) # returns the base times the power
# result = max(x, y, z) # returns the maximum among the values
# result = min(x, y, z) # returns the minimum among the values

# print(result)

# import math

# print(math.pi) # returns the value of pi
# print(math.e) # returns the value of e
# print(math.sqrt(36)) # returns the square root of a number
# print(math.ceil(9.1)) # returns the rounded up value
# print(math.floor(9.9)) # returns the rounded down value

# if = Do some code only if some condition is true 
# else do something

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote in INDIA!")
# elif age < 0:
#     print("You are not born yet!")  
# else:
#     print("Sorry, you are not eligible to vote in INDIA")

# logical operators = evaluate multiple conditions (or, and , not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

# logical or = or
# temp = 30
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# logical and = and

# is_sunny = True

# if temp >=28 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny")
# elif temp <=0 and is_sunny:
#     print("It is cold outside")
#     print("It is sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is sunny")

# logical not = not

# if temp >=28 and not is_sunny:
#     print("It is hot outside")
#     print("It is cloudy")
# elif temp <=0 and not is_sunny:
#     print("It is cold outside")
#     print("It is cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is cloudy")

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

# num = 5

# print("Positive" if num > 0 else "Negative")

# string methods

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# print(len(name)) # returns the length of the string
# result = name.find("n") # returns the index (starts at 0) of the first occurence of the character
# result = name.rfind("n") # returns the index of the last occurence of the character
# If the given character is not found in the string, python returns -1
# result = name.capitalize() # capitalizes the first character of the string
# result = name.upper() # capitalizes the entire string
# result = name.lower() # returns lowercase string
# result = name.isdigit() # returns true if the string only contains digits
# result = name.isalpha() # returns true if the string only contains alphabets
# result = phone_number.count("9") # counts the number of given character in the string
# result = phone_number.replace("9", "6") # replaces one character with another
# result = phone_number.startswith("0") # returns true if the string starts with the desired character
# result = phone_number.endswith("0") # returns true if the string ends with the desired character

# print(result)

# help(str) # returns all the string 

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step] 

# credit_number = "123-34343-2313-323"

# print(credit_number[0]) # returns the first character of the string 
# print(credit_number[:4]) # returns the characters till the end index (excluded) from the beginning if the start index is not mentioned
# print(credit_number[5:9]) # returns the characters within the range
# print(credit_number[5:]) # returns all the characters if from the start index if the end is not mentioned
# print(credit_number[-1]) # returns the last character, negative indices return characters from the end
# print(credit_number[::3]) # returns every 3rd character starting from the first character (included)
# print(credit_number[::-1]) # reverses the string, add -1 at the end to reverse the given string

# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.23

# print(f"Price 1 is {price1:.1f}")
# print(f"Price 2 is {price2:.1f}")
# print(f"Price 3 is {price3:.1f}")
# you can also use multiple specifiers together

# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# while is kind of "if statement" (executes the statements below it only once) but executes the statements until the condition evaluates to false

# for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc

# for i in range(1, 11): # end exclusive
#     print(i)

# for i in reversed(range(1, 11)): # counts from backwards, enclose the range function within the reversed() 
#     print(i)

# for i in range(1, 11, 2): # returns every 2nd element starting from 'start'
#     print(i)

# credit_card = "1233-2243-232-343"

# for i in credit_card: # iterates over every element of the string
#     print(i)

# continue, break keywords work in the same manner as it works with other programming languages

# import time

# my_time = int(input("Enter the time in seconds: "))

# for i in range(0, my_time):
#     print(i)
#     time.sleep(1) # Delay execution for a given number of seconds. The argument may be a floating-point number for subsecond precision.

# print("TIME'S UP!") 

