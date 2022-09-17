from bookMgmt import BookMgmt

def userMenuMgmt(uname):
    bookMgmt = BookMgmt()
    ch = 0 
    while(ch != 7):
        print('''
            1. Show All Books
            2. Search Book by Id
            3. Search Book by Name
            4. Search Book by Author
            5. Issue Book by Id
            6. Submit Book
            7. Return to main menu
        ''')
        try:
            ch = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter numeric value only.")

        else:    
            if(ch == 1):
                bookMgmt.showAllBook()

            elif(ch == 2):
                id = int(input("Enter Book Id to search: ")) 
                bookMgmt.searchBookById(id)

            elif(ch == 3):
                nm = input("Enter Book Name to search: ")
                bookMgmt.searchBookByName(nm)
            
            elif(ch == 4):
                nm = input("Enter Book Author to search: ")
                bookMgmt.searchBookByAuthor(nm)  

            elif(ch == 5):
                num=int(input("Enter no of books you want to issue:"))
                bookMgmt.issueBookById(num,uname)

            elif(ch == 6):
                num=int(input("Enter no of book you want to submit:"))
                bookMgmt.submitBookById(num,uname)     
            
            elif(ch == 7):
                return
                
            else:
                print("Invalid Choice..")

if(__name__ == "__main__"):
    userMenuMgmt() 