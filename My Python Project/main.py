# write a python program with two line messages
print('My name is fauzan mairah muhammad')
print('Practice makes man perfect')
# assign a radius
radius=20
#compute area
area= radius*radius*3.141
# display results
print('The area for the radius of circle', radius, 'is', area)
# compute the first area
#assign first radius
radius=1
#compute area
area=radius*radius*3
print('The are for the circle of radius', radius, 'is', area)
#compute for the secomd area
#assign first radius
radius= 2
#compute area
area= radius*radius*3
#display
print('The area for the circle of radius', radius,'is', area)
#assign 1 to variable x
x=1
#assign 4 to variable radius
radius=3


#Code the program that displays the following message on the screen in python.
#Enter the first number
#Enter secomd number
#Addition:60, multiplication:500

#assign first number to x
x = 10
#assign second number to y
y = 50
#compute sum
sum = x+y
#compute product
product = x*y 
print('The sum of x and y ', 'is',sum )
print('The product of x nad y', 'is', product)


#code the program that reads two sdes of rectangle and calculate its area
#assign value for length
length = 20
#assign value for width
width = 30
#compute area of a rectangle 
area = length * width
#display
print('The area of the rectangle', 'is', area)


#write a python program that calculate the results of mathematical operation
#(10*60)/9+56 + 70 - 2
#assign the mathematical operation to x
x = 10*60/9+56 + 70 -2 
print('10*60/9+56 + 70 -2', '=', x)




#Activity 3: Python as a powerful calculator
#Goal: Practice using all standard aithmetic operators in python: +(addition), -(subtraction), *(multiplication), /(division), //(floor division), %(modulus), and **(exponentiation).
#Task: Perfrom and display th results of several calculations to see how operator works.
#Instructions:
#1. Create two variables, num1 = 10 and num2 = 3
#2. Calculate the results for all seven operators list above
#3. Store result in each own variable 
#4. Print each result witha descriptive label


num1 = 10
num2 = 3

sum= num1 + num2
subtraction= num1 - num2
multiplication= num1 * num2
division= num1 / num2
floor_division= num1 // num2
modulus= num1 % num2
exponent= num1 ** num2

print(f"\n--- Calculations with {num1} and {num2}---")

print(f"{sum}")
print(f"{subtraction}")
print(f"{multiplication}")
print(f"{division}")
print(f"{floor_division}")
print(f"{modulus}")
print(f"{exponent}")

#---Activity 4---
#Goal: Translate a real-word problem into a single line of python code, using parenthesis () to ensure calculations happen in the correct order.
#The problem: You and your friend are at a bakery.You both decide to buy a spetial deal which includes one cupcake and one coffee.
#A single cupcake costs 3 dollars
#A single coffe costs 4 dollars
#You are buying this deal for 2 people
#After calculating the total, you add a five dollar tip
#Your task is to calculate the final bill in a single line of code.
#INSTRUCTIONS:
#First, figure out the cost of one deal (cupcake+coffee)
#Then, calculate the cost for two people
#Finally add the tip
# write one line of python code to solve this, assigning the result to final_bill. Use parenthesis() to control the calculation order.
#Print the result in a clear sentence.
#(3$ cupcake+4$ coffee)*2
#Let tip= 5$

final_bill= (3+4)*2+5
print(f"\nThe total cost of the two people, including the tip is, ${final_bill}\n")


#--- ACTIVITY 5: SIMPLE RECEPT CALCULATOR---
#GOAL: Combine everything you've learnt: print, input, data type conversion (int, float), arithmetic operations and formatted output
#TASK: Create a program that asks for the pric and quantity of an item, then calcualtes the subtotal, tax and final total.
#INSTRUCTIONS:
#1. Print a welcome message.
#2. Use input() to ask for the price of a single item and convert it to a float.
#3. Calculate the subtotal (price * quantity).
#4. Claculate the tax_amount by multiplying the subtotal by a tax rate of 8%.
#5. Calculate the total_cost by adding the subtotal and the tax_amount.
#6. Print a nicely formatted receipt

#This code is a calculator that combined everything learned so far 


print("\n--- Simple Receipt Calculator---")
#Print a simple welcome message
print("\n\t --- WELCOME TO FIS RESTAURANT---")
#Get user input and convert data types
item_price= float (input("What's the item price?"))

item_quantity= int (input("How many are you buying?"))



#Perfrom calculations
subtotal= item_price * item_quantity
tax_amount= subtotal * 0.08 # tax rate is 8%
total_cost= subtotal + tax_amount


#Print a nicely formatted receipt
print("\n--- Your Receipt---")
print("---------------------")
print(f"subtotal: \t${subtotal}")
print(f"tax_amount: \t${tax_amount}")
print(f"total_cost: \t${total_cost}")



#--- Home Work-----
#1. Read how much money you have then according to this, read two items' price that you buy from the market and decide you have enough money or not 
#2. Calculate the perimeter and area of the square from the console. If the computed area is less than or equal to 1000, print "small square", if it's larger than 1000, print "Large square".


#Read how much money you jave
available_cash= int(input("How much cash do you have on you?"))
#Read first item price
item_one_price= float(input("What's the first item price?"))
#Red scond item price
item_two_price= float(input("What's the second item price"))
#Read total cost
total_cost= item_one_price + item_two_price

#Read whether you have enough funds or not

if total_cost <= available_cash:
   print("Enough funds available")
else:
   print("Not enough funds")




#Ask user for the side of the square
side_of_the_square= int(input("What's the vlaue for one side of the square?"))

#Designate a formula fro calculating the perimeter of the circle
perimeter_of_the_square= 4 * side_of_the_square

#Designate a formula for the area of the circle
area_of_the_square= side_of_the_square ** 2

if area_of_the_square <= 1000:
   print("Small square")
if area_of_the_square > 1000:
   print("Large sqaure")


#Real life example
#Scenario 1: Getting a drivers license 
# . The condition (question): "Is your age greater than OR equal to 18?"
# . The Decision: If the answer is True, you can get a license. If it's false, you cannot.
#Scenario 2: Password Login
# . The condition (Question): "Is the password the user typed exactly equal to the password saved in the system?"
# . The Decision: If the answer is true, Log the user in. If it's false,show an "Incorrect Password" error.
#Scenario 3: Deciding ehat to wear
# . The condtion (Question): "Is the temperature less than 15 degrees Celcius?"
# . The Decision: If the answr is true, wear a jacket. If it's false you don't need a jacket.
#Scenario 4: Using a discount coupon
# . The Condition (Question): "Is the total amount in the shopping cart greater than or equal to 100? "
# . THe Decision: If the answer is true, apply the 10% discount. If it's false, do not apply the discount.
#Scenario 5: Graduation requirements
# . The Condition(Question): "Biomedical Engineering" or Molecular Biology and Genetics degree, is the student's status for the 'Computer Programming' course equal to 'passed'?
# . The Decision: If the answer is true, this specific graduation requirement is met. If it's false the student cannot graduate until they pass the course.


# Age is set directly in the code.
driving_age= 21
# Check gthe condtion
print(driving_age >= 18)

# Storing the correct password
saved_password= "Allah0249"
# Ask the user to enter their password
user_input= input("Type in password")
# Check whether it's correct or not 
print(saved_password == user_input)


#Set the temperature directly in the code
temperature = 13

#Check the condition
print(temperature < 15)

# Ask the user for their cart total 
# we use float to turn the users' input into a n umber 
cart_total = float(input("Enter your cart total"))

#Check condition
print(cart_total >= 100)


#Define the required status
required_status = "passed"
# Ask user fopr the current student status
# The input function captures text (a string) from the user 
course_status = input ("Enter the tudent's computer programming course status:")
# Check the condition
print(course_status == required_status)



# The AND Operator
# W e want to check if gthe number 15 is in the range (10, 20)
number = 15
# We check two condtions 
#1. Is the number > 10? (This is true)
#2. Is the number < 20? (This is false)

is_in_range = (number > 10) and (number < 20)
print("Is the number between 10 and 20?", is_in_range)

#The Or Operator
# You can enter the theme park for free if you're a child (under 5 years) OR if it's your birthday
# To get in free at least one condtion must be met
age = 30
it_is_your_birthday = True 

# Check the two conditions:
# Is age < 5? (false)
# It is your birthday == True? (True)
free_entry = (age < 5) and (it_is_your_birthday == True )
print("Do you qualify for free entry?", free_entry)


# Making Decisions: The "if" statement
# BASIC SYNTAX: The syntax is very important. iT uses a colon(:) and indentation (the space at the start of the line) to define what code "belongs" to the if statement.
some_condition_is_true= True
if some_condition_is_true:
   # This code block runs Only if the condition is True
   #Noice the colon:
   # Notic the INDENTATION (ususally 4 spaces)
   print("This code runs anyway because it is not indented.")


# From printing "True" to "Taking action"
#Scenario: Getting a driver's license

# two variables to be checked 
driving_age = 21 
passed_written_exam = True

# The if staement now checks both conditions 
# Both (driver_age >= 18) and (passed_written_exam == true)must be true


if (driving_age >= 18) and (passed_written_exam == True):
   print("Congratulations! You meet all requirememnts to get your license.")
else:
   # If either of the conditions is false or both are this else block will run
   print("You do nto meet all requirements yet. please review the rules.")


#==== Let's try a failure case---
drivers_age =17

passed_written_exam = True

if (drivers_age >= 17) and (passed_written_exam == True):
   print("\n(Test 2)Congratulations! You meet all requirements.")
else:
   # This 'else' will run because (driver_age >= 18) is false
   print("\n(Test 2)You do not meet the requirements. You're below 18")


   #scenario 2: Password login
   saved_password = "Allah0249@"
   user_input = input("Enter password:")

   #Check the condition 
   if saved_password == user_input:
      #the true block
      print("Login Suceccful. Welcome!")
   else:
      # The false block
      print("Incorrectt Password. Access Denied.")


#Now it's time to combine everything you have learned:
#• Getting user input (input())
#• Asking questions with Relational Operators (==, >, <=, etc.)
#• Making decisions (if, else)
#• Combining conditions (and, or)
#The Challenge:
#Write a program that tells a story or solves a problem based on user input.
#Your program MUST include:
#1. At least one input() questions.
#2. An if/else structure.
#3. At least one condition that uses the and operator.
#4. At least one condition that uses the or operator.



'''positive, negative or zero'''

number= 0
if number > 0:
   print('The number is positive')
elif number < 0:
   print('The number is negative.')
else:
   print('The number is zero')



'''Museum Ticket Pricing'''

age = int(input('Please enter your age:'))

#Let's check for invalid input
if age < 0:
   print('iInvalid age. Please enter a positive number.')

# Let's check categories from youngest to oldest
elif age <= 6:
   print('Ticket price: Free')
elif age <= 17:
   print('Ticket price: $10 (Student)')
elif age <= 64:
   print('Ticket price: 20$ (Adult)')
else:
   print('Ticket price: $15 ( Senior)')

#Nested if
# Cganging values to true or false
it_is_raining = True
it_is_windy = False

#Checking the main condition
if it_is_raining:
   print('It is raining outside')
   if it_is_windy:
      print('It is also windy. You need a strong umbrella')
   else:
      print('It is not windy. A regular umbrlla will be fine')
else:
   print('It is a clear day. No umbrella needed')


#Basic Login
#Correct username and password

saved_user_name = "admin"
saved_pass_word = "SecurePassword123"

#User input
user_username = input("Enter username:")
user_password = input('Enter password')

#check the username
if user_username == saved_user_name:
   if user_password == saved_pass_word:
      print('Access granted. Welcome, admin!')
   else:
      print('Incorrect password. Acess enied')
else:
   print('Incorrect username. Acess denied.')


'''Pattern Matching: The "match...case" statemnt
The "match...case" statement is a new, powerful, and clean alternative to long if-elif-else chains. It is
designed to check one varaible against many possible values or patterns.

It's very useful when you have one variable that could be one of many specific things.

Example: Your weekly plan
This program asks you for a day of the week and tells you the main "vibe" or activity for that day

Harder Way: The if-eleif-else chain Method
This method is functional, but it gets very long. Notice how we have to repeat the day "==" comparison for every single option'''


#Get the day from the user
#Title() makes the first letter capital (e.g "monday" -> "Monday")


day = input('Enter a day of the week:')

if day == "Monday":
   print('Back to school/ work....')
elif day == "Tuesday":
   print('The busiet day of the week.')
elif day == "Wednesday":
   print('Hump day! Halfway throuh')
elif day == "Thursday":
   print('Almost Friday!')
elif day == "Friday":
   print('The weekend is here!')
elif day == "Saturday":
   print('Time to relax and have fun')
elif day == "Sunday":
   print('Getting ready for the week...')
else:
   print(f"I dont know the day '{day}'.")

#Easier way: The match...case Method
#This is the modern and more readable way to handle this exact scenario. You state the variable you want to "match" (day) only once. Then, you simply list the "cases" it could be.

# Get the day from the user

day = input ('Enter a day of the week:')

match day:
 case "Monday":
   print('Back to work/school')
 case "Tuesday":
   print('The busiest day of the week.')
 case "Wednesday":
   print('Humpday! Halfway through.')
 case "Thursday":
   print('Almost friday')
 case "Friday":
   print('The weekend is here')
 case "Saturday":
   print('Time to relax and have fun')
 case "Sunday":
   print('Getting ready for the week')
 case _:
  #The underscore is the defalut case, just like 'else'
  print("f'I dont know the day '{day}'.")



  #Loops
  #While Loop
  #Summary: Repeats a block of code as long as conditions remain True.
  #Logic: Think of it like a countdown. It keeps working until a specific condition is met. If the condition becomes false, the loop stops.
  #Example: A countdown from 5 to 1

  count = 5

  while count > 0:
     print(f"Countdown: {count}")
     count -= 1 #Decreases count by 1

# for loop and range()
# Summary: Iterates through a sequence of numbers one by one
#Logic: The range (start, stop) function gnerates a sequence of numbers. It starts from the start number and goes up to (but does not include) the stop number
#Example: Printing numbers from 1 to 5.

# range (1,6) -> Stars at 1, ends before 6. It gives: 1,2,3,4,5.

for number in range (1,6):
   print(f"Number:{number}")



# break statement
# Summary: Immediately terminates (stops) the loop entirely when it is used
# Logic: It acts like an "Emergency stop" button. Even if the loop was supposd to run many more times, break kicks you out of the loop instantly.
#Example: Loop from 1 to 10, but stop if we find the number 7.


for i in range (1,11):
   if i == 7:
      print("found 7! stopping the loop.")
      break
   print(f"Processinf number:{i}")


#ontinue statement
#Summary: Skips the current iteration (step) and jumps to the netx one, without stopping the whole loop
#Logic: It means "skip this one,move to the next." It is useful for ignoring specific items.
#Example: Print numbers from 1 to 5, but skip nukmber 3


for i in range (1, 6):
    if i == 3:
       print("Skipping 3...")
       continue #skips the print below for this step only
    print(f"Number:{i}")



#Python Functions: rom Basic to Advanced
#Introduction: Key concepts
'''Before writing  a code, It is important to understand the structure of a function:
1. Definition(def): Tells Python we are creating a new function.
2. Parameters(Inputs): Variables inside the parenthesis (...) Data we send into the function.
3. Body: The indented code block where the logic happens.
4. Return ( Output): The final result sent back from the function.


When to Use Functions?
You don't need a function for everything. U se them in these situations:
1. The DRY Principle (DOn't repeat yourself):
   If you find yourself copy-pasting the same code block 2 or 3 times, stop! Turn that code into a 
   function and call it instead.
2. Orgnization (Decomposition):
   . Instead of writing 1000 lines of messy code, brka it down.
   . Example: get_user_data(), process_payment(), send_receipt(). It makes code easier to read.
3. Reusabilty:
   . Write th e code once, and use it in different parts if your program (or even in different projects).'''

#1. Function with Parameters and Logic (If-Else)
# This function takes a specific condiition and decides what to print based on logic.

def check_weather(status):
   #Checks the weather status and prints a suggestion.
   if status == "rainy":
      print("Don't forget to take your umbrella")
   elif status == "sunny":
      print("You can wear your sunglasses")
   else:
      print("Dress according to the weather.")

#Usage
check_weather("rainy")
check_weather("snowy")



#2. Default Parameters
# This is useful when a parameter to have a standard value if the user doesn't provide one.


def make_coffee(coffee_type, size="Medium"):
   #Prepaes coffee. Defalt size is Medium if not specified.
   print(f"preparing a {size} size {coffee_type}...")

#Usage
make_coffee("Latte")                      #Uses default size: "Medium"
make_coffee("Americano", "Large")        # Overrides default: "Large"



#3. Return Vlaues( Returning Data vs. Printing)
#. Print: Just shows text on the screen. You cannot use the result later.
#. Return: Gives the actual data back to your program.


def calculate_salary(daily_wage, days_worked):
   # Calculates total salary and returns the value.
   total = daily_wage * days_worked
   return total # sends the result back o be stored

#Usage:
my_salary = calculate_salary(100, 20)
print(f"Your calculated salary is: ${my_salary}")