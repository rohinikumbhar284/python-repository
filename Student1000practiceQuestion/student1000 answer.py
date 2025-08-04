#  1.Reverse each word of a string
#  str = "My name is rohini"
#  reverse_text =str[::-1] # using slicing
# print(f"string are reversed: {reverse_text}")
#----------------------------------------
#2. Calculate the multiplication and sum of two numbers
#  num = int(input("Enter number1:"))
#  num2 = int(input("Enter number2:"))
#  add_of = num + num2 
#  mul_of = num * num2
#  print(f"Addition of numbers is: {add_of} \n Multiplication of numbers is: {mul_of}")
#----------------------------------------
# 3 . Formatted Twinkle Poem
# print("""Twinkle, twinkle, little star,
#  	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
#  Twinkle, twinkle, little star, 
#  	How I wonder what you are""")
#---------------------------------------------
#  4.Write a Python program to find out what version of Python you are using
#  import sys 
# python_version = sys.version
#  print("Python version is:")
#  print(python_version)
#-----------------------------------------------
#  5.Write a Python program that calculates the area of a circle based on the radius entered by the user.
# print("------Circle area calculation -----")
# redius = int(input("Enter the redius:  "))
# pi = 3.14
# area = pi * redius ** 2
# print("Area of circle is : ",area)
#------------------------------------------------
# # 6.Reverse Full Name
# name =input("Enter your full name:")
# text =name[::-1]
# print("Reverse name :",text)
#---------------------------------------------------
# # 7.Write a Python program that accepts a filename from the user and prints the extension 
# # of the file.Sample filename : abc.java
# file =input("Enter your file name:")
# exten =".java"
# print(f"We use the extesion for file is:{file}{exten}")
#-----------------------------------------------

# 8.Display numbers divisible by 5
# print("Number divisible by 5:")
# for i in range(1,101):
#     if i % 5 == 0:
#         count += i 
#         print(count)
#----------------------------------------------------
# # 9.Write a Python program to get the volume of a sphere with radius six.
# import math
# redius = 6
# volume =(4/3) * math.pi *(redius ** 3)
# print(f"The volumne of sphere : {volume}")
#----------------------------------------------------
# 10. Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.
# num = int(input("Enter number:"))
# print(f"difference:{17 - num}")
# def num_def(n):
#     if n > 17:
#         return 2 ** abs(n-17)
#     else :
#         return abs(n-17)
    
# num = int(input("enter number:"))
# result = num_def(num)
# print(f" The differnce is: {result}")
#-------------------------------------------------
#  11. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
#  Output :
# List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

#  input_str = input("Enter comma-separated numbers: ")
#  num = input_str.split(',') # Generate a list by splitting the input string
#  num1= tuple(num) # Generate a tuple from the list
#  print("List :", num)
#  print("Tuple :", num1)
#--------------------------------------------
# 12.Write a Python program to display the first and last colors from the following list.
 #color_list = ["Red","Green","White" ,"Black"]

#  a_list =["Red","Green","White" ,"Black"]
#  first_color = a_list[0]
#  last_color =a_list[-1]
#  print(" The first color in listc: ", first_color)
#  print(" The last color in list :" , last_color)
#---------------------------------------------
# 13 .Write a Python program to test whether a number is within 100 of 1000 or 2000.
#  def num_check(n): # define  used
#      return abs(1000 - n) <= 100 or abs(2000 - n) <= 100
#  number = int(input("Enter a number: "))
#  if num_check(number):
#     print("The number is within 100 of 1000 or 2000.")
# else:
#     print("The number is NOT within 100 of 1000 or 2000.")
#--------------------------------------------------
# 14.Write a Python program to calculate the sum of three given numbers.
#  If the values are equal, return three times their sum.
#  num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
#  num3 = int(input("Enter 3rd number: "))
#  add_of = 3 * (num1 + num2 + num3)
# if num1 == num2 == num3 :
#      print("sum of number if value are same :" , add_of)
#  else:
#    print(f"sum of three number is : {num1 + num2 + num3 }")  
# -------------------------------------------------  
 # 15.Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
#  Return the string unchanged if the given string already begins with "Is".
#  def check_is_string(s):
#       if s.startswith("Is"):
#         return s
#       else:
#           return "Is"+ s
# Take_value = input("Enter String :")
#  result = check_is_string(Take_value)
#  print(result)
# # #-----------------------------------------
#  17.Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
#  def check_copies(s,n):
#     if n < 0:
#        return "Please Enter positive number :"
#      return s * n
#  Take_input = input("Enter string :")
#  num_of_copies = int(input("Enter the number :"))
# result = check_copies(Take_input,num_of_copies)
#  print("Result:",result)
# #-------------------------------------------------   
#  18 .Write a Python program that determines whether a given number (accepted from the user)
#  is even or odd, and prints an appropriate message to the user.
#  Num_check =int(input("Enter the number:"))
# if Num_check % 2 == 0:
#      print(f"{Num_check} Its Even Number!")
#  else:
#     print(f"{Num_check} Its Odd Number!")
# ---------------------------------------------
# 19 .Write a Python program to count the number 4 in a given list.
#  list_count =[1,2,3,4,5,6,7,8]
#  value_count =list_count.count(4)
# print(f"In list {user_define} place number :",value_count)
#--------------------------------------
#  20 .Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.
# def copie_two(s, n):
#     if n < 0:
#         return "Please enter a non-negative integer."
#     part = s[:2] if len(s) >= 2 else s ## Use first 2 characters if available, else use the full string
#    return part * n
#  user_string = input("Enter a string: ")
#  n = int(input("Enter a non-negative integer: "))
#  result = copie_two(user_string, n)
#  print("Result:", result)
#------------------------------------------
#  21.Write a Python program to test whether a passed letter is a vowel or not.
# def is_vowel(letter):
#    vowels = 'aeiouAEIOU'
#     return letter in vowels
#  char = input("Enter a single letter: ") 
#  if len(char) == 1 and char.isalpha():
#      if is_vowel(char):
#         print(f"'{char}' is a vowel.")
#      else:
#          print(f"'{char}' is not a vowel.")
#  else:
#     print("Please enter a single alphabet letter.")
# ------------------------------------------
# 22.Write a Python program that concatenates all elements in a list into a string and returns it.
#  my_list = ['Rohini',' ', 'Prakash ',' ', 'Kumbhar', '!', 2025]
#  result = ''# Initialize an empty string
#  for item in my_list:# Loop through each item in the list
#     result += str(item)  # Convert to string and add to result
# print("Concatenated string:", result)
 #-------------------------------------------
# 23.Write a Python program to print all even numbers from a given list of numbers in the same order and 
#  stop printing any after 237 in the sequence.
# for i in range(1,237):
#      if i % 2 == 0:
#        print(i)
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#      815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#  ]

#  for num in numbers:
#      if num == 237:
#         if num % 2 == 0:
#            print(num)
#          break
#     if num % 2== 0:
#          print(num)
#  #--------------------------------------
# 24.Write a Python program that prints out all colors from color_list_1 that are not
#  present in color_list_2.
#  color_lis_1 = {"Red", "Green", "Blue", "White"}
# color_lis_2 = {"Green", "White", "Black"}
#  def_color = color_list_1.difference(color_list_2) # use defference for not match
# print("Colors in color_list_1 not in color_list_2:")
#  for color in def_color:
#      print(color)

# ----------------------------
# 25.Write a Python program that will accept the base and height of a triangle and compute its area.
#  Base_of = int(input("Enter the base of triangle :"))
# hight_of = int(input("Enter the height of triangle:"))
# area_of = 1/2 * Base_of * hight_of 
# print("The area of triangle :",area_of)
# # #-----------------------------------------------
# 26.Write a Python program that computes the greatest common divisor (GCD) 
 # of two positive integers.

#--------------------------------------------

 # 27.Write a Python program to find the least common multiple (LCM) of two positive integers.
# def compute_gcd(a, b):
#     while b != 0:
#        a, b = b, a % b
#     return a
#  Function to compute LCM using GCD
#def compute_lcm(a, b):
#      return abs(a * b) // compute_gcd(a, b)
#  num1 = int(input("Enter the first positive integer: "))
# num2 = int(input("Enter the second positive integer: "))
#  if num1 > 0 and num2 > 0: # Validate and compute
#      lcm = compute_lcm(num1, num2)
#     print(f"The LCM of {num1} and {num2} is: {lcm}")
# else:
#     print("Please enter positive integers only.")
# ---------------------------------------------------
# 28 .Write a Python program to sum three given integers. However, if two values are equal, 
# the sum will be zero.
# num1 = int(input("Enter 1st value: "))
# # num2 = int(input("Enter 2nd value: "))
# num3 = int(input("Enter 3rd value: "))
#  sum_of = num1 + num2 + num3
#  if num1 ==num2 or num1 == num3 or num2 == num3:
#      print(f"sum of 3 num is = 0") 
#  else:
#      print("sum of 3 number is :" ,sum_of)
# ----------------------------------------
# 29. Write a Python program to sum two given integers. However, 
# if the sum is between 15 and 20 it will return 20.
#  num1 = int(input("Enter first number :"))
#  num2 = int(input("Enter second number :"))
# sum = num1 + num2 
#  if sum > 15 and sum < 20:
#      print("20")
#else:
#      print("Result :"sum)
# #----------------------------------------------
# 30 . Write a Python program that returns true if the two given integer values are equal or 
#  their sum or difference is 5.
#  num1 = int(input("Enter 1st number:"))
# num2 =int(input("Enter 2nd number: "))
#  if num1 == num2 or (num1 - num2) == 5 or (num1 + num2) == 5 :
#     print("true")
#  else:
#     print("False")
# #---------------------------------------------
 # 31 .Write a Python program to add two objects if both objects are integers.
#  a = input("Enter first value: ")
#  b = input("Enter second value: ")
#  if a.isdigit() and b.isdigit(): # Try to convert both to integ
#     result = int(a) + int(b)
#      print("Sum:", result)
#  else:
#     print("Both inputs must be integers.")
# #------------------------
# 32 .Write a Python program that displays your name, age, and address on three different lines.
# name = input("Enter your name: ")
# age = int(input("Enter your age :"))
#  address = input("Enter your address : ")
# print(f" My name is : {name}. \n my age is: {age}. \n I am from {address}.")

# #-------------------------------------------
#  33 .Write a Python program to solve (x + y) * (x + y).
#  Test Data : x = 4, y = 3
#Expected Output : (4 + 3) ^ 2) = 49
#  x = int(input("Enter 1st number: "))
#  y = int(input("Enter 2nd number :"))
#  add = x + y 
#  square = add * add 
#  print(f"Power of {add} :" , square)
# -----------------------------------------
#  34 . Write a Python program to compute the future value of a specified principal amount, 
 # rate of interest, and number of years.

# 
#  principal = float(input("Enter the principal amount: "))
# 
#  rate = float(input("Enter the annual interest rate (in %): "))
# years = int(input("Enter the number of years: "))
# future_value = principal * (1 + rate / 100) ** years # calculate future value
#  print(f"Future value after {years} years: {future_value:.2f}")
#---------------------------------------------
# 35.Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
 # x1 = float(input("Enter x1: "))
 # y1 = float(input("Enter y1: "))
 # x2 = float(input("Enter x2: "))
 # y2 = float(input("Enter y2: "))
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # Calculate distance
 # print(f"Distance between the points: {distance:.2f}")
 #---------------------------------------------------
 # 36. Write a Python program to sum the first n positive integers.
 # n = int(input("Enter a positive integer: "))
 # if n > 0: # Check if input is valid
 #     total = n * (n + 1) // 2  # Using integer division
 #     print(f"Sum of the first {n} positive integers is: {total}")
 # else:
 #     print("Please enter a positive integer.")
 #-----------------------------------------------
 #  37. Write a Python program to convert height (in feet and inches) to centimeters.
# feet = int(input("Enter height in feet: "))
#  # inches = int(input("Enter remaining inches: "))
# total_inches = feet * 12 + inches
# height_cm = total_inches * 2.54
# print(f"Height in centimeters: {height_cm:.2f} cm")
 #--------------------------------------------------------
# 38 . Write a Python program to calculate the hypotenuse of a right angled triangle.
#  import math
# a = float(input("Enter side a: "))
#  b = float(input("Enter side b: "))
#  c = math.sqrt(a**2 + b**2) # Calculate the hypotenuse
#  print(f"The hypotenuse is: {c:.2f}")
# ------------------------------------------------------
# 39 .Write a Python program to convert the distance (in feet) to inches, yards, and miles.
#  feet = float(input("Enter distance in feet: "))
#  inches = feet * 12     # 1 foot = 12 inches
#  yards = feet / 3        # 1 yard = 3 feet
#  miles = feet / 5280      # 1 mile = 5280 feet
#  print(f"Distance in inches: {inches:.2f} inches")
#  print(f"Distance in yards: {yards:.2f} yards")
#  print(f"Distance in miles: {miles:.6f} miles") 
 #----------------------------------------------------
#  40 .Write a Python program to calculate the body mass index.
#  weight = float(input("Enter your weight in kilograms: "))
# 
#  height = float(input("Enter your height in meters: "))
# 
#  bmi = weight / (height ** 2)   # Calculate BMI
#  print(f"Your BMI is: {bmi:.2f}")  
# if bmi < 18.5:
#     print("You are underweight.")
#  elif 18.5 <= bmi < 25:
#     print("You have a normal weight.")
# elif 25 <= bmi < 30:
#    print("You are overweight.")
# else:
#      print("You are obese.")
# #---------------------------------------------

#  41 .Write a Python program to convert pressure in kilopascals to pounds per square inch, 
# a millimeter of mercury (mmHg) and atmosphere pressure.
#  value  = float(input("Enter pressure in kilopascals (kPa): "))
#  psi = value * 0.145038 # Convert to other units
#  mmHg = value * 7.50062
# atm = value * 0.00986923
#  print(f"Pressure in pounds per square inch (psi): {psi:.2f}")
#  print(f"Pressure in millimeters of mercury (mmHg): {mmHg:.2f}")
#  print(f"Pressure in atmosphere (atm): {atm:.5f}")
 #------------------------------------------------------
#42 .Write a Python program to calculate sum of digits of a number
# num1 = int(input("Enter value :"))
# num2 = int(input("Enter value :"))
 # print(f"Addition of number is : {num1 + num2}")

 #-----------------------------------------------------------------
 # 43.Write a Python program to sort three integers without using conditional
 #  statements and loops.
 # num1 = int(input("Enter value :"))
# num2 = int(input("Enter value :"))
 # num3 = int(input("Enter value :"))
 # sort = sorted([num1,num2,num3])
 # print("Number sorted :",sort)
 #--------------------------------------
 # 44. Write a Python program to calculate the midpoints of a line
# a= int(input("Enter the lenth of line a:"))
# b = int(input("Enter the lenth of line b:"))
# c = int(input("Enter the lenth of line c:"))
# d = int(input("Enter the lenth of line d:"))
# mid_point1 = (a + b)/ 2
#  mid_point = (c + d) /2
#  print(f"The mid point of line is :{mid_point1,mid_point}")
#--------------------------------------------
# 45.  Write a Python program to hash a word.
# word = input("Enter a word to hash: ")
# hashed = hash(word)
#  print(f"The hash of the word is: {hashed}")

# #-------------------------------------------
#  46.Write a Python program to calculate the sum of all items of a container (tuple, list,
#   set, dictionary).
# a = [10, 20, 30]
# b= (5, 15, 25)
# c = {2, 4, 6, 8}
# d = {'a': 100, 'b': 200, 'c': 300}
# sum_list = sum(a)        # Sum of list
# print(f"Sum of list: {sum_list}")
# sum_tuple = sum(b)
# print(f"Sum of tuple: {sum_tuple}")
# sum_set = sum(c)
# print(f"Sum of set: {sum_set}")
# sum_dict = sum(d.values())
# print(f"Sum of dictionary values: {sum_dict}")

# -------------------------------------
#  46 .Given variables x=30 and y=20, write a Python program to print "30+20=50".
# x = 30
# y = 20
# print(f"Result :{x + y}")
#------------------------------------------
#  47 .Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day
#  of a Month!" and do nothing if the value is not equal.
# value = int(input("Enter the value: "))
# if value == 1:     # If the value equals 1, print the message; otherwise do nothing
#     print("First day of a Month!")
#-------------------------------
# 48 . Write a Python program to swap two variables.
# a = int(input("enter number: "))
# b = int(input("Enter number"))
# a,b = b,a
# print("After swaping")
# print("a =",a)
# print("b =",b)
#-------------------------------------------
#  49 .Write a Python program to define a string containing special characters in various forms.
# s1 = "\#{'}${\"}@/"
# print(s1)

# # 2. Escaping single quote inside single‑quoted string
# s2 = '\#{\'}${"}@/'
# print(s2)

# # 3. Using raw triple‑quoted string (no special‑character escaping)
# s3 = r"""\#{'}${"}@/"""
# print(s3)

# # 4. Single‑quoted form with an escaped single‑quote using "'" hack
# s4 = '\#{\'"\'}${"}@/'
# print(s4)

# # 5. Raw single‑type triple quotes
# s5 = r'''\#{'}${"}@/'''
# print(s5)
#--------------------------------
#  49 .Write a Python program to get the Identity, Type, and Value of an object.
# x = int(input("Enter number: "))
# print("Identity:", x)
# print("Type:    ", type(x))
# print("Value:   ", id(x))
#------------------------------------
# 50 .Write a Python program to check whether a string is numeric.
# str = input("Enter a string: ")
# if str.isdigit():
#     print("The string is numeric (digits only).")
# else:
#     print("Not a pure digit string.")
#-------------------------------------------
# 51 .Write a Python program to get the name of the host on which the routine is running.
# import socket
# hostname = socket.gethostname()
# print("Hostname:", hostname)
#--------------------------------------------
# 52.Write a Python program to determine the largest and smallest integers, longs, and floats.

# 53 .Write a Python program to check whether multiple variables have the same value.

# a = 10
# b = 10
# c = 10
# if a == b== c:
#     print("Variables are equal.")
# else:
#     print("Variables are not equal .")
#---------------------------
# 54 . Write a Python program to sum all counts in a collection.
# import collections
# num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
# counter = collections.Counter(num) # Count occurrences
# total_count = sum(counter.values())

# print("Total count of items:", total_count)
#----------------------------------------------
# 55. Write a Python program to check whether lowercase letters exist in a string.
# value = input("Enter string:")
# if value == value.lower():
#     print("You are going right way")
# else:
#     print("plz write in lower case")
#------------------------------------------
# 56 .Write a Python program that uses double quotes to display strings.
# a_str = " Use double quots to display string"
# print(a_str)

#  #Using double quotes to define the string
# print("Hello, World!")

# # Including single quotes inside double quotes
# print("It's a beautiful day.")

# # Including double quotes inside the string using escape character
# print("She said, \"Python is fun!\"")

# # Another example with a sentence in double quotes
# print("This string uses \"double quotes\" to highlight a word.")

#----------------------------------------------------------
# 57. Write a Python program to split a variable length string into variables.
# data = "Rohini Kumbhar karad 25"
# name, surname, country, age = data.split() # Split the string by spaces
# print("First Name:", name)
# print("Last Name:", surname)
# print("Country:", country)
# print("Age:", age)
#-------------------------------
#  58 .Write a Python program to input two integers on a single line.
# a,b = map(int, input("Enter two integers: ").split())
# print("First number:", a)
# print("Second number:", b)
#--------------------------------------
# 59 .Write a Python program to print a variable without spaces between values.
#Sample value : x =30
# x = 20
# print("Value of x" ,x , sep = '') 

#----------------------------------
#  60 .Write a Python program to convert true to 1 and false to 0.
# x = True 
# y = False 
# print(int(x))
# print(int(y))
#---------------------------------------
# 61 .Write a Python program to check whether a variable is an integer or string.
# var = input("Enter something : ")

# if type(var) == int:
#     print("The variable is an integer.")
# elif type(var) == str:
#     print("The variable is a string.")
# else:
#     print("The variable is neither an integer nor a string.")
# ---------------------------------
# 62 .Write a Python program to test if a variable is a list, tuple, or set.
#var = [1, 2, 3]  # Change this to a tuple (), set {}, or any other type
# var = {1,2,3,4}
# #var1= (1,3,4,5,5)
# if isinstance(var, list):
#     print("The variable is a list.")
# elif isinstance(var, tuple):
#     print("The variable is a tuple.")
# elif isinstance(var, set):
#     print("The variable is a set.")
# else:
#     print("The variable is none of these types.")
#------------------------------------------
#  63 .Write a Python function to check whether a number is divisible by another number. Accept two integer 
# values from the user.
# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# if num1 % num2 == 0:
#     print("Num1 is divisible by num2")
# else:
#     print("Num is not divisible by num2")
#--------------------------------------
# 64 . Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# def Fin_min_max(num):
#     minimum = min(num)
#     maximum = max(num)
#     return minimum , maximum
# num =[20,16,23,10,86,45,18,12]
# minimum ,maximum = Fin_min_max(num)
# print("Minimum =" ,minimum)
# print("Maximum =", maximum)

#---------------------------------------------
# 65. Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers
# smaller than the specified number.
# def sum_of_cubes(n):
#     return sum(i**3 for i in range(1, n))
# number = 5
# result = sum_of_cubes(number)
# print(f"Sum of cubes of all positive integers less than {number} is {result}")
#----------------------------------
# 66. Write a Python function to check whether a distinct pair of numbers whose product is 
# odd is present in a sequence of integer values.
# def has_odd_product_pair(numbers):
#    odd_numbers = [num for num in numbers if num % 2 == 1]
#    return len(odd_numbers) >= 2
# seq = [2, 4, 7, 9]
# if has_odd_product_pair(seq):
#     print("There is at least one distinct pair with an odd product.")
# else:
#     print("No such pair exists.")

#--------------------------------------------
# 67 .There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry
# . You are in trouble if both of them are angry or no one of them is angry.
# def in_trouble(j_angry, s_angry):
#     # You're in trouble if both are angry or neither is angry
#     if (j_angry and s_angry) or (not j_angry and not s_angry):
#         return True
#     else:
#         return False

# # Example usage:
# print(in_trouble(True, True))   # Output: True (both angry)
# print(in_trouble(False, False)) # Output: True (neither angry)
# print(in_trouble(True, False))  # Output: False
# print(in_trouble(False, True))  # Output: False

#  68 .write program that take input from user and display it 
# name = input("Enter your name :")
# add = input("Enter your address:")
# age = int(input("Enter your age :"))
# print("--------Student --------")
# print(f"Name of student : {name } \n  Address is : {add} \n Age of student : {age}")
#------------------------------------------
# 69 .Write a Python function to return the sum of the digits of a given number
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10      # get the last digit
#         total += digit      # add to total
#         n = n // 10         # remove the last digit
#     return total

# # Example usage: 
# num = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(num))
#---------------------------------------
#  69 . Write a Python program that takes a number from the user and prints its multiplication table up to 10.
# def multi_table(n):
#     num = int(input("Enter number: "))
#     print(f"Multiplication table  {num}: \n")
# for i in range(1,11):
#     print(f"{num } x {i} = num * i")
#-----------------------------------------
# 70. Given a list of integers, write a function that returns only the positive numbers.
# def get_positive_numbers(numbers):
#     positive = [num for num in numbers if num > 0]
#     return positive
# my_list = [10, -5, 0, 8, -2, 13, -1]
# result = get_positive_numbers(my_list)
# print("Positive numbers:", result)

# #or not run
# list = [10,-23,1,3,-2,-11,-29,18] 
# if list >= 0:
#     print("Positive numbers :" ,list)
#----------------------------------------------
#  71 .Build a game where the user plays Rock, Paper, Scissors against the computer.
# import random

# def rock_paper_scissors():
#     options = ["rock", "paper", "scissors"]
#     user_score = 0
#     computer_score = 0

#     while True:
#         user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()
#         if user_choice == 'exit':
#             print("\nFinal Score:")
#             print(f"You: {user_score} | Computer: {computer_score}")
#             print("Thanks for playing!")
#             break

#         if user_choice not in options:
#             print("Invalid choice. Try again.")
#             continue

#         computer_choice = random.choice(options)
#         print(f"Computer chose: {computer_choice}")

#         if user_choice == computer_choice:
#             print("It's a tie!")
#         elif (
#             (user_choice == "rock" and computer_choice == "scissors") or
#             (user_choice == "paper" and computer_choice == "rock") or
#             (user_choice == "scissors" and computer_choice == "paper")
#         ):
#             print("You win this round!")
#             user_score += 1
#         else:
#             print("Computer wins this round.")
#             computer_score += 1

#---------------------------------------------
# 72.Write a program that prints all even numbers from 1 to 100 and also prints their sum.
# def even_numbers_and_sum():
#     total = 0
#     print("Even numbers from 1 to 100:")
#     for num in range(1, 101):
#         if num % 2 == 0:
#             print(num, end=" ")
#             total += num
#     print("\n\nSum of even numbers from 1 to 100:", total)
# # Call the function
# even_numbers_and_sum()   
#----------------------------------------------
# 73 . Write a function that takes a number n and returns the sum of cubes of numbers less than n.
# def sum_of_cubes(n):
#     total = 0
#     for i in range(1, n):
#         total += i ** 3
#     return total
# num = int(input("Enter a positive number: "))
# print("Sum of cubes less than", num, "is:", sum_of_cubes(num))

#--------------------------------------
# 74 .Write a program that takes marks of 5 subjects and prints the grade:

# def calculate_grade():
#     marks = []
#     for i in range(1, 6):
#         score = float(input(f"Enter marks for subject {i}: "))
#         marks.append(score)

#     average = sum(marks) / 5

#     # Determine grade
#     if average >= 90:
#         grade = "A"
#     elif average >= 75:
#         grade = "B"
#     elif average >= 50:
#         grade = "C"
#     else:
#         grade = "Fail"

#     print(f"\nAverage Marks: {average:.2f}")
#     print(f"Grade: {grade}")
#-----------------------------------------------
# 75 .Print the sum of the current and previous number in a range from 1 to 10.
# def sum_current_and_previous():
#     previous = 0
#     print("Current  Previous  Sum")
#     for current in range(1, 11):
#         total = current + previous
#         print(f"{current:7}  {previous:8}  {total}")
#         previous = current
# sum_current_and_previous()

#-------------------------------------------------------
#76. write a program to count  not vowel in string
# def count_non_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char.isalpha() and char not in vowels:
#             count += 1
#     return count
# input_string = input("Enter a string: ")
# result = count_non_vowels(input_string)
# print("Number of non-vowel letters:", result)

# -------------------------------------------------
# 77 .write python program to display negative number in list
# def count_negative(numbers):
#     negative =[num for num in numbers if num < 0]
#     count = len(negative)
#     print("Negative numbers in the list:", negative)
#     print("Total negative numbers:", count)
# my_list = [10, -3, 5, -7, 0, 8, -1]
# count_negative(my_list)
# -----------------------------------
# 78 . Assign your name to a variable and print it.
# name = "Rohini"
# print(name)
#----------------------------------------
# 79 .Assign values of different data types to variables: int, float, string, bool, and print their types using type().
# a = 1234566
# b = "Rohini"
# c = 123.12000
# d = 34251e 
# e = 12239j
# print("data Type of a" ,type(a))
# print("data Type of b" ,type(b))
# print("data Type of c" ,type(c))
# print("data Type of d" ,type(d))
# print("data Type of e" ,type(e))
#--------------------------------------
# 80 . Create a variable price = 99.99 and quantity = 3. Calculate total cost.
# price = 99.99
# quantity = 3
# total_of = price * quantity
# print("Total =" ,total_of)
#------------------------------------------
# 81 .Assign values 1, 2, 3 to variables x, y, z in a single line. 
# x,y,z = 1,2,3 
# print("x = " ,x)
# print("y = " ,y)
# print("z = " ,z)

# 82 .Assign the same value (e.g., 100) to multiple variables a, b, c.
# a = b = c = 100
# print(a)
# print(b)
# print(c)

#----------------------------------------
# 83 .Assign your full name to a variable. Print the first and last name separately using slicing.
# full_name = "Rohini Kumbhar"

# # Find the index of the space
# space_index = full_name.find(" ")
# first_name = full_name[:space_index]
# last_name = full_name[space_index + 1:]
# print("Full Name:", full_name)
# print("First Name:", first_name)
# print("Last Name:", last_name)
#---------------------------------
#84 ..Store a sentence in a variable. Count how many words it contains.

# sentence = "Python is  a powerful and easy-to-learn programming language."

# # Split the sentence into words
# words = sentence.split()
# word_count = len(words)
# print("Sentence:", sentence)# Count the words  
# print("Number of words:", word_count)

# 85.Create a variable counter = 0. Increase it by 1, five times using a loop.
# counter = 0
# for  i in range(5):
#     counter += 1
#     print(f"after increment {i + 1} counter :{counter}")
#-----------------------------------
# 86 .Create a variable with a string "123" and convert it to an integer.
# var = "123"
# a = int(var)
# print(type(a))

#-------------------------------------------
# 87 .Check whether a variable is a string, integer, or list using isinstance().
# def check_type(variable):
#     if isinstance(variable, str):
#         print("The variable is a string.")
#     elif isinstance(variable, int):
#         print("The variable is an integer.")
#     elif isinstance(variable, list):
#         print("The variable is a list.")
#     else:
#         print("The variable is of some other type.")
# var1 = "Hello"
# var2 = 123
# var3 = [1, 2, 3]

# check_type(var1)  
# check_type(var2)  
# check_type(var3)
#--------------------------------------------------
# 87. What will be the output?
# x = 5
# x = x + 2 * 3 # 5+ 6 = 11
# print(x)
#-----------------------------------------
# 88 .Can a variable name start with a number? Try 1name = "Ravi" and observe what happens.
# 1name = "Ravi"
# print("1name")  # variable not start with any number

#----------------------------------------
# 89 .What's the difference between:
# a = [1, 2, 3]
# b = a
# b.append(4)  # using append add num in list
# print(a)
#------------------------------------------
# 90 .Write a program that:
# Takes name, age, and city from user input.
# Stores each in a variable.
# Prints a greeting like: "Hello John, age 25, from Mumbai!"
# name = input("Enter name :")
# age =int(input("Enter your age :"))
# city =input("Enter your city name :")
# print(f"Hello {name}, age {age},from {city} !/")
#----------------------------------------
#  91 . Take a sentence as input and convert it to uppercase using .upper().
# var = input("Enter which you like :")
# print(var.upper())
# ----------------------------------
# 92 .Check if a string ends with a given substring (use .endswith()).
# var = input("Enter subject: ")
# result = var.endswith("sub")
# print(result)
#----------------------------------------
# 93 . Count how many times a letter appears in a sentence (use .count()).
# char = input("Enter here something :")
# letter = input("Enter which letter you wants to count:")
# count = char.lower().count(letter.lower())
# print("Letter count in sentence :" , count)
#--------------------------
#94 .Remove leading and trailing spaces from a string using .strip().
# check_text = "   Hello friends !!!!   "
# clean_text = check_text .strip()
# print("Befor text :",check_text)
# print("After using strip text :", clean_text)

#----------------------------
# 95 .Replace all spaces with hyphens in a sentence (use .replace()).

# user ="My name is Rohini ."
# result = user.replace("","-")  # o/p = m-y-n-a-m-e-i-s
# print("Sentence :",result)

# user ="My name is Rohini ."
# result = user.replace(" ","-")  # o/p = my-name-is 
# print("Sentence :",result)
#---------------------------------------------
# 96 .Check if a string starts with a capital letter.
# str = "Hello Wolrd !!!!!!"
# if str[0].isupper():
#     print("Good !! you are enter correct string  .....")
# else:
#     print("hey!! plz Enter first Letter Capital...")

#--------------------------------------------
#97. Split a sentence into words and print each word on a new line using .split().
# sentence =input(" Enter line :" )
# word = sentence.split()
# for words in word:
#     print(words)

#--------------------------------
# 98.Join a list of words into a single sentence using " ".join(list).
# words = ["Learning", "Python", "is", "very", "interesting"]
# sentence = " ".join(words)
# print(sentence)
#-----------------------
#99 .Check whether a string is numeric using .isdigit().
# str = "704569"
# if str.isdigit():
#     print("The string is numeric :")
# else:
#     print("The string is not numberic.")
#-------------------------------------------
# 100 .Convert the first letter of each word to uppercase using .title().
# str =" we learn  python language .."
# text_title = str.title()
# print(text_title)

#--------------------------
# 101 .Reverse a string using slicing.
# var =" Good Morning !!"
# text = var[::-1]
# print("After reversing string look like: " ,text)
# def reverse_string(s):
#     return s[::-1]  # using function
# text = input("Enter a string: ")
# reversed_text = reverse_string(text)
# print("Reversed string:", reversed_text)
#--------------------------
#102 .Check if a string is a palindrome (e.g., "madam", "racecar").
# def is_palindrome(text):
#     cleaned = text.replace(" ", "").lower()  # Remove spaces and convert to lowercase for a fair comparison
#     return cleaned == cleaned[::-1]
# input_str = input("Enter a string: ")
# if is_palindrome(input_str):
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome.")
#--------------------------------------
# 103 . Write a loop that prints only the vowels in a string.
# def print_vowe(text):
#     vowels ="aeiouAEIOU"
#     print("Vowels in the string..")
#     for char in text:
#      if char in vowels :
#         print(char, end =" ")
# tak_input =input("Enter string :")
# print_vowe(tak_input)
#-----------------------------------
 
# 104. Write a loop that counts digits, letters, and spaces in a string.
# def count_d_l_S(text):
#     digit = 0
#     letter = 0
#     space = 0
#     for char in text :
#         if char.isdigit():
#           digit += 1
#         elif char.isalpha():
#           letter +=1
#         elif char.isspace():
#           space+=1

#     print("Digit count =" ,digit)
#     print("latter count =",letter)
# print("space count = ",space )
# input_str =input("Enter string :")
# count_d_l_S(char)
#-----------------------------------------
# 105 .Write a function to remove all duplicate characters from a string.
# def remove_duplicates(text):
#     result = ""
#     for char in text:
#         if char not in result:
#             result += char
#     return result
# input_str = input("Enter a string: ")
# unique_str = remove_duplicates(input_str)
# print("String without duplicates:", unique_str)

#------------------------------------
# 106 .Write a function that counts the number of uppercase and lowercase letters in a string.
# def coun_low_up(text):
#     lower = 0 
#     upper = 0
#     for char in text:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#     print("Upper count is =", upper)
#     print("Lower count os =", lower)
# User =input("Enter sentence :")
# coun_low_up(User)

#--------------------------------------------
# 107 Create a password checker:
# Must contain at least 8 characters
# Must include a digi
# Must include an uppercase lette
# Must include a lowercase letter .
# def is_valid_password(password):
#     if len(password) < 8:
#         return "❌ Password must be at least 8 characters long."

#     if not any(char.isdigit() for char in password):
#         return "❌ Password must contain at least one digit."
#     if not any(char.isupper() for char in password):
#         return "❌ Password must contain at least one uppercase letter."
#     if not any(char.islower() for char in password):
#         return "❌ Password must contain at least one lowercase letter."
#     return "✅ Password is valid!"
# user_password = input("Enter your password: ")
# result = is_valid_password(user_password)
# print(result)
#------------------------------------
# 108 . Write a program to onlt lower case  a string and print it in
# str =input("Enter string :")
# result = str.lower()
# print(result)

#---------------------------------------
# 109 Write a function that takes two integers and returns their product. Add type annotations.
# def multi_fun(x : int , y :int) -> int:
#     return  x * y
# print(multi_fun(5,9))

#-------------------------------------------
# 110. Use .format() to print a sentence using variabl
# name  =input("Enter name: ")
# age = int(input("Enter name :"))
# print("My name is {} .I am {}years old.".format(name,age))
#-----------------------------------
# 111. Write a function and declare a variable inside it. Try printing that variable outside the function. What happens?
# def my_function(message):
#     message = "Hello from inside the function!"
#     print("Inside function:", message)
# my_function()
# print("Outside function:", message) # Trying to access the variable outside the function
#        # error message not difine
#--------------------------
# 112. Use unpacking to assign values from a list: [10, 20, 30] to three variables a, b, c
# num =[10,20,30]
# a,b,c = num 
# print("a =",a )
# print("b =",b)
# print("c =",c)
#----------------------------
# 113 .Check if a variable contains a string using isinstance().
# var = "Hello"
# if isinstance(var ,str): 
#     print("variable contain string")
# else:
#     print("variable not contain string.")
#------------------------------------
#114 . Identify the invalid variable names:
# 1. _value
# 2. 2cool
# 3. user_name
# 4. user-name

# import keyword
# variable_names = ['_value', '2cool', 'user_name', 'user-name']
# def is_valid_variable(name):
#     # Check if it's a valid identifier and not a Python keyword
#     return name.isidentifier() and not keyword.iskeyword(name)
# for var in variable_names:
#     if is_valid_variable(var):
#         print(f"'{var}' is a valid variable name.")
#     else:
#         print(f"'{var}' is NOT a valid variable name.")
#---------------------------------
# 115. Concatenate two strings. 
# var = "Hello "
# var2 = " Good Morning"
# print(f" {var + var2}")             #OR

# first_name = "Ronini"
# last_name = "Kumbhar"
# Full_name = first_name +" " + last_name
# print("String concate :" ,Full_name)

#------------------------------------------
# 116 .Perform basic arithmetic operations (+, -, *, /) on numbers.
# a = int(input("Enter num :"))
# b = int(input("Enter num :"))
# print("---------Arithmatic operations----------")
# print("Addition =", a + b)
# print("substraction =" ,a-b)
# print("Multipliction =" , a * b)
# print("Division =", a / b )
#------------------------------
# 117 ,Write a program to find the largest of three numbers.
# num1 =int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# num3 = int(input("Enter third number :"))
# if num1 > num2 and num1 > num3 :
#     print("largest number is :", num1)
# elif num2 > num1 and num2 > num3 :
#     print("largest number is:" ,num2)
# elif num3 > num1 and num3 > num2:
#     print("largest number is :",num3)
# else:
#     print("numbers are same") 
#----------------------------------------
# 118 .Write a program to print the first 'n' natural numbers.
# n =int(input("Enter number :"))
# print(f" first{n} natural number :")
# for i in range(1,n+1):
#     print(i)
#---------------------------
# 119 .Find the sum of all numbers in a list using a loop.
# list =[30,27,18,37,74,36,44,28]
# total = 0
# for i in list:
#     total += i
# print("Total of list :",total)
#-------------------------------------
# 120 .Define a simple function that takes two numbers as input and returns their sum.
# def Sum_num(a,b):
#     return a + b
# num1 = 222
# num2 =899
# result =Sum_num(num1,num2)
# print("sum of num:" , result)
#---------------------------------
# 121.Convert a list to a tuple and vice versa. 
# list =[1,2,3,3,4,4,5,6]
# con_to = tuple(list) 
# print(con_to)
#---------------------------------------
# 122 .Create a list and perform operations like adding, removing, and updating elements.
# girls = ["Nehe", "Priya", "Nita","Richa","Tina"]
# girls.append ("Tina")
# girls.insert(1,"Rekha")
# print("after updating list" ,girls)
# girls.remove("Nita")
# del girls[3]
# print("After delete list :",girls)
#--------------------------------
#121 .Remove duplicates from a list
# numbers= [1,2,3,4,4,5,3,6,2,6,1]
# unique_num = list(set(numbers))  # using set operator
# print("List before: " ,numbers)
# print("List after removing duplicate :",unique_num)
#------ withou set
# numbers =[1,2,3,2,3,1,4,5,3,5,6,3,7,8,9,5]
# unique_value =[]
# for num  in numbers:
#     if num not in unique_value:
#         unique_value.append(num)
# print("Without duplicate list is :",unique_value)
#----------------------------------
# 122 .Reverse a list
# list =[2,3,11,7,5,66,7,88,9]
# for num in list[::-1]:
#     print(num , end =" ")
#-----using reverse 
# num =[2,3,11,7,5,66,7,88,9]
# reverse_list =list(reversed(num))
# print("After reversing list is :",reverse_list)
#-------------------------------------------
# 123 .Sort a list in ascending and descending order.
# list_sort =[2,5,3,7,1,9,]
# list_sort.sort()
# list_des = sorted (list_sort ,reverse = True)
# print("List ascending order :",list_sort)
# print("List are descending order :",list_des)
#------------------------------------------
# 124 . Sort a list in ascending and descending order.
# print("Print number 1 To 100 but stop on 50 ....")
# for i in range(1,101):
#     if i == 50:
#         break
#     print(i)
#--------------------------------------------
# 125 .Search for a number in a list. If found, print "Found" and exit the loop using break.
# numbers =[22,3,11,44,23,26,77,88,55,75]
# num = 44
# for i in numbers:
#     if i == num:
#          print("Found")
#          break
# else:
#     print("Not found") 
# --------------------------------
# 126 .Write a loop that keeps asking the user to enter a number until they enter 0. Use break to exit.
# while True:
#     num = int(input("Enter number(to stop enter 0 ) :"))
#     if num == 0 :
#         print("you stop loop .")
#         break
#     print("You enter numbers :",num)
#------------------------------------
# 127 .Mob number is 10 digit , break after greater than 10 digit
# while True:
#     mob_no =input("Enter your mobile number(enter 10 digit) :")
#     if len(mob_no) > 10:
#         print(" Enter 10 dogit number plz!!")
#         break
#     elif len(mob_no) == 10 and mob_no.isdigit():
#         print("Valid 10-digit number entered. Breaking loop.")
#         break
#     else:
#         print("Please enter exactly 10 digits.")
#----------------------------------
# 128 .Loop through numbers from 1 to 100. Stop the loop when you find the
#  first number that is divisible by both 2 and 7.
# for num in range(1,101):
#     if num % 2 ==0 and num % 7 == 0 :
#         print("First number is divisible by 2 or 7 is :" ,num)
#         break
#-----------------------------------------
# 129 .Ask the user to enter numbers repeatedly. Stop when the user enters the first prime number. Use break once found.
# while True:
#     num = int(input("Enter a number: "))

#     if num < 2:
#         print(f"{num} is not a prime number. Try again.")
#         continue

#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{num} is a prime number. Exiting loop.")
#         break
#     else:
#         print(f"{num} is not a prime number. Try again.")
#--------------------------------------
# 130. Given a string, loop through it and break the loop when the first vowel is found. Print the vowel.
# user = input("Enter something on here :")
# vowels ="aeiouAEIOU"
# for char in user:
#     if char == vowels:
#         print("fisrt vowel in string :",char)
#         break
#     else:
#         print("No vowel found in the string.")
# ----------------------------------
#131 .Create a number guessing game. Let the user guess until they get the correct number. Use
#  break to exit when correct.
# password = 100
# while True:
#     user =input("Guess number :")
#     if password == user :
#         print("congratulations !!you are guessing correct .")
#         break
#     else:
#         print("ohh !! you guess wrong")
#---------------------------------------
# 132.Ask the user to enter numbers one by one and store them in a list. Break the loop when the user enters a number that was already entered before.
# number =[]
# while True:
#     num = int(input("Enter number in list :"))
#     if num in number:
#         print(f"{num} already in list :")
#         break
#     else:
#         number = number.append(num)
#         print("store value.",num)
#----------------------------
# 133 .Ask for a username and password. Allow a maximum of 3 tries. Use
#  break to exit the loop when the login is successful or attempts are exhausted.
# correct_username = "admin"
# correct_password = "1234"

# for attempt in range(1, 4):
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == correct_username and password == correct_password:
#         print("Login successful!")
#         break
#     else:
#         print(f"Incorrect credentials. Attempt {attempt}/3\n")
# else:
#     print("Maximum attempts reached. Access denied.")correct_username = "admin"
# correct_password = "1234"
# for attempt in range(1, 4):
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == correct_username and password == correct_password:
#         print("Login successful!")
#         break
#     else:
#         print(f"Incorrect credentials. Attempt {attempt}/3\n")
# else:
#     print("Maximum attempts reached. Access denied.")
#--------------------------------------
#134.Keep asking the user to enter any word. If they enter the word "stop", break the loop.
# while True: 
#     User_ask =input("Enter words :")
#     if User_ask == "stop":
#         print("ohh!! you enter stop ")
#         break
#     else:
#         print("You enter words :",User_ask)
#----------------------------------------------------
# 135 .Simulate ATM PIN entry. Allow only 3 tries to enter the correct PIN. Break when the correct PIN is entered.
# correct_pin = "1234"
# attempts = 0
# max_attempts = 3
# while attempts < max_attempts:
#     entered_pin = input("Enter your ATM PIN: ") 
#     if entered_pin == correct_pin:
#         print("PIN accepted. Access granted.") 
#         break
#     else:
#         print("Incorrect PIN. Try again.")
#         attempts += 1
# if attempts == max_attempts: 
#     print("Too many incorrect attempts. Card blocked.") 
#--------------------------------------
# 136 .Keep asking the user for monthly salary inputs and store them in a list. Break the loop if a negative salary is entered.
# salaries = []

# while True:
#     salary_input = input("Enter monthly salary (negative to stop): ")
    
#     if salary_input.replace('.', '', 1).isdigit():  # allows float values like 5000.50
#         salary = float(salary_input)
#         if salary < 0:
#             print("Negative salary entered. Stopping input.")
#             break
#         salaries.append(salary)
#     else:
#         print("Invalid input. Please enter a numeric value.")
# print("\nAll valid salaries entered:")
# print(salaries)
#----------------------------------------
# 137 .Print the multiplication table of a number up to 10. Stop (break) if the result is greater than 50.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     result = number * i
#     if result > 50:
#         print(f"Result exceeded 50 at {number} x {i} = {result}. Stopping.")
#         break
#     print(f"{number} x {i} = {result}")
#-----------------------------
# 138 .Print numbers from 1 to 20, but skip all even numbers using continue.
# print("diplay number from 1 to 20 , but skip even number ...")
# for i in range(1,21):
#    if i % 2 == 0:
#     continue
#    print(i)
#----------------------------------
# 139 .Given a list of words, print only those words that have more than 4 
#characters. Use continue to skip short ones.
# count_char =["tina", "Rohan","Sita","Naina","Rohini","Vedanti"]
# for i in count_char :
#     if len(i) <= 4:
#         continue
#     print(i)
#----------------------------------
# 140 .Ask the user to enter 5 words. Skip (don't store or print) any word that starts with the letter 'a'
# accepted_words = []
# for i in range(5):
#     word = input(f"Enter word {i+1}: ")
#     if word.lower().startswith('a'):
#         continue  # Skip words starting with 'a' or 'A'
#     accepted_words.append(word)

# print("\nAccepted words (excluding those starting with 'a'):")
# for w in accepted_words:
#     print(w)
#---------------------------------
# 140 . Loop through a list of numbers and print only the positive ones. Use continue to skip negatives.
# num_list = [20,10,-25,66,-3,-1,11,-87]
# for i in num_list :
#     if i < 0:
#         continue
#     print(i)
# 141 .Print numbers from 1 to 50, but skip numbers that are divisible by 3.
# for num in range(1,51):
#   if num % 3 == 0:
#     continue
#   print(num)
# 142 .Ask the user for 5 inputs. If the input is not a number, 
#skip it using continue.
# valid_numbers = []
# count = 0
# while count < 5:
#     user_input = input(f"Enter input {count + 1}: ")
#     if not user_input.isdigit():
#         print("Not a number. Skipping.")
#         continue  # Skip non-numeric input
#     valid_numbers.append(int(user_input))
#     count += 1
# print("\nValid numbers entered:")
# print(valid_numbers)
#-----------------------------------------
# 143 .Given a string, print each character except vowels.
# str = input("Enter string:")
# vowel ="aeiouAEIOU"
# for i in str:
#     if i in vowel:
#         continue
#     print(i , end = "")
#----------------------------
# 144.From a list of mixed items (numbers and strings), print only the integers using continue.
# items = [12, "hello", 34, "world", 56]
# for i in items:
#     if not isinstance(i,int):
#         continue
#     print(i)
#------------------------------
# 145 .Keep asking the user for numbers. Skip printing if the number is
# divisible by 5. Stop when the user enters 0.
# while True:
#     take_num = int(input("Enter number :"))
#     if take_num == 0:
#         break
#     elif take_num % 5 == 0:
#         continue
#     print("you enterd ",take_num)
#----------------------------------------
# 146 .Given a string, print all characters except uppercase letters using continue.
# str = input("Enter string :")
# for char in str:
#     if char.isupper():
#         continue
#     print(str)
         
# text = "Hello World! PYTHON is Fun."

# for char in text:
#     if char.isupper():
#         continue  # Skip uppercase letters
#     print(char, end="")

# --------------------------------------------
# 147.Print numbers from 1 to 30, but skip numbers that are divisible by 3.
# for num in range(1,31):
#     if num % 3 == 0:
#         continue
#     print(num)
# 148 .Given a string with letters, digits, and special characters, print only
# the alphabetic characters.
# input_str = input("Enter a string: ")

# for char in input_str:
#     if char.isalpha():
#         print(char, end="") 
# print() 
#-----------------------------
# 149.From a list of numbers, print only those between 10 and 100 (inclusive), skip the rest.
# number =[20,11,30,200,101,40,76,105,100,155]
# for num in number:
#     if num < 10 or num > 100:
#         continue
#     print(num , end =" ")
#=--------------------------------
# 150.Keep asking the user for input. If the input contains any letter, skip it. Stop when the user types "done".
# while True:
#     user_input = input("Enter something (type 'done' to stop): ")
#     if user_input.lower() == "done":
#         break
#     if any(char.isalpha() for char in user_input):
#         continue  
#     print("Accepted input:", user_input)
#------------------------------------
# 151.Print only even numbers between 1 and 20 using continue to skip the odd ones.
# for num in range(1,21):
#     if num % 2 == 1:
#         continue
#     print(num)
#---------------------------------------
#152.From a list of strings, print only the non-empty strings.
# string_list = ["apple", " ", "banana", " ", "cherry", "", "  ", "date"]
# for item in string_list:
#     if item.strip() != "":
#         print(item)
#----------------------------
# 153. Print each character of a string except lowercase vowels (a, e, i, o, u).
# str = input("Enter string:")
# for i in str:
#     if i in 'aeiou':
#         continue
#     print(i)
#---------------------------------------
# 154 .Ask the user to enter 5 numbers. If a number is negative, 
# skip it and don’t count it.
# numbers =[]
# count =0
# while count < 5:
#     num = int(input(f"Enter number {count + 1}:"))
#     if num < 0:
#         print("negative number skip.")
#         continue
#     numbers.append(num)
#     count +=1
# print("Numbers in list",numbers)
#-------------------------------------------
#155.Keep asking the user for input. If the input contains any letter, skip it. Stop when the user types "done".
# while True:
#     user_input = input("Enter something (type 'done' to stop): ")

#     if user_input.lower() == "done":
#         break
#     if any(char.isalpha() for char in user_input):
#         print("Contains letters. Skipped.")
#         continue
#     print("Valid input:", user_input)
#---------------------------------------------------
# 156.Given a list of file names, skip printing any that contain the word "temp".
# name_of = ["python","java","c++","phptemp"]
# for char in name_of:
#     if "temp" in char:
#         continue
#     print(char, end =" ")
#--------------------------------------------------
# 157 .From a list of words, skip any word that ends with "s".
# skip_word =["goods","service","pen","mouse","home","light"]
# for char in skip_word:
#     if char.endswith("e"):
#         continue
#     print(char, end =" ")
#--------------------------------------------------
# # 158 .Print elements of a list only once, skip duplicates using a set and continue.
# items =["apple","banana","Mango","Tomato","banana"," grapes","Mango"]
# cheack = set()
# for item in items:
#     if item in cheack:
#         continue
#     cheack.add(item)
#     print(item ,end = " ")
#---------------------------------------------------
#159.Create a function called future_feature() that currently does nothing. Use pass in its body.
# def future_function():
#     pass
#-------------------------------------------------
# 160 .Write a loop that runs from 1 to 5. Use pass in the loop body.
# print("create loop for future use.") 
# for num in range(1,6):
#     print(num)
#     pass
#--------------------------------
#161 .Loop through a list of numbers. When the number is negative, just use pass.
# num_list =[11,22,33,-44,55,12,13,-23,-43]
# for num in num_list:
#     if num < 0:
#         print(num)
#         pass
#-------------------------------------------
# 162 .Ask the user to enter a number. If the number is even, print it. If it's odd, use pass.
# number =int(input("Enter number :"))
# if number % 2 == 1:
#     pass
# else:
#         print("even numbers" , number)
#-----------------------------------------
# 163 .Ask the user to enter a character.
# If it's a vowel, print "Vowel"
# If it's a consonant, pass
# If it's a number or symbol, print "Not a letter"
# user_in =input("Enter character :")
# if user_in.isalpha():
#     if user_in.lower() in'aeiouAEIOU':
#         print("vowel")
#     else:
#         pass          # cheack question
# else:
#     print("not letters.")
# #-----------------------------------------
# 164. Create a loop that runs from 1 to 10. If the number is 7, use pass and then 
# break the loop.
# for num in range(1,11):
#     if num == 7:
#         pass
#         break
#     print(num)
#----------------------------------------------
# 165 .Create a list of squares for numbers 1–10, but skip 5 using an if inside the comprehension. (You’ll simulate a pass.)
# square =[x ** 2 for x in range(1,11) if x != 5]
# print(square)
#---------------------------------------------
# 166 .Loop through indexes 0 to 5.
# Use pass when the index is 3.
# Print other indexes.
# for num in range(6):
#     if num == 3:
#         pass
#     else:
#         print(num)
#---------------------------------------------------
# 167.Ask user to enter a character If it's not a letter, print "Invalid".If it's a consonant, use pass.
# char =input("Enter character :")
# if  not char.isalpha():
#     print("Invalid ")
# elif char.lower() in 'aeiou':
#     print("vowel.")
# else :
#     pass
#------------------------------------------
# 168 .Given a string, loop through characters . Use pass for uppercase letters.Print lowercase characters only.
# user = input("Enter string :")
# for char in user:
#     if char.islower():
#         print(char, end =" ")
#     else:
#         pass
#------------------------------------------
# 170. Ask the user for a grade (A, B, C, D, F).Print custom messages for A, B, C.Use pass for D and F for now.
# user =input("Enter your grade: ")
# for char in user:
#     if char == 'A' or char == 'B' or char == 'C':
#         print(char)
#     else:
#         pass
#--------------------------------------------
# 171 .Ask the user for a number.If it's divisible by 2 and 3, print "Divisible by 2 and 3".
#If it's only divisible by 2 or 3, use pass.
# number =int(input("Enter number :"))
# if number % 2 ==0 or number % 3 == 0:
#     print("Number divisible by 2 and 3 .", number)
# else:
#     pass
#------------------------------------
# 172.Ask user for username and password.Check if both match predefined values.
#  If correct, print "Login Successful", else "Invalid login".
# useraname = "Rohini k"
# password = 120098
# user = input("Enter your username :")
# passw = int(input("Enter your password : "))
# if user == useraname or passw == password :
#     print("Login successful..")
# else:
#     print("Invalid login ...")
#------------------------------------------
# 173. Ask for two numbers and an operator (+, -, *, /)Use if-elif to perform the operation.
# num1 = float(input("Enter first number :"))
# num2 = float(input("Enter second number :"))
# enter_operator = input("Enter oprator for operation :")
# if enter_operator == "+":
#     result = num1 + num2
#     print(f"Addition = {result}")
# elif enter_operator == "-":
#     result = num1 - num2
#     print(f"Substraction ={result}")
# elif enter_operator == "*":
#     result == num1 * num2 
#     print(f"Multiplication = {result}")
# elif enter_operator == "/":
#     result =num1 / num2
#     print(f"Division ={result}")
#---------------------------------------
# 174 .Ask user to enter a character.Use if-elif-else to print:"Uppercase","Lowercase","Digit","Symbol"
# user = input("Enter chracter :")
# if user.isupper():
#     print("Uppercase")
# elif user.islower():
#     print("Lowercase .")
# elif user.isdigit():
#     print("Digit")
# else:
#     print("symbol")
#-------------------------------------------
#175 .Sum all numbers in a list using a loop.
# numbers = [4, 7, 2, 9, 5]
# total = 0
# for num in numbers:
#     total += num
# print("Sum of all numbers:", total)
#-------------------------------------
#176 .Create a new list with squares of numbers using a loop.
# num_list =[2,4,5,9,11,12,10]
# num_square =[]
# for num in num_list:
#     num_square.append(num ** 2)
#     print(f"normal list :{num_list}")
#     print(f"square of list :{num_square}")
#---------------------------------------
#180 .Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is tru
# def chcek_condition(a,b,flag):
#     if flag:
#          return a < 0 or b < 0
#     else :
#          (a >= 0) != (b >= 0)
#          print(check_condition(1, -5, False))   # True (one non-negative, one negative, flag is False)
#          print(check_condition(-1, -2, True))   # True (both negative, flag is True)
#          print(check_condition(3, 5, False))    # False (both non-negative)
#          print(check_condition(-3, 4, True))
#-----------------------------------------------
# 181 .You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
# def cat_hat_check (str):
#     cat_count = str.count("cat")
#     hat_count = str. count("hat")
#     return cat_count == hat_count
# print(cat_hat_check ("cat in hat"))
# print(cat_hat_check ("My cat in hat hat"))
# print(cat_hat_check("cat or cat that are in hat of hat"))
#----------------------------------------------------------------------------------
# 182.You are given a string s, you need to print its characters at even indices(index starts at 0).
# str = input("Enter string :")
# for  i in range(0,len(str), 2) :
#         print(str[i], end = "")
#---------------------------------------------------------------#
#183 . Let's get it more clearly through this question. Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
# num = int(input("Enter number :"))
# for i in range(num ,-1,-1):
#     print(i,end = " ")
#-----------------------------------------------------
# 184.Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
# num = int(input("Enter positive number: "))
# for i in range(1,num + 1):
#     print(f"{i}2", end = " ")
#--------------------------------------------------
#185 .ou are given a number n. The number n can be negative or positive. If n is negative, print
# #  numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
# def neg(n):
#     while n <= 0:
#         print(n, end=" ")
#         n += 1
# def pos(n):
#     n = n - 1
#     while n >= 0:
#         print(n, end=" ")
#         n -= 1
# # Main logic
# n = int(input("Enter a number: "))
# if n < 0:
#     neg(n)
# else:
#     pos(n)
#---------------------------------------------------
#186.Write a program to accept two integer numbers from the user and calculate their product .

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("product of these numbers is: ", num1 * num2)
#------------------------------------------------
# 187 Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
# print("my","name","is","Rohini" ,sep ="**")
#-----------------------------------------------
# 188 .Display Decimal Number to Octal using print() function
# num =int(input("Enter number: "))
# print("Octal number representstion :", oct(num))
#----------------------------------------------------
# 189 .Display Float Number with 2 Decimal Places
# num1 =float(input("Enter float number :"))
# print(f"{num1:.2f}")
#------------------------------------------
#190 . Accept a list of 5 float numbers as an input from the user
# float_list =[]
# num1= float(input("Enter decimal number to add in liat:"))
# float_list.append(num1)
# print(float_list)
#--------
# numbers = input("Enter 5 float numbers separated by space: ").split()
# # Convert each input to float using list comprehension
# float_list = [float(num) for num in numbers]
# print("Float list:", float_list)
#--------------------------------------------
# 191. Write all content of a file into a new file by skipping line number 5
# with open("source.txt", "r") as src:
#     lines = src.readlines()
# # Open the target file for writing
# with open("target.txt", "w") as tgt:
#     for i, line in enumerate(lines, start=1):
#         if i == 5:
#             continue  # Skip line number 5
#         tgt.write(line)
# print("Line 5 skipped and content copied to 'target.txt'")
#-----------------------------------------------
# 192 .Accept any three string from one input() call
# str1, str2 ,str3 = input("Enter string: ").split()
# print("first string is:", str1 )
# print("Second string is", str2)
# print("Third sting is :",str3)

#-----------------------------------------------------
# 193 .Write a program to use the string.format() method to format the following three variables according to the expected output.
# totalMoney = 1000
# quantity = 3
# price = 450
# output = "I have {} dollars so I can buy {} football for {:.2f} dollars.".format(totalMoney, quantity, price)
# print(output)
#----------------------------------------------
# 194 .Write a program to check if the given file is empty or 
# import os
# file_path = "example.txt"  # Replace with your file name
# # Check if the file exists first
# if os.path.exists(file_path):
#     if os.stat(file_path).st_size == 0:
#         print("The file is empty.")
#     else:
#         print("The file is not empty.")
# else:
#     print("The file does not exist.")
#-------------------------------------------------
#195 .Ask the user for a numerator and a denominator. Calculate the percentage and display 
# it with two decimal places followed by a percent sign (e.g., 75.50%).
# numerator = int(input("Enter the numerator: "))
# deno = int(input("Enter denominator: "))
# per = numerator / deno * 100
# print(f"Percentage is : {per:.2f} %")
#---------------------------------------
# 196.Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action
# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Calculate Square")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")
#     if choice == "1":
#         print("Hello!")
#     elif choice == "2":
#         num = float(input("Enter a number: "))
#         print(f"The square of {num} is {num ** 2}")
#     elif choice == "3":
#         print("Exiting program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#--------------------------------------------------------------
#197 .Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
# word =input("Enter the word: ")
# num = int(input("Enter the number: "))
# print(f"{word:> 20}{num}")
# 198. You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# # Print header
# print(f"{'Name':<10} {'Score':<5}")
# print("-" * 16)
# # Print each name with its corresponding score
# for name, score in zip(names, scores):
#     print(f"{name:<10} {score:<5}")
#--------------------------------------------
# 199 .Ask the user for a number. Print this number padded with leading zeros to a width of 5.
# num = input("Enter a number: ")
# print(num.zfill(5))
#------------------------------------------
# 200.Write a Python code to remove characters from a string from 0 to n and return
# def remove_char(word,n):
#     print("Remove n char from string")
#     print(remove_char,"Rohini",4)
#     print(remove_char,"Kumbhar ",2 )
#----------------------------------------------
# 201 Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
# chack_list =[12,20,15,30,35,12]
# if len(chack_list) > 0 and chack_list [0] == chack_list [-1]:
#     print("True")
# else:
#     print("False")
# #--- With function
# def cheack_first_last(number):
#     if len(number) < 1:
#         return False
#     return number[0] == number[-1]
# sample_list = [10, 20, 30, 10]
# print(cheack_first_last(sample_list))
#---------------------------------------------
# 202 . Write a Python code to display numbers from a list divisible by 5
# divisible_list = [5,10,66,11,25,30,33,35,40,15]
# print( "The number divisible by five :")
# for i in divisible_list :
#     if i % 5 ==0 :
#         print( i)
#------------------------------------------
#203 . Write a Python code to find how often the substring “Emma” appears in the given string.
# sentence = "Emma is good developer. Emma is a writer"
# words = sentence.split()

# count = 0
# for word in words:
#     if word == "Emma":
#         count += 1

# print("Emma appears", count, "times")
#-------------------------
# str = "Emma is good developer. Emma is a writer"
# count = str.count("Emma")
# print(f"Emma appeared {count} times")
#------------------------------------------------
# 203.  Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
# for i in range(1,6):
#     for j in range(i):
#         print(i, end =" ")
#     print()
#------------------------------------------
# 204 .Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
# num = int(input("Enter a number: "))
# original = str(num)
# reversed_num = original[::-1]

# if original == reversed_num:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")
#----------------------------------------------
#205. Given two lists of numbers, write Python code to create a new list containing odd numbers
#  from the first list and even numbers from the second list.
# list_num =[1,3,2,6,9,18]
# list_str =[12,14,33,11,44,18]
# odd_con = [i for  i in list_num  if i % 2 != 0]
# even_con =[num for num in list_str if num  % 2 == 0]
# list_merge = odd_con + even_con
# print(list_merge)
#--------------------------------------------
# 206.For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
# num = int(input("Enter number:"))
# reverse_num = str(num)[::-1]
# print(reverse_num)
#-------------------------------------
#207 .Calculate income tax for the given income by adhering to the rules below
# income = float(input("Enter your income: "))

# tax = 0

# if income <= 10000:
#     tax = 0
# elif income <= 20000:
#     tax = (income - 10000) * 0.10
# else:
#     tax = (10000 * 0.10) + (income - 20000) * 0.20

# print("Income Tax =", tax)
#----------------------------------------------
# 208. Write a code to generates a complete multiplication table for numbers 1 through 10.
# for num in range(1,11):
#     for j in range(1,11):
#         print(f"{num * j}",end ="\t")
#     print()
#---------------------------------------------
# 209.Print a downward half-pyramid pattern of stars
# row =5
# for i in range(row,0,-1):
#     for num in range(i):
#         print("*", end =" ")
#     print()
#---------------------------------------
# 210 . Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base, exp):
#     result = 1
#     for _ in range(exp):
#         result *= base
#     return result

# # Example usage:
# print(exponent(2, 3))  # Output: 8
# print(exponent(5, 4))
#---------------------------------------------
# 211 .Write a code find if a given year is a leap year.
# year = int(input("Enter year :"))
# if year % 4 == 0:
#     print(f" {year} is leap year..")
# else:
#     print(f"{year} is not leap year..")``
#-------------------------------------------------------
# 112. A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# # Step 1: Collect all primes till 20
# primes = []
# for num in range(2, 21):
#     if is_prime(num):
#         primes.append(num)
# #Step 2: Print alternate primes
# print("Alternate prime numbers till 20:")
# for i in range(0, len(primes), 2):
#     print(primes[i], end="")
#--------------------------------
#213. Print Reverse Number Pattern
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#-------------------------------------
# 214.Check if a user-entered string contains any digits using a for loop
# text = input("Enter a string: ")

# has_digit = False

# for char in text:
#     if char >= '0' and char <= '9':
#         has_digit = True
#         break
#     if has_digit:
#         print("The string contains digits.")
# else:
#     print("The string does not contain any digits.")
#--------------------------------------
# 215 .Capitalize the first letter of each word in a string
# str =input("Enter string:")
# capital = str.title()
# print(capital)
#-------------------------------------
# 216.Create a simple countdown timer using a while loop.
# import time
# count = int(input("Enter countdown time in seconds: "))
# while count > 0:
#     print(count)
#     time.sleep(1)  # Waits for 1 second
#     count -= 1

# print("Time's up!")
#-----------------------------------------
# 217.Print first 10 natural numbers using while loop
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

#--------------------------------------
# 218.Write a Python code to print the following number pattern using a loop.
# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#--------------------------------------
# 219.Calculate sum of all numbers from 1 to a given number
# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("Sum from 1 to", n, "is:", sum)
#------------------------------------------
# 220 Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop


