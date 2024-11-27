from ast import main
from random import choice
from time import sleep


class Library:

 def __init__(self, books):

     self.books = books

 def display_books(self):

     print("\nbooks available in the library:")

     for book in self.books:
         print(f"-{book}")

 def borrow_book(self,book_name):

   if book_name in self.books:

       self.books.remove(book_name)

       print(f"please return the book {book_name} on time")

   else:

       return f"sorry, this book {book_name} is not availble"



 def return_book(self, book_name):

     self.books.append(book_name)

     print(f"thanks for returning the {book_name}")


def Main():

 library_books = ["python basics", "introduction to data science", "Machine learning"]

 library = Library(library_books)

 print("welcome to the library management system")

 while True:

     print("\nMenu")
     print("1. display all books")
     print("2.borrow a book")
     print("3. return a book")
     print("4. exit")

     choice = input("\enter your choice (1-4):")

     if choice == "1":
         library.display_books()

     elif choice =="2":
       book_to_borrow = input("\nenter the name of the book to borrow:")
       message = library.borrow_book(book_to_borrow)
       print(message)

     elif choice =="3":
         book_to_return = input("\n enter the name of the book to return:")
         message = library.return_book(book_to_return)
         print(message)
     elif choice == "4":
         print("thank you for using library management system")
         break

     else:
         print("invalid choice : please enter the number from 1 to 4")

if __name__ == "__main__":
       Main()













