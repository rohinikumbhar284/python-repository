# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He couldn't see which way to go,
# If you did not twinkle so""");

# a="ashutosh"
# print(len(a))

# v="1234567890"
# print(len(v))


# print("sanaketsalunke") 
# sanaket salunke ---
# H  e   l   l    o
# 0  1   2   3    4

# b = "Hello, World!"
# print(b[:9])

# b = "Hello, World!"
# print(b[0:2:9])



# a="ashutosh"
# print(a.upper()) 

# a="ASHUTOSH"
# print(a.lower())


a = " Hello, World! "
# print(a)
print(a.strip()) # returns "Hello, World!"


# Slicing Strings
# Extract the first 5 characters from the string 
# "HelloWorld".
a = "HelloWorld"
print(a[0:5])

#Get every second character from "pythonprogramming".
a = "pythonprogramming"
text =(a[::2])
print(text)


#Reverse the string "DataEngineer".
a ="DataEngineer"
text =(a[::-1])  #start:stop:step ,step -1 mean reverse
print(text)

#Slice "machinelearning" to get "learn".
a ="machinelearning"
print(a[7:])

#replace()
#Replace all occurrences of "apple" with "orange" in
#  "apple apple banana".
a = "apple apple banana"
text =a.replace("apple","orange")
print(text)

#Replace only the first "is" with "was" in 
# "This is easy, is it not?".
a ="This is easy, is it not?"
text = a.replace("is" "was",1)
print(text)

# upper() and lower()
# Convert "welcome To Python" to all uppercase.

a = "welcome To Python" 
print(a.upper())
a ="HELLO EVERYONE"
print(a.lower())

# Concatenation
# Concatenate "Good" and "Morning" with a 
# space in between.
a ="Good"
b ="Morning"
result =a +" "+ b
print(result)

# Join three strings "Data", 
# "Science", "Rocks" using +.

Result ="Data" +" "+ "Science" +" "+ "Rocks"
print(Result)

# format()
# Use .format() to insert a name 
# "Ashutosh" and age 28 into 
# "My name is {} and I am {} years old.".
name =input("Enter your name :")
age =input("Enter your age:")
print("My name is {} and I am {} years old".format(name ,age ))

#Format the float value 45.6789 to
#  show only 2 decimal places.
a:float = 45.6789
print("{:.2f}".format(a))

a = 45.6789
a = float(a)
print("{:.2f}".format(a))

#capitalize()
#Capitalize the first letter of 
# "hello world".

a = "hello world"
text =a.capitalize()
print(text)

# casefold()
# Compare two strings "Python" and
#  "PYTHON" for equality using .
# casefold().
str1= "python"
str2 ="PYTHON"
if str1.casefold() == str2.casefold():
    print("Strings are equal")
else:
    print("Strings are not equal")

#center()
#Center the word "Python" in a string 
# of length 20 using * as the fill character.
text =" python"
result =text.center(20,'*')
print(result)

# count()
# Count the number of occurrences of 
# "a" in "banana".
text ="banana"
result =text.count('a')
print(result)
#Count how many times "the" appears in
#  "The theater is near the theme park"
#  (case-insensitive).
text ="The theater is near the theme park"
count =text.lower().count('the')
print(count)

# endswith()
# Check if "programming.py" ends with ".py".
text ="programming.py"
result =text.endswith(".py")
print(result)

# Mixed
# Take the string "hello world":

text ="hello world"
print(text.upper())
#Replace "HELLO" with "HI",
text ="hello world"
result =text.replace("hello","HI")
print(result)

#Slice the last 5 characters.
text ="hello world"
result =text[-5:]
print(result)