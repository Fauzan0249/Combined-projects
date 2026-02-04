
'''Your Turn: Write a for loop using “range()” to print the numbers from 10 to 20 (inclusive). Remember,
the stop value must be one higher than the last number you want.'''


for number in range (11,21):
 print(number)






'''Your Turn: Write a for loop using “range()” to print the numbers from 10 to 20 (inclusive). Remember,
the stop value must be one higher than the last number you want.'''


for number in range (10,21):
 print(number)




'''Your Turn: Write a while loop that starts x = 0 and increases it by 1 endlessly (while True:). However, use
an if statement to check if x equals 13. If it does, use break to stop the loop.'''


x = 0

while True:
    x += 1
    print(x)

    if x == 13:
        break




'''Your Turn: Write a for loop that iterates from 1 to 10. If the number is 5, use continue to skip it. Print all
other numbers.'''

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

