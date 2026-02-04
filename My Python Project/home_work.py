'''ACTIVITY: VENDING MACHINE
- The Challenge: combinng all new concepts(eleif, nested-if, and match) to create a smart vending machine program.
- The Logic:ACTIVITY: Vending Machine
The Challenge: Combine all the new concepts (elif, nested if, and match) to create a
smart vending machine program.
The Logic:
1. The machine has three main categories: (1) Drink, (2) Snack, or (admin).
2. The user will first choose a category.
3. If they choose Drink, they get a sub-menu with 3+ options (e.g., Water, Soda,
Coffee).
4. If they choose Snack, they get a sub-menu with 2 options (e.g., Chips,
Chocolate).
5. If they choose admin, they must enter a password.
Your Task:
1. Ask the user for their main choice: (1) Drink, (2) Snack, or (admin).
2. Use a match...case statement to control the main choice.
3. case "1" (Drink):
o Ask the user to choose from: (a) Water, (b) Soda, or (c) Coffee.
o Use an if-elif-else chain to print what they selected (e.g., "Dispensing Water...").
4. case "2" (Snack):
o Ask the user to choose from: (x) Chips or (y) Chocolate.
o Use a simple if-else statement for this (since there are only two options).
5. case "admin":
o Set a SECRET_PASSWORD = "1234" in your code.
o Ask the user to enter the password.
o Use a Nested if statement to check if the entered password matches SECRET_PASSWORD.
o If it matches, print "Welcome, Admin. System unlocked."
o If it doesn't match, print "Access Denied. Incorrect password."
6. case _:
o If the user enters anything other than "1", "2", or "admin", print "Invalid category."'''




#Categories
drink = "water", "soda", "coca-cola"
snacks = "chips", "bisquits", "chocolate"
admin = "My name"

#The use will first choose a category

print("drink\nsnacks\nadmin")


category = input("Please make a choice: ")

#use a match case to control the main choise

match category:
    case "1":
        print("\nwater\nsoda\ncoca-cola")
        user_input = input("Please make a choice: ")
        if user_input == "water":
             print("Dispensing water")
        elif user_input == "soda":
             print("Chilled soda")
        elif user_input == "coca-cola":
             print("Chilled coke")
        else:
             print("Not in stock")
        
       
    case "2":
        print("\nchips\nbisquits\nchocolate")
        user_input = input("Please make a choice: ")
        if user_input == "chips":
             print("Pringles")
        elif user_input == "bisquits":
             print("Jack & Jill")
        elif user_input == "chocolate":
             print("Kingsbite chocolate")
        else:
             print("Not in stock")
     
    case "admin":
        secret_password = "1234"
        user_input = input("Enter password: ")

        if user_input == secret_password:
               print("Welcome admin. System unlocked")
        else:
               print("Access denied. Incorrect passowrd. Please try again!!")
    case _:
          print("Invalid category")
          









