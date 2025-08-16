# my_set = {1, 2, 3, 4,4,2,1}
# print(my_set)

#typecasting 
# From a list using set()
# numbers = set([1, 2, 3, 3, 4])
# print(numbers)  # Output: {1, 2, 3, 4}


# # Empty set
# empty_set = set()
# print(type(empty_set))

#flow of excution for for Loop
# colors = {"red", "green", "blue"}
# for i in colors:
#     if i == "green":
#         print("colur is matching")
        
#     else:
#         print("invalid colour ")

   


# animals = {"dog", "cat"}

# # Add single
# animals.add("lion")
# print(animals)

# Add multiple
# animals.update(["tiger", "elephant"])
# print(animals)

# # Remove
# animals.remove("cat")
# print(animals)

# Discard
# animals.discard("cow")  # No error if 'cow' not present
# print(animals)
# # Pop
# item = animals.pop()
# print("Removed:", item)

# # Clear
# animals.clear()
# print(animals)  # Output: set()Think of a set like a "collection of friends in a WhatsApp group" — no friend can be added twice.


# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)   # Union → {1, 2, 3, 4, 5}
# print(A & B)   # Intersection → {3}
# print(A - B)   # Difference → {1, 2}
# print(A ^ B)   # Symmetric Difference → {1, 2, 4, 5}

#-------------------------------------------------------------------------------------------------------
#-------------------------------------HOMEWORK QUESTIONS
# Create a set of 5 fruits and print it.
# fruits ={"Apple","Orange","Mange","Banana","Grapes"}
# print("My favoirate fruits:",fruits)
#-----------------------------------------------------
# Create a set of numbers and show that duplicates are automatically removed.
# number ={ 1,2,3,1,2,3,5,6,4}
# print("Duplicate remove from list:",number) # {1,2,3,4,5,6}
#-------------------------------------------------------
# Create an empty set and add 5 city names to it.
# cities = set()
# cities.add("Pune")
# cities.add("Mumbai")
# cities.add("Karad")
# cities.add("satara")
# cities.add("Sangli")
# print(cities)
#-------------------------------
# city = {}   # here it work like dictionary ,error- dict' object has no attribute 'add'
# city.add("pune")
# city.add("Mumbai")
# city.add("karad")
# print(city)
#-----------------
# city_add = {"pune"}
# city_add.add("karad")
# city_add.add("Mumbai")
# city_add .add("Solapur")
# city_add. add("Satara")
# print(city_add)
#------------------------------------------------------------
# Add two new colors to a set called colors.
# colors = {"Orange"}
# colors.add("Blue")
# colors.add("White")
# print(colors)
#-----------------------------------------------------------
# Remove a fruit from a set using remove() method.
# fruits ={"Apple","Orange","Mange","Banana","Grapes"}
# fruits.remove("Orange")
# print(fruits)
#-----------------------------------------------------
# Remove an animal from a set using discard() method (animal might not exist).
# Animal = {"dog","mouse","cat"}
# Animal.discard("got")
# print(Animal)
#----------------------------------------------------
# Use pop() on a set and print the removed element.
# name = {"Rohan","Rohit","Ajay","Priya"}
# remove_item = name.pop()   #Unlike lists, pop() on a set removes a random element (since sets are unordered).
# print("Removed item:",remove_item)
# print("set after remove any item:",name)
#----------------------------------------------
# Clear all items from a set and print it.
# name = {"Rohan","Rohit","Ajay","Priya"}
# name.clear()
# print(name)
#---------------------------------------------------
# Create a set of subjects and check if "Math" is present in it.
# subject = {"English","Marathi","Hindi","Math"}
# if "Math" in subject:
#     print("Math in subject")
# else:
#     print("Not math in subject")
#-------------Another way
# subjects = {"Math", "Science", "English", "History", "Geography"}
# if {"Math"}.issubset(subjects):
#     print("Math is present in the set.")
# else:
#     print("Math is not present in the set.")
#---------------heack multiple value in set
# subject = {"English","Marathi","Hindi","Math"}
# if "Math" in subject and "Hindi" in subject:
#     print("Both Avilable.")
# else:
#     print("Not Avilable")
#-----------------------------------------------------------------
# Find the length of a set containing different countries.
# country = {"India","Ingland","USA","Uk","Canda","Brazil"}
# cheack_len = len(country)
# print("The length of country set:",cheack_len)
#-------------------------------------------
# country = {"India","Ingland","USA","Uk","Canda","Brazil"}
# print(len(country))
#-------------------------------------------------------------------
# Create two sets of numbers and find their union.
# set1 ={1,2,3,6,9}
# set2 ={ 2,7,9,3}
# cheack_union = set1 | set2
# print("Union values from two set :",cheack_union)
#-----------------Another way
# set1 ={1,2,3,6,9}
# set2 ={ 2,7,9,3}
# cheack_union = set1.union(set2)
# print(cheack_union)
#---------------------------------------------------------------------
# Create two sets of numbers and find their intersection.
# set1 ={1,2,3,6,9}
# set2 ={ 2,7,9,3}
# cheack_inter = set1 & set2 
# print(cheack_inter)
#-----------------------
# set1 ={1,2,3,6,9}
# set2 ={ 2,7,9,3}
# cheack_inter = set1.intersection(set2) 
# print(cheack_inter)
#-------------------------------------------------------------------
# Create two sets of names and find the difference between them.
# name = {"Rohini","Akash","Ajay","Rahul"}
# name2 ={"Rohit","Ajay","Rohan"}
# set_difference = name - name2  
# print(set_difference)
# set_difference = name2 - name
# print(set_difference)
#------------------------------------------
# name = {"Rohini","Akash","Ajay","Rahul"}
# name2 ={"Rohit","Ajay","Rohan"}
# set_difference = name.difference(name2)  
# print(set_difference)
#--------------------------------------------------------------------
# Create two sets of numbers and find the symmetric difference.
# set1 ={1,2,4,8,44,7}
# set2 ={4,77,44,15,2,9}
# syma_set = set1.symmetric_difference(set2)
# print(syma_set)
#------------------------------------------------------------------
# Create two sets: odd_numbers and even_numbers. Find their union.
# even ={ 2,4,6,8,10}
# odd = {1,3,5,7,9}
# find_union= even.union(odd)
# print(find_union)
#------------------------------------------------------------------
# Create two sets of sports and check if they have any common sport.
# set1 = {"Cricket", "Football", "Tennis", "Hockey"}
# set2 = {"Basketball", "Tennis", "Volleyball", "Football"}
# common_sports = set1.intersection(set2)
# if common_sports:
#     print("Common sports:", common_sports)
# else:
#     print("No common sports found.")
#-----------------------------------------------------------------
# Given A = {1, 2, 3} and B = {1, 2, 3, 4, 5}, check if A is a subset of B.
# A = {1, 2, 3}
# B= {1, 2, 3, 4, 5}
# if A.issubset(B):
#     print("A is the subset of B.")
# else:
#     print("A i not subset of B.")
#----------------------------------------------------------------
# Given X = {2, 4, 6, 8} and Y = {4, 8}, check if Y is a subset of X.
# X = {2, 4, 6, 8}
# Y = {4, 8}
# if  Y.issubset(X):
#     print("Y is the subset of X.")
# else:
#     print("Y is not subset of x")
#-------------------
# X = {2, 4, 6, 8}
# Y = {4, 8}
# if  X.issubset(Y):
#     print("X is the subset of Y.")
# else:
#     print("X is not subset of Y")
#---------------------------------------------------------------------
# Find if two sets are disjoint (no common elements).
# set1 = {1,2,3}
# set2 ={4,5,6}
# if set1.isdisjoint(set2):  #check any comman element 
#     print("The set1 is disjoint(no comman element)")
# else:
#     print("The set not disjoint ")
#-------------------------
# set1 = {1,2,3}
# set2 ={4,5,6}
# if not set1.intersection(set2):
#     print("The set1 is disjoint(no comman element)")
# else:
#     print("The set not disjoint ")
#-------------------------------------------------------------------
# Create two sets and update the first one with the union of both.
# set1 = {1,3,5}
# set2 = {2,4,6}
# set1.update(set2)
# print("Update set",set1)
#------------------------
# set1 = {1,3,5}
# set2 = {2,4,6}
# set1= set1.union(set2)  # update set1 using union
# print("Update set",set1)
#-----------------------------------------------------------------
# Loop through a set of animals and print each one.
# animal ={"cat","dog","deer","got"}
# for name in animal: 
#     if name in animal: 
#         print(name,end =" ")
#------------
# animal ={"cat","dog","deer","got"}
# for name in animal: 
#     print(name, end = " ")
#----------------------------------------------------------------------
# Count how many elements in a set are greater than 50.
# number ={ 10,20,55,50,66,76,45,67}
# count = 0 
# for num in number:
#     if num >= 50:
#         count += 1
# print("Total number greater than 50 is:",count)
#------------------------------------------------------------------------
# From a set of words, print only those words which have more than 5 letters.
# name = { "rohini","Priya","Raj","tina","Rajat"}
# for word in name:
#     if len(word) >= 5:
#         print(word)
#------------------------------------------------------------------------
# Merge two sets using a loop (without using union method).
# set1 = {"rohini", 25}
# set2 ={"Arati",44}
# for name in set2:
#     set1.add(name )
#     print(set1)
#------------------------------------------------------
# From a set of marks, print only marks greater than or equal to 90.
# marks ={ 65,88,90,99,91,65,88,92}
# for num in marks:
#     if num >= 90:
#         print("Marks greater than 90: ",num)
#--------------------------------------------------------
# Find common elements between two sets without using intersection method.
# set1 = {1,2,4,6,7,8,9}
# set2 = {4,6,12,7,9,1}
# comman = set() 
# for item in set1:
#     if item in set2:
#         comman.add(item)
# print("comman item in set1 and set2",comman)
#------------------------------------------------------
# Print the largest number from a set of integers.
# set1 ={12,33,55,78,90,45,97}
# max_number =max(set1)
# print("Max value in set1 is :",max_number)
# #---------------
# set1 ={12,33,55,78,90,45,97}
# largest = None 
# for num in set1:
#     if largest is None or num > largest:
#         largest = num 
# print("Largest value in set1 is:",largest)
#-------------------------------------------------------
# Print the smallest number from a set of integers.
# set1 ={12,33,55,78,90,45,97}
# smallest = min(set1)
# print(smallest)
#-------------------
# set1 ={12,33,55,78,90,45,97}
# smallest = None 
# for num in set1:
#     if smallest is None or num < smallest:
#         smallest = num 
# print("Smallest value in set: ",smallest)
#3-------------------------------------------------------
# From a set of strings, find the longest string.
# name = {"Rohini","Sandeep","rkkumbhar", "Rohinikumbhar", "sanjay kum"}
# longest = None 
# for num in name:
#     if longest is None or len(num) > len(longest):
#         longest = num
# print(longest)
#---------------------------------------------------------------
# From a set of strings, find the shortest string.
# name = {"Rohini","Sandeep","rkkumbhar", "Rohinikumbhar", "sanjay kum"}
# smallest = None 
# for num in name:
#     if smallest  is None or len(num) < len(smallest):
#         smallest = num
# print(smallest)
#-------------------------------------------------------------
# Convert a list of numbers with duplicates into a set (remove duplicates).
# list1 = [1,2,3,4,3,5,6,3,6,8]
# convert_set = set([1,2,3,4,3,5,6,3,6,8])
# print("list Convert into list:",convert_set)
#-------------------------------------------------------------
# Convert a tuple of fruits into a set.
# fruits = ("Mange","Orange","Apple","Graps")
# convert_set = set(("Mange","Orange","Apple","Graps"))
# print("Tuple convert into set:",convert_set)
#-------------------------------------------------------------
# Given a list of tuples with student marks, find all unique tuples using a set.
# mark = [(88,66),(80,90),(88,66),(66,56),(80,90)]
# uniqe_tuple = set(mark)
# print("Unique Tuple:",uniqe_tuple)
#---------------------------------------------------------------
# Convert a set of numbers into a list and sort it.
# set1 = {1,5,3,9,5,3,11,10}
# cov_list = list(set1)
# cov_list.sort()
# print("set convert into list:",cov_list)
# print("List sorted",cov_list)
#--------------------------------------------------------------
# Convert a set of numbers into a tuple and print it.
# set1 = {11,33,77,12,64,32}
# con_tuple = tuple(set1)
# print("Convert set into tuple: ",con_tuple)
#-------------------------------------------------------------
# Create a set from a list of city names and count unique cities.
# cities = ["karad","mumbai","satara","karad","pune","satara","solapur"]
# con_set = set(cities)
# count = 0
# for num in con_set:
#     count += 1
# print("Unique cities are: ", count)
#------------------------------------------------------------------
# Create a set from a tuple of roll numbers and check if a roll number exists.
# tuple1 = (12,33,15,17,20,22,25)
# con_set = set(tuple1)
# roll_num = 20
# if roll_num in con_set :
#     print(f"{roll_num} exists in set")
# else: 
#     print(f"{roll_num} not exist in set")
#-----------------------------------------------------------------------
# Given a list of names, remove duplicates using set and print sorted names.
# names = ["Rohini","Kalpna","Neha","Sakshi","Abhi","Abhay","Rohini"]
# remove_dup = set(names)
# name_sort = sorted(remove_dup)
# print("Remove duplicate :",remove_dup)
# print("Sorted name:",name_sort)
#----------------------------------------------------------------------
# Store seating arrangements (tuples) in a list, remove duplicates using set.
# setting = (110,112,104,102,116,107,112,110,118)
# con_list = list(setting)
# con_set = set(con_list)
# print("Convert into liat :",con_list)
# print("Remove duplicate:",con_set)
#----------------------------------------------------------------
# Given a list of tuples with cricket scores, find the unique score combinations.
# score =(160,147,133,187,166,143,160,147)
# unique_score = set(score)
# print("unnique score combination:",unique_score)
#------------------------------------------------------------------------------------------
