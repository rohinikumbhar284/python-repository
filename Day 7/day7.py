
# lst =["pradeeep",10,True,12.88]
# print(lst)

# print(lst[4])


# fruits = ["apple", "banana", "cherry"]

# print(fruits[0]) 

# print(fruits[2])  

# print(fruits[-1])


# lst =["sugar","salt","dryfruits","tea"]
# print(lst)
# lst.append("milk ")
# print(lst)
# lst =["sugar","salt","dryfruits","tea"]
# lst.insert(2,"milk")
# # print(lst)
# lst1=lst
# # print(lst1)

# lst1.remove("milk ")
# print(lst1)

# a="milk"
# b="milk  "
# print(len(a))
# print(len(b))

# stack  == 10 book (last in first out )



# ------
# ----
# ---
# --
# -

# queue =first in first out 

# - - - - - - - ====(:'.')===


# lst =["sugar","salt","dryfruits","tea"]
# lst.pop(2)
# print(lst)
# lst.insert(2,"dryfruits")
# print(lst)

# lst1 =["sugar","salt","dryfruits","tea"]
# lst2=[40,30,200,100]

# lst2.extend(lst1)
# print(lst2)




# pets = ["dog", "cat", "fish", "cat",10,22,"fish"]

# cat_index = pets.index("fish")
# print(cat_index)



# original = ["apple", "banana"]

# copy_list = original.copy()

# copy_list.append("cherry")

# print(original) # Output: ['apple', 'banana']

# print(copy_list) # Output: ['apple', 'banana', 'cherry']


# original = ["apple", "banana"]

# copy_list = original

# copy_list.append("cherry")

# print(original) # Output: ['apple', 'banana']

# print(copy_list) # Output: ['apple', 'banana', 'cherry']

# lst =["sugar","salt","dryfruits","tea"]
# # lst.clear() === all item

# # lst.remove("sugar") === perticular value 

# del lst[0:2]

# print(lst)

# ---------------------- Moderate Questions (1-50)
# -------------------------Basic Operations & Indexing
# 1.Create a list of your 5 favorite fruits and print the list.
# lst_of_Fruits =["Apple","Banana","graps","Mango","Watermeleon"]
# print(lst_of_Fruits)
#-----------------------------------------------------------
# 2.Print the third fruit from your list.
# lst_of_Fruits =["Apple","Banana","grape","Mango","Watermeleon"]
# lst1= lst_of_Fruits[3]
# print(lst1)
#-----------
#print(lst_of_Fruits[3])
#-------------------------------------------------------------
# 3.Print the last fruit from your list using a negative index.
# lst_of_Fruits =["Apple","Banana","graps","Mango","Watermeleon"]
# print(lst_of_Fruits[-1])
#-------------------------------------------------------------------
#4. Change the second fruit in your list to "grape" and print the updated list.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# lst_of_Fruits.insert(2,"grapes")
# print(lst_of_Fruits)
#-----------------------------------------------------------
# 5. Add a new fruit "mango" to the end of your list.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# lst_of_Fruits.append("mango")
# print(lst_of_Fruits)
#-------------------------------------------------------
# Insert "kiwi" at the beginning of your list.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# lst_of_Fruits.insert(0,"kiwi")
# print(lst_of_Fruits)
#------------------------------------
# fruits = ["Apple", "Banana", "Orange", "Mango"]
# fruits = ["Kiwi"] + fruits
# print(fruits)
#6. Print the fruits from the second to the fourth position.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# lst1= lst_of_Fruits[2:4]
# print(lst1)
#------------------------------------------------------------
# 7. Print all fruits from the third position to the end.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# lst1= lst_of_Fruits[3:]
# print(lst1)
#------------------------------------------------------
# 8.Print the number of fruits in your list.
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# print("Number of fruits:", len(lst_of_Fruits))
#------------------------------------------------------------
# 9. Check if "apple" is in your list and print the result (True or False).
# lst_of_Fruits =["Apple","Banana","Orange","Mango","Watermeleon"]
# cheack_apple = "apple" in lst_of_Fruits
# print(cheack_apple) # ---- ans False bcoz case sensitive
# cheack_apple = "Apple" in lst_of_Fruits
# print(cheack_apple) # ----- True

#----------------- List Methods----------------
#10.  Create a list of numbers: [10, 20, 30, 40, 50]. Use append() to add 60.
# list_append = [10, 20, 30, 40, 50]
# print(list_append.append(60)) # ---- None wrong way
# lst1 = list_append.append(60)
# print(lst1) #----- none
# list_append.append(60)
# print(list_append)
#--------------------------------------------------------------
# 11. Use insert() to add 25 at index 2 of the number list.
# list_no  = [10, 20, 30, 40, 50]
# list_no.insert(2,25)
# print(list_no)
#--------------------------------------------------------
#12 Use remove() to remove 40 from the number list.
# list_no  = [10, 20, 30, 40, 50]
# list_no.remove(40)
# print(list_no)
#-------------------------------------------------------------------
# 13. Use pop() to remove the last number from the list and print the removed number.
# list_no  = [10, 20, 30, 40, 50]
# remove = list_no.pop()
# print("remove number", remove)
# print("list Updated: ",list_no)
#-----------------------------------------------------------
# 14.Use clear() to empty the list.
# list_no  = [10, 20, 30, 40, 50]
# list_no.clear()
# print(list_no)
#----------------------------------------------------------
# 15.Create a new list [1, 5, 2, 8, 3]. Use sort() to sort it in ascending order.
# list_sort =[1, 5, 2, 8, 3]
# list_sort.sort()
# print(list_sort) 
#-------------------------------------------------------
#16. Sort the list from the previous question in descending order.
# list_sort =[1, 5, 2, 8, 3]
# list_sort.sort(reverse= True)
# print(list_sort)
#--------------------------------------------------
# 17. Create a list of strings: ["A", "C", "B"]. Sort it alphabetically.
# list_str = ["A", "C", "B"]
# list_str.sort()
# print(list_str)
#---------------------------------------------------
# 18.Create a list: ["red", "green", "blue"]. Use reverse() to reverse the order.
# list_reverse = ["red", "green", "blue"]
# list_reverse.reverse()
# print(list_reverse)
#-----------------------------------------------------
# 19.Create a list with duplicates: [1, 2, 2, 3, 4, 2]. Use count() to find how many times 2 appears.
# lst=[1, 2, 2, 3, 4, 2]
# lst2 = lst.count(2)
# print("count appernce of 2: ",lst2)
#--------------------------------------------------------
#-------------------------- Combining Lists
# 20.Create two lists: list_a = [1, 2] and list_b = [3, 4]. Combine them using + and store in list_c.
# list_a = [1, 2]
# list_b = [3, 4]
# list_c = list_a + list_b
# print("List combined: ",list_c)
#---------------------------------------------------------
# 21.Create two lists: list_d = ["a", "b"] and list_e = ["c", "d"]. Use extend() to add list_e to list_d.
# list_d = ["a", "b"]
# list_e = ["c", "d"]
# list_d.extend(list_e)
# print(list_d)
#------------------------------------------------------------
# 22. What's the difference between append() and extend()? Give an example.
# boys =["Rohan","Rohit", "Rahul","Ajay"]
# # boys.append(["Rakesh","Raj"])  #Adds the entire object you give as one single element at the end of the list
# # print("List appended:",boys)
# boys.extend(["abhi","sandeeep"])
# print("after extend:",boys)  #Iterates over the object you give and adds each element separately to the list.
#----------------------------------------------------------
# 23.Create a list my_list = [1, 2, 3] and assign new_list = my_list. Modify new_list by adding 4. What does my_list look like? Why?
# my_list = [1, 2, 3]
# new_list = my_list
# new_list.append(4)
# print(new_list)
#--------------------------------------------------------
# 24. Create a true copy of my_list from the previous question using copy(). Modify the copy and observe the original.
# my_list = [1, 2, 3]
# new_list = my_list.copy()
# new_list.append(5)
# print("orignal list :",my_list)
# print("after copy list",new_list)
#-------------------------------------------------------------
# ------------------------------Loops & List Comprehension
# 25.Use a for loop to print each item in a list of colors.
# list_color =["Red","orange","Blue","Green"]
# for item in list_color:
#     print(item, end =" ")
#--------------------------------------------------------------
# 26.Use a for loop to print the square of each number in [1, 2, 3, 4].
# number_list= [1, 2, 3, 4]
# for num in number_list:
#      print(num ** 2 , end =" ")
#---------------------------------------------------------
# 27. Use a for loop to find the largest number in a list of numbers.
# find_gretest =[ 23,12,44,16,55,37,98]
# grtest_num = find_gretest[0]
# for i in find_gretest:
#     if i > grtest_num: # wrong ans check it agin
#         i = grtest_num
# print("Gretest number in list:", i)
#----------------------------------------------------------
# 28.Create a new list using list comprehension that contains the squares of numbers from [1, 2, 3, 4].
# numbers = [1, 2, 3, 4]
# squares = [num ** 2 for num in numbers]
# print(squares)
# Create a new list using list comprehension that contains only the even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# list1 =[1, 2, 3
#-----------------------------------------------------------------
# Problem Solving
# ---------------------Vowel Counter: Create a list of vowels ['a', 'e', 'i', 'o', 'u']. Ask the user to input a word, then use a loop to count how many vowels are in the word.
#  29. Reverse a String: Take a string (e.g., "Python") and use a list to reverse it.
# str = "python"
# str_list =list(str)
# reverse_str = str_list.reverse()
# reversed_text = ''.join(reverse_str) #----- error
# print(reversed_text)
#------------------------------------------------------------
# 30.Sum of a List: Write a program that calculates the sum of all numbers in a list.
# lst_no =[ 10,20,30,44,55,33,89]
# total =0 
# for i in lst_no:
#     total += i
# print("sum of list:",total)
#------------------------------------------------------------
# 31. Find the Smallest Number: Write a program to find the smallest number in a list without using the min() function.
# number = [12,43,6,33,19,2]
# small_no = number[0]
# for num in number:
#     if num < small_no:
#         small_no = num
# print("smallest number:",num)
#----------------------------------------------------------
# 32.Remove Duplicates: Given a list with duplicate numbers, create a new list that contains only the unique numbers.
# list1 = [12,33,54,11,7,12,33,6,55]
# remove_duplicate= []
# for num in list1:
#     if num not in remove_duplicate:
#         remove_duplicate.append(num)
# print(remove_duplicate)
#-------------------------------------------------------------
# 33. Tic-Tac-Toe Board: Create a list that represents a simple Tic-Tac-Toe board [['', '', ''], ['', '', ''], ['', '', '']]. Print the board.
# game_board= [['', '', ''],
#          ['', '', ''],
#          ['', '', '']]
# for row in game_board:
#     print(row)
#----------------------------------------------------------
# 34. Guess the Number Game: Create a list of 5 numbers. Ask the user to guess a number. Check if the guessed number is in the list and tell them if they are correct.

# list1 =[ 12,33,11,44,2]
# guess_number = 2
# if guess_number in list1:
#     print("you are correct guessing:")
# else :
#     print("Not correct guess.")

# 35. Split a Sentence: Take a sentence from the user and use the split() method to create a list of words. Print the list.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("List of words:", words)
#---------------------------------------------------------------
#  36.Join a List: Take a list of words and use the join() method to turn it back into a single sentence.
# list1= ["my", "name", "is", "rohini", "kumbher"]
# sentence = " ".join(list1)
# print(sentence)
#----------------------------------------------------------------
#37.  Factorial: Create a list to store the factorial of a given number.
# number = int(input("Enter number:"))
# list_of_fact =[]
# fact = 1
# for num  in range(1, number + 1):
#     fact *= num
#     list_of_fact.append(fact)

# print("Factorial steps:", list_of_fact)
# print("Final factorial of", number, "is", list_of_fact[-1])
# #------------------------------------------------------------
# 38. Palindrome Checker: Take a word from the user and check if it's a palindrome (reads the same forwards and backwards) by comparing the original list of characters with its reversed version.
# word = input("Enter word: ")
# cheack_list = list(word)
# if cheack_list == cheack_list[::-1]:
#     print("Palidrome")
# else:
#     print("Not palidrome")
#--------------------------------------------------------------
#  39. Nested List: Create a list that contains two other lists (e.g., [[1, 2], [3, 4]]). Access and print the number 4.
# nested_list =[[1, 2], [3, 4]]
# print(nested_list[1][1])
#--------------------------------------------------------------
# 40. Matrix Addition: Add two matrices (represented as nested lists) of the same size.
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# B = [[9, 8, 7],
#      [6, 5, 4],   #### not understand
#      [3, 2, 1]]
# # Result matrix
# result = []
# # Loop through rows
# for i in range(len(A)):
#     row = []
#     # Loop through columns
#     for j in range(len(A[0])):
#         row.append(A[i][j] + B[i][j])
#     result.append(row)
# # Print result
# for r in result:
#     print(r)
    #----------------------------------------------------------
# 41.Counting Words: Take a sentence and count how many times each word appears. Store the result in a list of lists (e.g., [['hello', 2], ['world', 1]]).
# sentence = "hello world hello python world hello"
# words = sentence.split()
# word_list = [] 
# for word in set(words):    # Loop through unique words
#     word_list.append([word, words.count(word)])
# print(word_list)
#---------------------------------------------------------
# 42 .Shopping List: Create an empty list called shopping_list. Ask the user to enter 3 items and add each to the list. Print the final list.
# shopping_list = []
# for i in range(3):
#     user = input("Enter items: ")
#     i +=1
#     shopping_list.append(user)
# print("shopping list: ",shopping_list)
#---------------------------------------------------------------
# 43.Filter a List: Create a function that takes a list of numbers and a threshold value, then returns a new list containing only the numbers greater than the threshold.
# def filter_list(numbers, threshold):
#     filtered = []
#     for num in numbers:
#         if num > threshold:
#             filtered.append(num)
#     return filtered
# nums = [10, 5, 20, 3, 15]
# result = filter_list(nums, 10)
# print("Filtered list:", result)
#------------------------------------------------------------
# 44. Slicing Challenge: Given data = ['A', 'B', 'C', 'D', 'E', 'F'], print a new list containing ['C', 'D'] using slicing.
# list1 = ['A', 'B', 'C', 'D', 'E', 'F']
# new_list = list1[2:4] 
# print(new_list)
#-------------------------------------------------------------
# 45. index() with try-except: Use try-except to gracefully handle the error that occurs when index() is called on an item not in the list.
# list1 = ['A', 'B', 'C', 'D']
# try:
#     to_find = list1.index('E')  # trying to find an element not in the list
#     print(f"Element found at index {to_find}")
# except ValueError:
#     print("Element not found in the list.")
#-----------------------------------------------------------
# 46.Removing Specific Items: Write a program that takes a list and a v.alue, then removes all occurrences of that value from the list.
# list1 =[1,4,2,88,5,3,1,7,5,2,9,7]
# value = input("Enter which number have  to remove:")
# while value in list1:
#     list1.remove(value)
# print(f"after removing {value}:", list1)  # not run
#---------------------------------------------------------------
#  47. List of Tuples: Create a list of tuples, where each tuple contains a name and an age, e.g., [('Alice', 30), ('Bob', 25)]. Print the name of the second person.
# list1 = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
# print(list1[1][0])
#---------------------------------------------------------------------
# ----------------------------🧠 Complex Questions (51-75)
# -------------------------Advanced List Operations & Logic
# 48. Find Second Largest: Write a program to find ond largest number in a list.the sec
# list1 = [10, 25, 5, 40, 25, 40]
# unique_list = list(set(list1))
# unique_list.sort(reverse=True)   # Sort the list in descending order
# if len(unique_list) >= 2:
#     second_largest = unique_list[1]
#     print("Second largest number is:", second_largest)
# else:
#     print("List does not have enough distinct elements.")
#---------------------------------------------------------------------
# 49.Rotate List: Write a function that takes a list and an integer k, then rotates the list to the right by k steps. For example, [1, 2, 3, 4, 5] with k=2 becomes [4, 5, 1, 2, 3].
# def rotate_list(lst, k):
#     n = len(lst)
#     k = k % n  # handle cases where k > n
#     return lst[-k:] + lst[:-k]
# data = [1, 2, 3, 4, 5]                     # not undestand
# rotated = rotate_list(data, 2)
# print(rotated)
#----------------------------------------------------------------------
# 50.Flatten a Nested List: Given a nested list like [[1, 2, [3]], 4, 5], write a program to flatten it into a single list [1, 2, 3, 4, 5].
# def flatten(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flatten(item))  # recursively flatten
#         else:
#             result.append(item)
#     return result

# # Example usage
# nested_list = [[1, 2, [3]], 4, 5]
# flat_list = flatten(nested_list)
# print(flat_list)
#---------------------------------------------------------------
# 51.Pascal's Triangle: Generate the first n rows of Pascal's triangle and store them as a nested list.

# 52.list Comprehension with If-Else: Create a list using list comprehension that contains "Even" or "Odd" for each number in a list of integers.
# numbers = [1, 2, 3, 4, 5, 6]
# list1  = ["Even" if num % 2 == 0 else "Odd" for num in numbers]   # List comprehension with if-else
# print(list1)
# # 53.Sublist Search: Given two lists, list_A and list_B, check if list_B is a sublist of list_A.
# def is_sublist(list_A, list_B):
#     len_A = len(list_A)
#     len_B = len(list_B)
    
#     if len_B == 0:  # empty list is always a sublist
#         return True
    
#     for i in range(len_A - len_B + 1):
#         if list_A[i:i+len_B] == list_B:
#             return True
#     return False
# list_A = [1, 2, 3, 4, 5]
# list_B = [3, 4]
# print(is_sublist(list_A, list_B))  # Output: True

# list_B2 = [2, 5]
# print(is_sublist(list_A, list_B2))  # Output: False
#--------------------------------------------------------------
# 54. Sudoku Checker: Given a 9x9 grid represented as a nested list, write a function that checks if it is a valid Sudoku board (without checking the 3x3 squares).

# 55. Prime Numbers: Create a program that generates a list of prime numbers up to a given limit using a list and loops.
# limit = 20
# primes = []

# for num in range(2, limit + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)

# print(primes)

# 56. Fibonacci Sequence: Generate the first n numbers of the Fibonacci sequence and store them in a list.
# number = 10
# fib = [0,1]
# for i in range(2,number + 1):
#     fib.append(fib[i -1] + fib[i-2])
#     print(fib)

# 57.Sieve of Eratosthenes: Implement the Sieve of Eratosthenes algorithm to find all prime numbers up to a specified integer.
# def sieve_of_eratosthenes(limit):
#     # Create a list of True values, index represents the number
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

#     for num in range(2, int(limit**0.5) + 1):
#         if is_prime[num]:
#             # Mark all multiples of num as not prime
#             for multiple in range(num*num, limit + 1, num):
#                 is_prime[multiple] = False
#     # Collect all numbers that remain True (prime)
#     primes = [i for i, prime in enumerate(is_prime) if prime]
#     return primes
# limit = 30
# prime_numbers = sieve_of_eratosthenes(limit)
# print(prime_numbers)
#  58.Matrix Transpose: Given a matrix represented by a nested list, create a new list that is the transpose of the original.
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose = []
# for i in range(len(matrix[0])):  # iterate over columns
#     row = []
#     for j in range(len(matrix)):  # iterate over rows
#         row.append(matrix[j][i])
#     transpose.append(row)
# print(transpose)
#----------------------------------------------
# # 59. Anagrams: Given a list of words, group them into anagrams (e.g., ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] becomes [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]).
# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# anagrams = {}
# for word in words:
#     key = ''.join(sorted(word))  # sort letters to get the key
#     if key in anagrams:
#         anagrams[key].append(word)
#     else:
#         anagrams[key] = [word]
# Convert dictionary values to a list of lists
# grouped_anagrams = list(anagrams.values())
# print(grouped_anagrams)
# 60. Most Frequent Element: Find the element that appears most frequently in a list.
# from statistics import mode
# list1 = [33,44,12,33,66,33,11,22,44,33,12]
# count = 0
# print("Orignal list:",list1)
# res = mode(list1)
# count = list1.count(res)
# print("Element with highest frq is: ",res)
# print("Number of count :",count)
#----------------------------
# from collections import Counter
# list1 = [33,44,12,33,66,33,11,22,44,33,12]
# print("Orignal list:",list1)
# occurence_count = Counter(list1)
# res = occurence_count.most_common()
# print("Element with highest frq is: ",res)
#-----------------------------------
# from collections import Counter
# list1 = [33,44,12,33,66,33,11,22,44,33,12]
# print("Orignal list:",list1)
# occurence_count = Counter(list1)
# res = occurence_count.most_common(1)  # fetch actual value 
# print("Element with highest frq is: ",res)
#------------------------------------
# def most_frq():
#     list1 = [33,44,12,33,66,33,11,22,44,33,12]
#     counter = 0
#     num = list1[0]
#     for i in list1:
#         current_frq =list1.count(i)
#         if(current_frq > counter):
#             counter + current_frq
#             num = i
#             return num 
# print(most_frq())
#------------------------------------------------------------
#  61. Merge Sorted Lists: Given two sorted lists, merge them into a single sorted list. You cannot use the built-in sort() method on the final list.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]

# merged_list = []
# i, j = 0, 0

# # Compare elements from both lists and add the smaller one
# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         merged_list.append(list1[i])
#         i += 1
#     else:
#         merged_list.append(list2[j])
#         j += 1
# while i < len(list1):    # Add remaining elements (if any)
#     merged_list.append(list1[i])
#     i += 1
# else:
#         merged_list.append(list2[j])
#         j += 1
# while i < len(list1):     # Add remaining elements (if any)
#     merged_list.append(list1[i])
#     i += 1
# while j < len(list2):
#     merged_list.append(list2[j])
#     j += 1
# print("Merged sorted list:", merged_list)
#--------------------------------------------------------
#  62.Longest Common Subsequence: Find the length of the longest common subsequence between two lists.

# 63. Wave Array: Given an array, sort it into a "wave" form. An array arr[0...n-1] is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]...

# 64.List Intersection: Find the intersection of two lists (all elements that are in both lists).
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# intersection = [x for x in list1 if x in list2]
# print("Intersection:", intersection)
#-------------------------------------------------
# 65.List Union: Find the union of two lists (all unique elements from both lists).
# list1 = [12, 3, 2, 3, 4, 6, 8]
# list2 = [3, 4, 5, 6, 7]
# union_list = list(set(list1).union(list2))
# print("Union:", union_list)
#-------------------------
# list1 = [12, 3, 2, 3, 4, 6, 8]
# list2 = [3, 4, 5, 6, 7]
# # Using set to remove duplicates
# union_list = list(set(list1) | set(list2))
# print("Union:", union_list)
#------------------------
# list1 = [12, 3, 2, 3, 4, 6, 8]
# list2 = [3, 4, 5, 6, 7]

# union_list = []
# for item in list1 + list2:
#     if item not in union_list:
#         union_list.append(item)

# print("Union (order preserved):", union_list)
#------------------------------------------------------------ 
# 66.Cartesian Product: Given two lists, find their Cartesian product (a list of all possible pairs of elements from both lists).
# list1 =[1,2,3,4]
# list2 =[5,6,7]
# cartesian_product = [(x,y) for x in list1 for y in list2] 
# print(cartesian_product)
#---------------------------
# list1 =[1,2,3,4]
# list2 =[5,6,7]
# cartesian_product = []
# for x in list1:
#     for y in list2:
#         cartesian_product .append((x,y))
# print(cartesian_product)
#------------------------------------------------------
# 67.Spiral Matrix: Given a matrix (nested list), print all elements of the matrix in spiral order.

# 68.Remove Nth Node from End: Given a list, remove the nth element from the end of the list.
# def remove_nth_from_end(lst, n):
#     index_to_remove = len(lst) - n
#     if 0 <= index_to_remove < len(lst):
#         lst.pop(index_to_remove)
#     return lst
# my_list = [10, 20, 30, 40, 50]
# n = 2  # remove 2nd element from the end (40)
# print("Updated list:", remove_nth_from_end(my_list, n))
#-----------------------------------------------------------------
# 69.  Kadane's Algorithm: 
#----------------------------------------------
# Given a list of numbers, find the contiguous sub-array with the largest sum.

# Counting Inversions: In a list of numbers, an inversion is a pair of indices i, j such that i < j and a[i] > a[j]. Count the number of inversions.

# Permutations: Given a list of distinct numbers, return all possible permutations.

# Combination Sum: Given a list of distinct integers and a target integer, return a list of all unique combinations where the chosen numbers sum to the target.

