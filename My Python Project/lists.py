# Introduction: What is a list?
'''So far, we stored one value in one variable(name="Ahmet"). But what if we need to save 100 student names? we use lists.

 . Definition: A list is an ordered, changeable collection of items.
 . Syntax: Lists are creted using square bracket [].'''

#1. Creating Lits & Accessing elemets
#Lists can hold different data types (strings, integers, booleans) together.

# Creating a list

fruits = ["Apple","Banana","Cherry"]
numbers = [10, 20, 30, 40]
mixed_list = ["Biruni", 2025, True]

#Index (Position): Python uses 0-based indexing. The first item is at index 0.

my_courses = ["Math","Physics","Coding"]

print (my_courses[0])  #Output: Math
print (my_courses[1])   #Output: Physics
print (my_courses[-1])  # Output: Coding(Negative index counts from th end)



# 2. Modifying Lists (Add & Remove)
#Lists are mutable (changeable). We can add or remove items after changing the list.
'''Adding items:

   . append(item): Adds an item to the end of the list.
   . insert(index, item): Adds an item at a specific position.
   
   '''
colors = ["Red", "Blue"]
colors.append = ("Green")    # ["Red", "Blue", "Green"]
colors.insert = (0, "Yellow") # ["Yellow", "Red", "Blue", "Green"]


'''Removing items:

   . remove(value): Removes the first occurrence of the value.
   . pop(index): Removes the item at the index (default is the last one).'''

colors.remove("Red")
colors.pop()  # Removes the last item ("Green")

'''3. Joining Two Lists

Sometimes you need to combine two different lists into one. There are two common ways to do this:'''

class_a = ["Ali", "Veli"]
class_b = ["Ayse", "Fatma"]

all_students = class_a + class_b
print(all_students)

# Output: ["Ali", "Veli", "Ayse", "Fatma"]


'''4. Iterating Through Lists ( For Loops)

The most powerful way to use lists is with loops. You can run code for every item in the list

'''

students = ["Ali", "Ayse", "Mehmet"]

for student in students:
    print(f"Hello, {student}!")


#Checkking List Length: Len(list_name) gives the total number of items.


print(len(students)) # Output: 3S
