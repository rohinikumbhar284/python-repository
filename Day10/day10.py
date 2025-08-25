# students = {
#     "Amit": 85,
#     "Sneha": 92,
#     "Ravi": 78,
#     'sanket':59,
#     'pradeep':59
# }


# students["sanket"]=59
# del students[59]
# print(students)
# print(students.values())
# print(students.values)
# print(students.keys())
# data governance ----> data security 


# suspects = {
#     "Ravi": {"place": "Market", "item": "Banana"},
#     "Sneha": {"place": "School", "item": "Book"},
#     "Amit": {"place": "Bank", "item": "Gold Coin"},
#     "Priya": {"place": "Park", "item": "Ball"},
#     "Karan": {"place": "Cinema", "item": "Ticket"}
# }


# print ("welcome in the team of detective Rohini ")

# for name,details in suspects.items():
#     if details ['place']=="Bank" and details['item']=="Gold Coin" :
# #         print("the thief is :" , name, "!!!")



# suspects = [
#     ["Ravi", "Market", "Banana"],
#     ["Sneha", "School", "Book"],
#     ["Amit", "Bank", "Gold Coin"],
#     ["Priya", "Park", "Ball"],
#     ["Karan", "Cinema", "Ticket"]
# ]

# print("Welcome to the team of detective Rohini!")

# for suspect in suspects:
#     name, place, item = suspect
# #     if place == "Bank" and item == "Gold Coin":
# #         print("The thief is:", name, "!!!")
# #         break



# names = ["Ravi", "Sneha", "Amit", "Priya", "Karan"]
# places = ["Market", "School", "Bank", "Park", "Cinema"]
# items = ["Banana", "Book", "Gold Coin", "Ball", "Ticket"]

# print("Welcome to the team of detective Rohini!")

# for name, place, item in zip(names, places, items):
#     # if place == "Bank" and item == "Gold Coin":
#     #     print("The thief is:", name, "!!!")
#     #     break
#     print(names, places, items)

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# zipped_list = zip(names, ages)

# # To see the result, you need to convert the zip object to a list
# print(list(zipped_list))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
#---------------------------------------------------------Homework --------------------------------------------


# Create a dictionary of 3 fruits and their colors. Print it.
# fruits ={
#     "Mango"  : "Orange" ,
#     "Banana" : "Yellow" ,
#     "Appple" : "Res "
# }

# print( fruits)
# print(fruits.keys())
# print(fruits.values())  # give value of keys
# print(fruits.values)    # Give referencing address
#------------------------------------------------------------------------
# Create a dictionary of 3 countries and their capitals. Print only the capitals.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
#---------------------------------------------------------
# Add a new country-capital pair to the dictionary.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
# country["Japan"] = "tokyo"
# print("add the country ", country)
#------------------------------------------------------------
# Update the capital of an existing country.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
# country["Japan"] = "ABC"
# print("Update  the country ", country)
#-------------------------------------------------------------------------
# Delete one country from the dictionary.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
# del country["USA"]
# print(country)
#------------------------------------------------------------
# Print only the keys of a dictionary.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
# print("Only keys of dictionary:", country.keys())
#--------------------------------------------------------------
# Print only the values of a dictionary.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# print(country)
# print("Only values of dictionary:", country.values())
#-------------------------------------------------------------
# Check if "India" is present as a key in your dictionary.
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# if "India" in country:
#     print("The key India is avilable in dict.")
# else:
#     print("The key india not avilable in dict.")
#----------------------------- Another way ---------------------------------
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# if country.get("India") is not None:
#     print("The key India is avilable in dict.")
# else:
#     print("The key india not avilable in dict.")
#------------------------------
# country =  {
#     "India" : "New Delhi",
#     "USA" :  "Washington",
#     "France:" : "Paris"
# }
# if "India"in country.keys():
#     print("The key India is avilable in dict.")
# else:
#     print("The key india not avilable in dict.")
#-------------------------------------------------------------------------------
# Create a dictionary of your 3 friends and their ages. Print the age of one friend.
# friends ={
#     "Ajay" :  28,
#     "Nehe" :  21,
#     "Sneha" : 24
# }
# print("Age of Ajay: ", friends["Ajay"])
#---------------------------------------------------------------------
# Create an empty dictionary and add 3 key-value pairs one by one.
# emp_dict ={}
# emp_dict["Nehe"] = "karad"
# emp_dict["Snehe"] = "Mumbai"
# emp_dict["tina"] = "Pune"
# print("key and value in dict: ", emp_dict)
#---------------------------------------------------------
# Write a program to count how many times each letter appears in the word "banana".
# word ="banana"
# for letter in set(word):
#     print(letter ,":" , word.count(letter))
#---------------------------
# from collections import Counter

# word = "banana"
# count = Counter(word)
# print(count)
#------------------------------
# word = "banana"
# count_let ={}
# for letter in word:
#     if letter in count_let:
#         count_let[letter] += 1
#     else:
#         count_let[letter] = 1
# print(count_let)
#----------------------------------------------------------------
# Store 5 students’ names and their marks in a dictionary. Print the student who scored the highest marks.
# marks ={
#     "Nehe" : 87 ,
#     "Abhi " : 88,
#     "Priya" : 95,
#     "Ajay" : 89,
#     "Sneha" : 90
# }
# max_mark = max(marks.values())
# print(max_mark)
# #-------------------------
# marks ={
#     "Nehe" : 87 ,
#     "Abhi " : 88,
#     "Priya" : 95,
#     "Ajay" : 89,
#     "Sneha" : 90
# }
# topper = max(marks, key=marks.get)

# print("Topper is:", topper, "with marks", marks[topper])
#--------------------------------------
# students = {
#     "Ravi": 78,
#     "Sneha": 92,
#     "Amit": 85,
#     "Priya": 95,
#     "Kiran": 88
# }

# highest_marks = -1
# topper = ""

# for name, marks in students.items():
#     if marks > highest_marks:
#         highest_marks = marks
#         topper = name

# print("Topper is:", topper, "with marks", highest_marks)
#--------------------------------------------------------

# # Merge two dictionaries
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# d1.update(d2)
# print(d1)
#------------------------------

# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# merge = {**d1, **d2}
# print(merge)
#---------------------------------------------------------------------
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# merged = d1 | d2
# print(merged)
#-------------------------using zip()
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# merge = dict(zip(d1,d2))
# print(merge)   #--------------------------not  using zip 
#-------------------------------------------------------------
# Write a program to check if a dictionary is empty or not.
# emp_dict ={}
# if not emp_dict:
#     print("Dictionary is empty.")
# else:
#     print("Dictionary is not empty.")
#-----------------------------
# emp_dict = {}
# if len(emp_dict) == 0:
#     print("Dictionary is empty.")
# else:
#     print("Dictionary is not empty.")
#---------------------------------
# my_dict = {}
# if my_dict == {}:
#     print("Dictionary is empty")
# else:
#     print("Dictionary is not empty")
#----------------------------------------------------------------
# Given a dictionary:
# numbers = {1: "One", 2: "Two", 3: "Three"}
# Print the word for number 2.
# numbers = {1: "One", 2: "Two", 3: "Three"}
# print("The word for 2",numbers[2])
#---------------------------------------------------------------------
#  Write a program to create a dictionary of squares (keys 1 to 5, values = squares).
# square = {
#     1: '1',
#     2 : '4',
#     3 : '9',
#     4 : '16' ,
#     5 : '25'
# }
# print(square)
#---------------------------------------------------------------------------
#  Write a program to get the sum of all values in a dictionary.
# age_f ={
#     "amit" : 43,
#     "priya" : 33 ,
#     "nehe" : 23,
#     "rajat" : 28
# }
# sum_of = sum(age_f.values())
# print("The sum of all values in dict is :",sum_of)
#-----------------------
# age_f ={
#     "amit" : 43,
#     "priya" : 33 ,
#     "nehe" : 23,
#     "rajat" : 28
# }
# total = 0
# for value in age_f.values():
#     total += value
# print("sum of values in dict: ",total)
#---------------------------------------------------------------------
#  Write a program to find the key with the maximum value in a dictionary.
# age_f ={ 
#     "amit" : 43,
#     "priya" : 33 ,
#     "nehe" : 23,
#     "rajat" : 28
# }
# Findmax = max(age_f,key = age_f.get)
# print(Findmax) #####333333333333333333333333333333333333333333
#---------------------------------------------------------
#  Write a program to swap keys and values in a dictionary.
# age_f ={ 
#     "amit" : 43,
#     "priya" : 33 ,
#     "nehe" : 23,
#     "rajat" : 28
# }
# swapp = {v : k for k,v in age_f.items() }
# print(swapp)
#--------------------------
# age_f ={ 
#     "amit" : 43,
#     "priya" : 33 ,
#     "nehe" : 23,
#     "rajat" : 28
# }
# swapp = { }
# for k,v in age_f.items():
#     swapp[v] = k
# print(swapp)
#-----------------------------------------------------------------------
#  Write a program to check if two dictionaries are equal or not.
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 2, "a": 1}

# if d1 == d2:
#     print("Dictionaries are equal")
# else:
#     print("Dictionaries are not equal")
#-------------------------
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 2, "a": 1}
# if sorted(d1.items()) == sorted(d2.items()):
#     print("Dictionaries are equal")
# else:
#     print("Dictionaries are not equal")
#----------------------------------------------------------------------
# ----------------------------Part C – Nested & Practical (Q21–30)
# Create a nested dictionary of 3 employees with their name, age, and department. Print one employee’s department.
# emp = {
#     1:{"name" :"Amit","Age"  : 20 , "dept": "mec"},
#     2:{"name" :"Pooja","Age": 25 , "dept": "comp"},
#     3: {"name": "nehe" , "Age" :30 ,  "dept": "civil"}   
# }
# print("employee 2 department :",emp[2]["dept"])
#-----------------------------------------------------------
# Create a dictionary library with book titles as keys and authors as values. Print all book titles.
# library = {
#     "The Alchemist": "Paulo Coelho",
#     "1984": "George Orwell",
#     "Pride and Prejudice": "Jane Austen",
#     "To Kill a Mockingbird": "Harper Lee",
#     "The Great Gatsby": "F. Scott Fitzgerald"
# }

# print("Book Titles in the Library:")
# for title in library.keys():
#     print(title)
#-----------------------------------------------------------------
# Store your family members and their favorite food in a dictionary. Print the favorite food of your mom.
# my_family ={
#     "Me" : "Pizza",
#     "dad" : "Smosa",
#     "Mom" : "Pani poori",
#     "Brother" : "friuts"
# }
# print("My mom like :", my_family["Mom"])
#---------------------------------------------------------------
# Write a program to count the frequency of each word in a sentence.
# sentence = " my name is rohini. my brother is engineer"
# sentence = sentence.lower()
# words = sentence.split()
# count = {}
# for word in words :
#     count[word] = count.get(word,0) + 1
# print("Word Frequency:")
# for word, count1 in count.items():
#     print(f"{word}: {count1}")
#-------------------------------------------------------------------------------------
# Given a student dictionary with marks, calculate the average marks.
# marks = {
#     "Rohan" : 78,
#     "Abhi" : 88,
#     "Nehe" : 85,
#     "Priya" : 76
# }
# fin_avg = sum(marks.values()) / 4 
# print("The average of marks: ", fin_avg)

# #----------------------
# marks = {
#     "Rohan" : 78,
#     "Abhi" : 88,
#     "Nehe" : 85,
#     "Priya" : 76
# }
# total = sum(marks.values())
# count = len(marks)
# avg_of = total / count
# print("The sum of marks : ",total)
# print("Avg of marks :" , avg_of)
#-------------------------------------------------------------------
# Create a dictionary of 3 states and their cities (list of cities as values). Print all cities of one state.
# city_of = {
#     "maharashtra" : ["mumbai", "Karad","Solapur","akluj"],
#     "Karnataka": ["Bengaluru", "Mysuru", "Mangalore"],
#     "Gujarat": ["Ahmedabad", "Surat", "Vadodara"]
# }

# print("The cities in satate gujarat :" ,city_of["Gujarat"])
#-----------------------------------------------------------------------
# # Create a dictionary of 3 movies and their release years. Print movies released after 2010.
# movies = {
#     "Inception": 2010,
#     "Interstellar": 2014,
#     "Avengers: Endgame": 2019
# }
# print("Movies released after 2010:")

# for movie, year in movies.items():
#     if year > 2010:
#         print(f"{movie} ({year})")
#-------------------------------------------------------------
# Write a program to remove all duplicate values from a dictionary.

# Create a dictionary of fruits and prices. Print all fruits costing more than 50.
# fruits = {
#     "Apple" : 120 ,
#     "Banana" : 45 ,
#     "Mango" : 150,
#     "Orange" : 200
# }
# for fruit , price in fruits.items():
#     if price > 50 :
#         print(fruit, price)
#----------------------------------------------------------------
# Create a dictionary of rooms and treasures. Let the user choose a room and print the treasure.
# rooms = {
#     "Living Room": "Old Painting",
#     "Kitchen": "Golden Spoon",
#     "Bedroom": "Silver Necklace",
#     "Basement": "Ancient Coin"
# }

# room_choice = input("Choose a room (Living Room, Kitchen, Bedroom, Basement): ")
# if room_choice in rooms:
#     print(f"The treasure in the {room_choice} is: {rooms[room_choice]}")
# else:
#     print("No such room found!")
#------------------------------------------------------------------------------
# Build a dictionary of countries and capitals. Ask the user to type a country and print its capital.
# countries = {
#     "India": "New Delhi",
#     "USA": "Washington, D.C.",
#     "Japan": "Tokyo",
#     "France": "Paris",
#     "Brazil": "Brasília"
# }
# country_name = input("Enter a country name: ")
# if country_name in countries:
#     print(f"The capital of {country_name} is {countries[country_name]}")
# else:
#     print("Sorry, country not found in the list.")
#---------------------------------------------------------------
# Create a quiz dictionary with 3 questions and answers. Ask user to answer and give score.
# quiz = {
#     "What is the capital of France?": "Paris",
#     "What is 5 + 7?": "12",
#     "Who wrote 'Harry Potter'?": "J.K. Rowling"
# }
# score = 0  
# print("Welcome to the Quiz!\n")
# for question, answer in quiz.items():
#     user_answer = input(question + " ")
#     if user_answer.strip().lower() == answer.lower():  # case-insensitive check
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Wrong! The correct answer is {answer}\n")
# print(f"Your final score is {score}/{len(quiz)}")
#--------------------------------------------------------
# Store student roll numbers and names. Ask the user to enter a roll number → print the name.
# students = {
#     101: "Rohit",
#     102: "Sneha",
#     103: "Amit",
#     104: "Priya"
# }
# roll = int(input("Enter student roll number: "))
# if roll in students:
#     print(f"Student Name: {students[roll]}")
# else:
#     print("Roll number not found.")
#----------------------------------------------------------------
# Create a dictionary of English words and their Hindi meanings. Ask the user to translate a word.
# dictionary = {
#     "apple": "सेब",
#     "book": "किताब",
#     "water": "पानी",
#     "sun": "सूरज",
#     "moon": "चाँद"
# }
# word = input("Enter an English word to translate into Hindi: ").lower()
# if word in dictionary:
#     print(f"The Hindi meaning of '{word}' is: {dictionary[word]}")
# else:
#     print("Sorry, this word is not in the dictionary.")
#----------------------------------------------------------------
# Treasure Hunt: Store treasures in dictionary keys (Red Room, Blue Room, etc.). Let user guess the correct room.
# import random
# treasures = {
#     "Red Room": "Gold Coins",
#     "Blue Room": "Diamond",
#     "Green Room": "Silver Sword",
#     "Yellow Room": "Magic Potion"
# }
# treasure_room = random.choice(list(treasures.keys()))
# print("Welcome to the Treasure Hunt!")
# print("Rooms available:", ", ".join(treasures.keys()))
# guess = input("Guess the room that has the treasure: ")
# if guess == treasure_room:
#     print(f" Congratulations! You found the treasure: {treasures[treasure_room]}")
# else:
#     print(f" Wrong guess! The treasure was in {treasure_room} ({treasures[treasure_room]}).")
#---------------------------------------------------------------------------------------
# Create a dictionary of usernames and passwords. Ask user to login by checking dictionary.
# users = {
#     "rohit": "1234",
#     "sneha": "abcd",
#     "amit": "pass123",
#     "priya": "qwerty"
# }
# print("---- Login System ----")
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username in users and users[username] == password:
#     print("Login successful! Welcome,", username)
# else:
#     print("Invalid username or password!")
#-------------------------------------------------------------------------------
# Store 5 products and prices. Ask the user to enter product names → print total bill.
# products = {
#     "apple": 50,
#     "banana": 20,
#     "milk": 40,
#     "bread": 30,
#     "egg": 10
# }
# print("Available products and prices:")
# for item, price in products.items():
#     print(f"{item} - ₹{price}")
# total = 0
# # Ask user to enter items
# while True:
#     product = input("\nEnter product name to buy (or type 'done' to finish): ").lower()
    
#     if product == "done":
#         break
#     elif product in products:
#         qty = int(input(f"Enter quantity of {product}: "))
#         total += products[product] * qty
#     else:
#         print(" Product not available.")

# # Print total bill
# print("\n------ BILL ------")
# print(f"Total Amount = ₹{total}")
#---------------------------------------------------------------------
# Store cricket players and their scores. Ask the user to guess who scored the highest.
# players = {
#     "Virat Kohli": 85,
#     "Rohit Sharma": 102,
#     "MS Dhoni": 76,
#     "KL Rahul": 54,
#     "Hardik Pandya": 67
# }
# highest_player = max(players, key=players.get)
# highest_score = players[highest_player]

# print("Cricket Match Scores:")
# for name, score in players.items():
#     print(f"{name}: {score} runs")
# guess = input("\nWho do you think scored the highest? ")
# if guess.strip().lower() == highest_player.lower():
#     print(f" Correct! {highest_player} scored the highest with {highest_score} runs.")
# else:
#     print(f" Wrong! The highest scorer was {highest_player} with {highest_score} runs.")
#-----------------------------------------------------------------------
# Store suspects (name, place, item). Write code to find who is the thief (like detective puzzle).
# suspects = {
#     "Ravi": {"place": "Library", "item": "Book"},
#     "Sneha": {"place": "Kitchen", "item": "Knife"},
#     "Amit": {"place": "Garden", "item": "Wallet"},
#     "Priya": {"place": "Hall", "item": "Ring"}
# }
# clue_place = "Garden"
# clue_item = "Wallet"
# print("Detective Puzzle: Find the Thief!\n")
# print("Suspects List:")
# for name, details in suspects.items(): 
#     print(f"{name} was in the {details['place']} with a {details['item']}")  
# for name, details in suspects.items():  
#     if details["place"] == clue_place and details["item"] == clue_item: 
#         thief = name  
#         break
# guess = input("\nWho is the thief? ")
# if guess.strip().lower() == thief.lower():
#     print(f" Correct! The thief is {thief}.")
# else:
#     print(f" Wrong! The real thief is {thief}.")
#-------------------------------------------------------------------------------  