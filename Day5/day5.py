


# print("WELCOME TO THE ELECTION BOARD OF MAHARASHTRA ")

# age=age = int(input("Enter your age: "))

# if age <18 :
#     print("USER NOT VALID TO VOTE ")

# elif age >50 :
#     print("USER NOT VALID TO VOTE ")

# else:
#     print("USER IS VALID TO VOTE ")


# marks=int(input("Enter your Marks: "))

# if marks>=90:
#     print("grade A")

# elif marks>=75 :
#     print("grade B")

# elif marks>=50:
#     print("grade C")

# else:
#     print("fail")



from dev.config import Password
# print("welcome to the magic show ")

# guess=int(input("guess a number between 1 to 10:"))

# if guess == secret_number:
#     print("you guessed it right")
# else:
#     print("you guessed it wrong")

password=int(input("enter your password"))
if password ==Password:
    print("access granted")
else:
    print("access denied")

#Even or Odd: Ask the user for a number and check if it is even or odd.

num =int(input("Enter the number:"))
if num % 2 == 0 :
    print(f"This {num} is even number.")
else:
    print(f"This {num} is odd number.")

#Positive, Negative, or Zero: Take a number and check whether it is positive,
#  negative, or zero.

Num = int(input("Enter the number"))
if Num > 0 :
   print("This number is positive.")
elif Num < 0:
    print("This is Negative number.")
else:
    print("This is zero.")

#Voting Eligibility: Ask user's age and tell if they are eligible to vote (age >= 18).
Age = int (input("Enter the Age :"))
if Age >=18 :
    print("You are eligible for votting.")
else:
    print("You are not eligible for votting.")

#. Greatest of Two Numbers: Input two numbers and print which one is greater or 
# if they are equal.
num1 = int(input("Enter  first Number :"))
num2 =int(input("Enter Second Number:"))
least =num1 < num2
grtest = num1 > num2
if least :
    print(f"{num1} is least than {num2}")
elif grtest:
    print(f"{num1} is gretest than {num2}")
else :
    print(f"{num1} is equal to {num2}")
#-------------------------
num1 = int(input("Enter  first Number :"))
num2 =int(input("Enter Second Number:"))
if num1 < num2 :
    print(f"{num1} is smaller than {num2}")
elif num1 > num2 :
    print(f"{num1} is gretest than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#Pass or Fail: Ask marks out of 100. Print Pass if marks >= 40, else Fail.

Marks = int(input("Enter your marks:"))
if Marks >= 40 :
    print("You are Pass")
else:
    print("You are fail")

#6. Simple Login Check: Ask username and password. If username='admin' and password='1234',
username =input("Enter UserName:")
password =input("Enter your password:")
if username == "admin" and password == "1234" :
    print("You are login successfully")
else:
    print("Invalid login")

#7. Leap Year Checker: Input a year and check if it is a leap year.
year =int(input("Enter year:"))
if year % 4 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

#8. Ticket Price Calculator: Age <5: free, 5-12: Rs 50, >12: Rs 100.
Age = int(input("Enter  your age:"))
if Age < 5:
    print("Free")
elif Age > 12:
    print("Rs 100")
else:
    print("Rs 50")

#. Character Case Checker: Check if a character is uppercase, lowercase, digit, or special
#character.

var = input("Enter the value:")
if var.isupper():
    print(f"The {Var} is in Upppercase")
elif var.islower():
    print(f"The {var} is in lower case. ")
elif var.isdigit():
    print(f" The {var} is digit")
else:
    print(f"The{var} is speical character")

#10. Number Guessing Game: Secret number = 7. Ask user to guess and check.

from Dev.config import number_guess 
a =int(input("Enter the any number:"))
if a == number_guess :     # number_guess= 7
    print("Geuss correct.")  # it gake guess number from impert word number_guess
else:
    print("opps! wrong.")
#--------------------
from Dev.config import number_guess 
Number_guess=int(input("Enter the any number:"))
if Number_guess == Number_guess :     # case censitive
    print("Geuss correct.")  #it take guess Number_guess not number_guess
else:
    print("opps! wrong.")

# #1. Electricity Bill: Units <=50: Rs 2/unit; 51-150: Rs 3/unit; above 150: Rs 5/unit.
# unit = input("Enter the number ")
unit = int(input("Enter the number of units: "))
if unit <= 50:
    bill = unit * 2
elif unit <= 150:
    bill = (50 * 2) + (unit - 50) * 3
else:
    bill = (50 * 2) + (100 * 3) + (unit - 150) * 5
print(f"Total bill: ₹{bill}")


#12. Discount & GST: Apply 10% discount and then add 18% GST to original price.
price =float(input("Enter value :"))
discount_price =price -(price * 0.10)
Final_price =discount_price + (price * 0.18)
print(f"Original Price: Rs {price}")
print(f"Price after 10% discount: Rs {discount_price:.2f}")
print(f"Final Price after adding 18% GST: Rs {Final_price:.2f}")

#13. Second Largest: Find second largest among three numbers.
num1 =int(input(" Enter First number:"))
num2 = int(input("Enter second number:"))
num3 =int(input("Enter third number:"))
if (num1 > num3 and num1 < num2 ) or (num1 > num2 and num1 < num3):
    print(f" {num1}")
elif (num2 > num1 and num2 < num3) or (num2 <num1 and num2> num3):
    print(f"{num2}")
else:
    prinr(f"{num3}")


#14. BMI Calculator: BMI = weight/(height^2). Classify as Underweight (<18.5), 
# Normal (18.5-24.9), Overweight (>=25).
weight = float(input("Enter your weight (in kg):"))
height =float(input("Enter your height(in meter):"))
BMI = weight / height ** 2
if BMI < 18.5 :
    result = "Underweight"
elif BMI > 25:
    result ="Normalweight"
else:
    result ="Overweight"
print(f"Your BMI is {BMI:.2f}. result: {result}")
#15. Grade Calculator: Average marks of 5 subjects: A >=90, B >=75, C >=50, Fail <50.
marks = [] 
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)
average = sum(marks) / 5
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'
print(f"Average Marks = {average:.2f}")
print(f"Grade = {grade}")

#16.ATM Simulation: Ask balance and amount. Deduct only if balance 
# is sufficient. 

balance = float(input("Enter your account balance: "))
amount = float(input("Enter the amount to withdraw: "))
if amount <= balance:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: Rs {balance:.2f}")
else:
    print("Insufficient balance! Transaction failed.")
#17. Triangle Checker: Check if three sides form a valid triangle. If valid, print type: Equilateral,
#Isosceles, or Scalene.
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is a valid triangle.")
    if a == b == c:
        print("Type: Equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")


#18. Rock-Paper-Scissors: User vs computer. Decide winner.
import random
choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif user_choice in choices:
    print("Computer wins!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")

#9. Movie Ticket: Ask age and time. Apply 20% discount if student (<18).
age =int(input("Enter your age:"))
time =input("Enter your movie timing:")
ticket_price =float(input("Enter your ticket price:"))
discoun_of = 0.2*ticket_price
final_amount =  ticket_price - discoun_of
if age <18 :
    print( f"As you are a student (age < 18), you get a 20% discount.")
    print(f"Final ticket price: ₹{final_amount:.2f}")
else:
    print(f"No discount applied. Ticket price: ₹{ticket_price:.2f}")

print(f"Show time: {time}")

#20. Traffic Signal: Ask color. Green: Go, Red: Stop, Yellow: Wait.

colors= input("Enter trafic signal colors:").lower()
if colors == "green":
    print("Go !")
elif colors =="red" :
    print("Stop !")
else:
    print("Wait!")