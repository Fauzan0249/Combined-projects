# stylish text with escape sequences
#Goal; use escape sequnces like \n (new line), \t (tab), and \"( double quote) tp fromat your your output within a single print funvtion
#Task; create a simple,formatted "Student Profile" card.
#Instructions : you will use one print funtion for this entire avtivity
#Inside the string function,create a string that displays a profile header, your univeristy program and a personal motto
#Use the \n newline character to make sure each piece of iformation is on its own on a new line 
# Use the \t tab character to indent the program and the motto
#Use \" to put your motto inside actual double quotes


print("Student Profile","\n\t Department of Mollecular Biology and Genetics\n\t","\"\n\tI shall make it\"\n\t")


#Activity 2: interactiv greetings with input()
#Goal:Learn how to assk the user for information and use it in your program
#Task: Create a program that asks for the user's name an dtheir favorite color, and the n gives them a personalised message.
#Instructions: Create a variable called user name. Use the input function to ask whats your name 
# Create another variable called favorite. Use input to ask to aks what's your favorite color.
# finally use print function to dispolay a messagethat includes their name and color

user_name= input("What's your name?")
favorite_color= input("What's your favorite color?")

print("My name is", user_name, "and my favorite color is", favorite_color)
