#By Jose Fuentes

#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = float(input('Enter the score for test 1: '))  # Convert input to float for numerical calculations
test2 = float(input('Enter the score for test 2: '))  # Same conversion for test 2
test3 = float(input('Enter the score for test 3: '))  # Same conversion for test 3

# Calculate the average test score
average = (test1 + test2 + test3) / 3  # Perform numerical division

# Print the average
print('The average score is', average)

# If the average is a high score, congratulate the user
if average >= HIGH_SCORE:
    print('Congratulations!')
else:
    print("That's a great average")

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
# Get the dimensions of the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Calculate the area of the first rectangle
area1 = length1 * width1

# Get the dimensions of the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate the area of the second rectangle
area2 = length2 * width2

#Calculate area of both rectangles:
areat = area1 + area2
# Print the areas of both rectangles
print("The area of the first rectangle is:", area1)
print("The area of the second rectangle is:", area2)
print("This is the area of both rectangles:", areat)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name= str(input("Enter your name: "))
age = int(input("Enter your age: "))
#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print("Happy birthday,", name, "You are", age, "years old today!")



