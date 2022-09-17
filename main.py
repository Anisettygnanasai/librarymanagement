from admin import adminMenuMgmt
from user import userMenuMgmt

if(__name__ == "__main__"):
    print("********Library Management System********")
    ch=0
    while(ch != 3):

        print('''
            1. Admin Menu
            2. User Menu
            3. Exit
        ''')
        try:
            ch =  int(input("Enter your choice: "))

        except ValueError:
            print("Please enter numeric value only.")
        
        else:
            if(ch == 1):
                uname  = input("Enter username: ")
                pswd = input("Enter passward: ")
                if(uname == "Admin" and pswd == "Admin123"):
                    adminMenuMgmt()
                else:
                    print("Invalid Credientials...")
            elif(ch ==  2):
                uname  = input("Enter username: ")
                userMenuMgmt(uname)

            elif(ch == 3):
                print("********Thank You********")    
            else:
                print("Invalid choice..")    