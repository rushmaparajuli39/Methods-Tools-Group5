
from collections import UserDict
from unicodedata import category
import mysql.connector
import sys
from getpass import getpass


## attempts to connect to the database
try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="group5methods",
        password="Asdfg12345",
        db="group5")
    print("Successful connection.")
    print(mydb)
    
except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

## cursor to send queries through
cursor = mydb.cursor()





#classes
#class Account to store user information
class Account:
    def CreateAccount(UserID, Password, First_Name, Last_Name, Email, Phone_Number, 
                      Billing_Address, Zip, City, State, Card_Name, Card_Number, 
                      Shipping_Address, Shipping_Zip):

        ## sends query
        cursor.execute('INSERT INTO account (UserId, Password, First_Name, Last_Name, Email, Phone_Number, Billing_Address, Zip, City, State, Card_Name, Card_Number, Shipping_Address, Shipping_Zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                      (UserId, Password, First_Name, Last_Name, Email, Phone_Number, 
                      Billing_Address, Zip, City, State, Card_Name, Card_Number, 
                      Shipping_Address, Shipping_Zip))
        
        ## commits to database
        ## **needed** for changes to be made to a table
        mydb.commit() # # we commit(save) the records to the table

        

       
        print(cursor.rowcount, "record(s) inserted.")
        return True #return true if account created sucessful
      


    def EditAccount(UserId, Password, First_Name, Last_Name, Email, Phone_Number, 
                    Billing_Address, Zip, City, State, Card_Name, Card_Number, 
                    Shipping_Address, Shipping_Zip):

        ## creates a query to make multiple rows at once
        ## creates a list of multiple tuples where each tuple is a row to be insert
        query = 'INSERT INTO account WHERE UserId = userid (UserId, Password, First_Name, Last_Name, Email, Phone_Number, Billing_Address, Zip, City, State, Card_Name, Card_Number, Shipping_Address, Shipping_Zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (UserId, Password, First_Name, Last_Name, Email, Phone_Number, 
               Billing_Address, Zip, City, State, Card_Name, Card_Number, 
               Shipping_Address, Shipping_Zip)

        #push to database
        ## sends query and data
        ## notice: execute line has changed!
        cursor.execute(query,val)

        
        account =cursor.fetchone()
        if account:
            mydb.commit() ## commits change
            print(cursor.rowcount, "record(s) inserted.")
            return True #return true if account created sucessful
        else:
            return False


    def DeleteAccount(UserId):

        cursor.execute('DELETE FROM account WHERE UserId = %s',(UserId,))
        mydb.commit() # # we commit(save) the records to the table


    def login(x,y):
        cursor.execute('SELECT * FROM account WHERE UserId = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            ID=x
            return True
            # Redirect to home page
        else:
            return False


    def EditShiipingInfo(UserId):
        #get new shipping info from the user
        print("\nNew Shipping Info: ")
        print("Enter Street Address: \n")
        Shipping_Address=str(input())
        print("Enter Zip Code: \n")
        Shipping_Zip=str(input())
        cursor.execute('UPDATE account SET Shipping_Address = %s AND Shipping_Zip = %s WHERE UserId=%s', (Shipping_Address, Shipping_Zip, UserId))
        mydb.commit() # # we commit(save) the records to the table 


    def EditPaymentInfo(UserId):
        #get new shipping info from the user
        print("\nNew Payment Info: ")
        print("Enter Billing Address")
        Billing_Address=str(input())
        print("Enter Zip Code: \n")
        Zip=int(input())
        print("Enter City: \n")
        City=str(input())
        print("Enter State: ")
        State=str(input())
        print("Cardholder Name: \n")
        Card_Name=str(input())
        print("Enter Card Number: \n")
        Card_Number=str(input())
        cursor.execute('UPDATE account SET Billing_Address = %s, Zip = %s, City = %s, State = %s, Card_Name = %s AND Card_Number=%s WHERE UserId=%s', (Billing_Address, Zip, City, State, Card_Name, Card_Number, UserId))
        mydb.commit() # # we commit(save) the records to the table


    def showaccountinfo():
        UserId=str(input())
        cursor.execute('SELECT * FROM account WHERE UserId=%s', (UserId,))
        result = cursor.fetchone()
        print(result)
        
    def updateorderhistory():
        UserId=str(input())
        cursor.execute('SELECT Order FROM account WHERE UserID=%s', (UserId,))
        cursor.execute('SELECT Num_Order FROM account WHERE UserID=%s', (UserId,))
        result=cursor.fetchone()
        result=result+1
        cursor.execute('UPDATE account SET Order = %s AND Num_Order = %s WHERE UserID=%s', (result,UserId,))

    def logout():
        loggedin=False
        return loggedin

##class Inventory to store the items and details about the items in stock
class Inventory:
     def printinventorybooks():
        cursor.execute('SELECT * FROM Inventory WHERE Category = 1')
        result = cursor.fetchall()
  
# loop through the rows
        for row in result:
          print(row)
          print("\n")

        print("\nAdd item from this category to cart? (Y/N)")
        answer=str(input())
        if(answer=="Y"):
            print("Enter Item ID: ")
            ItemID=str(input())
            cursor.execute('INSERT INTO group5.cart (ItemName, ItemID, quantity, Category, Price) SELECT ItemName, ItemID, stock, Category, Price FROM group5.inventory WHERE ItemID= %s',(ItemID,))
            print("Sucessfully added to Cart.")
        else:
            sys.exit()
        
            
     def printinventorymovies():
        cursor.execute('SELECT * FROM Inventory WHERE Category = 2')
        result = cursor.fetchall()

        for row in result:
          print(row)
          print("\n")

        print("\nAdd item from this category to cart? (Y/N)")
        answer=str(input())
        if(answer=="Y"):
            print("Enter Item ID: ")
            ItemID=str(input())
            cursor.execute('INSERT INTO group5.cart (ItemName, ItemID, quantity, Category, Price) SELECT ItemName, ItemID, stock, Category, Price FROM group5.inventory WHERE ItemID= %s',(ItemID,))
            print("Sucessfully added to Cart.")
        else:
            sys.exit()
        
     def editstock():
        print("\n Which item would you like to change?:")
        print("\n Select Category 1 for Books, 2 for movies and 3 for Comics")
        item=int(input())
        print("\n No of items in the stock: ")
        stockitem=int(input())
        cursor.execute('UPDATE Inventory SET stock = %s WHERE ItemID=%s', (stockitem,item,))
        mydb.commit() # # we commit(save) the records to the table
        
     def printinventorycomics():
        cursor.execute('SELECT * FROM Inventory WHERE Category = 3')
        result = cursor.fetchall()
  
# loop through the rows
        for row in result:
          print(row)
          print("\n")  

        print("\nwould you like to add an item from this category to your cart? (Y/N)")
        answer=str(input())
        if(answer=="Y"):
            print("Enter Item ID: ")
            ItemID=str(input())
            cursor.execute('INSERT INTO group5.cart (ItemName, ItemID, quantity, Category, Price) SELECT ItemName, ItemID, stock, Category, Price FROM group5.inventory WHERE ItemID= %s',(ItemID,))
            print("Sucessfully added to Cart. Returning back to homepage.")
        else:
            sys.exit()

        
        
##class Cart 
class Cart:    
    def AddItem():
        ItemID=str(input())
        cursor.execute('INSERT INTO group5.cart (ItemName, ItemID, quantity, Category, Price) SELECT ItemName, ItemID, stock, Category, Price FROM group5.inventory WHERE ItemID= %s',(ItemID,))
        mydb.commit() # # we commit(save) the records to the table

    def printitems():
        cursor.execute('SELECT * FROM cart')
        result = cursor.fetchall()
  
# loop through the rows
        print("\nItems in cart:")
        print("\n..............")
        print("\n\nItemName, ItemID, stock, Category, Price")

        for row in result:
          print(row)
          print("\n")          

    def gettotalforitemsincart():
        print(cursor.execute('SELECT SUM(Price) FROM cart'))


    def deleteitemfromcart():
        itemid=str(input())
        Cart.printitems()
        cursor.execute('delete FROM cart WHERE Itemid = %s',(itemid,))




    def deleteallitemsfromcart():
        Cart.printitems()
        cursor.execute('delete FROM cart')



    def checkoutitemsincart():
        print("\n---------------------------------------------")
        Cart.deleteallitemsfromcart() #delete items from the cart

#main loop for menu driven program

    
class Books:
    def printitems():
        cursor.execute('SELECT * FROM books')
        result = cursor.fetchall()
        
    def AddBooks(ISBN, Price, Title):

        ## sends query
        cursor.execute('INSERT INTO book (ISBN, Price, Title) VALUES (%s, %s, %s)',
                      (ISBN, Price, Title))
        
        ## commits to database
        ## **needed** for changes to be made to a table
        mydb.commit() # # we commit(save) the records to the table
       
        print(cursor.rowcount, "record(s) inserted.")
        return True #return true if account created sucessful
    
    def displayPrice():
        ISBN=str(input())
        Books.printitems()
        cursor.execute('SELECT Price FROM book WHERE ISBN=%s' ,(ISBN,))
        
class Movies:
    def printitems():
        cursor.execute('SELECT * FROM movies')
        result = cursor.fetchall()
        
    def AddMovies(Name, Type, Price):

        ## sends query
        cursor.execute('INSERT INTO book (Name, Type, Price) VALUES (%s, %s, %s)',
                      (Name, Type, Price))
        
        ## commits to database
        ## **needed** for changes to be made to a table
        mydb.commit() # # we commit(save) the records to the table
       
        print(cursor.rowcount, "record(s) inserted.")
        return True #return true if account created sucessful
    
    def displayPrice():
        Name=str(input())
        Movies.printitems()
        cursor.execute('SELECT Price FROM book WHERE Name=%s' ,(Name,))
    
class Comics:
    def printitems():
        cursor.execute('SELECT * FROM comics')
        result = cursor.fetchall()
        
    def AddComics(Title, Publisher, Price):

        ## sends query
        cursor.execute('INSERT INTO book (Title, Publisher, Price) VALUES (%s, %s, %s)',
                      (Title, Publisher, Price))
        
        ## commits to database
        ## **needed** for changes to be made to a table
        mydb.commit() # # we commit(save) the records to the table
       
        print(cursor.rowcount, "record(s) inserted.")
        return True #return true if account created sucessful
    
    def displayPrice():
        Title=str(input())
        Books.printitems()
        cursor.execute('SELECT Price FROM book WHERE ISBN=%s' ,(Title,))
        

loggedin=False
while(True):
    while(loggedin==False):
        print("............................................................................................................")
        print("\nCommand Line Interface Ecommerce Store\n")
        print("\n1. Login")
        print("\n2. Create Account")
        print("\n3. Exit Program")

        print("\n\n Enter Choice: 1, 2 or 3")
        choice=int(input())

        print("............................................................................................................")

        #check to see if user chose between 1 and 3
        if(choice<1 or choice>3):
            print("Wrong Input. Please enter a number between 1-3.")
            exit()
        # if (choice == string):
       
            
        #user login page
        if(choice==1):
            print("............................................................................................................")
        # try = 3;
        #     while(try >3):
        #         try = try-1
            UserId = input("Enter your UserID: ")
                #print("User Login")
                #print("\n\n Enter UserID:")
                #username=input()

                #check input
            Password = getpass("Enter the password: ")
                #print("\n\n password")
                #userpassword=input()

                #check input

                #check database to see if username and password are a match
            result=Account.login(UserId,Password)
            if(result==True):
                print("\nLogged in ..")
                loggedin=True

            if(result==False):
                print("\n UserID Or Pwd incorrect ...")
            #         print("You have %d valid attempts left" %(try))
            #         loggedin=False
            #  while(try=0):
                exit()


#create account page
        if(choice==2):
            print("............................................................................................................")

            print("\nCreate Account Page")
            

            #ask user for newUserId
            print("\n\nUserId: ")
            UserId = input()

            #ask user for password
            print("\n\nPassword: ")
            newpassword=input()

            #ask user for name
            print("\nFirstName: ")
            firstname=input()
            print("\nLastName: ")
            lastname=input()
            
            #ask user for email
            print("\nEmail: ")
            email=input()
            
            #ask user for phone number
            print("\nPhone Number: ")
            phone_number=input()
           
            #ask user for Billing information
            print("\nBilling Info")
            print("\nStreet Address: ")
            Billing_Address=input()
            print("\nZip Code: ")
            Zip=input()
            print("\nCity: ") 
            City=input()
            print("\nState: ")
            State=input()
            #check input
            
            print("\nShipping Info")
            print("\nShipping Address: ")
            shipping_address=input()
            print("\nShipping Zip: ")
            shipping_zip =input()
            #check input

            print("\nPayment Info")
            print("\nCard Name: ")
            Card_Name=input()
            print("\nCard Number: ")
            Card_Number=input()




            #call create account function with these inputs to store in the database
            result=Account.CreateAccount(UserId, newpassword, firstname, lastname, email, phone_number, Billing_Address, Zip, City, State, 
                                         shipping_address, shipping_zip, Card_Name, Card_Number)

            if(result==True):
                print("\nAccount created successfully.")

            if(result==False):
                print("\n Failed to create an account.")

    #exit program choice

        if(choice==3):
            print("............................................................................................................")

            print("\nExiting ...")
            sys.exit(1)   

 #after login has succeeded
    while(loggedin==True):
        print("............................................................................................................")

        print("\nCommand Line Interface Ecommerce Store\n")
        print("\n1. Categories")
        print("\n2. Shopping Cart Information")
        print("\n3. User Account")
        print("\n4. Modify Stock")
        print("\n5. Logout")    
        print("\n6. Exit Program")    


        print("\n\nEnter Choice:")
        choice=int(input())

        print("............................................................................................................")


        #check input
        if(choice<1 or choice>6):
            print("Please choose in between 1-6")
            exit() 

        if(choice==1):
            print("............................................................................................................")

            print("\nCategories\n")
            print("\n1. Books")
            print("\n2. Movies")
            print("\n3. Comics")


            print("\n\nEnter Choice:")
            choice1=int(input())
            print("............................................................................................................")


                 #check input
            if(choice1<1 or choice1>3):
                print("Please choose in between 1-3")
                exit()     


        #category 1
            if(choice1==1):
                print("............................................................................................................")

                print("\nBooks")

            #print all items in category Books (1)
                Inventory.printinventorybooks()
            #if the user want to check an specific price of the book
                print("Do you want to check the price?\n")
                Books.displayPrice()





            if(choice1==2):
                print("............................................................................................................")

                print("\nMovies")
                Inventory.printinventorymovies()
            #if the user want to check an specific price of the book
                print("Do you want to check the price to buy the movie?\n")
                Name=str(input())
                Type=str(input())
                Price=str(input())
                Movies.displayPrice()



            if(choice1==3):
                print("............................................................................................................")

                print("\nComics")
                print("\n\nEnter Choice:")
                Inventory.printinventorycomics(Name)
                
        
         #cartinformation

        if(choice==2):
            print("\nCart Information")
            print("\n\n1. Add items to Cart")
            print("\n\n2. Items in Cart")
            print("\n3. Total for items in Cart")
            print("\n4. Remove Item")
            print("\n5. Checkout Items in Cart")

            print("\n\nEnter Choice:")
            choice1=int(input())


            #check input
            if(choice1<1 or choice1>5):
                print("Invalid Input")
                exit()   


      
            if(choice1==1):
                print("............................................................................................................")
                #call add item function
                print("\nEnter item ID")
                # item=int(input())
                # iteminfo=Inventory.GetItem(item)
                # for x in iteminfo:
                #     print(x)
                print("\nWhich item ID to add:")

          

                Cart.AddItem()
                print("\nWould you like to add this to your order history?(Y/N)")
                answer=str(input())
                if(answer=="Y"):
                    Account.updateorderhistory()


                
            if(choice1==2):
                print("............................................................................................................")
                #call show items function


                print("\mAll items are currently in cart:")

                print("\n")

                #call print items function for ShoppingCart

                Cart.printitems()




            if(choice1==3):
                print("............................................................................................................")
                #call checkout items function
                total=Cart.gettotalforitemsincart()
                print(total)


            if(choice1==4):
                print("............................................................................................................")
                #call remove item function
                print("Which itemID do you want to remove?")
                Cart.deleteitemfromcart()

            if(choice1==5):
                print("............................................................................................................")
                #call checkout items function
                Cart.checkoutitemsincart()


            #account
        if(choice==3):
            print("\n Account Information")
            print("\n1. Show account Info")
            print("\n2. Update Shipping Info")
            print("\n3. Update Payment Info")
            print("\n4. Delete Account")

            print("\n\nEnter Choice:")
            choice1=int(input())


            #check input
            if(choice1<1 or choice1>4):
                print("Invalid Input")
                exit()   

            if(choice1==1):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.showaccountinfo()


            if(choice1==2):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.EditShiipingInfo(UserId)
                print("Sucessfully Updated")


            if(choice1==3):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.EditPaymentInfo(UserId)
                print("Sucessfully Updated")

            if(choice1==4):
                print("--------------------------------------------------------")
                #call delete account function
                Account.DeleteAccount(UserId)


        if(choice==4):
            print("--------------------------------------------------------")
            Inventory.editstock()
            #add to the database for available books
            if (1):
                print("Enter the ISBN, Price and Title for books to add to database.")
                ISBN=input()
                Price=input()
                Title=input()
                Books.AddBooks(ISBN, Price, Title)
            if (2):
            #add to the database for available movies
                print("Enter the Name, Type and Price for movies to add to database.")
                Name=input()
                Type=input()
                Price=input()
                Movies.AddMovies(Name, Type, Price)

        if(choice==5):
            print("--------------------------------------------------------")
            #Account.logout()
            loggedin=False
        if(choice==6):
            print("--------------------------------------------------------")

            print("\nExiting ...")
            mydb.close() # Close connection
            sys.exit(1)  
            


    

