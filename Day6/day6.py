
# # Print numbers from 1 to 5 5+1=6
# for i in range(1, 11):
#     print(i)
 
# for i in range (start,end)

# fruits = ["apple", "banana", "mango"] #list dtype
# for fruit in fruits:
#     print("I like", fruit)


# i = 1
# while i  <= 5:
#     print(i) #=1,2,3,4,5
#     i += 1  # Important! To avoid infinite loop


# password = ""
# while password != "python":
#     password = input("Enter the password: ")
# print("Correct password! Access granted.")


# Example: Stop the loop when we find the number 7
# print("Demonstrating break:")
# for num in range(1, 11):
#     if num == 7:
# #         print("Found 7! Stopping the loop.")
# #         break  # Exits the loop immediately
# #     print(num)
# # print("Loop finished.\n")

# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i)


# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i)


# for i in range(1, 11):
#     print(i)

# list(map(print, [1,2,3,4,5,6,7,8,9,10]))


# Example: Skip the number 5, continue with the rest
# print("Demonstrating continue:")
# for num in range(1, 8):
#     if num == 2:
#         print("Skipping number 2.")
#         continue  # Skips the rest of the code in this iteration
#     print(num)
# print("Loop finished.\n")


# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==4:
        
#         break
#     print(item)
    

# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==3:
#         print(item)
#         break


# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==3:
        
#         break
# print(item)


# Example: Placeholder - do nothing when number is 3
# print("Demonstrating pass:")
# for num in range(1, 6):
#     if num == 3:
#         pass  # Placeholder: code will be added later
#     print(num)
# print("Loop finished.\n")

# from dev.comfig import Secret_number

# secret_number=Secret_number
# print("welcome to the no.guessing game!")

# print("guess the no. between 1 to 50 ")
# print("you have only 5 attempt ,enter 0 to quit this game !")

# for attempt in range (1,6):
#     guess=int(input(f"attempt {attempt}: enter your guess:"))

#     if guess==0:
#         print("game stopped by pradeep")
#         break

#     if guess <0 :
#         print("not a valid guess as the no is negative no.")
#         continue
    
#     if guess ==secret_number :
#         print ("congrates ,you guessed it right ,pradeep")
#         break
 
#     elif guess >secret_number:
#         print("too high ! try again")

#     else:
#         print("too low ,try again !")

#     if attempt ==3 :
#         print("the secret no is even no.")
#         pass 

# else:
#     print("sorry ! your guess is wrong !")

# #====================== LOGIC BUILDING QUESTIONS ==============

# # --------------- For Loops ---------------
# # Print all prime numbers between 1 and 100 using a for loop.
# print("Prime numbers between 1 and 100:")
# for num in range(2, 101):  
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):  
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")
# #Write a program to print a multiplication table for a number entered by the user.
# num = int(input("Enter Number:"))
# print(f"Multiplication of {num}:")
# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")

# #Count and display how many vowels are in a given string using a for loop.
# var = input("Enter any string here:")
# vowel= 'aeiouAEIOU'
# count = 0
# for char in var:
#     if char in vowel:
#         count += 1
# print(f"Number or vowels in string are:{count}")

# #Print a pattern like this using a for loop:
# # *
# # **
# # ***
# # ****
# print("*****Pattern******")
# for i in range(1,5):
#     print("*" * i)
# ###  by using list 

# for var in [1,2,3,4] :
#     print("*" * var)

# # try more
# # ****
# # ***
# # **
# # *
# print("*****Pattern******")
# for i in range(4,0,-1):
#     print("*" * i)

# #try
# # ****
# # **
# print("*****Pattern******")
# for i in range(4,0,-2):
#     print("*" * i)
# # try
# # *****
# # ****
# # **
# print("*****Pattern******")
# print("Using by list ")
# for i in [5,4,2]:
#     print("*" * i)

# #Write a program to reverse a string without using slicing, only with a for loop.
# str =input("Enter here any string you like:")
# print(str [::-1]) ## here i use slicing and reserve sting 

# ## using for string reserve
# str = input("Enter here any string which you like:")
# reserved_test = ""
# for char in str:     
#     reserved_test = char + reserved_test 
# print("Reserve text is:",reserved_test) # output is inihiro

# str = input("Enter here any string which you like:")
# reserved_test = ""
# for char in str:     
#     reserved_test = char + reserved_test 
#     print("Reserve text is:",reserved_test)  # here this print stat repeted and display every 
# #single vahlue mean Reserve text is: 
# # Reserve text is:r
# # Reserve text is:or
# # Reserve text is:hor

# #Create a list of 10 numbers and print the sum of only even numbers using for loop and continue.
# # print("Number list")
# # for i in range(1,11):
# #      print (i)
# #      if i % 2 == 0:
# #          print(i)

# number =[1,2,3,4,5,6,7,8,9,10]
# even_list =0
# for num in number:
#     if num % 2 !=0:
#         continue # skip odd num  
#     even_list +=num
# print(f" The addition of even num is {even_list}")

# #### WITHOUT Using Continue
# a = [1,3,2,10,20,11,16,14,17,10,18]
# even_add =0
# for num in a:
#     if num % 2 ==0:
#         even_add += num
#     print(f"addition of even number:{even_add}") # output 0,0,2,12,32,32,48 it is in loop

# a = [1,3,2,10,20,11,16,14,17,10,18]
# even_add =0
# for num in a:
#     if num % 2 ==0:
#         even_add += num
# print(f"addition of even number:{even_add}")  # it display just all num 90

# #Generate the Fibonacci sequence up to the first 15 numbers using for loop.
# a,b= 0,1
# print("Fibonaccic sequence up to 15")
# for i in range(15):
#     print(a,end =" ")  # end =" " --> use replace the default new line with space ,so the next point saty on same line 
#     a,b = b , a + b

# #-------------- While Loops ---------------
# #Keep asking the user for input until they type "exit", then stop using a while loop.

# while True:
#     take =input(("Enter here something(if you enter exist you go out of ):"))
#     if take.lower() == "exit":
#         print("oops! you exist from here:")
#         break
#     else:
#         print(f"You entered: {take}")
# #Write a program to check if a number is an Armstrong number, using a while loop.
# num = int(input("Enter a number: "))
# original_num = num
# n = len(str(num))  # Count of digits
# sum_of_powers = 0
# while num > 0:
#     digit = num % 10
#     sum_of_powers += digit ** n
#     num //= 10    ##### check this logic agin
# if sum_of_powers == original_num:
#     print(f"{original_num} is an Armstrong number.")
# else:
#     print(f"{original_num} is not an Armstrong number.")


# #Find the factorial of a number using a while loop.

# num = int(input("Enter number:"))
# fact = 1
# i = 1
# while i <= num :
#     fact *= i
#     i +=1
# print(f"Factorial of {num} is {fact}")

#  #Use a while loop to keep dividing a number by 2 until it becomes less
#  #  than 1, and print the number of divisions.
# num = int(input("Enter a number:"))
# count =0
# while num >=1:
#     num /= 2
#     count +=1
# print(f"Number of division:{count}")
# #Write a program that keeps asking for a password until the correct 
# # password ("python123") is entered.
# password =""
# while password != "python123":
#     password =input("Enter the password")
# print("oo woow ! You enter correct password , you get access .")


# -------------- Using break, continue, pass ---------------
# Write a program to display numbers from 1 to 50, but stop the loop if the
#  number is divisible by both 3 and 7 using break.
# print("Number break when it is divisible by 3 and 7")
# for i in range(1,51):
#     if i % 3 == 0 and i % 7 == 0:
#         break 
#     print(i)
# #Print all numbers between 1 and 30, skipping those that are divisible by 
# # 4 using continue.
# print("Number skip when it is divisible by 4")
# for i in range(1,31):
#     if i % 4 == 0:
#         continue
#     print(i)

# #Write a program where pass is used inside a loop as a placeholder for a 
# # future feature (e.g., add a feature later when the number is negative).
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     elif num < 0:
#         pass
#     else:
#         print(f"You entered: {num}")
# # --------------- Combination of All Concepts ---------------

# # --------------- ATM Simulation ---------------
# # Start with an account balance (e.g., ₹5000).
# # Menu-driven using while loop:
# # Deposit money
# # Withdraw money
# # Check balance
# # Exit
# # Use break to exit, continue for invalid choices, and pass for a 
# # "loan feature coming soon".

balance = 5000
while True:
    print("-------ATM Machine ------")
    print("1.Deposite money")
    print("2.Withdraw money")
    print("3.Check balance")
    print("4.loan")
    print("5.Exist")

    choice = input("Enter your choice (1 to 5):")

    if choice == '1':
        amount=float(input("Enter your amount for deposite:"))
        if amount > 0:
            balance += amount
            print(f"{amount} deposite successefully , New balance:{balance}")
        else:
            print("Invalid amount.")
    elif choice == '2':
        amount =float(input("Enter amount to withdraw:"))
        if amount> balance :
            print("Insufficient balance?")
        else:
            balance -=amount
            print(f"Rs {amount} Withdraw successfully !, New balance{balance}")
    elif choice == '3':
        print(f"Your current balnce is Rs{balance}")
    elif choice == '4':
        pass 
        print("Loan future coming soon!")
    elif choice == '5':
        print("Thank you for using the ATM. Goodbye!")
        break
    else :
        print("Invalid choice. Please try again.")
        continue

# balance = 5000  # Starting balance

# while True:
#     print("\n--- Bank Menu ---")
#     print("1. Deposit Money")
#     print("2. Withdraw Money")
#     print("3. Check Balance")
#     print("4. Loan Feature (Coming Soon)")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         amount = float(input("Enter amount to deposit: ₹"))
#         if amount > 0:
#             balance = balance + amount
#             print(f"₹{amount} deposited. New balance: ₹{balance}")
#         else:
#             print("Invalid amount. Must be greater than zero.")

#     elif choice == '2':
#         amount = float(input("Enter amount to withdraw: ₹"))
#         if amount > balance:
#             print("Insufficient balance!")
#         elif amount <= 0:
#             print("Invalid amount. Must be greater than zero.")
#         else:
#             balance = balance - amount
#             print(f"₹{amount} withdrawn. New balance: ₹{balance}")

#     elif choice == '3':
#         print(f"Your current balance is: ₹{balance}")

#     elif choice == '4':
#         # Placeholder for future loan feature
#         print("Loan feature coming soon!")
#         pass  # TODO: Implement loan feature later

#     elif choice == '5':
#         print("Thank you for banking with us. Goodbye")
#         break  # Exit the loop and program

#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")
#         continue  # Ask the user again


    
    
# # --------------- Simple Quiz Game ---------------

# # Ask 5 multiple-choice questions.

# # For each wrong answer, print "Wrong! Try again." and continue to the next question.

# # If the user types "quit", break the game.

# # Use pass for a future "hint system".


# print("---------------Simple Quiz Game-------------")
# print("-------Multiple Choice Question------------")

# questions= [
#     { 
#         "question":"Who create python ? " ,
#       "option": ["a.Guido von Rossum" , "b.Dennis Ritchie","c.James Gosting","d.Non of these"],
#       "answer":"a"
#     },
#     { "question": "Python is s specialized language which deals in ",
#       "option": ["a. AI","b. ML","c.Deep learing ","d.All of the above"],
#       "answer":"d"
#     },
#     {
#         "question":"Python First version was relesed in which year?",
#         "option":["a.1190" ,"b.1991","c.1992","d.1993"],
#         "answer":"b"
#     },
#     {
#         "question": "Which os these not valid identifier?",
#         "option": ["a.1st","b.First","c.position1","d.Rank1"],
#         "answer":"a"
#     },
#     {
#          "question": "Which of these is valid identifier?",
#          "option": ["a.For" ,"b.If","c.Return" ,"d.Allof these"],
#          "answer":"d"
#     }
# ]
# score = 0

# for q in questions:
#     print("\n" + q["question"])
#     for opt in q["option"]:
#         print(opt)
    
#     while True:
#         user_input = input("Your answer (a/b/c/d or type 'quit' to exit): ").lower()
        
#         if user_input == "quit":
#             print("Exiting the quiz. Thank you for playing!")
#             break
        
#         if user_input == "hint":
#             # Future feature
#             pass
        
#         if user_input == q["answer"]:
#             print("Correct!")
#             score += 1
#             break
#         else:
#             print("Wrong! Try again.")
    
#     if user_input == "quit":
#         break

# print(f"\nYour final score is: {score}/{len(questions)}")

# #--------------- Pattern Printing Tool ---------------
# # User chooses from 3 patterns (triangle, square, pyramid).
# # Use for loops to generate the patterns.
# # Use continue to skip invalid sizes and break if the user chooses "exit".
# # Tringle pattern logic 
# row = int(input("Enter number of row for pattern:"))
# for i in range(1,row + 1):
#     print("*" * i)
# #Square pattern logic
# row = int(input("Enter number for row for pattern: "))
# for i in range(row):
#     print("*" * row)

# #pyramide pattern
# rows = int(input("Enter the number of rows for the pyramid: "))
# for i in range(1, rows + 1):
#     spaces = rows - i
#     stars = 2 * i - 1
#     print(" " * spaces + "*" * stars)

# print("--------------Pattern Matching-----------------")
# while True:
#     pattern = input("Enter the pattern type (triangle, square, pyramid) or 'exit' to quit:").lower()
#     if pattern == "exit":
#         print("You have exited from the pattern tool.")
#         break
#     size = int(input("Enter the size for pattern which you like:"))
#     if size <= 0:
#         print("Invalid size ! plz enter positive size.")
#         continue
#     if pattern == "triangle":
#         print("Right angle Triangle pattern.")
#         for i in range(1,size + 1):
#             print("*" * i)
#     elif pattern == "square":
#         print("Square pattern")
#         for i in range(size ):
#             print("*" * size)
#     elif pattern == "pyramid": 

#         print("pyramid pattern.")
#         for i in range(1,size + 1):
#             print(" " * (size - i) + "*" * (2 * i - 1))
#     else:
#         print("Invalid pattern choice!")
#         continue
#     print()

# #--------------- Library Book Borrowing System ---------------
# # A list of available books is displayed.
# # User can borrow, return, or view books.
# # break to exit the system.
# # continue when the user enters a wrong book name.
# # pass for a "late fee calculator" feature to be added later.
# print("--------------- Library Book Borrowing System ---------------")

# books = ["The Alchemist", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "Harry Potter"]
# borrowed_books = []

# while True:
#     print("\nAvailable actions: borrow, return, view, late fee, exit")
#     action = input("Enter your action: ").lower()

#     if action == "exit":
#         print("Exiting the Library System. Goodbye!")
#         break

#     elif action == "borrow":
#         print("\nAvailable books:")
#         for book in books:
#             print("-", book)
#         book_name = input("Enter the name of the book to borrow: ")

#         if book_name in books:
#             books.remove(book_name)
#             borrowed_books.append(book_name)
#             print(f"You have borrowed '{book_name}'.")
#         else:
#             print("Book not found or already borrowed.")
#             continue  

#     elif action == "return":
#         book_name = input("Enter the name of the book to return: ")
#         if book_name in borrowed_books:
#             borrowed_books.remove(book_name)
#             books.append(book_name)
#             print(f"Thank you for returning '{book_name}'.")
#         else:
#             print("This book was not borrowed from our library.")
#             continue

#     elif action == "view":
#         print("\nBooks currently available:")
#         for book in books:
#             print("-", book)

#     elif action == "late fee":
#         pass

#     else:
#         print("Invalid action. Please choose again.")
#         continue







