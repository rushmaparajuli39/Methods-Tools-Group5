import math
import sys

## opens a file in read mode
## filename received as a parameter
## for openFile, we had an error when the directory did not exist
## so no exceptions for openFIle
def openFile(filename):
    infile = open(filename, "r")
    print("File opened.")

## takes two numbers and returns
## the result of a division
## Exceptions: will pass if denominator is not equal to 0
##             will pass if string is converted to integer
def numbers(num1, num2):
    try:
        string1toint=int(num1)
        string2toint=int(num2)
        if(string2toint==0):
            print("Denominator can not be zero")
            sys.exit("Error")
        else:
            return string1toint / string2toint
    except error:
        print("Enter an integer")

## takes in two points
## finds the distance between the points
## Exceptions: will pass if string is converted to integer
##             will pass if rounded to the smallest integer greater than or equal to the value
def dist(x1, y1, x2, y2):
    try:
        stringtointx1=int(x1)
        stringtointx2=int(x2)
        stringtointy1=int(y1)
        stringtointy2=int(y2)
        dist = (stringtointx2 - stringtointx1) ** 2 + (stringtointy2 - stringtointy1) ** 2
        dist = math.sqrt(dist)
#method ceil(x) in Python returns a ceiling value of x
        dist = math.ceil(dist)
        return dist
    except error:
        print("Enter an integer")


## takes in a string -- reverses it
## then compares the two
## Exceptions: will pass if integer is converted to string
def isPalindrome(temp):
    try:
        integertostring=str(temp)
        test = integertostring[::-1]
        if(test == integertostring):
            return True
        else:
            return False
    except error:
        print("Enter an string")

## has input to receive two numbers
## divides the two, then outputs the result
## Exceptions: will pass if denominator is not equal to 0
##             will pass if string is converted to integer
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if(num2==0):
        print("Denominator can not be zero")
        sys.exit("Error message")
    div = num1 / num2

    print("Your numbers divided is:", div)
    return div

## returns the squareroot of a particular number
##  Exceptions: will pass if string is converted to integer
def sq(num):
    try:
        stringtointnum=int(num)
        return math.sqrt(stringtointnum)
    except error:
        print("Enter an integer")
        
## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
## Exceptions: if index size is not out of bounds
def displayItem(numbers, index):
    if(index < 0 or index > len(numbers)): 
        sys.exit("Error message")
    else:
        print("Your item at", index, "index is", numbers[index])

