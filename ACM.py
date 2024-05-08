import os
import time

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

os.system('cls')
print("\n")
print(CBOLD + CGREEN + CITALIC + " [ Welcome to the ACM User Management System! ]" + CEND)

def main():

    print("\n")

    print(" What would you like to do today?")

    print("\n")

    print(" [1.] Create/Delete Account")
    print(" [2.] Enable/Disable Account")
    print(" [3.] Change Privileges")
    print(" [4.] Reset Password")
    print(" [5.] List All Accounts")
    print(" [6.] Main Menu")
    print(" [7.] Exit")

    print("\n")

    selection = input(" " + CSELECTED + "Enter your choice:" + CEND + "\n \n ")
    if selection.isdigit():
        selection = int(selection)
    
        if selection == 1:
            os.system('cls')
            createdeleteaccount()

        elif selection == 2:
            os.system('cls')
            enabledisableaccount()

        elif selection == 3:
            os.system('cls')
            changeprivileges()

        elif selection == 4:
            os.system('cls')
            resetpassword()

        elif selection == 5:
            os.system('cls')
            listallaccounts()

        elif selection == 6:
            os.system('cls')
            print('\n')
            print(CBOLD + CGREEN + CITALIC + " [ Welcome to the ACM User Management System! ]" + CEND)
            main()

        elif selection == 7:
            os.system('cls')
            exitconfirm()

        elif selection == '💀🎺':
            os.system('cls')
            print("womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp womp")

        else:
            os.system('cls')
            print('\n')
            print(CRED + " [ Invalid input. Integer must be listed. ]" + CEND)
            main()

    else:
        os.system('cls')
        print('\n')
        print(CRED + "[ Invalid input. Must be an integer. ]" + CEND)
        main()


def createdeleteaccount():

    os.system('cls')
    
    print("\n")

    print(CITALIC + " [ Are you Making or Deleting an Account? ]" + CEND)

    print("\n")

    print(CGREEN2 + " [1.] Create Account" + CEND)
    print(CRED2 + " [2.] Delete Account" + CEND)
    print(CYELLOW + " [3.] Main Menu" + CEND)

    print("\n")

    selection = input(" " + CSELECTED + "Enter your choice:" + CEND + "\n \n ") 
    if selection.isdigit():
        selection = int(selection)
    
        if selection == 1:
            os.system('cls')
            createaccount()

        elif selection == 2:
            os.system('cls')
            deleteaccount()

        elif selection == 3:
            os.system('cls')
            print("\n")
            print(CBOLD + CGREEN + CITALIC + " [ Welcome to the ACM User Management System! ]" + CEND)
            main()

        else:
            os.system('cls')
            print('\n')
            print(CRED + " [ Invalid input. Integer must be listed. ]" + CEND)
            main()

    else:
        os.system('cls')
        print("\n")
        print(CRED + "[ Invalid input. Must be an integer. ]" + CEND)
        main()

def createaccount():

    os.system('cls')

    print("\n")

    print(CITALIC + " just type exit if you want to go back. :)" + CEND)

    print("\n")

    username = input(" [ What should the username be? ]" + "\n \n ")

    if username == 'exit':
        os.system('cls')
        createdeleteaccount()

    print("\n")

    password = input(" [ What should the password be? ]" + "\n \n ")
    password = str(password)

    if password == 'exit':
        os.system('cls')
        createdeleteaccount()

    print("\n")

    print(" [ What should the privileges be? ]" + "\n \n ")

    print(" [1.] Admin")
    print(" [2.] User")

    print("\n")
    privileges = input(" Enter your choice:" + "\n \n ")
    if privileges.isdigit():
        privileges = int(privileges)

        if privileges == 'exit':
            os.system('cls')
            createdeleteaccount()

        elif privileges == 1:
            privileges = "admin"

        elif privileges == 2:
            privileges = "user"

        else:
            os.system('cls')
            print('\n')
            print(CRED + " [ Invalid input. Integer must be listed. ]" + CEND)
            main()
    else:
        os.system('cls')
        print('\n')
        print(CRED + "[ Invalid input. Must be an integer. ]" + CEND)
        main()

    print("\n")

    print(" [ Should the account be enabled or disabled? ]" + "\n \n ")
    print(" [1.] Enabled")
    print(" [2.] Disabled")
    
    print("\n")

    enabled = input(" Enter your choice:" + "\n \n ")

    if enabled == 'exit':
        os.system('cls')
        createdeleteaccount()

    if enabled.isdigit():
        enabled = int(enabled)

        if enabled == 1:
            enabled = "enabled"

        elif enabled == 2:
            enabled = "disabled"

        else:
            os.system('cls')
            print('\n')
            print(CRED + " [ Invalid input. Integer must be listed. ]" + CEND)
            main()

    else:
        os.system('cls')
        print('\n')
        print(CRED + "[ Invalid input. Must be an integer. ]" + CEND)
        main()

    print("\n")
    os.system('net user ' + username + ' ' + password + ' /add')
    if privileges == "admin":
        os.system('net localgroup administrators ' + username + ' /add')
    
    if enabled == "disabled":
        os.system('net user ' + username + ' /active:no')

    print(" [ Account Created! ]")
    print(" [ Username: " + username + " ]")
    print(" [ Password: " + password + " ]")
    print(" [ Privileges: " + privileges + " ]")
    print(" [ Account Status: " + enabled + " ]")

    print("\n")

    input(" [Press any key to go back. ]" + "\n \n ")
    os.system('cls')
    print("\n")
    print(CBOLD + CGREEN + CITALIC + " [ Welcome to the ACM User Management System! ]" + CEND)
    main()

def deleteaccount():

    os.system('cls')
    
    print('\n')
    
    print(CITALIC + " just type exit if you want to go back. :)" + CEND)

    print('\n')

    os.system('net user')

    print('\n')

    username = input(' [ What is the username of the account you want to delete?' + CRED + CBOLD + ' (WARNING: THIS ACTION IS IRREVERSABLE.)' + CEND + ' ] \n \n ')

    if username == 'exit':
        os.system('cls')
        createdeleteaccount()

    print('\n')

    print(CRED + ' [ Are you sure you want to delete the account ' + CEND + username + CRED + '? ]' + CEND)

    print('\n')

    print(CRED + ' [1.] Yes' + CEND)
    print(CGREEN + ' [2.] No' + CEND)

    print('\n')

    selection = input(CSELECTED + ' Enter your choice:' + CEND + '\n \n ')
    if selection.isdigit():
        selection = int(selection)

        if selection == 'exit':
            os.system('cls')
            createdeleteaccount()

        if selection == 1:
            os.system('cls')
            os.system('net user ' + username + ' /delete')
            print('\n')
            print(CRED + ' [ Account Deleted! ]' + CEND)
            print('\n')
            input(' [Press any key to go back. ]' + '\n \n ')
            os.system('cls')
            print('\n')
            print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
            main()

        elif selection == 2:
            os.system('cls')
            createdeleteaccount()

        else:
            os.system('cls')
            print('\n')
            print(CRED + ' [ Invalid input. Integer must be listed. ] ' + CEND)
            main()

    else:
        os.system('cls')
        print('\n')
        print(CRED + ' [ Invalid input. Must be an Integer. ] ' + CEND)
        main()

def enabledisableaccount():
    
    os.system('cls')

    print('\n')

    print(CITALIC + ' just type exit if you want to go back. :)' + CEND)

    print('\n')

    os.system('net user')

    print('\n')

    username = input(' [ What is the username of the account you want to enable/disable? ]' + '\n \n ')

    if username == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    print('\n')

    print(' [ Should the account be enabled or disabled? ]' + '\n \n ')
    print(' [1.] Enabled')
    print(' [2.] Disabled')

    print('\n')

    enabled = input(' Enter your choice:' + '\n \n ')

    if enabled == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    if enabled.isdigit():
        enabled = int(enabled)

        if enabled == 1:
            enabled = 'yes'

        elif enabled == 2:
            enabled = 'no'

        else:
            os.system('cls')
            print('\n')
            print(CRED + ' [ Invalid input. Integer must be listed. ] ' + CEND)
            main()

    else:
        os.system('cls')
        print('\n')
        print(CRED + ' [ Invalid input. Must be an Integer. ] ' + CEND)
        main()

    print('\n')

    os.system('cls')

    os.system('net user ' + username + ' /active:' + enabled)
    print(' [ Account Status Changed! ]')
    print(' [ Username: ' + username + ' ]')
    print(' [ Account Status: ' + enabled + ' ]')

    print('\n')

    input(' [Press any key to go back. ]' + '\n \n ')
    os.system('cls')
    print('\n')
    print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
    main()

def changeprivileges():
    
    os.system('cls')

    print('\n')

    print(CITALIC + ' just type exit if you want to go back. :)' + CEND)

    print('\n')

    os.system('net user')

    print('\n')

    username = input(' [ What is the username of the account you want to change the privileges of? ]' + '\n \n ')

    if username == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    print('\n')

    print(' [ What should the privileges be? ]' + '\n \n ')
    print(' [1.] Admin')
    print(' [2.] User')

    print('\n')

    privileges = input(' Enter your choice:' + '\n \n ')

    if privileges == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    if privileges.isdigit():
        privileges = int(privileges)

        if privileges == 1:
            privileges = 'admin'

        elif privileges == 2:
            privileges = 'user'

        else:
            os.system('cls')
            print('\n')
            print(CRED + '[ Invalid input. Integer must be listed. ]' + CEND)
            main()
    
    else:
        os.system('cls')
        print('\n')
        print(CRED + ' [ Invalid input. Must be an Integer. ] ' + CEND)
        main()

    print('\n')

    if privileges == 'admin':
        os.system('cls')
        os.system('net localgroup administrators ' + username + ' /add')
        print(' [ Privileges Changed! ]')
        print(' [ Username: ' + username + ' ]')
        print(' [ Privileges: ' + privileges + ' ]')
    
    elif privileges == 'user':
        os.system('cls')
        os.system('net localgroup administrators ' + username + ' /delete')
        print(' [ Privileges Changed! ]')
        print(' [ Username: ' + username + ' ]')
        print(' [ Privileges: ' + privileges + ' ]')

    print('\n')

    input(' [Press any key to go back. ]' + '\n \n ')
    os.system('cls')
    print('\n')
    print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
    main()

def resetpassword():
    
    os.system('cls')

    print('\n')

    print(CITALIC + ' just type exit if you want to go back. :)' + CEND)

    print('\n')

    os.system('net user')

    print('\n')

    username = input(' [ What is the username of the account you want to reset the password of? ]' + '\n \n ')

    if username == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    print('\n')

    password = input(' [ What should the new password be? ]' + '\n \n ')
    password = str(password)

    if password == 'exit':
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

    print('\n')

    os.system('net user ' + username + ' ' + password)

    os.system('cls')

    print('\n')

    print(' [ Password Reset! ]')
    print(' [ Username: ' + username + ' ]')
    print(' [ Password: ' + password + ' ]')

    print('\n')

    input(' [Press any key to go back. ]' + '\n \n ')
    os.system('cls')
    print('\n')
    print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
    main()

def listallaccounts():
    
    os.system('cls')

    print('\n')

    os.system('net user')

    print('\n')

    input(' [Press any key to go back. ]' + '\n \n ')
    os.system('cls')
    print('\n')
    print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
    main()

def exitconfirm():
    
    os.system('cls')

    print('\n')

    print(CRED + ' [ Are you sure you want to exit the ACM User Management System? (Default = N) ]' + CEND)

    print('\n')

    print(CRED + ' [1.] Yes' + CEND)
    print(CGREEN + ' [2.] No' + CEND)

    print('\n')

    selection = input(' ' + CSELECTED + 'Enter your choice:' + CEND + '\n \n ')

    if selection.isdigit():
        selection = int(selection)

        if selection == 1:
            os.system('cls')
            print('\n')
            print(CBOLD + CVIOLET + CITALIC + ' [ Goodbye! ]' + CEND)
            time.sleep(1)
            os.system('cls')
            exit()

        elif selection == 2:
            os.system('cls')
            print('\n')
            print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
            main()

        else:
            os.system('cls')
            print('\n')
            print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
            main()

    else:
        os.system('cls')
        print('\n')
        print(CBOLD + CGREEN + CITALIC + ' [ Welcome to the ACM User Management System! ]' + CEND)
        main()

main()