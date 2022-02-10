class Library:
    def __init__(self,library_name,listofbooks):
        self.name=library_name
        self.books=listofbooks
        self.lendDict={}
        

    def library(self):
        print(f"-------Welcome to {self.name} LIBRARY-------")
    
    def display_book(self):
        print("The available books in the library are as follows!")
        num=1
        for book in self.books:
            print(str(num)+"-"+book)
            num +=1
    def lend_book(self):
        name=input("Enter the name of the borrower :")
        bookName=input("Enter the book you need to borrow :")
        
        if bookName not in self.lendDict.keys():
            print(f"The book {bookName} has been issued to you.Please return it in 45 days")
            self.lendDict.update({bookName:name})
            self.books.remove(bookName)
        else:
            print(f"Sorry the following book is not available right now.This book is already been borrowed by {self.lendDict[bookName]}.Please come again in some time !")

    def add_book(self):
        book_Name=input("Enter the book name you want to sell :")
       
        print(f"{book_Name} has been added the the library's book colection")
        self.books.append(book_Name)
    def return_book(self):
        bookName=input("Enter the book name that you want to return :")
        
        print(f"{bookName} has been returned.Thank you for visiting the Library")
        self.books.append(bookName)


listofbooks=["python crash course","Hands on python","Python notes","Romeo and Juliet","HARRY POTTER","Tom and Jerry","Jerry and Juliet","Thompson","Kill Bill"]
lib=Library("NEW STATE ",listofbooks)

if __name__=="__main__":
    while True:
        lib.library()
        msg='''Please choose an option
             1. Display the available books
             2. Borrow a book
             3. To sell a book 
             4. To return a book
             5. To exit the library
           '''
        print(msg)
        Option=int(input("Enter a option :"))
        if Option==1:
            lib.display_book()
        elif Option==2:
            lib.lend_book()
        elif Option==3:
            lib.add_book()
        elif Option==4:
            lib.return_book()
        elif Option==5:
            print("Thank you visiting us.Please visit again!")
            exit()
        else:
            print("Please choose a valid option")

