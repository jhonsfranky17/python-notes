# Python complete notes
# Go through each topic/definition and remove the comment from the code below to observe the output of the explained concepts.

# Buckle up soldier, because we're about to start an exciting journey packed with fun and learning!!!

# Imagine you're giving instructions to your friend on how to build a LEGO castle. You would tell them exactly what to do, step by step—like "put the red block here" and "add a yellow piece there."

# Now, instead of talking to a person, you want to give instructions to a computer to do something like adding numbers, showing pictures, or playing music. But here’s the catch: the computer doesn't understand regular language like English or Spanish. It only understands a special language, that’s where programming languages come in!

# A programming language is a special set of instructions that we use to talk to computers. These instructions tell the computer what to do, just like how you give instructions to your friend to build something.

#  Why do we need Programming Languages?

# Computers are super powerful, but they only do what they're told in the right way. We need programming languages to tell them exactly what we want them to do!
# Want to build a game, a website, or an app? You need a programming language to make it happen! (Sorry, no shortcuts here! If you were thinking of using WordPress or Shopify, just don’t! Shortcuts are for the weak, chin up, soldier! Let’s do this the right way, no easy way out!)
# Programming languages let us create tools that solve problems, like helping people talk to each other online, calculating numbers, or even making robots move! (sounds interesting right?)

# Alright, enough chit-chat, let's get down to work!

# print function (Starting with the print() function is like learning how to speak in a new language. When you're learning Python, print() helps you talk to the computer and see the results of your code. Without it, you'd be writing all these cool instructions, but the computer wouldn’t tell you what's happening!)

# Imagine you have a magic speaker that can say whatever you tell it to. In Python, the print() function (function is nothing but a block of code that you can reuse 'n' number of times whenever you want) is like that magic speaker, it displays messages on the screen.
# Think of print() as your "hello world" moment. It’s like meeting a new friend for the first time, once you know how to communicate with Python using print(), everything else becomes a lot easier and more fun!

# The print() function prints the specified message to the screen, or other standard output device.
#         The message can be a string, or any other object, the object will be converted into a string before written to the screen.

# remove the comments below to see the magic of print()
# print("Hello guys!")
# print("I like Biriyani") 

# I asked you to remove the comments but what exactly are they?
# Imagine you're writing a note to yourself in a diary or on a piece of paper. You might write down something like, “Hey, don’t forget to buy ice cream later!” 🍦 It's something just for you to remember, but when someone else reads your diary, they don’t need to worry about your ice cream plans.

# Well, in Python, comments are just like that note to yourself! They’re a way to leave messages in your code so you can remember things or explain what your code does—without Python trying to run those messages!
# Two types:
# Single-line = If you want to leave a quick note on one line, use the # symbol.
# Multi-line = If you have a longer message or explanation, you can use triple quotes """ or ''' for multi-line comments.
# Get ready to leave notes in your code like a secret agent!

# input function
# Imagine you're playing a game where you need to ask your friend for their name. You shout, "Hey, what's your name?" and they reply. That’s exactly what the input() function does, it lets the computer ask you for information! 

# When you use input(), it pauses your program and waits for the user to type something in (sometimes I wish the people around me were computers, at least they'd wait patiently for me to respond like the input() function. But nope, they keep talking while I'm still processing!). Once they hit Enter, whatever they typed gets returned by input() as a string.

# name = input("What's your name? ")
# print(name)

# input() is super important because it’s how you get user interaction. Without it, the computer would be like a robot with no clue about what the user wants!

# Variables and Types

# Imagine you have a magic box where you can store different things, like a number, a word, or even a list of things. You can give this box a name so you can find it later.
# In programming, this magic box is called a variable. It holds information that the computer can use later.

# Types

# Integer(int) = Think of this like a box that holds only whole numbers (no decimals).

# age = 24 
# print(f"I am {age} years old") 

# Notice here I used formatted string or commonly known as f-string to incorporate my variable within the double quotation so that it prints the value which is stored in the variable. Python will replace {age} with the value stored in the variable age.
# You put a 'f' before quotes to make it a f-string and wrap the variable name within curly braces to get the value stored inside it.
# There are tons of ways to grab the value from a variable, but let’s be real, "f-strings" are the cool kids on the block! It’s all about personal preference, but hey, stick to one, just like you promised your partner you’d stay loyal! 

# Float(float) = This box holds numbers with decimals, like prices or temperatures.

# price = 10.99
# print(f"The price is {price}")

# String(str) = This box stores words, names, or any sequence of characters (anything inside quotes).

# first_name = "Franklin"
# food = "Biriyani"
# email = "jhonsfranky17@gmail.com"

# print(first_name)
# print(f"Hello {first_name}")
# print(f"I like {food}")
# print(f"My email is {email}")

# Boolean(bool) = This is a Yes/No box that stores only True or False

# is_student = True

# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")

# Typecasting = The process of converting a variable from one data type to another (text book definition but we don't want this :), I'll break it down for you )
# Imagine you have different types of boxes:
# A number box (for numbers)
# A word box (for text)
# A decimal box (for decimal numbers)
# Sometimes, you need to change the type of box to fit your needs. Typecasting (or Type Conversion) helps you do this in Python!

# Here are some typecasting functions in Python that lets you change the type of a variable from one to another.
# str(), int(), float(), bool(), list()[don't slam your heads against the wall trying to figure out lists, just hold your horses, soldier! I've got your back!]

# By default, Python treats all user inputs as strings, but you can easily change them to other types using typecasting.
# Even if you type a number, like 123, Python sees it as the string "123". If you want to work with numbers, you'll need to typecast them into an integer or float.

# name = "Franklin Johnson"
# age = 24
# gpa = 8.4
# is_student = True

# print(type(age)) # type() returns the type of the variable/value.
# age = str(age) # typecasting integer to string using str()
# age += "1" # Adding "1" to the string "24" (now age is "241", note that I used '+=' which is a shortcut for age = age + "1")

# print(type(age)) # Here the type of age was integer initially, but changed to string.(Don't believe me? Go ahead, hit run and watch the magic happen!)
# print(age)

# Built-in functions

# Built-in functions in Python are pre-written functions that come with the language. They’re like tools you can grab from a toolbox without needing to build them yourself.

# Think of it this way: If you’re playing a video game and you need to open a door, you don’t have to code the door opening mechanics yourself. Python already gives you a key to open the door whenever you need it, without any extra effort!

# These built-in functions are super handy because they allow you to perform common tasks quickly and easily. You don't have to reinvent the wheel every time you want to do something simple like adding numbers or converting data types.

# Ah, I know what you're thinking - "Do I really need to tell you some examples of built-in functions?" Come on, you already know them! input(), print(), type(), they're like old friends by now. I mean, if you don’t know them yet, where have you been?

# But okay, for the sake of a quick refresher, let's just say these are your everyday tools in the Python toolkit. So next time when you're stuck, just think of these buddies, they've got your back just like me :)!

# built-in math functions

# Built-in math functions in Python are like pre-built tools in a toolbox that help you do mathematical operations easily. Instead of writing complex formulas from scratch, you can just use these functions to perform things like addition, subtraction, or even more advanced math like square roots or trigonometric calculations.

# Python has a math module that contains many of these functions. Think of it as a magic library that makes your calculations super easy and fast. 

# import math # importing math module (modules are nothing but code in a separate file, you import or incorporate them in your program)

# print(math.pi) # returns the value of pi
# print(math.e) # returns the value of e
# print(math.sqrt(36)) # returns the square root of a number
# print(math.ceil(9.1)) # returns the rounded up value
# print(math.floor(9.9)) # returns the rounded down value

# x = 3.14
# y = -1
# z = 5

# result = round(x) # rounds off to the nearest integer
# result = abs(y) # returns the value without sign
# result = pow(x, 3) # returns the base times the power
# result = max(x, y, z) # returns the maximum among the values
# result = min(x, y, z) # returns the minimum among the values

# print(result) # make sure you uncomment one result at a time to see the output of different functions

# Conditional Statements

# Alright, imagine you’re standing at a fork in the road. One path leads to a candy shop and the other leads to a vegetable garden. Now, which path should you take? Well, it all depends on one thing: what you decide!

# This is where conditional statements come into play! They're like your decision-making superpower in Python. They let your program choose between different paths based on certain conditions.

# In Python, we use keywords like "if", "elif" (else if), and "else" to make those decisions.
# Keywords = reserved words by any programming language. You can not use a keyword as a name for your variable, function, etc.. In short, you can't use keywords as identifiers.
# Identifiers = name of your variable, function, etc. (Rules for naming identifiers: https://www.google.com/search?q=identifier+naming+rules+in+python&oq=identifier+naming+&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBggCEEUYOTIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIICAYQABgWGB4yCAgHEAAYFhgeMggICBAAGBYYHjIICAkQABgWGB7SAQkxMDk1NWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8)

# if = executes the code below only if some condition is True 
# syntax: if condition:
            # statement

# else = executes the code below only if all the condition evaluates to False
# syntax: if condition:
            # statement
        #   else:
            # statement

# elif = checks another condition if the condition in "if" evaluates to False
# syntax: if condition:
#            statement
#         elif condition:
#            statement
#         elif condition:
#            statement
#         else:
#            statement

# Note that conditions always evaluate to either True or False values (Boolean: now you know what a Boolean is. You're welcome!)

# age = int(input("Enter your age: ")) # typecasting to integer type because remember input() treats everything as strings

# if age >= 18:
#     print("You are eligible to vote in INDIA!")
# elif age < 0:
#     print("You are not born yet!")  
# else:
#     print("Sorry, you are not eligible to vote in INDIA")

# Logical Operators:
# Alright! Let’s talk about logical operators in Python. Think of them like the superheroes of the decision-making world. They help you combine multiple conditions together and make your program super smart.

# Imagine you're trying to decide whether to go out for a walk. Here's how it might go:

# You ask yourself: "Is it sunny?"
# You also ask: "Do I have enough time?" 
# Finally, you ask: "Am I feeling lazy?" 
# Now, to decide if you're going out, you’ll need to combine these conditions!
# Logical operators are like connectors in your decision-making. They help you combine different questions (conditions) into a single, bigger question.

# The three main logical operators are:
# or = Only one condition needs to be true for the whole thing to be true.
# and = Both conditions need to be true for the whole thing to be true.
# not = Reverses the condition. If it's true, it becomes false; if it's false, it becomes true.

# logical or: and

# temp = 30
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# logical and: and

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

# logical not: not

# if temp >=28 and not is_sunny:
#     print("It is hot outside")
#     print("It is cloudy")
# elif temp <=0 and not is_sunny:
#     print("It is cold outside")
#     print("It is cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is cloudy")

# Conditional Expressions/ Ternary Operators = 
# A one-line shortcut for the if-else statement
# Print or assign one of two values based on a condition
# X if condition else Y

# num = 5

# print("Positive" if num > 0 else "Negative")

# String Methods
# They help you manipulate strings (a.k.a. text) in super cool ways without breaking a sweat! Think of them as your little helpers that take care of the boring stuff, so you can focus on having fun with your code.

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
# The list goes on! If you want to know all the string methods, print what's written below
# help(str) # returns all the string methods

# Indexing:
# Alright, indexing in Python is like having a treasure map for a string, list, or any collection where you need to find specific items. It helps you pinpoint exactly where things are located, whether you're looking for the first letter of a word or the third item in a list.
# In Python, indexing is the way we access individual elements in sequences like strings, lists, or tuples. It’s like going through the pages of a book and pointing directly at the one you want to read. 

# We use the indexing operator "[]" to access individual elements
#            [start : end : step] 

# credit_number = "123-34343-2313-323"

# print(credit_number[0]) # returns the first character of the string 
# print(credit_number[:4]) # returns the characters till the end index (excluded) from the beginning if the start index is not mentioned
# print(credit_number[5:9]) # returns the characters within the range
# print(credit_number[5:]) # returns all the characters if from the start index if the end is not mentioned
# print(credit_number[-1]) # returns the last character, negative indices return characters from the end
# print(credit_number[::3]) # returns every 3rd character starting from the first character (included)
# print(credit_number[::-1]) # reverses the string, add -1 at the end to reverse the given string

# Format Specifiers:
# Alright, format specifiers are like your personal stylists for strings in Python! They help you control how values (like numbers, dates, etc.) appear in your output. Think of them as a way to tell Python, "Hey, I want this value to look a certain way!" and Python says, "Got it!" 

# syntax: {value:flags} format a value based on what flags are inserted

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

# Loops (Trust me, you’ll thank me for this topic for the rest of your career!)

# Imagine you want to do something over and over again, like practicing your dance moves, or maybe eating pizza (who wouldn't want to do that?). Well, loops in Python let you repeat tasks without writing the same thing again and again. Think of a loop as your personal repetition machine!
# In programming, loops are like repetitive tasks that you want to do over and over, but you don’t want to type the same thing repeatedly. Instead, you tell: “Hey, I want you to do this X number of times”, and the language listens to you. 
# Loops are like the secret sauce in programming, no matter which language you’re using! I work with languages like Java, TypeScript, C, and C++ (just a humble flex), and guess what? Loops are in all of them!

# There are mainly two loops in python:
# while loop and for loop

# while loop = executes the code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# while is kind of "if statement" ("if" executes the statements below it only once) but "while" executes the statements until the condition evaluates to False

# for loop = executes a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc
# It's like saying, "Do this for every item in the list, and we’ll repeat it until we’ve done everything." Think of it as doing homework problems one by one.

#  syntax: for variable in iterable:
#              code to be executed

# for i in range(1, 11): # end exclusive
#     print(i) # prints the numbers from 1 to 10

# for i in reversed(range(1, 11)): # counts from backwards, enclose the range function within the reversed() 
#     print(i)

# for i in range(1, 11, 2): # returns every 2nd element starting from 'start'
#     print(i)

# credit_card = "1233-2243-232-343"

# for i in credit_card: # iterates over every element of the string
#     print(i)

# continue, break keywords work in the same manner as it works with other programming languages
# continue = ignores the statements below the keyword "continue"
# break = breaks from the loop

# import time # importing time module

# my_time = int(input("Enter the time in seconds: "))

# for i in range(0, my_time):
#     print(i)
#     time.sleep(1) # delays execution for a given number of seconds. The argument may be a floating-point number for subsecond precision.

# print("TIME'S UP!") 

# nested loop = A loop within another loop (outer, inner)
# syntax:
#               outer loop:
#                   inner loop:

# for i in range(3): # iterates for 3 times
#     for j in range(1, 10): # iterates from 1 to 9
#         print(j, end = " ") # usually end of a print statement is new line, but we can modify it with the help of "end" argument (Hang tight! We’ll dive into arguments and parameters soon, but first, let’s understand some basics.)
#     print() # prints new line outside inner loop

# Collection:
# In programming, a collection refers to a group or container that holds multiple items or elements. It’s like a box where you can store different things (like toys, books, or candy), and each item inside the box is an element. The collection itself is a data structure that makes it easier to manage and manipulate these items.
# Single "variable" used to store multiple values

# Types:

# List: 
#  A collection of ordered items. You can think of it like a row of books on a shelf, where each book is in a specific place, and you can access them by their position (index).
# represented by [], ordered and changeable. Duplicates OK

# Set:
# A collection of unique items (no duplicates allowed). It's like a box where you can only put one of each toy, no duplicates.
# represented by {}, unordered and immutable, but Add/Remove is allowed whereas, duplicates are not allowed.

# Tuple:
# An ordered collection like a list, but immutable, meaning once you put something in a tuple, you can’t change it. It’s like a sealed box—once it’s packed, it’s done.
# represented by (), ordered and unchangeable. Duplicates are allowed. Faster than list

# Dictionary:
# A collection of key-value pairs. Think of it as a contact list where each name (key) is paired with a phone number (value).
# represented by {}, ordered and changeable, No duplicates are allowed

# List

# fruits = ["apple", "banana", "grape", "coconut"]
# print(fruits) # prints the entire list 
# print(fruits[3]) # prints the item at the 3rd index, here coconut. Also remember indexing operator has [start : end : step]

# for fruit in fruits: # iterates through the list items one at a time
#     print(fruit)

# print("apple" in fruits) # checks whether the element is present in the list or not. Returns a boolean value.
# fruits.append("pineapple") # to add an element to the end of the list, use append function
# fruits.remove("pineapple") # to remove an element from the list, use remove function
# fruits.insert(0, "pineapple") # to insert an element at the desired index, use insert function
# fruits.sort() # sorts the list in ascending order
# fruits.reverse() # reverses the list. If you want to sort the list in descending order, you sort the list first and then use the reverse function to reverse the list.
# fruits.clear() # to clear a list
# fruits.index("apple") # to find the index of the desired element in the list
# fruits.count("apple") # to count the number of times an element appears in the list, use count function as list supports duplicates.

# Set

# fruits = {"apple", "banana", "pineapple", "grape"}
# print(fruits) # unordered when printing

# fruits.add("orange") # adds an element to the set
# fruits.remove("apple") # removes an element from the set
# fruits.pop() # removes the first element from the set but it is unordered

# Tuple

# fruits = ("apple", "banana", "pineapple", "grape")
# print(len(fruits)) # returns the length of the tuple
# print(fruits.index("apple")) # returns the index of the element in the set
# print(fruits.count("apple")) # returns the count of the element

# Jan 20th, 2025

# 2D List = Made up of lists within list

# fruits = ["apple", "oranges", "banana"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats] # one way of creating a 2D list
# groceries = [["apple", "oranges", "banana"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]
#              ] # another way of creating a 2D list

# print(groceries[0][3]) # to access an element in a 2D List, we use two indexing operators (think of 2D Lists as Matrices)

# You can do the same with tuple and set

# Dictionary:

# capitals = {
#     "USA" : "Washington DC",
#     "India" : "New Delhi",
#     "China" : "Beijing",
#     "Russia" : "Moscow"
# }

# print(capitals.get("India")) # accessing values in a dictionary using the key
# capitals.update({"Germany" : "Berlin"}) # to add a new {key:value} pair to the dictionary
# capitals.update({"USA" : "Detroit"}) # you can also use the update method to update the existing {key:value} pair
# capitals.pop("China") # to remove a {key:value} pair from the dictionary, use pop method
# capitals.popitem() # to remove the latest {key:value} pair added
# capitals.clear() # to clear the dictionary

# keys = capitals.keys() # returns all the keys of the dictionary

# for key in keys: # iterating through every key of the dictionary
#     print(key)

# for value in capitals.values(): # iterating through all the values in the dictionary
#     print(value)

# items = capitals.items() # returns a 2D list of tuples like object providing a view on the dict's items

# for key, value in items: # iterating through each key value pair and printing it
#     print(f"{key} : {value}")

# Concession Stand Program

# menu = {
#     "pizza" : 3.00,
#     "popcorn" : 4.50,
#     "pepsi" : 3.00,
#     "fries" : 2.50,
#     "chips" : 4.50,
#     "pretzel" : 5.00
# }
# cart = []
# total = 0

# while True:
#     food = input("Add a food item to the cart (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#         total += menu.get(food)
#     else:
#         print(f"{food} is not present in the menu")

# for item in cart:
#     print(item, end=" ")

# print(f"TOTAL: {total}")

# Generating random numbers in Python (It's way easier in Python compared to other languages)

# import random # importing module named "random"

# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "A", "J", "K", "Q", "10"]

# number = random.randint(1, 6) # generates a random whole integer within the range specified
# number = random.random() # returns a random floating point number between 0 and 1
# option = random.choice(options) # returns a random choice from the options tuple (This is why Python is the superhero of competitive coding! I mean, generating a random choice from a list is a breeze here, but in Java, Well, let’s just say, you'd need a whole team of engineers to get it done!)

# random.shuffle(cards) # randomly shuffles the cards list

# print(cards)

# Function(the moment you've all been waiting for!):

# Alright! Imagine you have a magic box. Every time you put something in the box and ask it to do something, it gives you back a result. For example, you put in a number, and the box gives you back double that number. Or you put in a name, and the box says "Hello, [name]!"

# In programming, functions are like these magic boxes. You put in something (called "arguments"), and the function gives you back something (called the "return value").
# A function is block of reusable code that can be invoked/called as and when required.

# place () after the function name to invoke it

# def hello_world(): # using "def" keyword, we "define a function" followed by a valid function name, paranthesis and a colon
#     print("Hello World!")
#     print("My name is Franklin Jetty Johnson")
#     print("I am 24 years old")
#     print("I am currently doing Data Science in IIT Guwahati")
#     print("Thank You!") 

# hello_world() # invoking the function

# return = statement used to end a function and send a result back to the caller

# def add(x, y):
#     return x + y

# print(add(10, 20))

# Arguments and Parameters

# Ask a senior software engineer what a parameter and an argument are, and there’s a good chance they’ll give you a confused look like they’ve just been asked to solve a Rubik's cube blindfolded. The names are like twins, similar, but you’re never quite sure which one is which! I'll break it down for you so that next time someone asks you the difference between the both, you can easily answer.

# Parameter:
# A parameter is like a placeholder inside the function that tells you what kind of ingredient the magic box needs. It's like saying, "Hey, I need a number!" but not specifying what number exactly. It’s just the name of the ingredient.

# def greet(name):  # "name" is the parameter
#     print("Hello, " + name + "!")

# Argument:
# An argument is the actual thing you put into the magic box when you call the function. It’s like saying, “Here’s the number I’m giving you!” It’s the real ingredient that goes into the function.

# greet("Alice")  # "Alice" is the argument
# greet("Bob")    # "Bob" is the argument

# Different Types:

# Default = You can set a default value for a parameter
# Default is used when that argument is omitted
# It makes your functions more flexible, reduces number of arguments

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500)) # here discount and tax is not given in the function call and hence they take their default values 0 and 0.05 respectively.

# Note that the Default parameters should be at the end of the parameter list

# Keyword Arguments = an argument preceded by an identifier
# Helps with readability

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello(first="Franklin", greeting="Hello", last="Johnson", title="Mr.",) # order does not matter when you are usign keyword arguments

# print("1", "2", "3", "4", "5", sep="-") # here sep is a keyword argument

# Arbitrary Argument
# args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * = unpacking operator

# def add(*nums): # nums is a tuple which consists of all the arguments passed when invoked
#     total = 0
#     for num in nums:
#         total+= num
#     return total

# print(add(1,2,3,4,5,6,7))

# def print_details(**kwargs): # kwargs is a dictionary, so you can traverse through kwargs as you would traverse through a dictionary
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_details(first_name="Franklin", last_name="Johnson", age=24, state="Kerala")

# iterables = an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
# eg: list, set, tuple, dictionary, string


# TIME FOR A QUICK BREAK! KUDOS, SOLDIER! YOU'VE COME THIS FAR, AND YOU'RE DOING GREAT!
# I've got a secret to share once you reach the end! (No peeking now!)

# Membership Operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)

# 1. in
# 2. not in

# word = "FRANKLIN"

# letter = input("Enter a letter: ")

# while True:
#     if letter in word:
#         print(f"{letter} is present in the word {word}")
#         break
#     else:
#         print(f"{letter} is not present in the word")
#         letter = input("Enter a letter: ")

# if letter not in word:
#     print(f"{letter} is not present in the word")
# else:
#     print(f"{letter} is present in the word")


# List Comprehension = A concise way to create lists in python 
# Compact and easier to read than traditional loops
# syntax : [expression for value in iterable if condition (optional)]

# doubles = [x * 2 for x in range(1,11)]

# print(doubles)

# fruits = ["apple", "banana", "orange", "pineapple"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

# numbers = [1,2,-2,0,-5,9]

# positive_numbers = [number for number in numbers if number >= 0] # read as for every number in iterable numbers, if the number is greater than or equal to 0, return the number
# negative_numbers = [number for number in numbers if number < 0]  # read as for every number in iterable numbers, if the number is less than 0, return the number

# print(positive_numbers)
# print(negative_numbers)

# Match-Case Statement (switch) = an alternative to using many 'elif' statements
# Executes some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable 


# def day_of_week(day):
#     match day:
#         case 1:
#             print("Sunday")
#         case 2:
#             print("Monday")
#         case 3:
#             print("Tuesday")
#         case 4:
#             print("Wednesday")
#         case 5:
#             print("Thursday")
#         case 6:
#             print("Friday")
#         case 7: 
#             print("Saturday")
#         case _: # '_' is considered as a wildcard, if no other case is true, this case will be triggered
#             print("Not a valid day")

# day_of_week(1)

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False

# print(is_weekend("Monday"))

# Module = a file containting code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

# import math
# print(math.pi)

# import math as m # giving an alias
# print(m.pi)

# from math import pi 
# print(pi)

# Variable Scope = where a variable is visible and accessible
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Substitution Cipher Encryption Program

# import random
# import string

# chars = string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# keys = chars.copy()

# random.shuffle(keys)

# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# # encryption
# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += keys[index]

# print(f"Original message: {plain_text}")
# print(f"Encrypted message: {cipher_text}")

# # decryption

# cipher_text = input("Enter a message to decrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = keys.index(letter)
#     plain_text += chars[index]

# print(f"Original message: {cipher_text}")
# print(f"Decrypted message: {plain_text}")

# Class and Object (You definitely don’t want to skip this, trust me, you’ll regret it later!):

#  Let’s think of objects like action figures or stuffed animals.

# A class is like the manual or instructions that tells you how to create your action figure. It tells you what features your action figure should have. For example, an action figure might have a name, color, and a special move.

# An object is the actual action figure you create using the manual! Each action figure (object) has the features defined in the manual (class), but each action figure can be a little different. One might be named "Superhero Steve," and another might be named "Princess Sally," but both are action figures.

# A "bundle" of related attributes (variable) and methods (functions)
# eg: phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class Car: # class is created using the keyword class and note that I am making the first letter of my class name capital.
#     def __init__(self, model, year, color, for_sale): # constructor to initialise the object (constructor explained below)
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
    
#     def drive(self): # method (function inside an object)
#         print(f"You drive the {self.model}")

#     def stop(self): # method (function inside an object)
#         print(f"You stop the {self.model}")
    
# car1 = Car("BMW", 2025, "Black", False) # creating an object
# car2 = Car("Benz", 2024, "White", True) # creating an object

# # print(car1.model)
# # print(car1.year)
# # print(car1.color)
# # print(car1.for_sale)

# # print(car2.model)
# # print(car2.year)
# # print(car2.color)
# # print(car2.for_sale)

# car1.drive()
# car1.stop()

# Constructor:
# In Python, a constructor is a special method inside a class that gets called when you create an object (instance) of that class. It's like when you build a new toy from a box of parts, and the constructor is the person who sets everything up for you right when you open the box!
# In Python, we use a special method __init__ to initialise the object (methods that start with double underscore are called as dunder methods or magic functions, which we will explain in depth later!)
# Note that I am calling my functions as methods now. Any function defined inside a class is called as method.

# Class Variables:
# Shared among all instances(objects) of a class
# Defined outside the constructor
# Allow you to share data among all objects created from that class

# class Car: # class name should be capital

#     company = "Honda" # class variables are accessed by all objects, hence declared outside the constructor

#     def __init__(self, model, year, color, for_sale): # constructor to initialise the object
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


# print(Car.company) # you can also access the class variable using any of the objects but it is best to use it with the class name

# Inheritance(a must-know topic in interviews):

# Inheritance in Python is like when a child gets traits or abilities from their parents. Just like how you might inherit things like your hair color, height, or love for pizza from your parents, classes in Python can inherit features and behaviors from other classes.

# In programming, inheritance allows a class (called a child class) to inherit the properties and methods of another class (called a parent class). This way, you don’t have to rewrite code, and you can reuse and extend the functionality of the parent class.

# Syntax: class Child(Parent)

# class Animal: # parent class
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal): # inheriting parent class "Animal"
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal): # inheriting parent class "Animal"
#     def speak(self):
#         print("MEOW!")

# class Mouse(Animal): # inheriting parent class "Animal"
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Liz")
# mouse = Mouse("Rode")

# print(cat.name)
# print(cat.is_alive)

# cat.eat()
# cat.sleep()
# dog.speak()
# cat.speak()
# mouse.speak()

# Types:

# Multiple Inheritance;
# This is when a child class inherits from two or more parent classes. It’s like a child getting traits from both parents and grandparents. However, Python handles it carefully to avoid conflicts in methods or attributes from different parents.

# Multilevel Inheritance:
# This is when a child class inherits from a parent class, and then another class inherits from that child class. It’s like a family tree, where traits pass down from generation to generation.
# C(B) <- B(A) <- A

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator): # multiple inheritance
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# rabbit.flee()
# hawk.hunt()

# fish.hunt()
# fish.flee()

# rabbit.eat()
# rabbit.sleep()

# fish.eat()
# fish.sleep()

# rabbit.eat()

# super():
# In Python, super() is a built-in function that allows you to call a method from a parent class within a child class. It's used to access inherited methods from a parent class, especially in object-oriented programming (OOP).

# Imagine you're playing a video game where your character (child class) gets special abilities from their parent (the parent class). You want your character to use their parent's special abilities, but also add some of their own abilities on top of it. super() helps you do that!

# Allows you to extend the functionality of the inherited methods

# class Shape:
#     def __init__(self, color, filled):
#         self.color = color
#         self.filled = filled
        
# class Circle(Shape):
#     def __init__(self, color, filled, radius):
#         super().__init__(color, filled)
#         self.radius = radius

# class Square(Shape):
#     def __init__(self, color, filled, width):
#         super().__init__(color, filled)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, filled, width, height):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height

# circle = Circle("red", True, 5)
# print(circle.color)
# print(circle.filled)
# print(circle.radius)

# square = Square("green", True, 5)
# print(square.color)
# print(square.filled)
# print(square.width)

# triangle = Triangle("yellow", True, 5, 10)
# print(triangle.color)
# print(triangle.filled)
# print(triangle.width)
# print(triangle.height)

# You can also use super() to invoke a function defined in the parent class

# Polymorphism:
# Ah, Polymorphism! Now we're getting into some cool stuff in programming!
# Let’s break it down like you’re a 10-year-old:

# Imagine you have a magic button in your house. When you press it, it can do different things based on who is pressing it:
# When Mom presses the button, it makes dinner.
# When Dad presses the button, it makes a coffee.
# When You press the button, it plays music.
# Even though you’re pressing the same button, the action it performs is different. That’s Polymorphism in action!

# Polymorphism is a fancy word that basically means "many shapes" or "many forms". In programming, it means that one function or method can work with different types of objects in different ways. It allows you to use a single interface for different data types.

# Two ways to achieve polymorphism
# 1. Inheritance = an object could be treated of the same type as a parent class
# 2. "Duck Typing" = object must have necessary attributes/methods

# Duck Typing:
# The programming concept that sounds like it came straight from a farm, right? But trust me, it’s way cooler than it sounds!
# In duck typing, the type or class of an object is determined by its behavior, not by its specific type. Simply put, if it looks like a duck, swims like a duck, and quacks like a duck, then it’s a duck, even if it’s technically not a duck at all!
# You don’t have to check the type of an object before using it. If an object has the required method or behavior, Python lets you use it without caring what it is. As long as the object can do what you expect, you don’t need to worry about what class or type it is.

# Another way to achieve polymorphism besides Inheritance

# class Animal:
#     alive = True
    
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW")

# class Car:
#     alive = False

#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# Static Methods(A No-Object-Required Party):
# Imagine this: You have a method that you want to share with the world, but you don't need any of the fancy stuff that comes with class objects. You just want a plain old function, but inside a class. Enter Static Methods!

# A static method in Python is a method that belongs to a class, but doesn’t depend on any instance of the class (no need to create an object). It doesn’t need access to any instance-specific data—it's a standalone function that’s just inside a class for organization.

# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need access to class data

# class Employee:

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
    
#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cook", "CEO", "CTO", "Janitor"]
#         return position in valid_positions

# print(Employee.is_valid_position("Janitor")) # static methods are accessed using class name not by any objects

# Class Methods:
# Let’s talk about class methods, which are like the VIP members of the Python method family. They’re not just regular methods, they’re special methods that operate on the class itself instead of instances.

# Think of it this way: If a static method is just hanging out and doing its job without the need for the class or instance, then a class method is like a VIP guest who gets access to the class's secretive information (class variables) but still doesn’t need to be an object to do it!

# A class method is a method that belongs to the class rather than the instance. It has access to the class itself and can modify class-level variables. The key difference from instance methods is that class methods use the "cls" as their first argument (not self), and they’re defined using the @classmethod decorator.

# Instance (object) methods have "self" as the first parameter which refers to the object that is using the method at that point of time whereas, class methods have "cls" as the first parameter

# class Student:

#     count = 0
    
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         Student.count += 1
    
#     def get_info(self):
#         print(f"{self.name} : {self.roll_no}")
    
#     @classmethod
#     def get_count(cls):
#         print(f"Total number of students: {cls.count}")

# student1 = Student("Franklin", 10)
# student2 = Student("Freddy", 11)
# student3 = Student("Jen", 14)

# Student.get_count()

# Quick Recap!
# Instance Methods = best for operations on instances of the class (objects)
# Static Methods = best for utility functions that do not need access to class data
# Class Methods = best for class-level data or require access to the class itself

# Magic methods (The secret wizards of Python):
# Let’s dive into the world of magic methods, a.k.a. dunder methods (because they start and end with double underscores). These are special methods in Python that allow you to customize the behavior of your objects. They might seem like magic at first, but they’re just Python’s way of letting you define how objects behave when they’re interacted with in certain ways.

# Think of them as wizards that come out when you do something special with your objects—like adding two objects, comparing them, or printing them!

# Magic methods are predefined methods that let you control how your objects behave when you do certain operations on them. They’re not meant to be called directly (because they’re magical!), but you can trigger them when you interact with objects in specific ways.

# Commonly used dunder methods: __init__, __str__, __eq__

# class Book:

#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
    
#     def __str__(self):
#         return f"{self.name} by {self.author}"

#     def __eq__(self, other): # self holds the first object and other holds the second object
#         return self.name == other.name and self.author == other.author # returns a boolean based on the evaluation

# book1 = Book("The Alchemist", "Paulo Coelho")
# book2 = Book("The Alchemist", "Paulo Coelho")

# # print(book1) # if we try to print the object directly, it will give us the memory address. 
# If we want to customize this behavior, we can use magic method __str__ to return whatever we want

# # print(book1)
# # print(book2)

# # print(book1 == book2) # returns false even if the name and the author of the books is the same. We can use __eq__ to customize it

# print(book1 == book2) # returns true after customizing the magic method __eq__

# @property = decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method

# class Rectangle:

#     def __init__(self, width, height):
#         self._width = width # by preceding an underscore, we turn the variable into protected type which can only be accessed within the class
#         self._height = height # by preceding an underscore, we turn the variable into protected type which can only be accessed within the class
    

#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
    
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")
            
# rectangle = Rectangle(5, 10)

# print(rectangle.width)
# print(rectangle.height)

# rectangle.width = 9
# rectangle.height = 9

# print("New values: ")
# print(rectangle.width)
# print(rectangle.height)

# del rectangle.width
# del rectangle.height

# decorator = a function that extends the behavior of another function without modifying the base function
# Pass the base function as an argument to the decorator

# @add_sprinkles
# get_ice_cream("vanilla")

# def add_sprinkles(func): # decorator function
#     def wrapper(*args, **kwargs): # without this function, the get_ice_cream() gets invoked automatically when the decorator is added
#         print("You add sprinkles")
#         func(*args, **kwargs) # base function that we received as a parameter
#     return wrapper

# def add_fudge(func): # decorator function
#     def wrapper(*args, **kwargs): # without this function, the get_ice_cream() gets invoked automatically when the decorator is added
#         print("You add fudge")
#         func(*args, **kwargs) # base function that we received as a parameter
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream")

# get_ice_cream("vanilla")
# you can apply more than one decorator to the base function 

# Exception(Think of it as a "Oops!" moment):
# Alright, let’s talk about exceptions. In programming, an exception is like a problem or error that happens when something goes wrong while your code is running. Imagine you’re cooking, and you suddenly realize you’ve run out of salt. That’s an exception in your cooking process.

# In Python, when something goes wrong during your program's execution (like dividing by zero, or trying to open a file that doesn't exist), Python will raise an exception to tell you something is wrong. These exceptions are like Python’s way of saying, "Hey, something’s not right here! Help!"

# When an exception happens, the program stops executing and displays an error message. It’s like your program goes on pause and says, "I have a problem here, please fix it!"

# Common exceptions you might encounter
# (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

# ZeroDivisionError = occurs when we try to divide a number by 0. 
# TypeError = if we apply an operation that is not supported between the two objects, then a TypeError exception occurs
# ValueError = when an object is given the incorrect value, the ValueError is raised.

# try: # any code that can potentially lead to an exception should be placed under try
#     number = int(input("Enter a number: "))
#     print(1/ number)
# except ZeroDivisionError: # handles any ZeroDivisionError
#     print("You can't divide by zero")
# except ValueError: # handles any ValueError
#     print("Please enter a number")
# except Exception: # handles any other error
#     print("Something went wrong!")
# finally: # executes no matter what happens, usually performs clean up activities like closing the opened file, etc.
#     print("Do some cleanup here")

# Python File Detection(Let's check if that file exists!)
# So, let's talk about how to detect whether a specific file exists or not in Python. Imagine you're looking for your favorite book in a huge library. You can check whether the book is there or not before you start your search. Similarly, in Python, you can check if a file exists before trying to work with it. 

# import os # os module

# file_path = "test.txt" # relative file path

# if os.path.exists(file_path):
#     print(f"The location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("The location does not exist")

# python writing files (.txt, .json, .csv)

# txt_data = "I like BBQ"

# file_path = "output.txt"

# with open(file_path, "w") as file: # with statement is used to wrap the execution of a block with methods defined by a context manager
#     file.write(txt_data)
#     print(f"txt file {file_path} was created")

# import json

# employee = {
#     "name": "Franklin",
#     "age": 24,
#     "job": "Freelancer"
# }

# file_path = "output.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#     print("The file already exists!")

# import csv

# employees = [["Name", "Age", "Job"],
#             ["Spongebob", 37, "Cook"],
#             ["Franklin", 24, "Freelancer"],
#             ["Freddy", 27, "Software Engineer"]]

# file_path = "output.csv" # comma separated values

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file {file_path} was created")
# except FileExistsError:
#     print("The file already exists!")

# python reading files (.txt, .json, .csv)

# file_path = "output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("Permission is denied!")

# import json

# file_path = "output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("Permission is denied!")

# import csv

# file_path = "output.csv"

# try:
#     with open(file_path, "r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("Permission is denied!")

# date and time

# import datetime

# date = datetime.date(2025, 1, 23)
# today = datetime.date.today()

# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()

# print(date)
# print(today)

# print(time)
# print(now)

# now = now.strftime("%H:%M:%S %m-%d-%Y")
# print(now)

# Multithreading(We are almost done learning Python!):
# Imagine you're trying to finish your homework, make lunch, and text your friend all at once. It sounds impossible, right? But what if you could split those tasks into smaller chunks and work on them simultaneously? Well, that's what multithreading is like in Python!

# In programming, multithreading allows you to run multiple tasks (or "threads") at the same time within a single program. It's like juggling different tasks so they all get done faster, just like a superhero who can fly, solve mysteries, and save the world all at the same time. 

# Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs.

# Creating thread:
# threading.Thread(target=my_function)

# import threading
# import time

# def walk_dog(first, last):
#     time.sleep(8)
#     print(f"You finished walking {first} {last}")

# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# walk_dog()
# take_out_trash()  # executing functions in order i.e, we need to wait for a function to complete its execution before moving onto the next function
# get_mail()

# chore1 = threading.Thread(target=walk_dog, args = ("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)  # multitasking by executing all the functions simultaneously 
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join() # with the join(), we are waiting for all the tasks to complete before executing anything below it
# chore3.join()

# print("All chores are complete!")

# How to connect to an API using Python:
# API: The bridge between two worlds
# Imagine you're in a restaurant, and you’re hungry. You can't go directly to the kitchen (well, unless you’re a superhero). So, you tell the waiter what you want, and the waiter goes to the kitchen, picks up your food, and brings it back to you. The waiter here is like an API!

# import requests # to make an API request

# base_uri = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     uri = f"{base_uri}/pokemon/{name}"
#     response = requests.get(uri)
    
#     if response.status_code == 200:
#         print("Data fetched!")
#         pokemon_data = response.json() # converting json to python dictionary which consists of key: value pairs
#         return pokemon_data

#     else:
#         print("Failed to fetch the data {response.status_code}")
    
# pokemon_name = "typhlosion"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")


"""
 Congratulations, Soldiers!

You’ve made it to the end of this Python journey! That’s a huge achievement, and I’m super proud of you for sticking with it till the very end. Now, you've got all the basics and core concepts of Python under your belt. But remember, this is just the beginning. There’s a whole world of Python waiting for you to explore, and trust me, the more you dig, the more exciting it gets!

And hey, just a quick secret, I learned Python in under a week! So, if I can do it, YOU CAN DO IT TOO! Everyone has 24 hours in a day. It's how you utilize that time that sets you apart from others. So, take what you’ve learned here, keep practicing, and you’ll be mastering Python before you know it!

Happy Learning, and keep coding like a BOSS! 
"""