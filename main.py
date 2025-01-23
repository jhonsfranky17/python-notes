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
# str(), int(), float(), bool(), list()

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

# help(str) # returns all the string methods

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

# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# for i in range(3): # iterates for 3 times
#     for j in range(1, 10): # iterates from 1 to 9
#         print(j, end = " ") # usually end of a print statement is new line, but we can modify it
#     print() # prints new line outside inner loop

# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

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

# print(groceries[0][3]) # to access an element, we use two index operator

# you can do the same with tuple and set

# dictionary = a collection of {key:value} pairs
#              ordered and changeable, No duplicates

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

# concession stand program

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

# generating random numbers in python

# import random 

# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "A", "J", "K", "Q", "10"]

# number = random.randint(1, 6) # generates a random whole integer within the range specified
# number = random.random() # returns a random floating point number between 0 and 1
# option = random.choice(options) # returns a random choice from the options tuple
# random.shuffle(cards) # randomly shuffles the cards list

# print(cards)

# function = A block of reusable code
#            place () after the function name to invoke it

# def hello_world(): # using "def" keyword, we "define a function" followed by a valid function name, paranthesis and a colon
#     print("Hello World!")
#     print("My name is Franklin Jetty Johnson")
#     print("I am 24 years old")
#     print("I am currently doing Data Science in IIT Guwahati")
#     print("Thank You!") 

# hello_world() # invoking the function

# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     return x + y

# print(add(10, 20))

# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces number of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))

# default parameters should be at the end of the parameter list

# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello(first="Franklin", greeting="Hello", last="Johnson", title="Mr.",)

# print("1", "2", "3", "4", "5", sep="-") # here sep is a keyword argument

# arbitrary argument
# args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator
# 1. positional 2. default 3. keyword 4. ARBITRARY

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

# membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

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


# list comprehension = a concise way to create lists in python 
#                      compact and easier to read than traditional loops
#                      syntax : [expression for value in iterable if condition (optional)]

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

# match-case statement (switch) = an alternative to using many 'elif' statements
#                                 execute some code if a value matches a 'case'
#                                 benefits: cleaner and syntax is more readable 


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

# module = a file containting code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files


# import math
# print(math.pi)

# import math as m # giving an alias
# print(m.pi)

# from math import pi 
# print(pi)

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# substitution cipher encryption program

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

# object = a "bundle" of related attributes (variable) and methods (functions)
# eg: phone, cup, book
# you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class Car: # class name should be capital
#     def __init__(self, model, year, color, for_sale): # constructor to initialise the object
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

# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

# class Car: # class name should be capital

#     company = "Honda" # class variables are accessed by all objects, hence declared outside the constructor

#     def __init__(self, model, year, color, for_sale): # constructor to initialise the object
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale


# print(Car.company) # you can also access the class variable using any of the objects but it is best to use it with the class name

# inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               syntax: class Child(Parent)

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

# multiple inheritance = child class inherits from more than one parent class
#                        C(A,B)
# multilevel inheritance = child class inherits from a parent class which in turn inherits from another parent
#                          C(B) <- B(A) <- A

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

# super() = function used in a child class to call methods from a parent class(superclass).
#           allows you to extend the functionality of the inherited methods

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

# you can also use super() to invoke a function defined in the parent class

# polymorphism = greek words meaning to "have many forms or faces"
#                poly = many
#                morphe = form

#                two ways to achieve polymorphism
#                1. inheritance = an object could be treated of the same type as a parent class
#                2. "duck typing" = object must have necessary attributes/methods

# duck typing = another way to achieve polymorphism besides inheritance
#               object must have the minimum necessary attributes/methods
#               if it looks like a duck and quacks like a duck, it must be a duck

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

# static methods = a method that belongs to a class rather than any object from that class (instance)
#                  usually used for general utility functions

# instance methods = best for operations on instances of the class (objects)
# static methods = best for utility functions that do not need access to class data

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

# class methods = allow operations related to the class itself
#                 take (cls) as the first parameter, which represents the class itself

# instance (object) methods have "self" as the first parameter whereas, class methods have "cls" as the first parameter

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

# instance methods = best for operations on instances of the class (objects)
# static methods = best for utility functions that do not need access to class data
# class methods = best for class-level data or require access to the class itself

# magic methods = dunder methods (double underscore) __init__, __str__, __eq__
#                 they are automatically called by many of python's built-in operations
#                 they allow developers to define or customize the behavior of objects


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
# #                If we want to customize this behavior, we can use magic method __str__ to return whatever we want

# # print(book1)
# # print(book2)

# # print(book1 == book2) # returns false even if the name and the author of the books is the same. We can use __eq__ to customize it

# print(book1 == book2) # returns true after customizing the magic method __eq__

# @property = decorator used to define a method as a property (it can be accessed like an attribute)
#             benefit: add additional logic when read, write, or delete attributes
#             gives you getter, setter, and deleter method

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

# decorator = a function that extends the behavior of another function
#             w/o modifying the base function
#             pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

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

# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

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

# python file detection

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

