
# empty_tuple = ()
# print(empty_tuple)
# empty_tuple2 = tuple()
# print(empty_tuple2)
# print(type(empty_tuple2))


# lst=[1,2,3,4,5]
# tup=tuple[1,2,3,4,5]
# print(type(tup))
# print(type(lst))

# tup=(1,2,3,4)
# l1=list(tup)
# print(type(l1))



# fruits = ("apple", "banana", "cherry")

# print(fruits[-1])  # Output: apple

# print(fruits[2])  # Output: cherry

# print(fruits[-1]) # Output: cherry (counting from the end)



# votes = ("yes", "no", "yes", "yes")

# yes_votes = votes.count("yes")
# print(yes_votes)
# no_votes = votes.count("no")
# print(no_votes)

# pets = ["dog", "cat", "fish", "cat",10,22,"fish"]
# cat_index = pets.index("fish")
# print(cat_index)

# colors = ("red", "green", "blue", "green")
# green_index = colors.index("green")
# print(green_index) # Output: 1


# coordinates = (10, 20)

# x, y = coordinates

# print(x) # Output: 10

# print(y) # Output: 20

# clas= ("sanket","pradeep","rohini")
# a,b,c=clas
# print(a)
# print(b)
# print(c)


# personal_info = ("John", 30)

# location = ("New York", "USA")

# full_profile = personal_info + location
# print(full_profile)


# short_tuple = (12)
# short_tuple = [12]
# long_tuple = short_tuple * 3
# print(long_tuple)


# weekdays = ["Monday", "Tuesday", "Wednesday"]
# weekdays = ("Monday", "Tuesday", "Wednesday")
# print("Monday" in weekdays) # Output: True

# print("Sunday" in weekdays) # Output: False



# # Nested Tuples:
# nested = ((1, 2), (3, 4))
# print(nested[1][0])  # 2


# ✈️ Flight Seat Bookings - List, Tuple, and Set Example (Beginner Friendly)

# Step 1: Data (List of Tuples - each tuple = fixed row seating)
# bookings = [
#     ("Amit", "Ravi", "Priya"),   # Row 1
#     ("Sita", "Rahul", "Neha"),   # Row 2
#     ("Amit", "Ravi", "Priya"),   # Row 3 (duplicate of Row 1)
#     ("Vijay", "Meena", "Arun")   # Row 4
# ]

# # Step 2: Show all bookings (LIST allows duplicates)
# print("📋 All Seat Bookings (List Format):")
# row_number = 1
# for row in bookings:
#     print("Row", row_number, ":", row)
#     row_number += 1

# print("-" * 40)

# # Step 3: Convert List → Set to find UNIQUE bookings
# unique_bookings = set(bookings)

# print("✅ Unique Seat Arrangements (Set Format):")
# for row in unique_bookings:
#     print(row)

# print("-" * 40)

# # Step 4: Count unique arrangements
# print("Total Unique Arrangements:", len(unique_bookings))

# print("-" * 40)

# # Step 5: Search for a passenger in the bookings
# search_name = input("🔍 Enter a passenger name to search: ").strip()

# found_rows = []
# row_number = 1
# for row in bookings:
#     if search_name in row:
#         found_rows.append(row_number)
#     row_number += 1

# if found_rows:
#     print(f"🎯 {search_name} is seated in Row(s):", found_rows)
# else:
#     print(f"❌ {search_name} is not found in any booking.")
#----------------------------Questions homework----------------
# Create an empty tuple and print its type.
# empt_tuple =()
# print(type(empt_tuple))
#----------------------------------------------------
# Create a tuple with numbers 1 to 5 and print it.
# number =(1,2,3,4,5)
# print(number)
#------------------------------------------------------
# Create a tuple with different data types (integer, string, boolean, float).
# tuple_with_diff =(12,"rohini," "True", 44.5)
# print(tuple_with_diff)
#------------------------------------------------------
# Create a tuple without using parentheses and print it.
# ex_tuple = 20,10,30,40,25
# print("Tuple",ex_tuple)
# print("type",type(ex_tuple))
#-------------------------------------------------------
# Create a tuple with a single element and show its type.
# my_tuple =("rohini") 
# print(type(my_tuple)) # str
# my_tuple = (20)
# print(type(my_tuple)) # int
#---------------------------------------------------
# tCreate a tuple from a list [1, 2, 3] using the tuple() funcion.
# list1 = [1, 2, 3]
# list2 =tuple(list1)
# print(list2)
# print(type(list2))
#-------------------------------------------------------
# Create a tuple from the string "Python" and print it.
# text = "python"
# my_tuple = tuple(text)
# print("tuple",my_tuple)
# print(type(my_tuple))
#----------------------------------------------------
# Access the 3rd element of a tuple (10, 20, 30, 40, 50).
# my_tuple =(10, 20, 30, 40, 50)
# list2 = my_tuple[2]
# print("Third element in tuple:",list2)
#------------------------------------------------------
# Access the last element of a tuple (5, 10, 15, 20).
# my_tuple =(5, 10, 15, 20)
# last_ele = my_tuple[-1]
# print("last element in tuple:",last_ele)
#--------------------------------------------------------
# Create a tuple (1, 2, 3, 1, 4, 1) and count how many times 1 appears.
# my_tuple = (1, 2, 3, 1, 4, 1)
# count_one = my_tuple.count(1)
# print("Count one appearnce: ",count_one)
#-----------------------------------------------------
# Find the index of 50 in (10, 20, 30, 40, 50).
# my_tuple = (10, 20, 30, 40, 50)
# index_of = my_tuple.index(50)
# print("Index of 50 is:",index_of )
#----------------------------------------------------
# Try to modify a tuple (1, 2, 3) by changing its first element. What happens?
# tuple1 = (1,2,3)
# tuple1[0] =20 
# print(tuple1) #error
# Concatenate (1, 2, 3) and (4, 5, 6) and print the result.
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print("concatenate tuple1 and tuple2:",tuple3)
#-----------------------------------------------------------
# Repeat the tuple (10, 20) three times using the * operator.
# tuple_ex =(10,20)
# repeat = tuple_ex * 3
# print(repeat)
#-------------------------------------------------------
# Check if 30 is in (10, 20, 30, 40).
# tuple1 = (10, 20, 30, 40)
# print(30 in tuple1)
# #-----------------------
# my_tuple = (10, 20, 30, 40)
# if 30 in my_tuple:
#     print("30 is in the tuple")
# else:
#     print("30 is not in the tuple")
# Unpack (100, 200, 300) into three variables and print them.
# tuple_ex = (100, 200, 300)
# x,y,z = tuple_ex
# print("x:", x)
# print(":y", y)
# print("z:",z)
#------------------------------------------------------------
# Swap the values of two variables using tuple unpacking.
# tuple1 = (20,30)
# a,b = tuple1
# print("orignal a value:",a)
# print("orignal b value:",b)
# a,b = b,a  # value swapping
# print("after value swapping of a:",a)
# print("After value swapping of b:", b)
#-------------------------------------------------------------
# Create a nested tuple ((1, 2), (3, 4)) and print the second element of the first tuple.
# nested_tuple =((1, 2), (3, 4))
# # print(nested_tuple[0][2])  # second 2 take - error -tuple index outof range
# print(nested_tuple[0][1])
#------------------------------------------------------------
# Create a tuple (1, 2, 3) and convert it into a list.
# tuple1 = (1, 2, 3)
# convert_into_list = list[tuple1]
# print(convert_into_list)
#----------------------------------------------------------
# Iterate over (10, 20, 30, 40) and print each element.
# tuple1 =(10,20,30,40)
# for num in tuple1:
#     print(num)
#-------------------------------------------------------
# Iterate over (5, 10, 15) and print only even numbers.
# tuple1 = (5,10,15)
# for num in tuple1:
#     if num % 2 == 0:
#         print(num)
#-------------------------------------------------------
# Find the length of (1, 2, 3, 4, 5).
# tuple1 =(1,2,3,4,5)
# find_len = len(tuple1)
# print("Length of tuple is :", find_len)
#----------------------------------------------------------
# Write a program to check if a tuple is empty.
# tuple1 =(1)   # work as int , error int has no len 
# if len(tuple1) <= 0:
#     print("Tuple is empty..")
# else:
#     print("Tuple not empty..")
    #---------------------------
# tuple1 =(1,2)   # work as tuple
# if len(tuple1) <= 0:
#     print("Tuple is empty..")
# else:
#     print("Tuple not empty..")
#------------------------------------------------------
# Reverse (10, 20, 30, 40) using slicing.
# tuple1 = (10, 20, 30, 40)
# reverse_tuple = tuple1[::1]  # [::1]-10,20,30,40,  [:1]-10,[1] -20,[10:]- 20,30,40
# print("Tuple reversed: ", reverse_tuple)
#-----------------------------------------------------------
# Create a tuple (1, 2, 3, 4, 5) and get elements at even indexes only.
# tuple1 =(1,2,3,4,5)
# even_index = tuple(tuple1[i] for i in range(len(tuple1)) if i % 2 == 0)
# print(even_index)
#----------------------
# tuple1 =(1,2,3,4,5)
# even_index = tuple1[0::2]
# print(even_index)
#---------------------------------------------------------------
# Create a tuple (10, 20, 30, 40, 50) and get elements from index 1 to 4.
# tuple1 = (10, 20, 30, 40, 50)
# get_index = tuple1[1:4]
# print(get_index)
#-------------------------------------------------------------
# Create a tuple (10, 20, 30) and check if all elements are greater than 5.
# tuple1 = (10,20,30)
# for i in range(len(tuple1)):
#     if tuple1[i] >= 5:
#         print("All element in tuple are greater than 5.")
#     else:
#         print("Not grater than 5")  # display o/p repetedly 
#----------------------------
# tuple1 = (10, 20, 30)
# all_greater = True   # assume all are greater
# for i in range(len(tuple1)):
#     if tuple1[i] < 5:   # check each element
#         all_greater = False
#         break
# if all_greater:
#     print("All elements in tuple are greater than 5.")
# else:
#     print("Not all elements are greater than 5.")
#------------------------------------------
# tuple1 = (10, 20, 30)
# if all( i > 5 for i in tuple1):
#     print("All element are greater than 5.")
# else:
#     print("All element are small ")
#--------------------------------------------------------------
# Create a tuple (5, 10, 15, 20) and calculate the sum of all elements.
# tuple1 =(5, 10, 15, 20)
# total = 0
# for i in tuple1:
#     total += i
# print("sum of all element in tuple: ",total)
#-------------------------------------------------------------------
# Create a tuple (1, 2, 3, 4) and print elements in reverse order using a loop.
# numbers = (1, 2, 3, 4)
# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i])
#---------------------------
# tuple1 = (1,2,3,4)
# for i in reversed(tuple1):
#     print(i , end = " ")
#--------------------------------------------------------------------
# Store the coordinates (27.1751, 78.0421) in a tuple and print them in “Latitude: X, Longitude: Y” format.
# coordinates = (27.1751, 78.0421)
# x ,y = coordinates
# print("Latitude: ",x)
# print("Longitude: ",y)
#-----------------------------------------------------------------
# Store RGB values for red, green, and blue in tuples and print them.
# red =( 255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# print("Red" ,red)
# print("Green", green)
# print("Blue",blue)
#------------------
# color = [("Red",(255,0,0)),
#          ("Green",(0,255,0)),
#          ("Blue",(0,0,255))]
# for name ,rgb in color:
#     print(f"{name}, {rgb}")
#----------------------------------------------------------------
# Create a tuple containing the names of the days of the week. Print only weekends.
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print("Weekends:")
# print(days[5])
# print(days[6])  
# #----------------------------------------------------------
# Store student details (Name, Age, Grade) in a tuple and print them in a formatted way.
# student = ("Rohini", 26, "Bgarde" )
# print("Student information.")
# print(f"Student name:  {student[0]}")
# print(f"Student age : {student[1]}")
# print(f"Student Grade : {student[2]}")
#-----------------------------------------------------------
# Create a tuple containing multiple lists and modify one of the lists inside it.
# tuple1 =(["Rohini", 25],["Rohan",27,"karad"], ["Rohit","karad"])
# print("Orignal tuple:",tuple1)
# tuple1[0].append("karad")
# tuple1[2].insert(1,29)
# print("After modify tuple is: ",tuple1 )
#------------------------------------------------------------
# Create a tuple (1, 2, 3) and another tuple (4, 5, 6) — merge them without using +.
# tuple1 =(1,2,3)
# tuple2 =(4,5,6)
# merge_tuple = tuple1 + tuple2
# print("Tuple merged:", merge_tuple)
#------------------------------------------------------------
# Write a program to check if two tuples have any elements in common.
# tuple1 = (1,2,3,4,5,7,9)
# tuple2 =(4,6,8,9,5,7)
# comman = set(tuple1) & set(tuple2)
# if comman:
#     print("comman element:",comman)
# else:
#     print("no comman")
#--------------------------------------------------------------
# Write a program to convert a tuple of strings into a single concatenated string.
# single = ("Rohini","kumbhar","from","karad")
# to_concate = " ".join(single)
# print("string concatenated: ",to_concate)
#------------------------------------------------------
# Write a program to find the maximum and minimum value from (5, 8, 2, 9, 1).
# tuple1= (5, 8, 2, 9, 1)
# min_find = min(tuple1)
# max_find = max(tuple1)
# print("Max value in tuple: ",max_find)
# print("Min value in tuple : ", min_find)
#----------------------------------------------------
# Write a program to count how many strings in a tuple start with the letter “A”.
# tuple1 = ("Abhi","Ajay","rohan","Aditi","Rohini","priya")
# count = 0
# for name in tuple1:
#     if name.startswith("A"):
#         count += 1
# print("Words start with A in tuple are: ",count) 
