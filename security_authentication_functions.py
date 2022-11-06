#Module list_______________________________________________________________________________________________________________
import mysql.connector
from pprint import pp
from variables import p_to_login
from variables import p_account_login_name
from variables import p_account_login_password
from variables import LOGED_IN
from accessing_database_class import AccessDatabase


#Create a log in function_______________________________________________________________________________________________________________
#This code block sets the conditions for the user to log into their account. The details from this process allow the user to interact with 
#other aspects of the program as a whole. Here, the username is assigned and turned into a global variabel so that it can be accesed by other functions.

def account_log_in():
    to_login = input(p_to_login) 
    to_login = to_login.lower()
    #global loged_in
    #loged_in = False
    login_process = True
    while login_process == True:
        try:
            if to_login == "yes":
                account_login_name = input(p_account_login_name)                      
                account_login_password = input(p_account_login_password)
                #global USER_NAME
                USER_NAME = account_login_name
                
                AccessDatabase.accessing_userprofiles_database()                     #update this to point to password table
                accesser = AccessDatabase.accessing_userprofiles_database()
                mycursor = accesser[1]  
                
                point_to_username_cell = mycursor.execute(f"SELECT Name FROM user_login_data WHERE Name = '{account_login_name}'")
                mycursor.execute(point_to_username_cell)
                the_name_cell = mycursor.fetchall()
                the_users_username = the_name_cell[0][0]

                point_to_password_cell = mycursor.execute(f"SELECT Password FROM user_login_data WHERE Name = '{account_login_name}'")
                mycursor.execute(point_to_password_cell)
                the_password_cell = mycursor.fetchall()
                the_users_password = the_password_cell[0][0]
                
                if account_login_name == the_users_username and account_login_password == the_users_password:                   

                    LOGED_IN = True
                    login_process = False
                    print(f"Welcome {account_login_name}, You have successfully logged into your account")

                    AccessDatabase.accessing_userprofiles_database()
                    accesser = AccessDatabase.accessing_userprofiles_database()
                    mycursor = accesser[1]

                    point_to_user = mycursor.execute(f"SELECT * FROM user_profiles WHERE Name = '{USER_NAME}'")
                    mycursor.execute(point_to_user)
                    the_user = mycursor.fetchall()
                    for item in the_user:
                        print("These are your account details:")
                        pp(item)

                elif account_login_name != the_users_username or account_login_password != the_users_password:   
                    print(f"Oops, incorrect username and password, please try again")
                    user_choice = input("Oops, you have either entered the incorrect username or password,\nplease press 1 to try again or press 2 to cancel: ")
                    if user_choice == "1":
                        pass
                    else:
                        print("Thanks you for visiting!\nSee you again soon.")
                        login_process = False           
            
            elif to_login == "no":                              
                print("Thanks you for visiting! See you again soon.")
                login_process = False
                LOGED_IN = False
                USER_NAME =  None 

            else:
                print("Invalid input. Program shutting down for security. Please restart.")
                login_process = False
                USER_NAME = None

        except IndexError:
                print("Oops, looks like you entered a value that is not in our database.\nThe program will close now for security.")
                USER_NAME = None
                login_process = False
                        
        else: 
            pass      
        
    return LOGED_IN, USER_NAME
