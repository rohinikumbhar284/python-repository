p="sanket"  # sanket is my manager - This is singal line comment 
print(p)

R="Practice time" # we store practice time in the R variable
print(R)

# a=1   # this is an addition of two no 
# b=2
# c=4
# print(a+b+c)

A ="Rohini"  # varible can have short name
B="Kumbhar"
print(A + B)

Age1 = 20  # Varible have descriptive name like age ,cname
Age2 = 30
print(Age1 + Age2) # output 50


# _s = "sanket"
# P = 9
# print(_s)     #output=sanket
#print(P)     #output=9

_A = 200  # Varibale start with underscore
B = 100
print(_A+B)


3="rohini "  # name can't start with number
print(3)
R_1 = "Rohini"  #it contain alpha-numeric characters and 
print(R_1)               #underscores (A-z, 0-9, and _ )

# print="abc"
# print(print)

R = "Good Luck"
print(r)   # Not run - Bcoz its case-sensitive. use-R 


#s = "sanket"
# s = 9
# s="pradeep"
# print(s)

R= "Rohini"
R= "tina"
R ="Ritu"  # output = Ritu
print(R) #bcoz = new refernce consider

########## QUESTION3############
# Q: Assign your name and age to two variables and print them.
# Example output: My name is Ashutosh and I am 25 years old.
N= "My name  is Rohini and "
A= "I am 25 years old"
print(N+A) 

# Q: Identify which variable names are valid or invalid:
# _myvar, my_var, 2ndname, user-name, class, userName

# Try writing code with these names and see which give error
_myvar ="Is it correct"
print(_myvar) # valid

my_var = "I am cheking it "
print(my_var) # valid

2ndname = "Can it start with no"
print(2ndname)  # Invalid- bcoz invalid decimal 

user-name ="valid or not"
print(user-name)  #Invalid -cannot assign special character like hypen
                  # User_name is correct
class = "Class is valid or not"
print(class) # invalid = it is reserved keyword
             #Python uses class to define classes

userName = "check it"
print(userName)  #valid

 #Assign values 10, 20, 30 to a, b, c in one line and print them.
a=10, b=20,c=30 #Python does not allow multiple assignments like that with commas.
print(a,b,c)
#-------
a =10
b=20
c=30
print(a,b,c)
#-----------
a,b,c =10,20,30
print(a,b,c)
 #Assign the value 100 to variables x, y, z in one line. Then print all three.
x,y,z =100,100,100
print(x,y,z)
#-------
x = y = z = 100
print(x, y, z)
# Q: Assign a float to a variable and print its type using type() function.
num = 99.9
print(type(num))
#--
num = "Rohini" 
print(type(num))
# Take two variables a = 5, b = 10 and swap them without using a third variable
a =5
b =10
a,b = b,a
print(a,b)

#Use f-string to print: "Ashutosh is 27 years old and lives in Pune"
# Use variables for name, age, city.
name = "Ashutosh"
age = 27
city = "Pune"

print(f"{name} is {age} years old and lives in {city}")

#Take name and age as input from the user and print: 
# "Hello, [name]! You are [age] years old."
Name = input("Enter your name here :")
Age= input("Enter your actual age :")
print(f"Hello, {Name}! You are {Age} years old.")  

# Write a program to take 2 numbers from the user and print their
#  sum, difference, product, and division.
Num1 =input("Enter first number:")
Num2 =input("Enter second number")
print(F"Add is= {Num1+ Num2} Difference is = {Num1+ Num2} Product of ={Num1+ Num2} Division of ={Num1+ Num2}")

 #Define a variable `PI = 3.14`. Use it to calculate the area of
 # a circle with radius 5.
# Note: Though Python doesn't support constants, use capital
#  letters as a convention.# constant by convention

PI = 3.14 
radius = 5
area = PI * radius ** 2
print(f"The area of the circle with radius {radius} is {area}")

PI = 3.14 
radius = float(input("Enter the redius:")) # use float bcoz input return the string
A = PI * radius ** 2         # you can't use ** operator in string
print(f"Area  of circule using redius {radius} is : {A} ")

#Assign your first and last name to two variables.
# Print your full name in one line using string concatenation.

first_name = "Rohini"
Last_name ="Kumbhar"
Full_name = first_name + " " + Last_name 
print(Full_name)

#Create a variable with an underscore (e.g., user_age) 
# and assign it a value.
# Print it using an f-string.

first_stud = "Rohini"
second_stud ="Kartiki"
third_stud ="Nisha"
print(f"First price goes to:{first_stud} \n Second Price goes to:{second_stud} \n  Third price goes to :{third_stud}")

#: Create two variables `value` and `Value`, assign them different numbers.
# Print both and observe the output.
value = 4         # Paython is case sensitive it cosider valus(small v) is one varible 
Value =8           # Value (Capital V) is another variavble 
print(F"value is = {value}") 
print(f"Value is = {Value}")

#Assign an integer to variable `x`, then assign a string to the same `x`.
# Print type before and after re-assignment.
x = 50
print(f"Before re-assignment x :{x} , type = {type(x)}")
x = "Rohini" 
print(f"After re-assignment x :{x} , type = {type(x)}")

# Try creating a variable named `class` and assign it a value.
# Observe the error and fix it with a valid name.

class = 200 # class is a reserved keyword in Python
print(f"Chaking error :{class}")   #and cannot be used as a variable name

class_vari = 400  # If you use any reserved keyword then use Uderscore or any varibale with this 
print(f"class has number : {class_vari}")

# Q: Use `.format()` method to print: “The cost of 5 apples is ₹150”
# Use variables for quantity and price
quantity = 5
price = 150
print("The cost of {} apples is:{} Rs ".format(quantity ,price))

quentity =int(input("Enter your device quentity :"))
price = float(input("Enter apple price :"))
Total_price = quentity * price 
print("Divice quentity is :{} \n One apple price is :{} \n Total amount is: {}" .format(quentity ,price ,Total_price))
 
 #Print a message using `%s` and `%d` formatting style. Example: "User Ashutosh is 27 years old."
Name = "Ashutosh"
Age = 27
print("User %s is %d year old." % (Name,Age) )

Assign values to multiple variables using line continuation:
# Example:
# x = 1 + \
#     2 + \
#     3
# Print x.

a,b,c =10,\
       20,\
       30
print(f"a:{a},\n b:{b},\n c:{c}")

a = 5 + \
    5 
print(a)

a ,b ,c= 5+5 ,\
         2*3,\
         4%2 
print(a,b,c)

#Q: Assign the result of a mathematical expression (e.g., 10 + 5 * 2) to a variable.
# Print it.
    
a = 10 + 5 * 2
print(a)

a =int(input("value1:"))
b =float(input("Value2:"))
c =int(input("value3:"))
d = a + b * c -a
print(d)
#Q: x = y = z = 5 + 10
# Print x, y, z

x = y = z = 5 +10
print(x,y,z)

x = y = z = 5 +10  # not display output 
print("x,\n y, \nz")

x = y = z = 5 +10
print(f"x:{x},\n y:{y},\nz:{z}")

#Take two numbers as input from the user, assign 
# to `a` and `b`, and print their average.

a = float(input("Enter number"))
b = float(input("Enter number"))
avg = (a + b) / 2
print(f"Average of the  {a} and  {b} is :{avg}")

## Q: Assign a string with special characters like newline (`\n`) and tab (`\t`) to a variable.
# Print it and observe the effect.
msg = "Hello frds \n Good morning ..... \n\t My name is Rohini Kumbhar I am from Akluj."
print(msg)

#Q: Use `print(a, b, sep='-', end='!')` to customize print output.

a = "Rohini"
b ="kumbhar"
print(a, b, sep='-', end='!')

# Create two variables with the same value and print their 
# `id()` to check if they refer to the same object.

a = 100  #For small integers (typically between -5 and 256), 
b = 100  #Python uses object interning, so both variables point to
print(f"a = {a}, id(a) = {id(a)}") #the same memory address.
print(f"b = {b}, id(b) = {id(b)}")

a =600
b =600
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")