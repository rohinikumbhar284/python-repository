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
# 220. Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

#--------------------------------------------------
# 221 . Print list in reverse order using a loop
# my_list =[23,11,44,34,86,56,88]
# for num in my_list[::-1]:
#     print(num , end =" ")
#-----------------------------------------
# 222. Display numbers from -10 to -1 using for loop
# for num in range(-10 , 0):
#     print(num,end =" ")
#----------------------------------------
# 223 . Display a message “Done” after the successful execution of the for loop
# for num in range(5):
#     print(num)
# print("done !")
#-----------------------------------------
# #######224.  Print all prime numbers within a range


#------------------------------------------
# 225 . Display Fibonacci series up to 10 terms


#--------------------------------------'
# 226.Find the factorial of a given number
# num = int(input("Enter number: "))


# #-------------------------------------------
# # 227.Reverse a integer number
# num = int(input("Enter number :"))
# for num in  range[::-1]:
#     print(num)

#------------------------------------
# 228. Swap the values of two variables without using a third variable or temp.
# a = 10
# b = 5
# a = a + b  # a = 15
# b = a - b  # b = 10
# a = a - b  # a = 5
# print("a =", a)
# print("b =", b)
# 229.Take input for two numbers and print their average rounded to 2 decimal places.
# a = int(input("Enter number :" ))
# b = int(input("Enter number: "))
# avg_of = a = b / 2
# print(f"Average of number is: { avg_of:.2f}")
#-------------------------------------
# 230. Show how to assign the same value to multiple variables and then change one—what happens?
# a = b = c = 100  
# print(a, b, c)  # Output: 100 100 100
# a = 200         # Now 'a' is reassigned to a new int object (200)
# print(a, b, c)  # Output: 200 100 100
# b = 400    # 'b' is reassigned
# print(a,b,c)
# a = 80
# print(a)

# 231.Declare a variable, delete it using del, and try accessing it—what happens?
# a =" rohini"
# print(a)
# b = 600
# print(b)
# del a
# print(a) # this will raise nameerror
#-----------------------------------------
# 232.take a float input, convert it to int, and explain the output.
# number_float =float(input(" Enter number to convert into integers:"))
# convert = int(number_float)
# print("Number in float:",number_float)
# print("number after convert into int:",convert)
#---------------------------------------------
# 233.Convert a number string "123" to integer and add 10.
# str = "123"
# convert = int(str)
# print(f"string convert into number:{convert + 10}")
#----------------------------------------------
# 234.Use type() and isinstance() to check types of multiple variables.
# a = 10            
# b = 3.14         
# c = "hello"       
# d = [1, 2, 3]     # list
# e = (4, 5)        # tuple
# f = {"x": 1}      # dict
# g = True          # bool
# # Using type()
# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# print(type(c))  # <class 'str'>
# print(type(d))  # <class 'list'>
# print(type(e))  # <class 'tuple'>
# print(type(f))  # <class 'dict'>
# print(type(g))  # <class 'bool'>
# print(isinstance(a, int))    # True  # Using isinstance()
# print(isinstance(b, float))  # True
# print(isinstance(c, str))    # True
# print(isinstance(d, list))   # True
# print(isinstance(e, tuple))  # True
# print(isinstance(f, dict))   # True
# print(isinstance(g, bool))   # True
#-----------------------------------------------
# 235.What will be the result of int("10.5")? Try it and fix the error.
# num = int("10.5")
# print(num)     #invalid literal for int() with base 10: '10.5'
# 236. Use eval() to convert a string "3 + 5" to an expression and execute it.
# exp = "3 + 5"
# convert = eval(exp)
# print("orignal: ",exp)
# print(f"convert to expression: {convert}" )
#------------------------------------------------
# 236. Write a function that modifies a global variable.
# count = 0
# def increment():
#     global count   # Tell Python we are referring to the global 'count'
#     count += 1     # Modify the global variable
# # Call the function multiple times
# increment()
# increment()
# print("Final count:", count)  # Output: 2
# increment()
# increment()
# print(" Ater add :",count)
#-------------------------------------------------
# 237.Use a local variable with the same name as a global variable—what’s printed?
# num = 22
# def check_golbal_local():
#     num = 11
#     print("Inside function")
# check_golbal_local()
# print("Outside:", num)
#-----------------------------------------------
# 238.Create a nested function where the inner one accesses variables from the outer function.
# def outer_fun ():
#     var = " Rohini"
#     print("My name is:" ,var)
#     def innaer_fun():
#         age= 30
#         print(f"hello , {var} , I thik you are {age} years old")
#     innaer_fun()
# outer_fun()
#------------------------------------------
# 239.Find the sum of all numbers from 1 to N.
# num = int(input("Enter number:"))
# total = 0
# for i in range(1, num+1):
#     total +=i
  
#     print(f" Addition of {num} is :" ,total)
#-------------------------------------------
# 240.Get the current year and birth year from the user. Calculate and print their age.
# current_year = int(input("Enter current year :"))
# birth_year = int(input("Enter your bith year: "))
# age = current_year - birth_year
# print("Your age is: ", age)
#---------------------------------------------
# get a number from the user and print the square and cube of it.
# number= int(input("Enter the number: "))
# square_of = number ** 2
# cube_of = number ** 3
# print(f"The square of {number} is : {square_of} ")
# print(f"The cube of {number} is: {cube_of} ")
#---------------------------------------
# 241.Store the prices of three products in variables and print the total and average price.
# car = int(input("Enter the car price: " ))
# book =int(input("Enter the book price: "))
# pen = int(input("Enter pen price: " ))
# total = car + book + pen
# Avg_of = (car + book + pen)/3
# print("Total: ",total)
# print("Average :", Avg_of)
#=----------------------------------------
#  242.Take temperature in Celsius from the user and convert it to Fahrenheit.
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit:", fahrenheit)
#-----------------------------------------------------
# 243 .Take a 4-digit number and separate it into thousands, hundreds, tens, and units.
# number = int(input("Enter a 4-digit number: "))
# # Extract digits
# thousands = number // 1000
# hundreds = (number % 1000) // 100
# tens = (number % 100) // 10
# units = number % 10
# # Display result
# print("Thousands:", thousands)
# print("Hundreds:", hundreds)
# print("Tens:", tens)
# print("Units:", units)
# -----------------------------------------
# 244.Take two variables (width and height) and calculate area and perimeter of a rectangle.
# Width_of = int(input("Enter the width of rectangle: "))
# lenth_of =int(input("Enter the lenth of rectangle: "))
# area = Width_of * lenth_of
# perimeter = 2 *(Width_of + lenth_of)
# print(f"Area of rectangle: {area}")
# print(f"Perimeter of rectangle: {perimeter} ")
#--------------------------------------------
# 245. Store marks of 5 subjects in different variables and print the total, average, and percentage.
# subject1 = float(input("Enter marks for Subject 1: "))
# subject2 = float(input("Enter marks for Subject 2: "))
# subject3 = float(input("Enter marks for Subject 3: "))
# subject4 = float(input("Enter marks for Subject 4: "))
# subject5 = float(input("Enter marks for Subject 5: "))
# total = subject1 + subject2 + subject3 + subject4 + subject5
# average = total / 5
# percentage = (total / 500) * 100  # Assuming each subject is out of 100

# print("Total Marks:", total)
# print("Average Marks:", average)
# print("Percentage:", percentage, "%")
#-------------------------------------------
# 246.Ask the user for their monthly income and monthly expenses. Calculate and print:
# Savings amount
# Savings percentage
# income = float(input("Enter your monthly income: "))
# expenses = float(input("Enter your monthly expenses: "))
# savings = income - expenses   # Calculate savings
# savings_percent = (savings / income) * 100 if income != 0 else 0
# print("Savings amount:", savings)
# print("Savings percentage:", round(savings_percent, 2), "%")
#----------------------------------------
# 247.Get a number from the user and show the last digit, first digit, and sum of digits.
# number =input("Enter number: ")
# last_di =int(number[-1])
# first_di = int(number[0])
# sum_di = sum(int(digit) for digit in number)
# print("First digit is:", first_di)
# print("Last digit is:", last_di)
# print("Sum of number :", sum_di)
#------------------------------------------
# 248.Ask for distance in kilometers. Convert and print:# In meters # In centimeter # In millimeters
# km = float(input("Enter distance in kilometers: "))
# meters = km * 1000
# centimeters = km * 100000
# millimeters = km * 1000000
# print("Distance in meters:", meters)
# print("Distance in centimeters:", centimeters)
# print("Distance in millimeters:", millimeters)
#------------------------------------------------
# 249.ake length and breadth of a box and height. Calculate and print volume.
# length = float(input("Enter the length of the box: "))
# breadth = float(input("Enter the breadth of the box: "))
# height = float(input("Enter the height of the box: "))
# volume = length * breadth * height
# print("Volume of the box:", volume)
#---------------------------------------------
#250. Input 3 sides of a triangle. Calculate and print perimeter and semi-perimeter.
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# perimeter = a + b + c
# semi_perimeter = perimeter / 2
# print("Perimeter of the triangle:", perimeter)
# print("Semi-perimeter of the triangle:", semi_perimeter)
#----------------------------------------------
# 251. Create a variable for your full name. Print initials and the length of your name.
# full_name = input("Enter your full name: ")
# name_parts = full_name.strip().split()    # Split name into words
# initials = "".join([part[0].upper() for part in name_parts])
# name_length = len(full_name.replace(" ", ""))    # Length of name (excluding spaces)
# print("Initials:", initials)
# print("Length of name (without spaces):", name_length)
#---------------------------------------------
# 252. Create variables to store current hour and minutes. Calculate how many minutes have passed since midnight.
# hour = int(input("Enter current hour (0-23): "))
# minute = int(input("Enter current minutes (0-59): "))
# # Calculate total minutes since midnight
# minutes_since_midnight = hour * 60 + minute
# print("Minutes passed since midnight:", minutes_since_midnight) 
#-------------------------------------------------
# 253.Ask the user for number of hours and rate per hour. Print their total earnings.
# hours = int(input("Enter  number of Hours :"))
# rate_per_hour =float(input("Enter rate per hour: "))
# total_earning = hours * rate_per_hour
# print("Total eranings:",total_earning)
#----------------------------------------------
# 254. Write a program to convert total seconds to hours, minutes, and seconds.
# total_seconds = int(input("Enter total seconds: "))
# hours = total_seconds // 3600    
# # Convert to hours, minutes, and seconds
# remaining_seconds = total_seconds % 3600
# minutes = remaining_seconds // 60
# seconds = remaining_seconds % 60
# print("Time: {} hour(s), {} minute(s), {} second(s)".format(hours, minutes, seconds))

#---------------------------------------------------
# 255. Get 3 subject marks from user and check:# If all are above 35 → print "Pass"# If any one is below 35 → print "Fail"
# sub1 = int(input("Enter sub1 marks: "))
# sub2 = int(input("Enter sub2 marks: "))
# sub3 = int(input("Enter sub3 marks: "))
# if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
#     print( "pass")
# else:
#     print("Fail") 
#---------------------------------------------------
# 256. Ask the user for a number and print its square root (without using math module).
# num = float(input("Enter a number: ")) 
# # Calculate square root
# sqrt = num ** 0.5
# print("Square root of", num, "is", sqrt)
#----------------------------------------------------
# 257.Input the side of a square. Calculate and print the perimeter and area.
# squ_side = float(input("Enter side of aquare: "))
# area = squ_side * squ_side
# perimeter = 4 * squ_side
# print("Area of square: ", area)
# print(" perimeter of square: ", perimeter)
#-----------------------------------------
# 258.Enter length and width of a rectangle. Calculate diagonal using Pythagorean theorem.
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# # Calculate diagonal using Pythagorean theorem
# # diagonal² = length² + width² → diagonal = √(length² + width²)
# diagonal = (length ** 2 + width ** 2) ** 0.5
# print("Diagonal of the rectangle:", diagonal)
#--------------------------------------------
# 259.Ask for the base and height of a triangle. Print whether the triangle is equilateral, isosceles, or scalene.
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# if a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")
#------------------------------------------
# 260. Input the radius of a circle. Calculate and print the area and circumference.
# redius_of = float(input("Enter the redius of circle:"))
# area = 3.14 * redius_of ** 2
# cicumference = 2 * 3.14 * redius_of
# print("Area of circle is: ",area)
# print("Circumference of circle is: ",cicumference)
#-----------------------------------------------
# 261.Take employee name, basic salary, HRA (20%), and DA (30%). Calculate gross salary.
# name = input("Enter the Employee name: ")
# basic_sal = float(input("Enter basic salary: "))
# hra_of = 0.20 * basic_sal
# da_of = 0.30 * basic_sal
# gross_sal = basic_sal + hra_of + da_of
# print("Employee Name: ",name)
# print("Gross salary of  employee :",gross_sal)
#-------------------------------
# 262.Take total sales amount and commission rate. Calculate and print the commission earned.
# sales = float(input("Enter sales amunt:"))
# rate = int(input("Enter commission rate(in %): "))
# commission =(rate / 100) * sales
# print("Commision earned:",commission)
#--------------------------------------------
# 263.A shopkeeper buys a product for ₹200 and sells for ₹275. Calculate profit and profit %.
# buy = 200
# sales = 275
# profit = sales - buy 
# profit_in = (profit / buy ) * 100
# print(f"profit on {buy} product is ", profit)
# print("Profit in percentage is", profit_in)
#--------------------------------------------
# 264.Take a loan amount, interest rate, and time in years. Calculate simple interest.
# principal = float(input("Enter the loan amount (Principal): ₹"))
# rate = float(input("Enter the annual interest rate (%): "))
# time = float(input("Enter the time (in years): "))
# simple_interest = (principal * rate * time) / 100
# print("Simple Interest is: ₹", simple_interest)
#---------------------------------------------
# 265.Take 3 months of expenses. Calculate average monthly expense and estimate yearly expense.
# mon1 = float(input("Enter first month expenses: "))
# mon2 = float(input("Enter second month expenses: "))
# mon3 = float(input("Enter third month expenses: "))
# mon_avg = (mon1 + mon2 + mon3) / 3
# year_avg = mon_avg * 12
# print(" 3 month of Expenses: ", mon_avg)
# print("Yearly expenses: ",year_avg)
#----------------------------------------------------
# 266.Ask the user to input hours and convert it into minutes and seconds.
# hour = int(input("Enter hour: "))
# cov_min = hour * 60
# con_sec = hour * 3600
# print("Minutes: ",cov_min)
# print("Second: ", con_sec)
#-------------------------------------------
# 267. Ask for total number of seconds. Convert and print hours, minutes, and remaining seconds.
# total_seconds = int(input("Enter total seconds: "))
# # Calculate hours
# hours = total_seconds // 360
# # Calculate remaining minutes
# minutes = (total_seconds % 3600) // 60
# # Remaining seconds
# seconds = total_seconds % 60
# print("Hours:", hours)
# print("Minutes:", minutes)
# print("Seconds:", seconds)
#---------------------------------------
# 268. Convert temperature:
# Celsius to Fahrenheit: F = C × 9/5 + 32
# Fahrenheit to Celsius: C = (F - 32) × 5/9
# print("Temperature Conversion")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")

# # Take user's choice
# choice = int(input("Enter your choice (1 or 2): "))

# if choice == 1:
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = celsius * 9 / 5 + 32
#     print("Temperature in Fahrenheit:", round(fahrenheit, 2))

# elif choice == 2:
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5 / 9
#     print("Temperature in Celsius:", round(celsius, 2))

# else:
#     print("Invalid choice. Please enter 1 or 2.")
#-----------------------------------------------------------
# 269. Ask for weight in kilograms and convert it to grams, pounds, and ounces.
# kg = float(input("Enter weight in kg: "))
# grams = kg * 1000
# pounds = kg * 2.20462
# ounces = kg * 35.274
# print("Weight in grams:", round(grams, 2))
# print("Weight in pounds:", round(pounds, 2))
# print("Weight in ounces:", round(ounces, 2))

#-----------------------------------------
# 270. onvert distance from kilometers to: meters,centimeters,miles
# distance = float(input("Enter a distance in kilometer: "))
# in_meter = distance * 1000
# in_centimeter = distance * 100000
# in_miles = distance * 0.621371
# print(f" {distance} kg Distance in meter: ",in_meter)
# print(f" {distance} kg Distance in centimeter: ",in_centimeter)
# print(f" {distance} kg Distance in miles : ",in_miles)

#-----------------------------------------------------
# 271. Ask user for birth year. Calculate and print their current age and years left to reach 100.
# from datetime import datetime
# birth = int(input("Enter your birth year: "))
# current = datetime.now().year
# cur_age = current - birth
# left_to = 100 - cur_age
# print("Your current age is :", cur_age)
# print(f" After {left_to} year you reach 100.")
#--------------------------------------------------
# 272. Ask user for current time (hour only). Tell them how many hours are left until midnight.
# current_hour = int(input("Enter the current hour (0 to 23): "))
# if 0 <= current_hour <= 23:
#     hours_left = 24 - current_hour
#     print("Hours left until midnight:", hours_left)
# else:
#     print("Invalid hour! Please enter a value between 0 and 23.")
#------------------------------------------------------
# 273 .Input the user's first and last name. Print:Full name  ,Initials,Total character count (excluding space)
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# full_name = first_name + " " + last_name
# initials = first_name[0].upper() + last_name[0].upper()  # Initials
# char_count = len(first_name + last_name)   # Total characters excluding space
# print("Full Name:", full_name)
# print("Initials:", initials)
# print("Total Characters (excluding space):", char_count)
#-----------------------------------------------------------
# 274. Ask a user to input their name and lucky number. Print a fun message like:
# “Hey Alex! Your lucky number is 7 — try your luck today!”
# name = input("Enter your name: ")
# number= input("Enter your lucky number : ")
# print(f"Hey {name} ! Your Lucky number is {number} - try your luck today!")
#-----------------------------------------------------------------
# 276.Ask for two float numbers. Round them to 2 decimal places and add them.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num_rount = round(num1 ,2)
# num2_round = round(num2 , 2)
# total = num_rount + num2_round
# print("Addition of number.", total)
#------------------------------------------
# 277.  Input a string from the user.Ignore spaces.Find the character that appears most frequently. Print that
# character.
# text = input("Enter a string: ")
# text = text.replace(" ", "") 
# # Step 3: Count frequency of each character
# freq = {}
# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# # Step 4: Find the character with the highest frequency
# max_char = max(freq, key=freq.get)
#-----------------------------------------------
# 278. Ask the user for a number and print whether it is a multiple of 3 or 5.
# num = int(input("Enter number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print(f" {num}  multiple of 3 and 5.")
# else:
#     print("It's not multiple of 3 and 5.")
#-----------------------------------------------
# 279. Print numbers from 10 to 1 using a loop.
# for num in range(10,0,-1):
#     print(num)
#-------------------------------------
# 280. Input a string and a character. Count how many times the character appears.
# text = input("Enter a string: ")
# char = input("Enter a character to count: ")
# count = text.count(char)
# print(f"The character '{char}' appears {count} time(s).")

#------------------------------------
# 281. Input a sentence. Print the first and last word.
# sentence = input("Enter your sentence.")
# word = sentence.split()
# if len(word ) >= 1:
#     print("First word:",word[0])
#     print("Last word :",word[-1])
# else:
#     print("No word")
#=----------------------------------------------
# 282.Input a string. Remove all spaces from it.
# str= input("Enter string : ")
# word = str.replace(" ","")
# print(str)
# print(word)
#--------------------------------------------
# 283.Input a string and print it in title case (first letter of each word capital).
# str= input("Enter string : ")
# word = str.title()
# print(str)
# print(word)
#=----------------------------------------------
# 284.Replace all spaces in a sentence with hyphens
# str= input("Enter string : ")
# word = str.replace(" ", "#")
# print(str)
# print(word)
#--------------------------------------------------
# 285 .Check if two input strings are anagrams (same letters, different order).
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()
# # Check if sorted characters are equal
# if sorted(str1) == sorted(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
#--------------------------------------------------
# 286.input a string. Find the character that appears most frequently.# Input a string from the user
# text = input("Enter a string: ")

# # Dictionary to store character frequencies
# freq = {}
# # 
# # Loop through characters, ignoring spaces
# for char in text:
#     if char != " ":
#         freq[char] = freq.get(char, 0) + 1

# # Find the character with the highest frequency
# if freq:
#     most_frequent = max(freq, key=freq.get)
#     print("Most frequent character:", most_frequent)
# else:
#     print("No characters to check.")
#-------------------------------------------------
# 287.Input a string and print all words that are longer than 4 letters
# str = input("Enter string: ")
# word = str.split()
# for i in word:
#     if len(i) > 4 :
#         print("words gretwr than length 4 :", i)
#----------------------------------------------
# 288. Remove all duplicate characters from a string (preserve order).
# text = input("Enter a string: ")

# Create an empty string to store result
# result = ""

# # Set to track seen characters
# seen = set()
# # Loop through each character
# for char in text:
#     if char not in seen:
#         result += char
#         seen.add(char)

# # Print result
# print("String after removing duplicates:", result)
#-------------------------------------------
# 289 .Input a string. Swap the case of every letter (upper → lower, lower → upper).
# text = input("Enter a string: ")
# Swap the case of each character
# swapped = text.swapcase()
# # Print the result
# print("Swapped case string:", swapped)
# # without using swapcase 

# text = input("Enter your string: ")
# swapped =" "
# for char in text:
#     if char.isupper():
#         swapped += char.lower()
#     elif char.islower():
#         swapped += char.upper()
#     else:
#         swapped += char
# print("Ater swap string: ",swapped)
#--------------------------------------
# 290. Input a sentence. Count the number of words.
# sentence = input("Enter sentence: ")
# word = sentence.split()
# count_word = len(word)
# print("Number of words in sentence:",count_word )
#----------------------------------------
# 291.Input a sentence and print each word in reverse (but keep word order).
# sentence = input("Enter sentence: ")
# words = sentence.split()
# word_repeat = [word[::-1] for word in words]
# #Join the reversed words with a space
# result = ' '.join(word_repeat)
# print(sentence)
# print("After each word reverse in senternce: ",result)
#-----------------------------------------------------
# 292. Take a string and print only the characters at even indexes.
# text = input("Enter a string: ")
# # Get characters at even indexes using slicing
# even_index_chars = text[::2]
# # Print the result
# print("Characters at even indexes:", even_index_chars)
#-------------------------Another way - using loop
# text = input("Enter a string: ")
# result = ""
# # Loop through each index
# for i in range(len(text)):
#     if i % 2 == 0:  # Check if index is even
#         result += text[i]
# print("Characters at even indexes:", result)
#--------------------------------
# 293.Input a string. Replace every vowel with *.
# str= input("Enter string : ")
# vowel ="aeiouAEIOU"
# result =" "
# for char in str:
#     if char in vowel:
#         result += "*"
#     else: 
#         result += char
# print("String after replace vowel: ",result)
#----------------------------------------------
# 294 .Input a string and print all unique characters in it.
# str = input("Enter string: ")
# for char in str:
#     if str.count(char) == 1:
#         print(char, end = " ")
#--------------------------------------------------
# 295. Find the longest word in a given sentence.
# str = input("Enter string: ")
# word = str.split()

# longest = " "
# for words in word:
#     if len(words) > len(longest):
#         longest = words
# print("In sentence longest word is : ", longest)
#-----------------------------------------
# 296.Input two strings. Print True if one string is a substring of the other.
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
# if str1 in str2 and str2 in str1:
#     print("True")
# else:
#     print("False")
#-----------------------------------
# 297.Check whether a string contains only digits (without using str.isdigit()).
# text = input("Enter string: ")
# only_digit = True
# for char in text:
#     if char < '0' and char > '9':
#         only_digit = False
#         break 
# print("Contain only digit: ",only_digit)
#-------------------------------------------------
#298. Input a string and shift every character forward by 1 (a → b, z → a).
# text = input("Enter a string: ")

# shifted = ""

# for char in text:
#     if 'a' <= char <= 'y' or 'A' <= char <= 'Y':
#         shifted += chr(ord(char) + 1)
#     elif char == 'z':
#         shifted += 'a'
#     elif char == 'Z':
#         shifted += 'A'
#     else:
#         shifted += char  # Keep non-alphabet characters unchanged

# print("Shifted string:", shifted)
#-----------------------------------------------
#299 .Input a string and print a frequency dictionary of all characters.
# str = input("Enter string: ")
# freq = { }
# for char in str:
#     if char in freq:
#         freq[char] +=1
#     else:
#         freq[char] = 1
# print("Character frequency dictionary:")
# print(freq)
#----------------------------------------------
# 300. Check if all characters in a string are alphabetic (A-Z, a-z).
# text = input("Enter a string: ")
# all_alpha = True
# for char in text:
#     if not ('A' <= char <= 'Z' or 'a' <= char <= 'z'):
#         all_alpha = False
#         break
# print("All characters are alphabetic:", all_alpha)
#----------------------------------------
# 301. Remove all special characters and digits from a string.
# str = input("Enter string: ")
# result =" "
# for char in str:
#     if 'A' <= char <= 'z' or 'a' <= char <= 'z':
#         result += char
# print("Remove all digit and special char from string: ",result)
# #-------------------Using isalpha
# str = input("Enter sting: ")
# for char in str:
#    if char.isalpha():
#        print("Remove all digit :" ,char)
#-----------------------------------------------------
# 302. Input a sentence. Count how many words start with a capital letter
# sentence = input("Enter sentence: ")
# word = sentence.split()
# count = 0
# for char in sentence:
#     if char and char[0].isupper():
#         count += 1
# print("Number of words starting with a capital letter:", count)

#_---------------------------------------------------
# #303. Find the second most frequent character in a string.
# text = input("Enter a string: ")

# # Dictionary to store character frequencies
# freq = {}

# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# # Sort characters by frequency (highest to lowest)
# sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# # Check if there are at least 2 unique characters
# if len(sorted_freq) >= 2:
#     second_most = sorted_freq[1]
#     print("Second most frequent character:", second_most[0])
#     print("Frequency:", second_most[1])
# else:
#     print("Not enough unique characters to determine second most frequent.")
# #---------------------- 
# from collections import Counter

# text = input("Enter a string: ")

# # Count frequency of each character
# counter = Counter(text)

# # Get most common characters sorted by frequency
# common = counter.most_common()

# # Check if there are at least 2 unique characters
# if len(common) >= 2:
#     second_most_char, freq = common[1]
#     print("Second most frequent character:", second_most_char)
#     print("Frequency:", freq)
# else:
#     print("Not enough unique characters to determine second most frequent.")
#-----------------------------------------------
# 304 .Input a string and compress it: "aaabbcc" → "a3b2c2"
# text = input("Enter a string: ")
# compressed = ""
# count = 1
# for i in range(1, len(text)):
#     if text[i] == text[i - 1]:
#         count += 1
#     else:
#         compressed += text[i - 1] + str(count)
#         count = 1
# # Add the last character and its count
# if text:
#     compressed += text[-1] + str(count)

# print("Compressed string:", compressed)
#----------------------------------------
# 304. Find all positions of a given character in a string.
# str = input("Enter string: ")
# char = input("Enter char to find : ")
# position =[]
# for i in range(len(str)):
#     if str[i] == char:
#         position.append(i)
# print("Position of ,char, in string is: ",position)
#---------------------------------------------
# 305.Check if a given string is a valid identifier (like variable names in Python).
# text = input("Enter a string: ")

# if text.isidentifier():
#     print("Valid Python identifier.")
# else:
#     print("Not a valid Python identifier.")


#--------------------------------------------------
# 306 .Convert a camelCase string to snake_case.
# text = input("Enter a camelCase string: ")

# snake = ""

# for char in text:
#     if char.isupper():
#         snake += '_' + char.lower()
#     else:
#         snake += char

# print("snake_case string:", snake)
#-------------------------------------------
# 307. Find the first non-repeating character in a string.
# text = input("Enter a string: ")

# for char in text:
#     if text.count(char) == 1:
#         print("First non-repeating character:", char)
#         break
# else:
#     print("No non-repeating character found.")
# -----------------------------------#
# 308. Compress a string:"aaabbcc" → "a3b2c2"
# def compress_string(s):
#     if not s:
#         return ""
#     result = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             result += s[i - 1] + str(count)
#             count = 1
#     result += s[-1] + str(count)  # for the last group
    
#     return result
# # Example
# s = "aaabbcc"
# print(compress_string(s))  # Output: a3b2c2
#------------------------------------
#309. Check whether a string is a valid email address.


#-------------------------------------
# 310. Remove all whitespace characters from a string.
import re

def remove_whitespace(s):
    return re.sub(r'\s+', '', s)

# Example
# text = "  He llo \t Wo\nrld "
# cleaned = remove_whitespace(text)
# print(cleaned)  # Output: HelloWorld
# #---------------------- using join , split
# def remove_whitespace(s):
#     return ''.join(s.split())

# # Example
# text = "  He llo \t Wo\nrld "
# cleaned = remove_whitespace(text)
# print(cleaned)  # Output: HelloWorld

#--------------------------------------------------------------
# 311.Check if a string contains only alphabetic characters.
# def is_only_alphabets(s):
#     return s.isalpha()

# # Example
# text = input("Enter a string: ")

# if is_only_alphabets(text):
#     print("The string contains only alphabetic characters.")
# else:
#     print("The string contains non-alphabetic characters.")
#--------------------------------------------
# 312 .Count the number of words that start with a vowel.
# def count_vowel_starting_words(sentence):
#     vowels = "aeiouAEIOU"
#     words = sentence.split()
#     count = 0
#     for word in words:
#         if word[0] in vowels:
#             count += 1
#     return count
# text = input("Enter a sentence: ")
# result = count_vowel_starting_words(text)
# print("Number of words starting with a vowel:", result)
#--------------------------------------------------
# 313. Count how many even and odd digits are in a number.
# def count_even_odd_digits(number):
#     even = 0
#     odd = 0
#     for digit in str(number):
#         if digit.isdigit():
#             if int(digit) % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#     return even, odd
# num = input("Enter a number: ")
# even_count, odd_count = count_even_odd_digits(num)
# print("Even digits:", even_count)
# print("Odd digits:", odd_count)
#----------------------------------------
# 314.Find the reverse of a number using a loop.
# def reverse_number(n):
#     reversed_num = 0
#     while n > 0:
#         digit = n % 10
#         reversed_num = reversed_num * 10 + digit
#         n //= 10
#     return reversed_num
# num = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(num))
#---------------------------------------
# 315.Find the smallest digit in a number.
# def smallest_digit(n):
#     n = abs(n)  # Step 1: Make sure the number is positive
#     min_digit = 9  # Step 2: Start with the highest possible digit
#     while n > 0:
#         digit = n % 10  # Step 3: Get the last digit
#         if digit < min_digit:  # Step 4: Compare with current smallest
#             min_digit = digit
#         n //= 10  # Step 5: Remove the last digit from the number
#     return min_digit
#-------------------------------------
# 316.Find the sum of this pattern using a loop:
# n + nn + nnn + nnnn
# def pattern_of(n):
#     n = int(n)
#     total = 0
#     term = "" 
#     for i in range(1,5):
#         term +=str(n)
#         total += int(term)
#     return total
# n = input("Enter a single digit (0-9): ")
# print("Sum of the pattern:", pattern_of(n))
#----------------------------------------------
# 317. Count the number of digits in a number using a while loop.
# def count_digits(n):
#     n = abs(n)  # handle negative numbers
#     if n == 0:
#         return 1  # special case: 0 has 1 digit

#     count = 0
#     while n > 0:
#         n //= 10  # remove last digit
#         count += 1
#     return count
# num = int(input("Enter a number: "))
# print("Number of digits:", count_digits(num))
#-------------------------------------------
# 318.. Find the first digit of a number using a loop.
# def find_first_digit(n):
#     n = abs(n)  # Handle negative numbers

#     while n >= 10:
#         n //= 10  # Remove last digit
#     return n
# num = int(input("Enter a number: "))
# print("First digit:", find_first_digit(num))
#---------------------------------------
# 319. Count how many times a specific digit appears in a number.
# def count_digit_occurrence(number, digit_to_count):
#     number = abs(number)  # Handle negative numbers
#     count = 0
#     while number > 0:
#         digit = number % 10  # Get the last digit
#         if digit == digit_to_count:
#             count += 1
#         number //= 10  # Remove the last digit
#     return count

# # Example usage
# num = int(input("Enter a number: "))
# target_digit = int(input("Enter the digit to count: "))
# print("Digit", target_digit, "appears", count_digit_occurrence(num, target_digit), "times.")
#------------------------------------------------
# 320.Count how many numbers between 1 and 100 are divisible by 7 or 9.
# count = 0
# for num in range(1,101):
#     if num % 7== 0 and num % 9 == 0:
#         count +=1
# print("num divisible by 7 and 9 :",count)
#-----------------------------------------------------------
# 321.Find the power of a number using a loop.
# def power(base, exponent):
#     result = 1
#     for _ in range(exponent):
#         result *= base
#     return result

# # Example usage
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# print(f"{base} raised to the power {exponent} is: {power(base, exponent)}")
#-------------------------------------------------------
# 322.Find and print all digits in a number that are even.
# def digit_is_even(n):
#     num = abs(num)
#     even =""
#     for i in range(num):
#         if i.isdigit() % 2== 0:
#             even += num
#             return even 
#----------------------------------------------------
# 323.Print the sum of digits of a number until the sum becomes a single digit
# num = int(input("Enter a number: "))
# while num >= 10:
#     sum_digits = 0
#     while num > 0:
#         sum_digits += num % 10
#         num //= 10
#     num = sum_digits

# print("Single digit sum is:", num)
#----------------------------------------
# 324.Print a square pattern with numbers
# num= int(input("Enter number for square pattern: "))
# for i in range(1,num + 1):
#     for j in range(1,num + 1):
#         print(i, end =" ")
#     print()
# ---------------------------------------------
# 325.Print a diamond pattern
# n = int(input("Enter the number of rows for the diamond (half part): "))
# for i in range(1, n + 1):   # Upper half
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):      # Lower half
#     print(" " * (n - i) + "*" * (2 * i - 1))
#-------------------------------------------
# 326.Print a hollow square of stars
# n = int(input("Enter the size of the square: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         # Print * if we're on the border (first/last row or column)
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#------------------------------------------------
# 327.Count how many times a specific digit appears in a number
# num = int(input("enter number: "))
# num_count = input("Enter which number you have to count: ")
# count = str(num).count(num_count)
# print(f"The digit {num_count} appears {count} times.")
#-------------------------------------------------
# 328.Print hollow triangle of stars
# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         # Print star at first row, last column, or last row
#         if j == 1 or j == i or i == rows:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # Move to next line
        
#---------------------------------------------
# 329 .Take two numbers as input. Find and print the sum of all even numbers between them (inclusive).
# start_of = int(input("Enter the first number: "))
# end_of = int(input("Enter the second number: "))
# even_sum = 0
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         even_sum += num
# print("Sum of even numbers between", start, "and", end, "is:", even_sum)
#-------------------------------------------------------
# 330.Input a number and reverse its digits using only loops and arithmetic operators.
# num = int(input("Enter a number: "))
# reverse_num = 0  # Store the reversed number
# original_num = num  
# while num > 0:# Loop until num becomes 0
#     digit = num % 10          # Get the last digit
#     reverse_num = reverse_num * 10 + digit  # Append digit
#     num = num // 10           # Remove last digit
# print("Reversed number of", original_num, "is:", reverse_num)
#----------------------------------------------------
# 331. Pattern printing – right-aligned triangle
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     # Print spaces first
#     print(" " * (rows - i), end="")
#     # Then print stars
#     print("*" * i)
#------------------------------------------------
# 332.Armstrong number: sum of the cubes of its digits equals the number itself (e.g., 153).
# num = int(input("Enter a number: "))
# original_num = num
# sum_of_cubes = 0
# # Calculate sum of cubes of digits
# while num > 0:
#     digit = num % 10
#     sum_of_cubes += digit ** 3
#     num //= 10
# if sum_of_cubes == original_num:
#     print(original_num, "is an Armstrong number.")
# else:
#     print(original_num, "is not an Armstrong number.")
#------------------------------------------------------
#333.Check if a number is a palindrome
# Without converting it to a string.
# num = int(input("Enter a number: "))
# original_num = num
# reversed_num = 0
# # Reverse the number using arithmetic
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# if original_num == reversed_num:
#     print(original_num, "is a palindrome.")
# else:
#     print(original_num, "is not a palindrome.")
#------------------------------------------------------------
# 334.Take a number n and print its table from 1 to m (both n and m are inputs).
# n = int(input("Enter number: "))
# m = int(input("Enter how far the table should go: "))
# for i in range(1, m + 1):
#     print(n, "x", i, "=", n * i)
#----------------------------------------------------
# 335.Factorial without using math module , Input a number and find its factorial using a loop.
# n = int(input("Enter a number: "))
# fact = 1  # Factorial starts with 1
# for i in range(1, n + 1):
#     fact *= i
# print("Factorial of", n, "is", fact)
#--------------------------------------------------
# 336. Find the GCD of two number.Use a loop (not math.gcd).
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# # Find smaller number
# smaller = a if a < b else b
# gcd = 1
# # Loop to find highest number that divides both
# for i in range(1, smaller + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print("GCD of", a, "and", b, "is", gcd)
#--------------------------------------------------
# 337.Print all factors of a number . Input a number and print all of its factors.
# num = int(input("Enter number: "))
# for i in range(1, num + 1):
#     if num % i == 0 :
#      print(f"Factor of number: {i} ")
#--------------------------------------------------
# 338. Keep summing digits until the result becomes a single digit.
#n = int(input("Enter a number: "))
# Repeat until n becomes single digit
# while n > 9:
#     sum_digits = 0
#     while n > 0:
#         sum_digits += n % 10
#         n //= 10
#     n = sum_digits
# print("Single digit sum is:", n)
#-----------------------------------------------------
# 339. Count words in a sentence.Without using .split().
# sentence = input("Enter a sentence: ")
# count = 0
# in_word = False  # Flag to track if we're inside a word
# for ch in sentence:
#     if ch != " " and not in_word:
#         count += 1       # New word starts
#         in_word = True
#     elif ch == " ":
#         in_word = False  # Word ended
# print("Number of words:", count)
#----------------------------------------------------
# 340.Take two numbers and print all numbers divisible by 3 and 5 in that range.
# start = int(input("Enter the first number: "))
# end = int(input("Enter the second number: "))
# print(f"Numbers divisible by 3 and 5 between {start} and {end}:")
# for i in range(start, end + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#-------------------------------------------------------
# 341. Input a number and print the sum of the squares of its digits.
# num = int(input("Enter a number: "))
# sum_of_squares = 0
# while num > 0:
#     digit = num % 10  # Get the last digit
#     sum_of_squares += digit ** 2  # Square the digit and add it to sum
#     num //= 10  # Remove the last digit
# print("The sum of the squares of the digits is:", sum_of_squares)
#--------------------------------------------------
# 342 .Input two numbers and print both HCF and LCM using loops only.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# hcf = 1
# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         hcf = i  # store the largest common divisor
# # ---- Find LCM using formula ----
# lcm = (a * b) // hcf
# # Print results
# print("HCF:", hcf)
# print("LCM:", lcm)
#---------------------------------------------------
# 343.A happy number is one where repeatedly summing the squares of its digits eventually results in 1.
# num = int(input("Enter a number: "))
# def sum_of_squares(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit ** 2
#         n //= 10
#     return total
# # Keep checking until we reach 1 or repeat endlessly
# seen = []
# while num != 1 and num not in seen:
#     seen.append(num)   # store visited numbers to detect loops
#     num = sum_of_squares(num)
# if num == 1:
#     print("Happy Number")
# else:
#     print("Not a Happy Number")
#---------------------------------------------------
# 344. A perfect number equals the sum of its proper divisors (excluding itself).
# num = int(input("Enter a number: "))
# # Sum of proper divisors
# sum_divisors = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum_divisors += i
# # Check if perfect
# if sum_divisors == num:
#     print(num, "is a Perfect Number")
# else:
#     print(num, "is NOT a Perfect Number")
#-------------------------------------------------------
# 345 .Sum of alternate digits
# num = input("Enter a number: ")
# sum_alternate = 0
# # Loop through digits with step 2 (alternate digits)
# for i in range(0, len(num), 2):
#     sum_alternate += int(num[i])
# print("Sum of alternate digits:", sum_alternate)
#--------------------------------------------------------
# 346 .Find the first digit of a number using a loop
# num = int(input("Enter a number: "))
# while num >= 10:  # Keep removing last digit until only one digit remains
#     num = num // 10
# print("First digit is:", num)
#--------------------------------------------------------
# 347 .Input two numbers, find all primes between them, and sum them.
# Input two numbers
# start = int(input("Enter the first number: "))
# end = int(input("Enter the second number: "))
# prime_sum = 0
# # Loop through each number in the range
# for num in range(start, end + 1):
#     if num > 1:  # Prime numbers are greater than 1 
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_sum += num
# print("Sum of primes between", start, "and", end, "is:", prime_sum) 
#-----------------------------------------------------------
# 348.Sum of cubes of first N natural 
# n = int(input("Enter N: "))
# sum_cubes = 0
# for i in range(1, n + 1):
#     sum_cubes += i ** 3
# print("Sum of cubes of first", n, "natural numbers is:", sum_cubes)
#--------------------------------------------------------------
# 349.Print inverted right triangle pattern
# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):   # Start from rows down to 1
#     for j in range(i):
#         print("*", end="")
#     print()  # Move to the next line
#-----------------------------------------------------
# 350. Find all numbers divisible by the sum of their digits
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# print("Numbers divisible by sum of their digits:")
# for num in range(start, end + 1):
#     # Calculate sum of digits
#     temp = num
#     digit_sum = 0
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     # Check divisibility (avoid division by zero)
#     if digit_sum != 0 and num % digit_sum == 0:
#         print(num, end=" ")
#--------------------------------------------
# 351.Print all twin primes between 1 and 100
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# print("Twin primes between 1 and 100:")  # Find twin primes
# for num in range(2, 100):
#     if is_prime(num) and is_prime(num + 2):
#        print(f"({num}, {num + 2})")
#----------------------------------------------------
# 352.Sum of digits at even positions
# num = input("Enter a number: ")
# sum_even_pos = 0
# # Loop through digits at even positions (index starting from 1)
# for i in range(1, len(num), 2):
#     sum_even_pos += int(num[i])
# print("Sum of digits at even positions:", sum_even_pos)
#------------------------------------------------------
# 353. Reverse the digits of a number but keep zeros at the end
# num = int(input("Enter a number: "))
# # Count trailing zeros
# temp = num
# zero_count = 0
# while temp % 10 == 0 and temp != 0:
#     zero_count += 1
#     temp //= 10
# rev = 0      # Reverse the number without trailing zeros
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# rev = rev * (10 ** zero_count)  # Add trailing zeros back
# ---------------------------------------------------------
# 354. Find all perfect squares between two numbers
# Input range
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# print("Perfect squares between", start, "and", end, ":")
# for num in range(start, end + 1):
#     root = int(num ** 0.5)  # integer square root
#     if root * root == num:
#         print(num, end=" ")
#--------------------------------------------------
# 355. Sum of numbers in a range that are divisible by either 3 or 7
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# total_sum = 0
# for num in range(start, end + 1):
#     if num % 3 == 0 or num % 7 == 0:
#         total_sum += num

# print("Sum of numbers divisible by 3 or 7 between", start, "and", end, "is:", total_sum)
#-----------------------------------------------------------
# 356.Check if a number is an automorphic number. (Automorphic: its square ends with the same number, e.g., 25²=625)
# num = int(input("Enter a number: "))
# square = num * num   # Find square of the number
# temp = num    # Check last digits usingloop
# match = True
# while temp > 0:
#     if temp % 10 != square % 10:
#         match = False
#         break
#     temp //= 10
#     square //= 10
# if match:
#     print("Automorphic Number")
# else:
#     print("Not an Automorphic Number")
    #-------------------------------------------------------
# 357.Keep summing digits until one digit remains, e.g., 987 → 9+8+7=24 → 2+4=6)
#     num = int(input("Enter a number: "))
# while num >= 10:     # Keep looping until num is a single digit
#     digit_sum = 0
#     temp = num
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     num = digit_sum  # replace num with its digit sum
# print("Final single digit:", num)
#----------------------------------------------------
# 358 .Sum of digits at odd positions
# num = input("Enter a number: ")
# sum_odd_pos = 0
# # Loop through digits at odd positions (index 0, 2, 4, ...)
# for i in range(0, len(num), 2):
#  sum_odd_pos += int(num[i]) 
# print("Sum f digits at odd positions:", sum_odd_pos)
#---------------------------------------------
# 359.Print Floyd’s triangle
# rows = int(input("Enter number of rows: "))
# num = 1  
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()  # move to next line
    #----------------------------------------------------
# 360 .Input an m x n matrix and print its transpose.
# m = int(input("Enter number of rows (m): "))
# n = int(input("Enter number of columns (n): "))
# matrix = []   # Input matrix elements
# print("Enter the elements row-wise:")
# for i in range(m):
#     row = []
#     for j in range(n):
#         val = int(input(f"Element [{i}][{j}]: "))
#         row.append(val)
#     matrix.append(row)
# transpose = []     # Compute transpose (n x m)
# for j in range(n):
#     trans_row = []
#     for i in range(m):
#         trans_row.append(matrix[i][j])
#     transpose.append(trans_row)
# #-----------------------------------------------------
# 361.Input n and find number of trailing zeros in n! (use loops).
# n = int(input("Enter n: "))
# count = 0
# i = 5
# # Count factors of 5, 25, 125, ... in n!
# while i <= n:
#     count += n // i
#     i *= 5
# print("Number of trailing zeros in", n, "factorial is:", count)
#---------------------------------------------------------
# 362.Given hour and minute, compute the smaller angle between hour and minute hands (use loops / integer ops).

# 363. Sum of digits raised to successive powers
# num = input("Enter a number: ")
# result = 0
# power = 1
# for digit in num:
#     result += int(digit) ** power
#     power += 1

# print("Sum of digits raised to successive powers:", result)
#------------------------------------------------
 # 364. Generate all substrings of digits of a number .Example: 123 → 1,2,3,12,23,123.

# num = input("Enter a number: ")

# substrings = []

# length = len(num)

# # Generate all substrings
# for i in range(length):
#     for j in range(i + 1, length + 1):
#         substrings.append(num[i:j])

# # Print all substrings
# print("All substrings:")
# for s in substrings:
#     print(s)
#---------------------------------------------------------
# 365. Find longest increasing contiguous subsequence in digits.Example: 1245793 → length 5 (1,2,4,5,7,9) — stop when decreases.
# num = input("Enter a number: ")
# max_len = 1
# current_len = 1
# for i in range(1, len(num)):
#     if num[i] > num[i-1]:
#         current_len += 1
#     else:
#         if current_len > max_len:
#             max_len = current_len
#         current_len = 1
# # Check at the end
# if current_len > max_len:
#     max_len = current_len

# print("Length of longest increasing contiguous subsequence is:", max_len)
#-----------------------------------------------------------------
#366 .Print diamond number pattern
# n = int(input("Enter the number of rows for half diamond: "))

# # Upper half
# for i in range(1, n + 1):
#     for _ in range(n - i):                 # Print spaces
#         print(" ", end="")             # Print numbers from 1 to i
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(n - 1, 0, -1):   # Lower half
#     for _ in range(n - i):            # Print spaces
#         print(" ", end="")
#     # Print numbers from 1 to i
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#-------------------------------------------------------------
# 367. Check if two numbers have same set of digits .(Anagram of digits, e.g., 1213 and 31211 → False).
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# def count_digits(num):                 # Function to count digits frequency
#     freq = [0] * 10  # digits 0-9
#     for d in num:
#         freq[int(d)] += 1
#     return freq
# freq1 = count_digits(num1)
# freq2 = count_digits(num2)
# if freq1 == freq2:
#     print("Both numbers have the same set of digits.")
# else:
#     print("Numbers do NOT have the same set of digits.")

#--------------------------------------------------------
# 368. Count numbers between A and B where sum of first half digits = sum of second half
#(Like simple “lucky ticket” check; consider even-length numbers.)

# A = int(input("Enter start number (A): "))
# B = int(input("Enter end number (B): "))
# count = 0
# for num in range(A, B + 1):
#     s = str(num)
#     length = len(s)
#     if length % 2 == 0:  # only even length numbers
#         half = length // 2
#         first_half_sum = 0
#         second_half_sum = 0
#         # sum first half digits
#         for i in range(half):
#             first_half_sum += int(s[i])
#         # sum second half digits
#         for i in range(half, length):
#             second_half_sum += int(s[i])
#         if first_half_sum == second_half_sum:
#             count += 1
# print("Count of lucky numbers between", A, "and", B, "is:", count)
#-----------------------------------------------
# 369. Check if a given year is in the 20th or 21st century.
# year = int(input("Enter a year: "))
# if 1901 <= year <= 2000:
#     print(year, "is in the 20th century.")
# elif 2001 <= year <= 2100:
#     print(year, "is in the 21st century.")
# else:
#     print(year, "is NOT in the 20th or 21st century.")
#--------------------------------------------------------
# 370.  Check if a character is an alphabet or not.
# ch = input("Enter a character: ")
# if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
#     print(ch, "is an alphabet.")
# else:
#     print(ch, "is NOT an alphabet.")
#------------------------------------------------------
 # 371. Check if a triangle can be formed with given sides (triangle inequality).
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# if (a + b > c) and (b + c > a) and (a + c > b):
#     print("Yes, the sides can form a triangle.")
# else:
#     print("No, the sides cannot form a triangle.")
#----------------------------------------------------
# 372 .Input a temperature and print if it’s hot, warm, cool, or cold based on ranges.
# temp = float(input("Enter temperature in °C: "))
# if temp >= 30:
#     print("It's hot.")
# elif 20 <= temp < 30:
#     print("It's warm.")
# elif 10 <= temp < 20:
#     print("It's cool.")
# else:
#     print("It's cold.")
#-----------------------------------------------------
# 373.Find the day of the week given a number 1–7.. (1=Monday, 7=Sunday, else invalid.)
# day_num = int(input("Enter a number (1-7): "))

# if day_num == 1:
#     print("Monday")
# elif day_num == 2:
#     print("Tuesday")
# elif day_num == 3:
#     print("Wednesday")
# elif day_num == 4:
#     print("Thursday")
# elif day_num == 5:
#     print("Friday")
# elif day_num == 6:
#     print("Saturday")
# elif day_num == 7:
#     print("Sunday")
# else:
#     print("Invalid input")
#-------------------------------------------
# 374.Input a month number and print the number of days in that month (consider leap year for February).
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))
# # Function to check leap year
# def is_leap_year(y):
#     return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
# if month in [1, 3, 5, 7, 8, 10, 12]:
#     days = 31
# elif month in [4, 6, 9, 11]:
#     days = 30
# elif month == 2:
#     if is_leap_year(year):
#         days = 29
#     else:
#         days = 28
# else:
#     days = -1  # Invalid month

# if days == -1:
#     print("Invalid month number")
# else:
#     print(f"Number of days in month {month} of year {year} is: {days}")
#------------------------------------------------------------------
# 375.Input three angles and check if they form a valid triangle.
# a = float(input("Enter angle 1: "))
# b = float(input("Enter angle 2: "))
# c = float(input("Enter angle 3: "))
# if a > 0 and b > 0 and c > 0 and (a + b + c) == 180:
#     print("Yes, the angles form a valid triangle.")
# else:
#     print("No, the angles do NOT form a valid triangle.")
#--------------------------------------------------------
# 376 .Check if a password is strong based on conditions:Length ≥ 8,Contains uppercase, lowercase, digit, special char
# password = input("Enter password: ")
# # Initialize flags
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False
# special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
# if len(password) >= 8:
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_digit = True
#         elif ch in special_chars:
#             has_special = True
# else:
#     print("Password is too short (must be at least 8 characters).")
#     exit()

# if has_upper and has_lower and has_digit and has_special:
#     print("Strong password")
# else:
#     print("Weak password. Make sure it has uppercase, lowercase, digit, and special character.")
#--------------------------------------------------------
# 377. Calculate the discount based on purchase amount: $500 → 20% off,$200–500 → 10% off ,< $200 → no discount
# amount = float(input("Enter purchase amount: $"))
# if amount > 500:
#     discount = 0.20 * amount
# elif 200 <= amount <= 500:
#     discount = 0.10 * amount
# else:
#     discount = 0
# final_price = amount - discount
# print(f"Discount: ${discount:.2f}")
# print(f"Final price after discount: ${final_price:.2f}")
#---------------------------------------------------------
# 378.   Convert numeric marks to GPA points (4.0 scale) based on ranges.
# marks = float(input("Enter numeric marks (0-100): "))
# if marks >= 90:
#     gpa = 4.0
# elif marks >= 80:
#     gpa = 3.5
# elif marks >= 70:
#     gpa = 3.0
# elif marks >= 60:
#     gpa = 2.5
# elif marks >= 50:
#     gpa = 2.0
# elif marks >= 40:
#     gpa = 1.0
# else:
#     gpa = 0.0

# print(f"GPA points: {gpa}")
#---------------------------------------------
# 379.Check if a character is a hexadecimal digit (0–9, A–F, a–f).
# ch = input("Enter a character: ")
# if (ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F') or (ch >= 'a' and ch <= 'f'):
#     print(ch, "is a hexadecimal digit.")
# else:
#     print(ch, "is NOT a hexadecimal digit.")
#------------------------------------------------------
# 380 .Check if a number is divisible by 4 but not by 6.
# num = int(input("Enter a number: "))
# if num % 4 == 0 and num % 6 != 0:
#     print(num, "is divisible by 4 but NOT by 6.")
# else:
#     print(num, "does NOT satisfy the condition.")
#---------------------------------------------------
# 381.Check if two numbers are equal, or if one is divisible by the other.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a == b:
#     print("The numbers are equal.")
# elif a != 0 and b % a == 0:
#     print(f"{b} is divisible by {a}.")
# elif b != 0 and a % b == 0:
#     print(f"{a} is divisible by {b}.")
# else:
#     print("Neither equal nor divisible by each other.")
#-------------------------------------------------
# 382. Determine the quadrant of a point (x,y) in the Cartesian plane.
# x = float(input("Enter x-coordinate: "))
# y = float(input("Enter y-coordinate: "))
# if x == 0 and y == 0:
#     print("Point is at the origin.")
# elif x == 0:
#     print("Point lies on the Y-axis.")
# elif y == 0:
#     print("Point lies on the X-axis.")
# elif x > 0 and y > 0:
#     print("Point lies in Quadrant 1.")
# elif x < 0 and y > 0:
#     print("Point lies in Quadrant 2.")
# elif x < 0 and y < 0:
#     print("Point lies in Quadrant 3.")
# else:  # x > 0 and y < 0
#     print("Point lies in Quadrant 4.")
#-------------------------------------------------
# 383. Input a time (hours and minutes) and check if it’s AM or PM.
# hour = int(input("Enter hour (0-23): "))
# minute = int(input("Enter minutes (0-59): "))
# if hour < 0 or hour > 23 or minute < 0 or minute > 59:
#     print("Invalid time input.")
# else:
#     if hour == 0:
#         print("12:{:02d} AM".format(minute))
#     elif hour < 12:
#         print(f"{hour}:{minute:02d} AM")
#     elif hour == 12:
#         print(f"12:{minute:02d} PM")
#     else:
#         print(f"{hour - 12}:{minute:02d} PM")
#------------------------------------------
# 384. Given point coordinates (x,y) and circle radius r centered at origin.
# x = float(input("Enter x-coordinate: "))
# y = float(input("Enter y-coordinate: "))
# r = float(input("Enter radius of circle: "))
# distance_squared = x**2 + y**2
# radius_squared = r**2
# if distance_squared < radius_squared:
#     print("Point lies inside the circle.")
# elif distance_squared == radius_squared:
#     print("Point lies on the circle.")
# else:
#     print("Point lies outside the circle.")

#----------------------------------------------------------
 # 385. Calculate electricity bill based on units consumed: Up to 100 units: ₹5 per unit,101-200 units: ₹7 per unit,Above 200 units: ₹10 per unit
# units = int(input("Enter units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = 100 * 5 + (units - 100) * 7
# else:
#     bill = 100 * 5 + 100 * 7 + (units - 200) * 10

# print(f"Total electricity bill: ₹{bill}")
#--------------------------------------------------------
# 386. Find the smallest of four numbers.
# nums = []
# for i in range(4):
#     n = float(input(f"Enter number {i+1}: "))
#     nums.append(n)
# # Initialize smallest with first number
# smallest = nums[0]
# # Compare with rest
# for i in range(1, 4):
#     if nums[i] < smallest:
#         smallest = nums[i]

# print("The smallest number is:", smallest)
#----------------------------------------------
# 387. Determine if a number is a perfect square.
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Negative numbers cannot be perfect squares.")
# else:
#     i = 0
#     while i * i < num:
#         i += 1
#     if i * i == num:
#         print(num, "is a perfect square.")
#     else:
#         print(num, "is NOT a perfect square.")
#------------------------------------------------------
# 388. Classify a student’s attendance: Attendance ≥ 75%: Allowed to sit in exams,Attendance < 75%: Not allowed
# attendance_percentage = float(input("Enter attendance percentage: "))

# if attendance_percentage >= 75:
#     print("Allowed to sit in exams.")
# else:
#     print("Not allowed to sit in exams.")


#----------------------------------------------------------
# 389. Check if a given time is valid (hours: 0–23, minutes: 0–59).
# hour = int(input("Enter hour (0-23): "))
# minute = int(input("Enter minutes (0-59): "))

# if 0 <= hour <= 23 and 0 <= minute <= 59:
#     print("Valid time.")
# else:
    #------------------------------------------------------
# 390. Check if a person qualifies for a loan:,Salary ≥ ₹50,000 and credit score ≥ 700
# salary = float(input("Enter salary (₹): "))
# credit_score = int(input("Enter credit score: "))
# if salary >= 50000 and credit_score >= 700:
#     print("Person qualifies for the loan.")
# else:
#     print("Person does NOT qualify for the loan.")
#-------------------------------------------------
# 391. Determine the type of a triangle based on its angles :Right-angled, Acute, Obtuse
# a = float(input("Enter angle 1: "))
# b = float(input("Enter angle 2: "))
# c = float(input("Enter angle 3: "))
# if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
#     print("Invalid angles for a triangle.")
# else:
#     if a == 90 or b == 90 or c == 90:
#         print("Right-angled triangle.")
#     elif a < 90 and b < 90 and c < 90:
#         print("Acute triangle.")
#     else:
#         print("Obtuse triangle.")
#---------------------------------------------
# 392.Check if a password contains special characters.
# password = input("Enter password: ")

# special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
# contains_special = False
# for ch in password:
#     if ch in special_chars:
#         contains_special = True
#         break
# if contains_special:
#     print("Password contains special characters.")
# else:
#     print("Password does NOT contain special characters.")
#--------------------------------------------------
# 393. Check if a given year is a century year (divisible by 100) and if it’s a leap year.
# year = int(input("Enter a year: "))

# # Check if century year
# if year % 100 == 0:
#     print(year, "is a century year.")
# else:
#     print(year, "is NOT a century year.")

# # Check leap year
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is NOT a leap year.")
#---------------------------------------------------------
# 394. Determine if a number is divisible by 3 or 7 but not both.
# num = int(input("Enter a number: "))

# div_by_3 = (num % 3 == 0)
# div_by_7 = (num % 7 == 0)

# if div_by_3 != div_by_7:  # XOR condition
#     print(num, "is divisible by 3 or 7 but NOT both.")
# else:
#     print(num, "is NOT divisible by 3 or 7 exclusively.")
#------------------------------------------------------------
# 395. Check if a person is a teenager (age between 13 and 19 inclusive).
# age = int(input("Enter age: "))

# if 13 <= age <= 19:
#     print("Person is a teenager.")
# else:
#     print("Person is NOT a teenager.")
#---------------------------------------------
# 396. Find the absolute difference between two numbers and check if it’s greater than 10.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# diff = a - b
# if diff < 0:
#     diff = -diff  # absolute value without abs()
# print("Absolute difference:", diff)

# if diff > 10:
#     print("Difference is greater than 10.")
# else:
#     print("Difference is not greater than 10.")
#-------------------------------------------------------
# 397. Check if a number is a multiple of 4 or 6 but not both.
# num = int(input("Enter a number: "))
# div_by_4 = (num % 4 == 0)
# div_by_6 = (num % 6 == 0)
# if div_by_4 != div_by_6:  # True if exactly one is True
#     print(num, "is a multiple of 4 or 6 but NOT both.")
# else:
#     print(num, "is NOT a multiple of 4 or 6 exclusively.")
#-------------------------------------------------------------
# 398. Determine if a number is within a specific range (e.g., 50 to 100).
# num = float(input("Enter a number: "))

# if 50 <= num <= 100:
#     print(f"{num} is within the range 50 to 100.")
# else:
#     print(f"{num} is NOT within the range 50 to 100.")
#--------------------------------------------------------------
# 399. Check if a given character is a digit, letter, or whitespace.
# ch = input("Enter a character: ")
# if ch >= '0' and ch <= '9':
#     print(f"'{ch}' is a digit.")
# elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
#     print(f"'{ch}' is a letter.")
# elif ch == ' ' or ch == '\t' or ch == '\n':
#     print(f"'{ch}' is a whitespace character.")
# else:
#     print(f"'{ch}' is neither digit, letter, nor whitespace.")
#--------------------------------------------------------------
# 400. Validate if an input string contains only alphabets.
# s = input("Enter a string: ")
# only_alpha = True
# for ch in s:
#     if not ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#         only_alpha = False
#         break
# if only_alpha:
#     print("The string contains only alphabets.")
# else:
#     print("The string contains characters other than alphabets.")
#--------------------------------------------------------
# 401. Determine if a number is even and a multiple of 5.
# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 5 == 0:
#     print(f"{num} is even and a multiple of 5.")
# else:
#     print(f"{num} is NOT both even and a multiple of 5.")
#--------------------------------------
# 402 .Check if a number is both a multiple of 3 and a multiple of 4.
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 4 == 0:
#     print(f"{num} is a multiple of both 3 and 4.")
# else:
#     print(f"{num} is NOT a multiple of both 3 and 4.")
#-----------------------------------------------
# 403. Find the greatest among five numbers.
# numbers = []
# for i in range(5):
#     num = float(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# greatest = numbers[0]
# for i in range(1, 5):
#     if numbers[i] > greatest:
#         greatest = numbers[i]

# print("The greatest number is:", greatest)
#------------------------------------------------------------
# 404. Check if a given day number corresponds to a weekend or weekday.
# day_num = int(input("Enter day number (1 for Monday to 7 for Sunday): "))
# if day_num < 1 or day_num > 7:
#     print("Invalid day number.")
# elif day_num == 6 or day_num == 7:
#     print("It's a weekend.")
# else:
#     print("It's a weekday.")
#------------------------------------------------------------
# 405. Validate if a triangle can be formed with given side lengths (triangle inequality).
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# if (a + b > c) and (b + c > a) and (a + c > b):
#     print("Yes, the sides can form a triangle.")
# else:
#     print("No, the sides cannot form a triangle.")
#-----------------------------------------------------
# 406 .Check if a year is a leap year using nested conditions.
# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year.")
#         else:
#             print(year, "is NOT a leap year.")
#     else:
#         print(year, "is a leap year.")
# else:
#     print(year, "is NOT a leap year.")
#------------------------------------------------------------------------
# 407.Check if the last digit of a number is 0 or 5.
# num = int(input("Enter a number: "))

# last_digit = num % 10

# if last_digit == 0 or last_digit == 5:
#     print(f"The last digit of {num} is {last_digit}, which is 0 or 5.")
# else:
#     print(f"The last digit of {num} is {last_digit}, which is NOT 0 or 5.")
#-------------------------------------------------------
# 408 .Check if a number lies outside the range 10 to 50. 
# num = int(input("Enter a number: "))
# if num < 10 or num > 50:
#     print(f"{num} is outside the range 10 to 50.")
# else:
#     print(f"{num} is within the range 10 to 50.")
#----------------------------------------------------
# 409 Determine if a string starts with a vowel.
# text = input("Enter a string: ")
# if text:  # check if string is not empty
#     first_char = text[0].lower()
#     if first_char in 'aeiou':
#         print("The string starts with a vowel.")
#     else:
#         print("The string does not start with a vowel.")
# else:
#     print("Empty string entered.")
#------------------------------------------------------
# 410 .temp = float(input("Enter temperature in °C: "))
# if temp < 15:
#     print("Cold")
# elif 15 <= temp <= 30:
#     print("Moderate")
# else:
#     print("Hot")
#--------------------------------------------------
# 411.Check if the sum of two numbers is greater than 100.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if num1 + num2 > 100:
#     print("Sum is greater than 100")
# else:
#     print("Sum is not greater than 100")
#-------------------------------------------------------
# 412 .Input a number and print it in words (e.g., 45 → "Forty Five").
# ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
#          "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
# tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
# num = int(input("Enter a number (0-99): "))
# if 0 <= num <= 9:
#     print(ones[num])
# elif 10 <= num <= 19:
#     print(teens[num - 10])
# elif 20 <= num <= 99:
#     if num % 10 == 0:
#         print(tens[num // 10])
#     else:
#         print(tens[num // 10] + " " + ones[num % 10])
# else:
#     print("Number out of range")
#----------------------------------------------------------
# 413 .Given day, month, and year, check if the date is valid.
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# # Check leap year
# def is_leap(y):
#     return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
# # Days in each month
# days_in_month = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
#                  31, 31, 30, 31, 30, 31]

# if month < 1 or month > 12:
#     print("Invalid date: Month out of range")
# elif day < 1 or day > days_in_month[month - 1]:
#     print("Invalid date: Day out of range")
# else:
#     print("Valid date")
#--------------------------------------------
# 414 .Input a color (Red, Yellow, Green) and print the action (Stop, Ready, Go).
# color = input("Enter a color (Red, Yellow, Green): ").strip().lower()

# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")
#----------------------------------------------------
# 415. Student scholarship eligibility:Marks ≥ 85 → Full scholarship,Marks ≥ 75 → Half scholarship,Otherwise →
#  No scholarship
# marks = float(input("Enter your marks: "))
# if marks >= 85:
#     print("Full scholarship")
# elif marks >= 75:
#     print("Half scholarship")
# else:
#     print("No scholarship")
#----------------------------------------------------------------------------------------
# 416 .Input balance and withdrawal amount, check if it’s possible (consider minimum balance requirement).
# balance = float(input("Enter your account balance: "))
# withdraw = float(input("Enter withdrawal amount: "))
# min_balance = 500  # Minimum balance required
# if withdraw <= 0:
#     print("Invalid withdrawal amount.")
# elif withdraw > balance - min_balance:
#     print("Withdrawal not possible. Minimum balance requirement not met.")
# else:
#     print("Withdrawal successful.")
#-------------------------------------------------------------
# 417. Print “Weak”, “Medium”, or “Strong” based on length and character variety.
# password = input("Enter password: ")
# length = len(password)
# has_upper = any(ch.isupper() for ch in password)
# has_lower = any(ch.islower() for ch in password)
# has_digit = any(ch.isdigit() for ch in password)
# has_special = any(not ch.isalnum() for ch in password)
# if length < 6:
#     print("Weak")
# elif length >= 6 and (has_upper or has_lower) and has_digit:
#     if has_special and has_upper and has_lower:
#         print("Strong")
#     else:
#         print("Medium")
# else:
#     print("Weak")
#--------------------------------------------------------
# 418.Input birth date and month, print the zodiac sign.
# day = int(input("Enter birth day: "))
# month = int(input("Enter birth month (1-12): "))

# if (month == 3 and day >= 21) or (month == 4 and day <= 19):
#     sign = "Aries"
# elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#     sign = "Taurus"
# elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
#     sign = "Gemini"
# elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
#     sign = "Cancer"
# elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#     sign = "Leo"
# elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#     sign = "Virgo"
# elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#     sign = "Libra"
# elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#     sign = "Scorpio"
# elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#     sign = "Sagittarius"
# elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
#     sign = "Capricorn"
# elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
#     sign = "Aquarius"
# elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#     sign = "Pisces"
# else:
#     sign = "Invalid date"

# print("Your zodiac sign is:", sign)
#-----------------------------------------------------------------------------
# 419. Price changes based on age group and day of week.
# age = int(input("Enter age: "))
# day = input("Enter day of week: ").strip().lower()  # e.g., monday, saturday
# # Check if it's a weekend
# weekend_days = ["saturday", "sunday"]
# is_weekend = day in weekend_days
# if age <= 12:
#     price = 120 if is_weekend else 100
# elif age <= 59:
#     price = 250 if is_weekend else 200
# else:
#     price = 180 if is_weekend else 150

# print(f"Ticket price: ₹{price}")
#---------------------------------------------------------------------
# 420.Check if a number lies between 100 and 200.
# num = int(input("Enter a number: "))
# if 100 <= num <= 200:
#     print("Number is between 100 and 200.")
# else:
#     print("Number is NOT between 100 and 200.")
#-------------------------------------------------------
# 421.Check if the sum of two numbers is greater than 50.
# num = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num + num2 > 50:
#     print(f"The sum of {num} and {num2} is greater than 50.")
# else:
#     print("the sum not grater than 50")
#----------------------------------------------------
# 422.Check if the first digit of a number is even.
# num = int(input("Enter a number: "))
# first_digit = int(str(abs(num))[0])  

# if first_digit % 2 == 0:
#     print("The first digit is even.")
# else:
#     print("The first digit is odd.")
#-----------------------------------------------
#423.num = int(input("Enter a number: "))
# if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
#     print(f"{num} is divisible by 2, 3, or 5.")
# else:
#     print(f"{num} is not divisible by 2, 3, or 5.")

#------------------------------------------------------
# 424.Check if two numbers are equal or if one is divisible by the other.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a == b:
#     print("Both numbers are equal.")
# elif a % b == 0 or b % a == 0:
#     print("One number is divisible by the other.")
# else:
#     print("Numbers are not equal and not divisible by each other.")
# --------------------------------------------------------------
# 425 .Check if a string contains at least one digit.
# text = input("Enter a string: ")
# if any(char.isdigit() for char in text):
#     print("String contains at least one digit.")
# else:
#     print("String does not contain any digit.")
#---------------------------------------------------------------
# 426.Check if a string’s length is greater than 10.
# str = input("Enter string: ")
# if len(str) > 10:
#     print("length of string is greater than 10.")
# else:
#     print(str)
#-----------------------------------------------------
# 427.Check if a point lies inside, outside, or on a circle.

# h = float(input("Enter circle center X (h): "))
# k = float(input("Enter circle center Y (k): "))
# r = float(input("Enter radius of the circle: "))
# x = float(input("Enter point X: "))  # Input point coordinates
# y = float(input("Enter point Y: "))
# distance = ((x - h)**2 + (y - k)**2)**0.5  # Calculate distance from point to center
# if distance < r: # Check position of point
#     print("Point is inside the circle.")
# elif distance == r:
#     print("Point is on the circle.")
# else:
#     print("Point is outside the circle.")
#------------------------------------------------------
# 428. Check if a rectangle is a square.
# Input length and breadth
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))
# if length == breadth:# Check if rectangle is a square
#     print("It is a square.")
# else:
#     print("It is not a square.")
#---------------------------------------------------------
# 429.Check if a number is the area of a perfect square.
# import math
# num = int(input("Enter a number: "))
# sqrt_num = math.isqrt(num)  # gives integer square root
# if sqrt_num * sqrt_num == num:  # Check if it's a perfect square
#     print("It is the area of a perfect square.")
# else:
#     print("It is not the area of a perfect square.")
#-------------------------------------------------------
 # 430. Compare two distances and print which is larger.
# d1 = float(input("Enter first distance (in km): "))
# d2 = float(input("Enter second distance (in km): "))
# if d1 > d2:
#     print("First distance is larger.")
# elif d2 > d1:
#     print("Second distance is larger.")
# else:
#     print("Both distances are equal.")
#-----------------------------------------------------
# 431. Check if a point lies on an axis or origin.
# x = float(input("Enter x-coordinate: "))
# y = float(input("Enter y-coordinate: "))
# if x == 0 and y == 0:
#     print("The point is at the origin.")
# elif x == 0:
#     print("The point lies on the Y-axis.")
# elif y == 0:
#     print("The point lies on the X-axis.")
# else:
#     print("The point is not on any axis.")

#---------------------------------------------
# 432. Voting eligibility check.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
#---------------------------------------------
# 433. Driving license eligibility check.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for a driving license.")
# else:
#     print("You are not eligible for a driving license.")
#---------------------------------------------
# 434.usage = int(input("Enter water usage in liters: "))
# bill = 0
# if usage <= 5000:    # Slab calculation
#     bill = (usage / 100) * 2
# elif usage <= 15000:
#     bill = (5000 / 100) * 2 + ((usage - 5000) / 100) * 3
# else:
#     bill = (5000 / 100) * 2 + (10000 / 100) * 3 + ((usage - 15000) / 100) * 5
# print(f"Water Bill: ₹{bill:.2f}")
#---------------------------------------------------------
# 435.Mobile recharge plan suggestion based on usage.
# data_gb = float(input("Enter monthly data usage (in GB): "))
# calls_min = int(input("Enter monthly call usage (in minutes): "))
# # Plan suggestion
# if data_gb <= 2 and calls_min <= 100:
#     plan = "₹99 Plan (Basic)"
# elif data_gb <= 10 and calls_min <= 500:
#     plan = "₹199 Plan (Standard)"
# else:
#     plan = "₹299 Plan (Unlimited)"
# print(f"Suggested Plan: {plan}")
#-----------------------------------------
# 436. Theme park entry fee based on age group.
# age = int(input("Enter your age: "))
# if age < 5:
#     fee = 0
# elif age <= 12:
#     fee = 200
# elif age <= 59:
#     fee = 500
# else:
#     fee = 300
# if fee == 0:
#     print("Entry is Free!")
# else:
#     print(f"Entry Fee: ₹{fee}")
#--------------------------------------------
# 437.Restaurant discount eligibility based on bill amount.
# bill = float(input("Enter your total bill amount: ₹"))
# if bill >= 1000:
#     discount = bill * 0.20
# elif bill >= 500:
#     discount = bill * 0.10
# else:
#     discount = 0
# final_amount = bill - discount  # Calculate final amount
# if discount > 0:
#     print(f"Discount: ₹{discount:.2f}")
# else:
#     print("No discount applicable.")

# print(f"Final bill after discount: ₹{final_amount:.2f}")

#--------------------------------------------------------------
# 438.Cricket run rate classification (low, medium, high).
# run_rate = float(input("Enter the run rate: "))

# if run_rate < 4:
#     print("Low run rate ")
# elif 4 <= run_rate <= 6:
#     print("Medium run rate ")
# else:
#     print("High run rate ")
#----------------------------------------------------
# 439. Chess piece movement check (valid or not).
# piece = input("Enter chess piece (Pawn, Rook, Knight, Bishop, Queen, King): ").lower()
# start_x = int(input("Enter starting x (1-8): "))
# start_y = int(input("Enter starting y (1-8): "))
# end_x = int(input("Enter ending x (1-8): "))
# end_y = int(input("Enter ending y (1-8): "))

# dx = abs(end_x - start_x)
# dy = abs(end_y - start_y)

# valid = False

# if piece == "pawn":
#     # Simple pawn rule: 1 step forward (not considering captures or first move double step)
#     if dx == 0 and dy == 1:
#         valid = True
# elif piece == "rook":
#     if dx == 0 or dy == 0:
#         valid = True
# elif piece == "bishop":
#     if dx == dy:
#         valid = True
# elif piece == "queen":
#     if dx == dy or dx == 0 or dy == 0:
#         valid = True
# elif piece == "king":
#     if dx <= 1 and dy <= 1:
#         valid = True
# elif piece == "knight":
#     if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
#         valid = True
# if valid:
#     print("Valid move ")
# else:
#     print("Invalid move ")
#-----------------------------------------------
# 440. Tic-Tac-Toe win check for a row/column/diagonal.
# board = [
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]

# winner = None

# # Check rows
# for row in board:
#     if row[0] == row[1] == row[2] != " ":
#         winner = row[0]

# # Check columns
# for col in range(3):
#     if board[0][col] == board[1][col] == board[2][col] != " ":
#         winner = board[0][col]
# if board[0][0] == board[1][1] == board[2][2] != " ":
#     winner = board[0][0]
# if board[0][2] == board[1][1] == board[2][0] != " ":
#     winner = board[0][2]
# if winner:
#     print(f"{winner} wins! ")
# else:
#     print("No winner yet.")
#--------------------------------------------------------
# 441.   Dice game: check if sum is even or odd.
# dice1 = int(input("Enter the value of first dice (1-6): "))
# dice2 = int(input("Enter the value of second dice (1-6): "))
# if 1 <= dice1 <= 6 and 1 <= dice2 <= 6:
#     total = dice1 + dice2
#     print(f"Sum of dice: {total}")

#     if total % 2 == 0:
#         print("Result: Even")
#     else:
#         print("Result: Odd")
# else:
#     print("Invalid dice value! Please enter numbers between 1 and 6.")
#-----------------------------------------------
# 442. Card game: check if card is a face card or number card.
# card = input("Enter a card (e.g., A, 2-10, J, Q, K): ").strip().upper()

# face_cards = ["A", "J", "Q", "K"]

# if card in face_cards:
#     print("This is a Face Card.")
# elif card.isdigit() and 2 <= int(card) <= 10:
#     print("This is a Number Card.")
# else:
#     print("Invalid card input.")
#---------------------------------------------
# 443. Lottery win check.
# winning_number = 50
# ticket_number = int(input("Enter your lottery ticket number: "))

# if ticket_number == winning_number:
#     print(" Congratulations! You won the lottery!")
# else:
#     print("Sorry, better luck next time.")
#---------------------------------------------------
# 444. Basketball score check (win, lose, draw).

# team_score = int(input("Enter your team's score: "))
# opponent_score = int(input("Enter opponent's score: "))

# if team_score > opponent_score:
#     print("You Win!")
# elif team_score < opponent_score:
#     print(" You Lose!")
# else:
#     print("It's a Draw!")
#-----------------------------------------
# 445. Football offside decision simulation.
# attacker_position = float(input("Enter attacker's distance from goal (in meters): "))
# second_last_defender_position = float(input("Enter second last defender's distance from goal (in meters): "))
# ball_position = float(input("Enter ball's distance from goal (in meters): "))

# if attacker_position < second_last_defender_position and attacker_position < ball_position:
#     print(" No Offside")
# else:
#     print(" Offside!")

#-------------------------------------------------
# 446. Check if a year is a century year.

# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     print(f"{year} is a Century Year.")
# else:
#     print(f"{year} is NOT a Century Year.")
#-----------------------------------------------------------
# 447. Check if a time is valid (hh:mm).
# time_str = input("Enter time in hh:mm format: ")

# if ":" in time_str:
#     parts = time_str.split(":")
#     if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
#         hh = int(parts[0])
#         mm = int(parts[1])
#         if 0 <= hh <= 23 and 0 <= mm <= 59:
#             print("Valid time")
#         else:
#             print("Invalid time")
#     else:
#         print("Invalid format")
# else:
#     print("Invalid format")
#---------------------------------------------------------
# 448. Check if a month has 30, 31, or 28/29 days.
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print("This month has 31 days.")
# elif month in [4, 6, 9, 11]:
#     print("This month has 30 days.")
# elif month == 2:
#     # Leap year check
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("This month has 29 days (Leap Year).")
#     else:
#         print("This month has 28 days.")
# else:
#     print("Invalid month number.")
#-------------------------------------------------------------
# 449.Find the season based on month number.
# month = int(input("Enter month number (1-12): "))

# if month in [12, 1, 2]:
#     print("Winter")
# elif month in [3, 4, 5]:
#     print("Spring")
# elif month in [6, 7, 8]:
#     print("Summer")
# elif month in [9, 10, 11]:
#     print("Autumn")
# else:
#     print("Invalid month number.")
#---------------------------------------------------
# 450. Days until birthday.
# from datetime import date, datetime, timedelta

# # Input birthday (day and month only)
# b_day = int(input("Enter birth day (1-31): "))
# b_month = int(input("Enter birth month (1-12): "))
# # Today's date
# today = date.today()
# current_year = today.ye
# # Next birthday in this year
# birthday_this_year = date(current_year, b_month, b_day)
# # If birthday already passed, take next year
# if birthday_this_year < today:
#     birthday_next = date(current_year + 1, b_month, b_day)
# else:
#     birthday_next = birthday_this_year
# # Calculate days left
# days_left = (birthday_next - today).days

# print(f"Days until your next birthday: {days_left}")
#----------------------------------------------------------
# 451. Weekend or weekday check.
# import datetime
# # Input date in format YYYY-MM-DD
# date_str = input("Enter a date (YYYY-MM-DD): ")
# # Convert to date object
# year, month, day = map(int, date_str.split("-"))
# given_date = datetime.date(year, month, day)
# # Get weekday number (0 = Monday, 6 = Sunday)
# weekday_num = given_date.weekday()
# # Check weekend or weekday
# if weekday_num >= 5:
#     print("It's a weekend!")
# else:
#     print("It's a weekday.")
#-----------------------------------------------------------
# 452. Age category classification (child, teen, adult, senior).
# age = int(input("Enter your age: "))
# if age >= 0 and age <= 12:
#     category = "Child"
# elif age <= 19:
#     category = "Teen"
# elif age <= 59:
#     category = "Adult"
# elif age >= 60:
#     category = "Senior"
# else:
#     category = "Invalid age"

# print(f"Age category: {category}")
#---------------------------------------------------
# 453.Blood donation eligibility check.
# age = int(input("Enter your age: "))
# weight = float(input("Enter your weight in kg: "))
# if 18 <= age <= 65 and weight >= 50:  # Check eligibility
#     print("You are eligible to donate blood.")
# else:
#     print("You are not eligible to donate blood.")
#--------------------------------------------------
# 454.Delivery charge calculation based on distance.
# Input distance in km
# distance = float(input("Enter delivery distance in km: "))
# if distance <= 5:
#     charge = 20
# elif distance <= 15:
#     charge = 50
# else:
#     charge = 100

# print(f"Delivery charge: ₹{charge}")
#----------------------------------------------------
# 455. Discount calculation based on purchase amount.
# amount = float(input("Enter purchase amount: ₹"))
# if amount >= 500:
#     discount = amount * 0.20
# elif amount >= 200:
#     discount = amount * 0.10
# else:
#     discount = 0
# # Final price after discount
# final_price = amount - discount
# print(f"Discount: ₹{discount:.2f}")
# print(f"Final price after discount: ₹{final_price:.2f}")
# ------------------------------------------------------
# 456. Tax calculation based on income.
# income = float(input("Enter your annual income: ₹"))
# if income <= 250000:      # Calculate tax
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = (500000 - 250000) * 0.05 + (income - 500000) * 0.20
# else:
#     tax = (500000 - 250000) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

# print(f"Tax to be paid: ₹{tax:.2f}")
#------------------------------------------------------------
# 457 .Online order free shipping check.
# order_amount = float(input("Enter your order amount: ₹"))
# if order_amount >= 500:
#     print("You are eligible for FREE shipping! ")
# else:
#     print("Shipping charge: Rs.50")
#------------------------------------------------------------------
# 458. Train ticket class suggestion based on budget.
# Input budget
# budget = float(input("Enter your budget for train ticket (₹): "))
# if budget >= 1500:
#     ticket_class = "AC First Class"
# elif budget >= 1000:
#     ticket_class = "AC 2 Tier"
# elif budget >= 600:
#     ticket_class = "Sleeper Class"
# else:
#     ticket_class = "General Class"

# print(f"Suggested ticket class: {ticket_class}")
#------------------------------------------------------------
# 459. Valid email ID format check.
# import re   # use for regular expression

# email = input("Enter email ID: ").strip()

# # Basic regex pattern for email validation
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# if re.match(pattern, email):
#     print("Valid email ID.")
# else:
#     print("Invalid email ID.")
#------------------------------------------------------
# 460. Time-based greeting (Good Morning, Afternoon, Evening).
# from datetime import datetime
# hour = datetime.now().hour  # Get current hour (24-hour format)
# if 5 <= hour < 12:
#     greeting = "Good Morning"
# elif 12 <= hour < 17:
#     greeting = "Good Afternoon"
# elif 17 <= hour < 21:
#     greeting = "Good Evening"
# else:
#     greeting = "Good Night"

# print(greeting)
#-----------------------------------------------------
# 461. Validate IP address format.
# ip = input("Enter an IPv4 address: ").strip()

# parts = ip.split(".")

# if len(parts) == 4 and all(part.isdigit() for part in parts):
#     valid = True
#     for part in parts:
#         num = int(part)
#         if not (0 <= num <= 255):
#             valid = False
#             break
#     if valid:
#         print("Valid IPv4 address.")
#     else:
#         print("Invalid IPv4 address.")
# else:
#     print("Invalid IPv4 address.")
#-----------------------------------------------
# 462. Determine winner in a penalty shootout.

# team1_score = int(input("Enter Team 1 successful penalties (0-5): "))
# team2_score = int(input("Enter Team 2 successful penalties (0-5): "))
# if not (0 <= team1_score <= 5 and 0 <= team2_score <= 5):
#     print("Invalid scores. Scores must be between 0 and 5.")
# else:
#     if team1_score > team2_score:
#         print("Team 1 wins the shootout!")
#     elif team2_score > team1_score:
#         print("Team 2 wins the shootout!")
#     else:
#         print("The shootout is a draw! Proceed to sudden death.")
#---------------------------------------------------------------
# 463. Currency converter with invalid currency check.
# rates = {
#     "USD": 82.50,
#     "EUR": 90.10,
#     "GBP": 101.20,
#     "JPY": 0.61,
#     "AUD": 55.00
# }

# amount = float(input("Enter amount: "))
# from_currency = input("Convert from (USD, EUR, GBP, JPY, AUD): ").upper()
# to_currency = input("Convert to (USD, EUR, GBP, JPY, AUD): ").upper()

# if from_currency not in rates:
#     print(f"Invalid source currency: {from_currency}")
# elif to_currency not in rates:
#     print(f"Invalid target currency: {to_currency}")
# else:
#     # Convert amount to INR first, then to target currency
#     amount_in_inr = amount * rates[from_currency]
#     converted_amount = amount_in_inr / rates[to_currency]
#     print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
#--------------------------------------------------------------------
# 464. Parking fee calculation based on hours parked.
# hours = float(input("Enter hours parked: "))
# fee = 0
# if hours <= 2:
#     fee = hours * 20
# elif hours <= 5:
#     fee = 2 * 20 + (hours - 2) * 15
# else:
#     fee = 2 * 20 + 3 * 15 + (hours - 5) * 10

# print(f"Parking fee: ₹{fee:.2f}")
#-------------------------------------------------------------
# 465. Temperature category with extreme weather alerts.
# temp = float(input("Enter temperature in °C: "))

# # Categorize and alert
# if temp < 0:
#     category = "Cold"
#     alert = "Extreme Cold Alert! Stay warm and safe."
# elif 0 <= temp <= 15:
#     category = "Cold"
#     alert = None
# elif 16 <= temp <= 30:
#     category = "Moderate"
#     alert = None
# elif 31 <= temp <= 45:
#     category = "Hot"
#     alert = None
# else:
#     category = "Hot"
#     alert = "Extreme Heat Alert! Stay hydrated and avoid outdoor activities."

# print(f"Temperature category: {category}")
# if alert:
#     print(alert)
#----------------------------------------------------------
# 466. Check if a number’s digits are in ascending order.
# num = input("Enter a number: ")
# ascending = True
# for i in range(1, len(num)):
#     if num[i] < num[i-1]:
#         ascending = False
#         break
# if ascending:
#     print("Digits are in ascending order.")
# else:
#     print("Digits are NOT in ascending order.")
#-----------------------------------------------
# 467. Check if a number’s digits are in descending order.
# num = input("Enter a number: ")

# descending = True
# for i in range(1, len(num)):
#     if num[i] > num[i-1]:
#         descending = False
#         break

# if descending:
#     print("Digits are in descending order.")
# else:
#     print("Digits are NOT in descending order.")
#---------------------------------------------
#468. Check if a number has repeating digits.
# num = input("Enter a number: ")

# digits_seen = set()
# has_repeat = False

# for digit in num:
#     if digit in digits_seen:
#         has_repeat = True
#         break
#     digits_seen.add(digit)

# if has_repeat:
#     print("The number has repeating digits.")
# else:
#     print("The number does NOT have repeating digits.")
#-----------------------------------------------------
# 469. Sum of digits is even or odd.
# num = input("Enter a number: ")
# total = 0
# for digit in num:
#     total += int(digit)

# if total % 2 == 0:
#     print(f"Sum of digits ({total}) is even.")
# else:
#     print(f"Sum of digits ({total}) is odd.")
#------------------------------------------------------
# 470. Last two digits of a number divisible by 4.
# num = input("Enter a number: ")

# last_two = num[-2:] if len(num) >= 2 else num
# # Convert to int and check divisibility
# if int(last_two) % 4 == 0:
#     print(f"The last two digits ({last_two}) are divisible by 4.")
# else:
#     print(f"The last two digits ({last_two}) are NOT divisible by 4.")
#-----------------------------------------------
# 471. Find the middle character(s) of a string.
# s = input("Enter a string: ")

# length = len(s)
# mid = length // 2

# if length % 2 == 0:
#     middle_chars = s[mid - 1: mid + 1]       # Even length: two middle characters
# else:
#     middle_chars = s[mid]    # Odd length: single middle character

# print(f"Middle character(s): {middle_chars}")
#-------------------------------------------------------------
# 472. Compare sum of first half and second half of digits.
# num = input("Enter a number (even length): ")

# length = len(num)

# if length % 2 != 0:
#     print("Please enter a number with even length.")
# else:
#     half = length // 2
#     first_half = num[:half]
#     second_half = num[half:]

#     sum_first = sum(int(d) for d in first_half)
#     sum_second = sum(int(d) for d in second_half)

#     print(f"Sum of first half digits: {sum_first}")
#     print(f"Sum of second half digits: {sum_second}")

#     if sum_first == sum_second:
#         print("Sums are equal.")
#     else:
#         print("Sums are not equal.")
#---------------------------------------------
# 473. Check if a string contains both uppercase and lowercase.s = input("Enter a string: ")
# s = input("Enter a string: ")

# has_upper = any(c.isupper() for c in s)
# has_lower = any(c.islower() for c in s)

# if has_upper and has_lower:
#     print("String contains both uppercase and lowercase letters.")
# else:
#     print("String does NOT contain both uppercase and lowercase letters.")
#--------------------------------------------------------
# 474. Count number of vowels in a string and check if even or odd.
# s = input("Enter a string: ").lower()
# vowels = "aeiou"
# count = sum(1 for char in s if char in vowels)

# print(f"Number of vowels: {count}")

# if count % 2 == 0:
#     print("The number of vowels is even.")
# else:
#     print("The number of vowels is odd.")
#------------------------------------------------
# 475. Special lucky number check: divisible by 3, contains digit 7.
# num = input("Enter a number: ")
# div_by_3 = (int(num) % 3 == 0)     # Check divisibility by 3

# # Check if digit 7 is present
# contains= '7' in num

# if div_by_3 and contains:
#     print(f"{num} is a special lucky number!")
# else:
#     print(f"{num} is NOT a special lucky number.")
#--------------------------------------------
# 476. Check if a number is divisible by 9 but not by 6.
# def check_number(num):
#     if num % 9 == 0 and num % 6 != 0:
#         return True
#     else:
#         return False
# n = 27
# if check_number(n):
#     print(f"{n} is divisible by 9 but not by 6.")
# else:
#     print(f"{n} does not satisfy the condition.")
#--------------------------------------------------
# 477.Find if the product of two numbers is positive, negative, or zero.
# def product_sign(a, b):
#     product = a * b
#     if product > 0:
#         return "Positive"
#     elif product < 0:
#         return "Negative"
#     else:
#         return "Zero"
# x = 5
# y = -3
# result = product_sign(x, y)
# print(f"The product of {x} and {y} is {result}.")
#----------------------------------------------------
# 478. Check if a number is a multiple of 11 or 13.
# def is_multiple_of_11_or_13(num):
#     if num % 11 == 0 or num % 13 == 0:
#         return True
#     else:
#         return False
# n = 143
# if is_multiple_of_11_or_13(n):
#     print(f"{n} is a multiple of 11 or 13.")
# else:
#     print(f"{n} is NOT a multiple of 11 or 13.")
# ------------------------------------------------------
# 479.Check if a number is within 10 units of 100 (i.e., between 90 and 110).
# def within_10_of_100(num):
#     return 90 <= num <= 110 
# n = 105
# if within_10_of_100(n):
#     print(f"{n} is within 10 units of 100.")
# else:
#     print(f"{n} is NOT within 10 units of 100.")
#----------------------------------------------
# 480.Determine if the sum of three numbers is even or odd.
# def sum_even_or_odd(a, b, c):
#     total = a + b + c
#     if total % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# x, y, z = 4, 7, 2
# result = sum_even_or_odd(x, y, z)
# print(f"The sum of {x}, {y}, and {z} is {result}.")
#------------------------------------------------------
#481. Check if a year is between 1900 and 2100 and is a leap year.
# def is_leap_year(year):
#     # Leap year if divisible by 400, or divisible by 4 but not by 100
#     return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# def check_year(year):
#     if 1900 <= year <= 2100:
#         if is_leap_year(year):
#             return True
#         else:
#             return False
#     else:
#         return False
# year = 2000
# if check_year(year):
#     print(f"{year} is between 1900 and 2100 and is a leap year.")
# else:
#     print(f"{year} is NOT a leap year or not in the range 1900 to 2100.")
#--------------------------------------------------
# 482. Validate if a password contains both uppercase and lowercase letters.
# def validate_password(password):
#     has_upper = any(c.isupper() for c in password)
#     has_lower = any(c.islower() for c in password)
#     return has_upper and has_lower
# pwd = "Password123"
# if validate_password(pwd):
#     print("Password contains both uppercase and lowercase letters.")
# else:
#     print("Password does NOT contain both uppercase and lowercase letters.")
#-----------------------------------------------
# 483 . Find if two numbers are both even or both odd.
# def both_even_or_both_odd(a, b):
#     if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
#         return True
#     else:
#         return False
# x, y = 4, 8
# if both_even_or_both_odd(x, y):
#     print(f"{x} and {y} are both even or both odd.")
# else:
#     print(f"{x} and {y} are not both even or both odd.")
#-------------------------------------------------------
# 485. Check if the first and last character of a string are the same.
# def check_first_last_char(s):
#     if len(s) == 0:
#         return False  # Empty string case
#     return s[0] == s[-1]
# text = "radar"
# if check_first_last_char(text):
#     print(f"The first and last characters of '{text}' are the same.")
# else:
#     print(f"The first and last characters of '{text}' are different.")
#----------------------------------------------
# 486.Input three numbers and check if they can form an arithmetic progression
# def is_arithmetic_progression(a, b, c):
#     return (b - a) == (c - b)
# x, y, z = map(int, input("Enter three numbers separated by space: ").split())
# if is_arithmetic_progression(x, y, z):
#     print(f"{x}, {y}, and {z} form an arithmetic progression.")
# else:
#     print(f"{x}, {y}, and {z} do NOT form an arithmetic progression.")
#------------------------------------------------------
# 487. Check if a number is a multiple of 5 or 10 but not both.
# def check_multiple(num):
#     # multiple of 5 but not multiple of 10
#     if num % 5 == 0 and num % 10 != 0:
#         return True
#     else:
#         return False
# n = 15
# if check_multiple(n):
#     print(f"{n} is a multiple of 5 or 10 but not both.")
# else:
#     print(f"{n} does NOT satisfy the condition.")
#-------------------------------------------------
# 488. Determine if a number is a three-digit number with all digits distinct.
# def is_three_digit_distinct(num):
#     # Check if number is between 100 and 999 (inclusive)
#     if 100 <= num <= 999:
#         num_str = str(num)
#         # Check if all digits are distinct
#         return len(set(num_str)) == 3
#     return False
# n = 374
# if is_three_digit_distinct(n):
#     print(f"{n} is a three-digit number with all distinct digits.")
# else:
#     print(f"{n} is NOT a three-digit number with all distinct digits.")
#-----------------------------------------------------
# 489. Given three numbers, check if they form an arithmetic progression, geometric progression, or neither.
# def check_progression(a, b, c):
#     # Check arithmetic progression: difference between consecutive terms is same
#     if (b - a) == (c - b):
#         return "Arithmetic Progression"
#     # Check geometric progression: ratio between consecutive terms is same (and not zero)
#     elif a != 0 and b != 0 and (b / a) == (c / b):
#         return "Geometric Progression"
#     else:
#         return "Neither"
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# # Check and print the progression type
# result = check_progression(num1, num2, num3)
# print(result)
#-------------------------------------------------------
# 490.Check if a five-digit number is a palindrome and if the sum of its digits is divisible by 7.
# def is_palindrome(num_str):
#     return num_str == num_str[::-1]

# def sum_of_digits(num_str):
#     return sum(int(digit) for digit in num_str)
# number = input("Enter a five-digit number: ")  # Input a five-digit number as string to easily check palindrome
 
# if len(number) != 5 or not number.isdigit():
#     print("Please enter a valid five-digit number.")
# else:
#     if is_palindrome(number):
#         print("The number is a palindrome.")
#     else:
#         print("The number is not a palindrome.")

#     total = sum_of_digits(number)
#     print(f"Sum of digits: {total}")

#     if total % 7 == 0:
#         print("The sum of digits is divisible by 7.")
#     else:
#         print("The sum of digits is not divisible by 7.")
#--------------------------------------------------------------
# 491. Input two dates (day, month, year) and check which one comes first.
# def is_valid_date(d, m, y):
#     # Basic check for valid day, month, year ranges (not fully exhaustive)
#     if y < 1:
#         return False
#     if m < 1 or m > 12:
#         return False
#     # Days in each month, ignoring leap year for simplicity
#     days_in_month = [31, 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if d < 1 or d > days_in_month[m-1]:
#         return False
#     return True
# def compare_dates(d1, m1, y1, d2, m2, y2):
#     if (y1, m1, d1) < (y2, m2, d2):
#         return "First date comes first."
#     elif (y1, m1, d1) > (y2, m2, d2):
#         return "Second date comes first."
#     else:
#         return "Both dates are the same."
#-------------------------------------------------
# 492. Check if a string is a valid palindrome ignoring spaces, punctuation, and case.
# import string

# def is_valid_palindrome(s):
#     # Remove spaces and punctuation, and convert to lowercase
#     allowed_chars = set(string.ascii_lowercase + string.digits)
#     filtered = ''.join(ch.lower() for ch in s if ch.lower() in allowed_chars)
#     # Check if filtered string is palindrome
#     return filtered == filtered[::-1]
# text = input("Enter a string: ")

# if is_valid_palindrome(text):
#     print("The string is a valid palindrome (ignoring spaces, punctuation, and case).")
# else:
#     print("The string is not a valid palindrome.")
#--------------------------------------------------------
# 493. Input a positive integer and check if it’s a Harshad number (divisible by the sum of its digits).
# def is_harshad(num):
#     digit_sum = sum(int(digit) for digit in str(num))  # Calculate sum of digits
#     return num % digit_sum == 0    # Check divisibility
# # Input positive integer
# n = int(input("Enter a positive integer: "))

# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     if is_harshad(n):
#         print(f"{n} is a Harshad number.")
#     else:
#         print(f"{n} is not a Harshad number.")
#---------------------------------------------------
# 494.Input a string and check if it contains at least two vowels.
# def has_two_vowels(s):
#     vowels = set("aeiouAEIOU")
#     count = 0
#     for ch in s:
#         if ch in vowels:
#             count += 1
#             if count >= 2:
#                 return True
#     return False
# text = input("Enter a string: ")

# if has_two_vowels(text):
#     print("The string contains at least two vowels.")
# else:
#     print("The string does not contain at least two vowels.")
#-----------------------------------------------
# 495.Input a list of numbers and find the second largest number using only conditionals (no sorting).
# def second_largest(numbers):
#     if len(numbers) < 2:
#         return None  # Not enough elements
#     largest = None
#     second = None
#     for num in numbers:
#         if largest is None or num > largest:
#             second = largest
#             largest = num
#         elif num != largest and (second is None or num > second):
#             second = num

#     return second
# # Input list of numbers (space-separated)
# nums = list(map(int, input("Enter numbers separated by space: ").split()))

# result = second_largest(nums)

# if result is None:
#     print("List should have at least two distinct numbers.")
# else:
#     print(f"The second largest number is: {result}")
#-----------------------------------------------------
# 496. Check if a string has balanced parentheses (like “(())” is balanced, “(()” is not).
# def is_balanced_parentheses(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return len(stack) == 0
# text = input("Enter a string with parentheses: ")

# if is_balanced_parentheses(text):
#     print("The parentheses are balanced.")
# else:
#     print("The parentheses are not balanced.")
#-------------------------------------------------------
# 497. Given a list of integers, check if it forms a strictly increasing sequence.
# def is_strictly_increasing(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] >= lst[i+1]:
#             return False
#     return True
# # Input list of integers (space-separated)
# numbers = list(map(int, input("Enter integers separated by space: ").split()))

# if is_strictly_increasing(numbers):
#     print("The list forms a strictly increasing sequence.")
# else:
#     print("The list does not form a strictly increasing sequence.")
#----------------------------------------------------
# 498.Check if a number is a “happy number” (a number which eventually reaches 1 when replaced by the sum of the square of each digit).
# def sum_of_squares(n):
#     return sum(int(digit)**2 for digit in str(n))

# def is_happy_number(n):
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum_of_squares(n)
#     return n == 1
# num = int(input("Enter a number: "))

# if is_happy_number(num):
#     print(f"{num} is a happy number.")
# else:
#     print(f"{num} is not a happy number.")
#---------------------------------------------------
# 499 .Input three integers and check if any two add up to the third.
# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))
# c = int(input("Enter third integer: "))
# if a + b == c or a + c == b or b + c == a:
#     print("Yes, any two numbers add up to the third.")
# else:
#     print("No, none of the two numbers add up to the third.")
#----------------------------------------------------
# 500. Write a program to convert a decimal number to binary without using built-in functions.
# def decimal_to_binary(n):
#     if n == 0:
#         return "0"
#     binary_digits = []
#     while n > 0:
#         remainder = n % 2
#         binary_digits.append(str(remainder))
#         n = n // 2
#     # Since we get digits in reverse order, reverse the list
#     binary_digits.reverse()
#     return ''.join(binary_digits)
# num = int(input("Enter a non-negative decimal number: "))

# if num < 0:
#     print("Please enter a non-negative integer.")
# else:
#     binary = decimal_to_binary(num)
#     print(f"Binary representation: {binary}")
#-----------------------------------------------
# 501.Input a list of numbers and find the maximum difference between any two elements such that the larger element comes after the smaller element.
# def max_difference(arr):
#     if len(arr) < 2:
#         return 0  # or None, no pairs available
#     min_element = arr[0]
#     max_diff = arr[1] - arr[0]

#     for i in range(1, len(arr)):
#         current_diff = arr[i] - min_element
#         if current_diff > max_diff:
#             max_diff = current_diff
#         if arr[i] < min_element:
#             min_element = arr[i]
#     return max_diff
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# result = max_difference(numbers)
# print(f"Maximum difference: {result}")
#--------------------------------------------------
# 502 .Check if a number is greater than 100 or less than 10
# num = float(input("Enter a number: "))

# if num > 100 or num < 10:
#     print("The number is either greater than 100 or less than 10.")
# else:
#     print("The number is between 10 and 100 (inclusive).")
#------------------------------------------------------
# 503. Input a character and check if it is an uppercase vowel.
# char = input("Enter a single character: ")

# if len(char) == 1 and char in "AEIOU":
#     print("The character is an uppercase vowel.")
# else:
#     print("The character is not an uppercase vowel.")
#---------------------------------------------------------------------
# 504.Print “Afternoon” if time is between 12-17.
# time = int(input("Enter the hour (0-23): "))

# if 12 <= time <= 17:
#     print("Afternoon")
# else:
#     print("Time is not in the afternoon range.")
#------------------------------------------------------------
# 505 . Input a number and check if it is a multiple of 11 or 13.
# num = int(input("Enter a number: "))

# if num % 11 == 0 or num % 13 == 0:
#     print(f"{num} is a multiple of 11 or 13.")
# else:
#     print(f"{num} is not a multiple of 11 or 13.")
#------------------------------------------------------------
# 506. Check if they form an isosceles triangle.
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# if a + b > c and b + c > a and c + a > b:
#     # Check for isosceles: at least two sides equal
#     if a == b or b == c or c == a:
#         print("The sides form an isosceles triangle.")
#     else:
#         print("The sides do not form an isosceles triangle.")
# else:
#     print("The sides do not form a valid triangle.")
#------------------------------------------------------------
# 507. Check if they form a scalene triangle.
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
# if a + b > c and b + c > a and c + a > b:
#     # Check for scalene: all sides different
#     if a != b and b != c and c != a:
#         print("The sides form a scalene triangle.")
#     else:
#         print("The sides do not form a scalene triangle.")
# else:
#     print("The sides do not form a valid triangle.")
#--------------------------------------------------------------
# 508. Check if the sum of digits of a number is equal to the product of digits.
# def sum_and_product_equal(num):
#     digits = [int(d) for d in str(num)]
#     total_sum = sum(digits)
#     product = 1
#     for d in digits:
#         product *= d
#     return total_sum == product
# n = int(input("Enter a number: "))

# if sum_and_product_equal(n):
#     print("Sum of digits is equal to the product of digits.")
# else:
#     print("Sum of digits is NOT equal to the product of digits.")
#-------------------------------------------------------------
# 509.Input a string and count the number of vowels; check if even or odd.
# def count_vowels(s):
#     vowels = set("aeiouAEIOU")
#     count = sum(1 for ch in s if ch in vowels)
#     return count
# text = input("Enter a string: ")

# vowel_count = count_vowels(text)
# print(f"Number of vowels: {vowel_count}")

# if vowel_count % 2 == 0:
#     print("The number of vowels is even.")
# else:
#     print("The number of vowels is odd.")
#-------------------------------------------------------------
# 510. Input a string and count the number of consonants; check if even or odd.
# def count_consonants(s):
#     vowels = set("aeiouAEIOU")
#     count = 0
#     for ch in s:
#         if ch.isalpha() and ch not in vowels:
#             count += 1
#     return count
# text = input("Enter a string: ")

# consonant_count = count_consonants(text)
# print(f"Number of consonants: {consonant_count}")

# if consonant_count % 2 == 0:
#     print("The number of consonants is even.")
# else:
#     print("The number of consonants is odd.")
#----------------------------------------------------
# 511 . Input a string and replace all vowels with ‘*’.
# def replace_vowels(s):
#     vowels = "aeiouAEIOU"
#     result = ''
#     for ch in s:
#         if ch in vowels:
#             result += '*'
#         else:
#             result += ch
#     return result
# text = input("Enter a string: ")

# replaced_text = replace_vowels(text)
# print("String after replacing vowels with '*':")
# print(replaced_text)
#-------------------------------------------------------
# 512.Input a number and check if it’s a Kaprekar number.
# def is_kaprekar(num):
#     if num == 1:
#         return True  # 1 is a Kaprekar number
    
#     sq_num = str(num ** 2)
#     for i in range(1, len(sq_num)):
#         left = sq_num[:i]
#         right = sq_num[i:]
        
#         # Avoid cases where right part is zero or empty
#         if right == '' or int(right) == 0:
#             continue
        
#         if int(left) + int(right) == num:
#             return True
#     return False

# n = int(input("Enter a number: "))
# if n < 1:
#     print("Please enter a positive integer.")
# else:
#     if is_kaprekar(n):
#         print(f"{n} is a Kaprekar number.")
#     else:
#         print(f"{n} is not a Kaprekar number.")
#--------------------------------------------------
# 513 .Input two strings and check if one is a rotation of the other.
# def is_rotation(str1, str2):
#     # Two strings must be of the same length and not empty
#     if len(str1) != len(str2) or len(str1) == 0:
#         return False

#     # If str2 is a substring of str1 concatenated with itself, it's a rotation
#     return str2 in (str1 + str1)
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if is_rotation(s1, s2):
#     print(f'"{s2}" is a rotation of "{s1}".')
# else:
#     print(f'"{s2}" is NOT a rotation of "{s1}".')
#---------------------------------------------------------
# 514. Input a number and convert it to hexadecimal.
# def decimal_to_hex(num):
#     if num == 0:
#         return "0"
    
#     hex_chars = "0123456789ABCDEF"
#     hex_result = []
    
#     while num > 0:
#         remainder = num % 16
#         hex_result.append(hex_chars[remainder])
#         num //= 16

#     hex_result.reverse()
#     return ''.join(hex_result)
# number = int(input("Enter a non-negative integer: "))

# if number < 0:
#     print("Please enter a non-negative integer.")
# else:
#     hex_value = decimal_to_hex(number)
#     print(f"Hexadecimal representation: {hex_value}")
#-----------------------------------------------------
# 515. Input a list and separate even and odd numbers into two lists.
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# even_numbers = []
# odd_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
#--------------------------------------------------
# 516 .Input a string and replace each vowel with the next vowel (a->e, e->i, etc.).
# def replace_vowels(s):
    # Mapping vowels to the next vowel (lowercase and uppercase)
#     vowel_map = {
#         'a': 'e',
#         'e': 'i',
#         'i': 'o',
#         'o': 'u',
#         'u': 'a',
#         'A': 'E',
#         'E': 'I',
#         'I': 'O',
#         'O': 'U',
#         'U': 'A'
#     }
#     result = ''
#     for ch in s:
#         if ch in vowel_map:
#             result += vowel_map[ch]
#         else:
#             result += ch
#     return result
# text = input("Enter a string: ")

# new_text = replace_vowels(text)
# print("String after replacing vowels with next vowels:")
# print(new_text)
#---------------------------------------------------
# 517. Input a number and check if the sum of even digits is greater than sum of odd digits.

# def compare_even_odd_sums(num):
#     even_sum = 0
#     odd_sum = 0
    
#     for digit in str(num):
#         d = int(digit)
#         if d % 2 == 0:
#             even_sum += d
#         else:
#             odd_sum += d
#     return even_sum > odd_sum
# n = int(input("Enter a number: "))

# if compare_even_odd_sums(n):
#     print("Sum of even digits is greater than sum of odd digits.")
# else:
#     print("Sum of even digits is NOT greater than sum of odd digits.")
#---------------------------------------------------------
# 518. Input a list and print all pairs with difference equal to a given number.
# def find_pairs_with_diff(nums, diff):
#     pairs = []
#     nums_set = set(nums)  # For faster lookups
#     for num in nums:
#         target1 = num + diff
#         target2 = num - diff
#         if target1 in nums_set:
#             pairs.append((num, target1))
#         if target2 in nums_set:
#             pairs.append((target2, num))
#     # To avoid duplicate pairs like (a,b) and (b,a), use a set or filter duplicates
#     unique_pairs = set()
#     for a, b in pairs:
#         # Sort the pair so (min, max) is stored
#         sorted_pair = tuple(sorted((a, b)))
#         unique_pairs.add(sorted_pair)
#     return unique_pairs
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# difference = int(input("Enter the difference value: "))

# result_pairs = find_pairs_with_diff(numbers, difference)

# if result_pairs:
#     print("Pairs with difference", difference, ":")
#     for pair in sorted(result_pairs):
#         print(pair)
# else:
#     print("No pairs found with the given difference.")
#----------------------------------------------------------------
# 519. Input a number and print the next prime number greater than it.
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# def next_prime(n):
#     candidate = n + 1
#     while True:
#         if is_prime(candidate):
#             return candidate
#         candidate += 1
# num = int(input("Enter a number: "))

# result = next_prime(num)
# print(f"The next prime number greater than {num} is {result}.")
#----------------------------------------------------------
# 520. Input a number and check if all digits are odd.
# def all_digits_odd(num):
#     for digit in str(num):
#         if int(digit) % 2 == 0:
#             return False
#     return True
# n = int(input("Enter a number: "))

# if all_digits_odd(n):
#     print("All digits are odd.")
# else:
#     print("Not all digits are odd.")
#---------------------------------------------
# 521. Input a string and check if it contains any repeated substring.
# def has_repeated_substring(s):
#     n = len(s)
#     # Check substrings of all lengths from 1 to n//2
#     for length in range(1, n // 2 + 1):
#         seen = set()
#         for i in range(n - length + 1):
#             substring = s[i:i+length]
#             if substring in seen:
#                 return True
#             seen.add(substring)
#     return False
# text = input("Enter a string: ")

# if has_repeated_substring(text):
#     print("The string contains a repeated substring.")
# else:
#     print("The string does not contain any repeated substring.")

#-----------------------------------------------------
# 522 .Input a string and check if it contains any numeric substring.
# def contains_numeric_substring(s):
#     # Iterate through the string and check for consecutive digits
#     for i in range(len(s)):
#         if s[i].isdigit():
#             # Found a digit, check if next chars also digits
#             j = i
#             while j < len(s) and s[j].isdigit():
#                 j += 1
#             return True
#     return False
# text = input("Enter a string: ")

# if contains_numeric_substring(text):
#     print("The string contains a numeric substring.")
# else:
#     print("The string does not contain any numeric substring.")
#--------------------------------------------------
# 523. Input two strings and find the length of the longest common prefix.
# def longest_common_prefix_length(s1, s2):
#     min_length = min(len(s1), len(s2))
#     count = 0
#     for i in range(min_length):
#         if s1[i] == s2[i]:
#             count += 1
#         else:
#             break
#     return count
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")

# length = longest_common_prefix_length(string1, string2)
# print(f"The length of the longest common prefix is: {length}")
#--------------------------------------------------
# 524. Input two dates and calculate the difference in days (simple version).

#--------------------------------------------------
# 525. Input a number and check if it can be expressed as the sum of two squares.
# import math
# def can_be_expressed(n):
#     for a in range(int(math.isqrt(n)) + 1):
#         b_squared = n - a*a
#         if b_squared < 0:
#             break
#         b = int(math.isqrt(b_squared))
#         if b*b == b_squared:
#             return True
#     return False
# num = int(input("Enter a non-negative integer: "))

# if num < 0:
#     print("Please enter a non-negative integer.")
# else:
#     if can_be_expressed(num):
#         print(f"{num} can be expressed as the sum of squares of two integers.")
#     else:
#         print(f"{num} cannot be expressed as the sum of squares of two integers.")
#-------------------------------------------
# 526. Input a list and check if it can be partitioned into two subsets with equal sum.
# def can_partition(nums):
#     total_sum = sum(nums)
#     # If total sum is odd, can't partition equally
#     if total_sum % 2 != 0:
#         return False

#     target = total_sum // 2
#     n = len(nums)

#     # DP table: dp[i][j] = True if subset of first i numbers has sum j
#     dp = [[False] * (target + 1) for _ in range(n + 1)]

#     # Sum 0 is always possible (empty subset)
#     for i in range(n + 1):
#         dp[i][0] = True

#     for i in range(1, n + 1):
#         for j in range(1, target + 1):
#             if nums[i - 1] <= j:
#                 dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i - 1]]
#             else:
#                 dp[i][j] = dp[i-1][j]

#     return dp[n][target]
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# if can_partition(numbers):
#     print("The list can be partitioned into two subsets with equal sum.")
# else:
#     print("The list cannot be partitioned into two subsets with equal sum.")
#----------------------------------------------------------------
# 527. Input a number and check if its digits alternate between even and odd.
# def digits_alternate(num):
#     digits = [int(d) for d in str(num)]
    
#     for i in range(len(digits) - 1):
#         # Check if current and next digits have opposite parity
#         if (digits[i] % 2) == (digits[i+1] % 2):
#             return False
#     return True
# n = int(input("Enter a number: "))

# if digits_alternate(n):
#     print("Digits alternate between even and odd.")
# else:
#     print("Digits do not alternate between even and odd.")
#------------------------------------------------------
# 528. Input two numbers and check if their sum is prime.
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# total = a + b

# if is_prime(total):
#     print(f"The sum {total} is a prime number.")
# else:
#     print(f"The sum {total} is not a prime number.")
#---------------------------------------------------
# 529. Input a list of integers and check if all are prime numbers.
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# numbers = list(map(int, input("Enter integers separated by space: ").split()))

# if all(is_prime(num) for num in numbers):
#     print("All numbers in the list are prime.")
# else:
#     print("Not all numbers in the list are prime.")
#-----------------------------------------------------------
# 530. Write a while loop that takes input from the user repeatedly until the user types “stop”. Use break to exit.
# while True:
#     user_input = input("Enter something (type 'stop' to quit): ")
#     if user_input.lower() == "stop":
#         print("Stopping the loop.")
#         break
#     print(f"You entered: {user_input}")
#------------------------------------------------------
# 531. Use a for loop to print numbers from 1 to 10, but stop printing when the number reaches 5 using break.
# for num in range(1, 11):
#     if num == 5:
#         break
#     print(num)
#----------------------------------------------------
# 532. Print numbers from 1 to 100 but stop if a number is divisible by 13.
# for num in range(1, 101):
#     if num % 13 == 0:
#         break
#     print(num)
# -----------------------------------------------------
# 533. Iterate over a list and print each element until you encounter the number 7; then use break.
# numbers = [3, 5, 2, 7, 8, 10, 7, 12]
# for num in numbers:
#     if num == 7:
#         break
#     print(num)
#---------------------------------------------------
# 534. Input a list of numbers and find the first negative number using break.
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# first_negative = None
# for num in numbers:
#     if num < 0:
#         first_negative = num
#         break

# if first_negative is not None:
#     print(f"The first negative number is: {first_negative}")
# else:
#     print("There is no negative number in the list.")
# ---------------------------------------------------
# 535 . Use a while loop to find the first prime number greater than 50 and stop using break.
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# num = 51  # Start checking from 51
# while True:
#     if is_prime(num):
#         print(f"The first prime number greater than 50 is: {num}")
#         break
#     num += 1
# ----------------------------------------------------
# 536. Input integers continuously and stop inputting when a number greater than 100 is entered.
# while True:
#     num = int(input("Enter an integer (stop if > 100): "))
#     if num > 100:
#         print("Number greater than 100 entered. Stopping input.")
#         break
#     print(f"You entered: {num}")
#----------------------------------------------
# # 537. Print the first 10 even numbers using a for loop and break when you reach 10 numbers.
# count = 0

# for num in range(2, 1000, 2):  # Start from 2, go up by 2 to get even numbers
#     print(num)
#     count += 1
#     if count == 10:
#         break
#------------------------------------------------
# 538. Find the first multiple of 7 between 1 and 100 and stop using break.
# for num in range(1, 101):
#     if num % 7 == 0:
#         print(f"The first multiple of 7 between 1 and 100 is: {num}")
#         break
#-----------------------------------------------------
# 539. Iterate over characters in a string and stop at the first vowel using break.
# vowels = "aeiouAEIOU"
# text = input("Enter a string: ")

# for ch in text:
#     if ch in vowels:
#         print(f"First vowel encountered: {ch}")
#         break
#     print(ch)

#---------------------------------------------------------
# 540. Input a list and print numbers until the sum exceeds 100, then break.
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# total_sum = 0
# for num in numbers:
#     total_sum += num
#     if total_sum > 100:
#         break
#     print(num)
#-----------------------------------------------------
# 541. Use a loop to find the smallest divisor of a number (other than 1) and break when found.
 
# num = int(input("Enter a number greater than 1: "))

# if num <= 1:
#     print("Please enter a number greater than 1.")
# else:
#     divisor = None
#     for i in range(2, num + 1):
#         if num % i == 0:
#             divisor = i
#             break
#     print(f"The smallest divisor of {num} (other than 1) is: {divisor}")

#-------------------------------------------------------------------
# 542. Input a list of strings and stop printing when a string “exit” is encountered.
# strings = input("Enter strings separated by space: ").split()

# for s in strings:
#     if s == "exit":
#         break
#     print(s)
#----------------------------------------------------
# 543. Print the Fibonacci sequence numbers but stop once the number exceeds 1000 using break.
# a, b = 0, 1
# while True:
#     if a > 1000:
#         break
#     print(a)
#     a, b = b, a + b
# 544. Input numbers and stop when the sum of input numbers is exactly 50.
# total_sum = 0
# while True:
#     num = int(input("Enter a number: "))
#     total_sum += num
#     if total_sum == 50:
#         print("Sum reached exactly 50. Stopping input.")
#         break
#     elif total_sum > 50:
#         print(f"Sum exceeded 50 (current sum: {total_sum}). Continue or stop as needed.")
     

#----------------------------------------------------------------
# 545. Iterate through a list of words and break when you find the longest word.
# words = input("Enter words separated by space: ").split()
# max_length = max(len(word) for word in words)
# for word in words:
#     if len(word) == max_length:
#         print(f"Longest word found: {word}")
#         break
#     print(word)
#--------------------------------------------------
# 546. Use a for loop to iterate from 1 to 50 but skip printing numbers divisible by 5 using continue and stop at 30 using break.
# for num in range(1, 51):
#     if num > 30:
#         break
#     if num % 5 == 0:
#         continue
#     print(num)
#-----------------------------------------------
# 547. Write a program that asks for passwords and stops asking when the correct password is entered.
# correct_password = "secret123"
# while True:
#     user_input = input("Enter password: ")
#     if user_input == correct_password:
#         print("Password accepted. Access granted.")
#         break
#     else:
#         print("Incorrect password. Try again.")
#------------------------------------------------------
# 548. Use a while loop to find the first palindrome number greater than 200.
# def is_palindrome(num):
#     return str(num) == str(num)[::-1]
# num = 201  # Start checking from 201
# while True:
#     if is_palindrome(num):
#         print(f"The first palindrome number greater than 200 is: {num}")
#         break
#     num += 1
#--------------------------------------------------
# 549.Search a list of numbers for the first even number and stop when found.
# numbers = [3, 7, 5, 9, 8, 11, 14]
# for num in numbers:
#     if num % 2 == 0:
#         print("First even number found:", num)
#         break
# else:
#     print("No even number found in the list.")
#--------------------------------------------------------
# 550.In a string, find the first vowel and stop printing characters.
# text = "python programming"
# vowels = "aeiouAEIOU"
# for char in text:
#     if char in vowels:
#         break
#     print(char, end='')

#-------------------------------------------------
# 551. Find the first prime number in a given range using a loop and break.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# start = 10
# end = 50

# for num in range(start, end + 1):
#     if is_prime(num):
#         print("First prime number in range:", num)
#         break
# else:
#     print("No prime number found in the range.")
#------------------------------------------------------
# 552.   Find the first perfect square greater than 100 and stop.
# import math
# num = 101  # Start checking from 101
# while True:
#     root = math.isqrt(num)  # integer square root
#     if root * root == num:
#         print("First perfect square greater than 100 is:", num)
#         break
#     num += 1
#------------------------------------------------------
# 553 . In a list of names, find the first name starting with 'A' and break.
# names = ["John", "Bob", "Alice", "Anna", "Mark"]
# for name in names:
#     if name.startswith('A'):
#         print("First name starting with 'A':", name)
#         break
# else:
#     print("No name starting with 'A' found.")
#---------------------------------------------------------
# 554. Print multiplication tables from 1 to 10 but stop the entire process if a product equals 36.
# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         print(f"{i} x {j} = {product}")
#         if product == 36:
#             print("Product 36 found, stopping all tables.")
#             break  # break inner loop
#     else:
#         continue 
#     break  # break outer loop if inner loop was broken
#----------------------------------------------------------------------------
# 555. For each row in a matrix, print numbers until you find a negative, then move to the next row.
# matrix = [
#     [3, 5, 7, -1, 9],
#     [2, 4, 6, 8],
#     [10, -2, 12, 14],
# ]
# for row in matrix:
#     for num in row:
#         if num < 0:
#             break  # Stop printing numbers in this row on first negative
#         print(num, end=' '
#     print()  # Move to next line after each row
#--------------------------------------------------
# 556. Search for a pair of numbers (i, j) where i + j = 10 and break both loops once found.
# found = False
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i + j == 10:
#             print(f"Pair found: ({i}, {j})")
#             found = True
#             break  # break inner loop
#     if found:
#         break  # break outer loop
#---------------------------------------------------
# 557. Keep asking user for input until a valid integer between 1 and 10 is entered.
# while True:
#     user_input = input("Enter an integer between 1 and 10: ")
#     if user_input.isdigit():
#         num = int(user_input)
#         if 1 <= num <= 10:
#             print("Valid input:", num)
#             break
#     print("Invalid input. Try again.")3
#-------------------------------------------------
# 558. Input a username repeatedly until it contains no spaces.
# while True:
#     username = input("Enter username (no spaces allowed): ")
#     if ' ' not in username:
#         print("Username accepted:", username)
#         break
#     # print("Username should not contain spaces. Try again.")
#--------------------------------------------
# 559. Continuously input ages and stop when an age less than 0 is entered.
# while True:
#     age = input("Enter age (negative to stop): ")
#     if age.lstrip('-').isdigit():  # Allow negative sign for checking
#         age_num = int(age)
#         if age_num < 0:
#             print("Negative age entered, stopping input.")
#             break
#         print("Age entered:", age_num)
#     else:
#         print("Invalid input. Please enter a valid integer.")
#------------------------------------------------------
# 560. Input numbers until the input is exactly 0, then break.
#while True:
    # num = input("Enter a number (0 to stop): ")
    # if num.lstrip('-').isdigit():
    #     num_int = int(num)
    #     if num_int == 0:
    #         print("Zero entered, stopping input.")
    #         break
    #     print("You entered:", num_int)
    # else:
    #     print("Invalid input, please enter an integer.")
    #-----------------------------------------------------
# 561. Scan text and stop reading when a stop word ("END") is found.
# print("Enter text (type 'END' to stop):")

# while True:
#     line = input()
#     if line == "END":
#         print("Stop word found, ending input.")
#         break
#    print("You entered:", line)
#------------------------------------------------
# 562. Keep simulating dice rolls until a 6 appears.
# import random
# while True:
#     roll = random.randint(1, 6)
#     print(f"Rolled: {roll}")
#     if roll == 6:
#         print("Got a 6! Stopping.")
#         break
#------------------------------------------------
# 563. Input scores for players until a player scores above 100 points.
# while True:
#     score = input("Enter player score: ")
#     if score.isdigit():
#         score_num = int(score)
#         if score_num > 100:
#             print(f"Score above 100 detected: {score_num}. Stopping input.")
#             break
#         print(f"Score recorded: {score_num}")
#     else:
#         print("Invalid input. Please enter a valid integer score.")
#-------------------------------------------------------
# 564. Find the first divisor of a number other than 1 and itself using break.
# num = 91 
# for divisor in range(2, num):
#     if num % divisor == 0:
#         print(f"First divisor of {num} other than 1 and itself is: {divisor}")
#         break
# else:
#     print(f"{num} has no divisors other than 1 and itself (it is prime).")

#----------------------------------------------------------
# 565. Search for Pythagorean triples under 100 using nested loops and break when found.
# for a in range(1, 100):
#     for b in range(a, 100):  # start from a to avoid duplicates like (3,4,5) and (4,3,5)
#         c_squared = a**2 + b**2
#         c = int(c_squared**0.5)
#         if c < 100 and c * c == c_squared:
#             print(f"Pythagorean triple found: ({a}, {b}, {c})")
#             break  # breaks inner loop
#     else:
#         continue  # continue outer loop if inner loop not broken
#     break  # break outer loop if inner loop was broken
#----------------------------------------------
# 566. Input numbers and stop when you encounter a number that is a perfect cube.
# def is_perfect_cube(n):
#     if n < 0:
#         return False  # Assuming only non-negative cubes for this example
#     cube_root = round(n ** (1/3))
#     return cube_root ** 3 == n
# while True:
#     num_input = input("Enter a number: ")
#     if num_input.lstrip('-').isdigit():
#         num = int(num_input)
#         if is_perfect_cube(num):
#             print(f"{num} is a perfect cube. Stopping input.")
#             break
#         else:
#             print(f"{num} is not a perfect cube. Continue.")
#     else:
#         print("Invalid input, please enter an integer.")
#-------------------------------------------------------------
# 567. Print the multiplication table of 5 but stop when the product is greater than 30.
# for i in range(1, 11):
#     product = 5 * i
#     if product > 30:
#         break
#     print(f"5 x {i} = {product}")
#-----------------------------------------------------------
# 568. Search for the first uppercase letter in a string and break once found.
# text = "hello World, this is OpenAI"
# for char in text:
#     if char.isupper():
#         print("First uppercase letter found:", char)
#         break
# else:
#     print("No uppercase letter found in the string.")
#--------------------------------------------------------------
# 567.Find the first prime number greater than 50 by checking each number and breaking when found.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = 51  # Start checking from 51

# while True:
#     if is_prime(num):
#         print("First prime number greater than 50 is:", num)
#         break
#     num += 1
# -----------------------------------------------------------
# 568. Keep reading temperatures until a temperature above 100 is entered, then break.
# while True:
#     temp_input = input("Enter temperature: ")
#     if temp_input.lstrip('-').isdigit():
#         temp = int(temp_input)
#         if temp > 100:
#             print(f"Temperature above 100 detected: {temp}°C. Stopping.")
#             break
#         else:
#             print(f"Temperature recorded: {temp}°C")
#     else:
#         print("Invalid input. Please enter a valid integer temperature.")
#------------------------------------------------------------------------
# 569. Print numbers from 1 to 100 but break when a number contains the digit '3'.
# for num in range(1, 101):
#     if '3' in str(num):
#         break
#     print(num)
#---------------------------------------------------------
# 570 .Input a list of numbers and break when the cumulative sum exceeds 100.
# total = 0
# while True:
#     num_input = input("Enter a number: ")
#     if num_input.lstrip('-').isdigit():
#         num = int(num_input)
#         total += num
#         print(f"Cumulative sum: {total}")
#         if total > 100:
#             print("Cumulative sum exceeded 100. Stopping.")
#             break
#     else:
#         print("Invalid input. Please enter an integer.")
#--------------------------------------------------------------
# 571. Print characters of a string until a space character is found, then break.
# text = "Hello World from Python"
# for char in text:
#     if char == " ":
#         break
#     print(char, end="")
#----------------------------------------------------------
# 572 .Input numbers and break if the number is divisible by 11.
# while True:
#     num_input = input("Enter a number: ")
#     if num_input.lstrip('-').isdigit():
#         num = int(num_input)
#         if num % 11 == 0:
#             print(f"{num} is divisible by 11. Stopping.")
#             break
#         else:
#             print(f"{num} is not divisible by 11. Continue.")
#     else:
#         print("Invalid input. Please enter an integer.")
#-------------------------------------------------------------
# 573. Print characters of a string until a space character is found, then break.
# text = "Hello World from Python"
# for char in text:
#     if char == " ":
#         break
#     print(char, end="")
#-------------------------------------------------------------
# 574.Keep asking the user for input until they enter 'yes' or 'no', then break.
# while True:
#     response = input("Enter 'yes' or 'no': ").strip().lower()
#     if response in ("yes", "no"):
#         print(f"You entered: {response}")
#         break
#     else:
#         print("Invalid input. Please enter only 'yes' or 'no'.")
#-------------------------------------------------------------------
# 575. Iterate over a list of names and break once you find a name starting with 'J'.
# names = ["Alice", "Bob", "John", "Michael", "Jenny", "Sara"]
# for name in names:
#     if name.startswith("J"):
#         print(f"Found name starting with 'J': {name}")
#         break
#-------------------------------------------------------------
# 576 .Find the first number divisible by 4 in a list and break the loop.
# numbers = [5, 9, 13, 20, 25, 32]
# for num in numbers:
#     if num % 4 == 0:
#         print("First number divisible by 4:", num)
#         break
# else:
#     print("No number divisible by 4 found.")
#-------------------------------------------------------------
# 577. Keep asking the user for a positive number and break when a positive number is given.
# while True:
#     num_input = input("Enter a positive number: ")
#     if num_input.lstrip('-').isdigit():
#         num = int(num_input)
#         if num > 0:
#             print(f"Positive number entered: {num}")
#             break
#         else:
#             print("That's not positive. Try again.")
#     else:
#         print("Invalid input. Please enter a valid number.")
#------------------------------------------------------
# 578. Input scores of students and break if any score is below 35 (fail).
# scores = [78, 65, 89, 34, 90, 56]  # example scores
# for score in scores:
#     if score < 35:
#         print(f"Fail detected! Score: {score}")
#         break
#     else:
#         print(f"Score: {score} - Pass")
#-----------------------------------------------------
# 579. Print numbers from 1 upwards but break when the square of the number is greater than 500.
# num = 1
# while True:
#     if num ** 2 > 500:
#         break
#     print(num)
#     num += 1
#-----------------------------------------------------------
# 580. Find the first repeated character in a string and break.
# text = "programming"
# seen = set()
# for char in text:
#     if char in seen:
#         print("First repeated character:", char)
#         break
#     seen.add(char)
# else:
#     print("No repeated characters found.")
#----------------------------------------------
# 581. Check if a list contains the number 100 and break once found.
# numbers = [10, 25, 50, 75, 100, 200]
# for num in numbers:
#     if num == 100:
#         print("Number 100 found in the list.")
#         break
# else:
#     print("Number 100 not found in the list.")
#-----------------------------------------------
# 582. Keep inputting numbers and break if the average of all inputs exceeds 70.
# numbers = []
# while True:
#     num_input = input("Enter a number: ")
#     if num_input.lstrip('-').isdigit():
#         num = int(num_input)
#         numbers.append(num)
#         avg = sum(numbers) / len(numbers)
#         print(f"Current average: {avg:.2f}")
#         if avg > 70:
#             print("Average exceeded 70. Stopping.")
#             break
#     else:
#         print("Invalid input. Please enter a valid integer.")
# ----------------------------------------------------
# 583. Print numbers from 1 to 20, but skip the multiples of 5.
# for num in range(1, 21):
#     if num % 5 == 0:
#         continue
#     print(num)
#-------------------------------------------
# 584 .Print all characters of a string except vowels.
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# for ch in text:
#     if ch in vowels:
#         continue
#     print(ch, end="")

#----------------------------------------
# 585. Print numbers from 1 to 50, skipping even numbers.
# for i in range(1, 51):
#     if i % 2 == 0:
#         continue
#     print(i)
#----------------------------------------)
# 586. Print numbers from 1 to 30, but skip numbers divisible by 3.
# for i in range(1, 31):
#     if i % 3 == 0:
#         continue
#     print(i)

#-----------------------------------------
# 587. Input integers from the user and skip negative numbers when printing.
# while True:
#     num = int(input("Enter an integer (0 to stop): "))
#     if num == 0:  # stop condition
#         break
#     if num < 0:   # skip negative numbers
#         continue
#     print(num)
#------------------------------------------------
# 588.Print only positive numbers from a given list.
# numbers = [2,-5,23,-7,-1,22,56]
# for num in numbers:
#     if num <= 0:  
#         continue
#     print(num)
#---------------------------------------------
# 587. Print numbers between 1 and 100 that are not divisible by 7.
# for num in range(1, 101):
#     if num % 7 == 0:
#         continue
#     print(num)
#-----------------------------------------------------
#588. Iterate over a list of names and skip names shorter than 4 characters.
# names = ["dev", "Tina", "Ajay", "Sara", "Naina", "Rohini"]
# for name in names:
#     if len(name) < 4:
#         continue
#     print(name)
#----------------------------------------------------------------
#589. Iterate over a string and skip spaces when printing characters.
# text = "Python is fun"
# for char in text:
#     if char == " ":
#         continue
#     print(char, end="")
#--------------------------------------------------
#590. Print all numbers from 1 to 20 except those that end with digit 3.
# for i in range(1, 21):
#     if i % 10 == 3:  # check if the last digit is 3
#         continue
#     print(i)
#---------------------------------------------
# 591. Take 5 user inputs, skip printing if the input is not a number.
# for _ in range(5):
#     user_input = input("Enter a number: ")
#     if not user_input.isdigit():  # checks if it's not a number
#         continue
#     print(int(user_input))
#-------------------------------------------------
# 592.Keep reading scores and skip invalid scores (less than 0 or more than 100).
# while True:
#     score = int(input("Enter score (0-100, -1 to stop): "))
#     if score == -1:  # exit condition
#         break
#     if score < 0 or score > 100:  # invalid score
#         continue
#     print("Valid score:", score)
#---------------------------------------------------
# 593.Input ages and skip if age is below 0.
# while True:
#     age = int(input("Enter age (-1 to stop): "))
#     if age == -1:  # exit condition
#         break
#     if age < 0:  # skip negative ages
#         continue
#     print("Valid age:", age)
#-----------------------------------
# 594.Skip any words in a sentence that start with a vowel.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# for word in words:
#     if word[0].lower() in 'aeiou':
#         continue
#     print(word, end=' ')
#---------------------------------
# 595 .Read email addresses and skip invalid ones (not containing “@”).
# emails = ["user@example.com", "testmail.com", "hello@world", "abc@", "noatsign"]
# for email in emails:
#     if "@" not in email:
#         continue
#     print(email)
##----------------------------------------
# 596. Print a multiplication table from 1 to 10, skipping products greater than 50.
# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         if product > 50:
#             continue
#         print(f"{i} x {j} = {product}")
#     print()
#----------------------------------------------
# 597. Print a pattern of numbers but skip 5 in each row.
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         if j == 5:
#             continue
#         print(j, end=" ")
#     print()
#-------------------------------------------------
#598. For each number from 1 to 5, print its multiples except when the multiple is divisible by 4.
# for i in range(1, 6):  # Numbers from 1 to 5
#     for j in range(1, 11):  # Multiples up to 10
#         multiple = i * j
#         if multiple % 4 == 0:  # Skip if divisible by 4
#             continue
#         print(multiple, end=" ")
#     print()
#-----------------------------------------------
# 599. In nested loops, skip printing if the sum of indices is even.
# for i in range(1, 6):      
#     for j in range(1, 6):    
#         if (i + j) % 2 == 0:  # Skip if sum of indices is even
#             continue
#         print(f"({i},{j})", end=" ")
#     print()
#------------------------------------------------
# 600. From a list of transactions, skip ones with zero amount.
# transactions = [100, 0, -50, 200, 0, 75]
# for amount in transactions:
#     if amount == 0:  # Skip zero transactions
#         continue
#     print(f"Transaction amount: {amount}")
#-----------------------------------------
# 601. Skip products with price above ₹500 when printing a product list.
# ts = [
#     ("Laptop Bag", 750),
#     ("Mouse", 250),
#     ("Keyboard", 450),
#     ("Headphones", 1200),
#     ("Notebook", 50)
# ]
# for name, price in products:
#     if price > 500:  # Skip products priced above ₹500
#         continue
#-----------------------------------------------
# 602. In a class attendance list, skip students marked as “Absent”
# attendance_list = [
#     ("Amit", "Present"),
#     ("Rohini", "Absent"),
#     ("Neha", "Present"),
#     ("Vikas", "Absent"),
#     ("Priya", "Present")
# ]
# for name, status in attendance_list:
#     if status == "Absent":  # Skip absent students
#         continue
#     print(f"{name} is {status}")

#---------------------------------------------------
# 603. Skip names in a list that don’t start with a capital letter.
# names = ["Rohini", "amit", "Neha", "vikas", "Priya", "arun"]
# for name in names:
#     if not name[0].isupper():  # Skip if first letter is not uppercase
#         continue
#     print(name)
#-------------------------------------------------
# 604.In a quiz app, skip invalid answers (anything other than A, B, C, D).
# answers = ["A", "E", "B", "X", "C", "D", "F", "B"]
# for ans in answers:
#     if ans not in ["A", "B", "C", "D"]:
#         continue  # Skip invalid answers
#     print(f"Valid answer: {ans}")
#-------------------------------------------------
# 605. Print characters of a string except digits.
# text = input("Enter a string: ")
# for char in text:
#     if char.isdigit():  
#         continue
#     print(char, end="")
#----------------------------------------------------
# 606. Print words in a list except those containing “ing”.
# words = ["playing", "run", "swimming", "jump", "reading", "walk","Dancing","cook"]
# for word in words:
#     if "ing" in word:
#         continue  # Skip words containing "ing"
#     print(word)
#--------------------------------------------------------
# 607 .Skip palindrome words in a sentence.
# sentence = "madam went to the racecar event level ground"
# words = sentence.split()
# for word in words:
#     if word.lower() == word[::-1].lower():  # Check palindrome ignoring case
#         continue
#     print(word)
#------------------------------------------------
# 608 .Skip numbers in a list that are perfect squares.
# import math
# numbers = [3, 4, 5, 9, 12, 16, 18, 20, 25, 30]
# for num in numbers:
#     if math.isqrt(num) ** 2 == num:
#         continue
#     print(num)
#----------------------------------------------
# 609. Print numbers from 1 to 20, skipping the 5th, 10th, and 15th numbers.
# for i in range(1, 21):
#     if i in [5, 10, 15]:
#         continue
#     print(i, end=" ")
#---------------------------------------------------
#610. 
