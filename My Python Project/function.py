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
   #Prepaes coffee. Default size is Medium if not specified.
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
   return total # sends the result back to be stored

#Usage:
my_salary = calculate_salary(100, 20)
print(f"Your calculated salary is: ${my_salary}")