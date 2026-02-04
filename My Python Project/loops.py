'''Your Turn: Write a while loop that starts with a variable number = 1. Multiply the number by 2 in each
step and print it. The loop should stop when the number is greater than 100.'''



number = 1
while number <= 100:
 print(number)
 number = number * 2




 ''' Question 1: The "Battery Charger" Simulation
Concept: while loop basics.
Scenario: Imagine you are writing software for a smartphone. The phone is currently at 10% battery. It needs
to charge until it reaches 100%.
Instructions:
1. Create a variable named battery_level and set it to 10.
2. Create a while loop that runs as long as the battery_level is less than or equal to 100.
3. Inside the loop, print the current battery level (e.g., "Charging... Battery is at 10%").
4. Increase the battery_level by 10 in every step.
5. Once the loop finishes, print "Battery Full!".'''
  


Battery_level = 10
while Battery_level <= 100:
 print(f"Charging ... Battery is at {Battery_level}%")
 Battery_level +=10

print("Battery full")

'''The "ATM PIN System"
Concept: while loop with input() and break.
Scenario: You are designing the security system for an ATM. The user has only 3 attempts to enter the
correct PIN code. The correct PIN is "1234".
Instructions:
1. Create a variable attempts and set it to 3.
2. Create a variable correct_pin and set it to "1234".
3. Create a while loop that runs as long as attempts is greater than 0.
4. Inside the loop, ask the user to enter the password using the input() function.
5. Check the password:
a. If the input matches correct_pin: Print "Login Successful!" and use the break command to
stop the loop immediately.
b. If the input is wrong: Decrease attempts by 1.
6. After wrong input:
a. If attempts reaches 0, print "Account Blocked!".
b. Otherwise, print "Wrong password. Attempts left: [number]".'''

Attempts = 3


correct_pin = "1234"

while Attempts > 0:
  user_input = input("Enter password: ")
   

  if user_input == correct_pin:
   print("Login successfull")

   break

  if user_input != correct_pin:
        Attempts -= 1
        print(f"incorrect password. Attempts left: {Attempts}")

  if Attempts == 0:
   print("Account blocked!")



'''The "Odd Number Collector"
Concept: for loop with continue and Modulo (%).
Scenario: We need a program that scans numbers from 1 to 20. The goal is to calculate the sum of only the
odd numbers. If a number is even, the program should ignore it.
Logic: To check if a number is even, use number % 2 == 0.
Instructions:
1. Create a variable total_sum and set it to 0.
2. Write a for loop that iterates through numbers 1 to 20 using range().
3. Inside the loop, check if the number is even.
4. If it is even, use continue to skip the rest of the code for that number.
5. If it is odd, add the number to total_sum and print "Added: [number]".
6. Print the final total at the end.'''



Total_sum = 0

for number in range (1,21):
  print(number)

  if number % 2 == 0:
    continue
  if number % 2 != 0:
    Total_sum += number
    print(f"Added: {number}") 

print(f"final total: {Total_sum}")


'''The "Classroom Seating Chart"
Concept: Nested Loops (Simple).
Scenario: You are labeling desks in a small classroom. There are 3 Rows and each row has 2 Desks. You need
to print a label for every desk.
Instructions:
1. Create an outer for loop for row using range(..., ...) function. (represents Row 1, Row 2, Row 3).
2. Inside that loop, create an inner for loop for desk using range(..., ...) (represents Desk 1, Desk 2).
3. Inside the inner loop, print the label: "Row [row] - Desk [desk]".'''


for row in range (1, 4):
  
  for desk in range(1,3):
    print(f"Row {row}- desk {desk}")
