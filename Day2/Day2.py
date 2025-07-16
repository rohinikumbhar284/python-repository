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