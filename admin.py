from book import Book
from bookMgmt import BookMgmt

def adminMenuMgmt():
    bookMgmt = BookMgmt()
    ch = 0 
    while(ch != 8):
        print('''
            1. Add Book
            2. Show All Books
            3. Search Book by Id
            4. Search Book by Name
            5. Search Book by Author
            6. Delete Book by Id
            7. Edit Book by Id
            8. Return to main menu
        ''')
        try:
            ch = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter numeric value only.")

        else:    
            if(ch == 1):
                id = int(input("Enter book Id: "))
                nm = input("Enter Book Name: ")
                au= input("Enter Book Author: ") 
                q=int(input("Enter quantity:"))
                book = Book(id,nm,au,q)
                bookMgmt.addBook(book)

            elif(ch == 2):
                bookMgmt.showAllBook()

            elif(ch == 3):
                id = int(input("Enter Book Id to search: "))
                bookMgmt.searchBookById(id)

            elif(ch == 4):
                nm = input("Enter Book Name to search: ")
                bookMgmt.searchBookByName(nm)

            elif(ch == 5):
                nm = input("Enter Book Author to search: ")
                bookMgmt.searchBookByAuthor(nm)    

            elif(ch == 6):
                id = int(input("Enter Book Id to delete: "))
                bookMgmt.deleteBookById(id)   

            elif(ch == 7):
                id = int(input("Enter Book Id to edit: "))
                bookMgmt.editBookById(id)     

            elif(ch == 8):
                return
                
            else:
                print("Invalid Choice..")

if(__name__ == "__main__"):
    adminMenuMgmt()