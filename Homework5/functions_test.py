from functions import *
import os
import os.path
import pytest


## ********************************
## TESTING for Function divide()

## multiple input set up
## this makes it where each item follows the inputs
## in order of input statements
def geninputs():
    inputs = ["6", "3"]
    for item in inputs:
        yield item
def geninputs1():
    inputs = ["10","0"]

    for item in inputs:
        yield item

def geninputs2():
    inputs = ["Khem", 5]

    for item in inputs:
        yield item

def geninputs3():
    inputs = ["10","2"]

    for item in inputs:
        yield item

## sets up our inputs
GEN = geninputs()
GEN1=geninputs1()
GEN2=geninputs2()
GEN3=geninputs3()

#should pass
def test_divide(monkeypatch):
    ## passes input to the command-line
    ## if a single input statement, can just pass the string
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    assert divide() == 2.0
    
#should fail
#invalid operation because denominator can not be 0
def test_divide1(monkeypatch):
    ## passes input to the command-line
    ## if a single input statement, can just pass the string
    monkeypatch.setattr('builtins.input', lambda _: next(GEN1))
    assert divide() == 2.0

#type_error
#values of two different types are being passed; strings and integer 
#will pass if correct type in list
def test_divide2(monkeypatch):
        monkeypatch.setattr('builtins.input',lambda _: next(GEN2))
        assert divide() == 2.0

#should fail due to the ouput not being 2.0
#if we passed GEN1 or GEN2 instead of GEN3, the output would be 2.0 and the test would pass
def test_divide3(monkeypatch):
    ## passes input to the command-line
    ## if a single input statement, can just pass the string
    monkeypatch.setattr('builtins.input', lambda _: next(GEN3))
    assert divide() == 2.0


## ********************************
## TESTING for Function sq()

#should pass
def test_sq():
    assert sq(25)==5

#should pass
def test_sq1():
    assert sq(4)==2.0
    
#should fail
#will work if set == 7
def test_sq2():
    assert sq(125)==5
    
#should fail
#type error: invalid data types
#will work if 49 converted first
def test_sq3():
    assert sq("25")==5

## ********************************
## TESTING for Function numbers()
## passing ints within the function parameters: num1 and num2

#should pass
def test_numbers():
    assert numbers(40,1)==40

#should pass
def test_numbers1():
    assert numbers(20,5)==4.0

#should fail because denominator is zero
#will pass if second input is !0
def test_numbers2():
    assert numbers(100,0)==0

#type error
#should fail due to invalid type being input
#will pass if converted to integers
def test_numbers3():
    assert numbers("15","3")==5

## ********************************
## TESTING for Function dist()
#dist(x1,y1,x2,y2)=dist(2,2,5,6)
#should pass with supplied integers
def test_dist():
    assert dist(2,2,5,6)==5

#should pass 
def test_dist1():
    assert dist(2,2,5,6)==5.0

#result should not be equal
#result is not supposed to be 1
def test_dist2():
    assert dist(6,5,4,3)==1

#changed dist function to round up. The decimal places make it harder to compare (#this fails on purpose)
#explores equality with first decimal point. It fails
#result should have been 1.4142135623730951
def test_dist3():
    assert dist(2,2,1,1)==1.4
    
#type error: invalid data types string instead of integers
def test_dist4():
    assert dist("2","2","5","6")==5
    
## ********************************
## TESTING for Function isPalindrome()

#should pass
def test_isPalindrome():
    assert isPalindrome("aibohphobia")==True

#should fail
#type error: integer instead of string data type
def test_isPalindrome1():
    assert isPalindrome(5)==True

#should fail because it is not palindrome
def test_isPalindrome2():
    assert isPalindrome("aashma")==True

#should pass because it is not palindrome
def test_isPalindrome3():
    assert isPalindrome("aashma")==False

## ********************************
## TESTING for Function greetUser()

#should pass
def test_greetUser(capsys):
    greetUser("Khem", "Bahadur", "Dhami")

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Khem Bahadur Dhami\nGlad to have you!"
    
#should pass
#with greetUser, the program won't crash 
def test_greetUser1(capsys):
    greetUser(1, 2, 3)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program 1 2 3\nGlad to have you!"

#should fail
#typos in the sentence
def test_greetUser2(capsys):
    greetUser("Khem", "Bahadur", "Dhami")

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Khem B Dhami\nGlad to have you!"
    
## ********************************
## TESTING for Function displayItem()
## displays the item at the index provided on a Python List

#Python List

#item list
items = ["desktop","keyboard","mouse"]


#should pass
def test_displayItem(capsys):
    displayItem(items, 0)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 0 index is desktop"


#should not pass. This is because the item at index number 1 is keyboard

def test_displayItem1(capsys):
    displayItem(items, 1)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 1 index is mouse"


#should not pass. This is to simulate indexes out of bounds 
def test_displayItem2(capsys):
    displayItem(items, 3)
    captured_stdout,captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 3 index is mouse"

## ********************************
## TESTING for Function openFile()
FILE="/Users/mr.k/Desktop/homework5/testing.txt"

#should pass if testing.txt exists
def test_openFile():
    assert os.path.exists(FILE) == 1 #essentially stat file
    openFile(FILE)

FILE1="/Users/mr.k/Desktop/homework5/testing1.txt"
#should pass if testing1.txt exists
def test_openFile1():
    assert os.path.exists(FILE) == 1 #essentially stat file
    openFile(FILE1)
    
FILE2="/Users/mr.k/Desktop/homework5/testing2.txt"
#should pass if testing2.txt exists
def test_openFile2():
    assert os.path.exists(FILE) == 1 #essentially stat file
    openFile(FILE2)
    

#should fail because FILE3 does not exist 
FILE3="abc"
def test_openFile3():
    assert os.path.exists(FILE) == 1 #essentially stat file
    openFile(FILE3)

