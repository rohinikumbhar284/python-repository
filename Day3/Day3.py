a="hi there !"
print(type(a))


# x = ("Hello World")		
# x = int(20)		
# x = float(20.5)	float	
# x = complex(1j)
# print(type(x))

# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))


# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))



# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))


# name = "Ashutosh"
# message = 'Hello'
# # print(type(name)) 

# print(f"{message} {name}")
# print("{} {}".format(message,name))
# print(message + name)


# z = 3 + 4j
# # print(type(z))  # Output: <class 'complex'>
# print(z.real)   # Output: 3.0
# print(z.imag)   # Output: 4.0


# is_valid ="True"
# is_empty = "False"
# print(type(is_valid))


# is_valid = True =1
# is_empty = False =0
# print(type(is_valid))  # Output: <class 'bool'>

# a=None
# print(type(a))


# x = 1    # int 
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# import random 

# print(random.randrange(100, 900))



# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3


# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2


# name = input("Enter your name: ")
# print("Hello,", name)


# age = int(input("Enter your age: "))
# print("You will be", age + 1, "next year.")


# salary = float(input("Enter your salary: "))
# print("Salary entered:", salary)


# x, y = input("Enter two numbers separated by space: ").split()
# x = int(x)
# y = float(y)
# print("Sum is:", x + y)

############# HW #######
# Section 1: Built-in Data Types (int, float, str, list, tuple,
#  dict, bool, set)
# Check Data Type:
# Ask the user to enter a value and print its data type. 
# Then determine if it’s a number or not.
a=20
print(type(a))

a=265888.2
print(type(a))

a = 1341e44    # e= float
print(type(a))

a= "Rohini"
print(type(a))

a = 2311j   # j=complex
print(type(a))

a = True 
b = False 
print(type(a),type(b)) 

Userdata = input("Enter any value")
print(f"Data type of number is" , type(Userdata))

#list - 
Stud_name=["Rohini","Tina","Megha"]
print(Stud_name[1]) 
Stud_name.append("Sita")
print(stud_name)

#tuple
collect =(10,200,125)
print(collect[0])

#Dict
Info_of={"Name":"Rohini", "Age": 25,"mark":78}
print(Info_of["Name"])


# Dynamic Type Detector:
# Take three inputs from the user and detect which one is integer, float, or string using type() and conditionals.

a= input("Enter value 1 :")
b = input("Enter value 2:")
c = input("Enter value 3:")

if a.isdigit():
    print(a, "is Integer")
else:
    try:
        float(a)
        print(a, "is Float")
    except ValueError:
        print(a, "is String")
if b.isdigit():
    print(b, "is Integer")
else:
    try:
         float(b)
         print(b, "is Float")
    except ValueError:
        print(b, "is String")
if c.isdigit():
    print(c, "is Integer")
else:
    try:
        float(c)
        print(c, "is Float")
    except ValueError:
        print(c, "is String")

# Section 2: Setting Specific Data Types / Type Conversion
# Type Conversion Challenge:
# Input 2 numbers as strings and add them as:

# Strings (concatenation)

# Integers (sum)

# Floats (sum)

val1 = input("Enter value")
val2 = input("Enter value")
string_con = val1 + val2
print("String Concat :",string_con)
int_con = int (val1) + int(val2) 
print("Integer addition :",  int_con)
float_add = float(val1) + float(val2)
print("Float addition :", float_add)

#print("string concatation :%s \n, Integer addition: %d \n, float Addition: %d" % (string_con,int_con,Folat_con) )

# Temperature Converter:
# Take temperature in Celsius from the user, convert to Fahrenheit and Kelvin using correct type conversions.

celcius =input("Enter your temprature :")
celcius =float(celcius)
fehrenheit = (celcius * 9 / 5 )+ 32 
kelvin = celcius + 273.15
print("Temperature in Fahrenheit:", fehrenheit)
print("Temperature in Kelvin:", kelvin)

# Year and Age Logic:
# Take user’s birth year (as string), convert to
#  integer, and calculate their age assuming the current year is 2025.

birth_d= input("Enter your birth year here :")
birth_d=int(birth_d)
c_year = 2025 
Age = c_year - birth_d
print(f"my birth year is {birth_d} and i am :{Age} years old")

# Add Two Numbers Function:
# Create a program that takes two floats and 
# returns their rounded sum. Use proper type hinting.

def Add_number(a:float ,b:float) -> float:
    return round(a+b,3)
num1 = float(input("Enter number"))
num2 = float(input("Enter numbar"))
print("Rounded sum of numbers :" ,Add_number (num1 ,num2))

# Area Calculator:
# Write a program to calculate the area of a rectangle. 
# Accept length and width as floats. Use -> float in return.

def area_calculation(a:float ,b:float) ->float:
    return round(a * b ,2)
length =float(input("Enter rectanle length :"))
width =float(input("Enter width of rectangle :"))
Area =area_calculation(length ,width)
print("The Area of rectangle is :",Area)

# Student Info Storage:
# Accept name, roll_no, and marks from the user. 
# Use type annotations and store in a dictionary.
name: str = input("Enter your name :")
roll_no: int = int(input("Enter your roll number:"))
mark :float= float(input("Enter your marks:"))
student_info: dict = {
    "Name": name,
    "Roll No": roll_no,
    "Marks": mark
}
print("Students information :",student_info)

# Formatted Receipt Generator:
# Accept item name (str), quantity (int), and price 
# (float). Calculate total and display the receipt
#  with formatted output.
item_name: str = input("Enter item name:") 
quentity: int =int(input("Enter the quentity of item:"))
price :float  =float(input("Enter the price of item :"))
total_of:float  = quentity * price 
print("\n=============Receipt=========")
print(f" Product Name:{item_name}")
print(f" Total Quentity:{quentity}")
print(f" price of item : Rs{price:.2f}")
print(f" Total Amount: Rs{total_of:.2f}")
print("=======================================")



