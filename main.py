class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in the library are :")
        for book in self.books:
            print(book)
    def borrowBook(self,bookName):

        if bookName in self.books:
            print(f"You have been issued {bookName}.Please return it within 45 days")
            self.books.remove(bookName)
        else:
            print("Sorry,this book has already been isssued to someone else.Please wait until the book has been returned")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book")


class Student:
    def requestBook(self):
        self.book=input("Enter the book you need to isuue :")
        return self.book
 
    def returnBook(self):
        self.book=input('Enter the name of the book you want to return :')
        return self.book


if __name__=="__main__":
    centralLibrary=Library(["Algorithms","Django","Python crash course","fluent in python","automate the boring stuff in python","harry potter"])
    
    student=Student()

    while True:
        welcomeMsg='''---Welcome to Central Library--- 
        Please choose an option :
        1. List all the books
        2. Request a book
        3. Return a book
        4 .Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("Enter a choice :"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing central library.Have a great day ahead !")
            exit()
        else:
            print("Invalid choice !")
