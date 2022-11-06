#Module list_______________________________________________________________________________________________________________
from variables import p_opening_message
from variables import p_account_actions
from variables import p_confirm_logout
from variables import LOGED_IN
from security_authentication_functions import account_log_in
from user_bank_account_class import UserBankAccount
from user_functions import registration


#Function to run the fintech program_______________________________________________________________________________________
#This function is used to start abd manage the users interactions with the fintech program.

def start_program():

    opening_message = input(p_opening_message)
    
    if opening_message == "1":
        #account_login_function =  account_log_in()
        #LOGED_IN = account_login_function[0]
        LOGED_IN = account_log_in()[0]
        if LOGED_IN == True:
            while LOGED_IN:
                account_actions = input(p_account_actions)
                if account_actions == "1":
                    UserBankAccount.payment()
                elif account_actions == "2":
                    UserBankAccount.loan()
                elif account_actions == "3":
                    confirm_logout = input(p_confirm_logout)
                    if confirm_logout == "yes":
                        print("You have successfully logged out. See you again soon.")
                        LOGED_IN = False
                    elif confirm_logout == "no":
                        account_actions = input(p_account_actions)

    elif opening_message == "2":
        confirm_registration = registration()
        registration_completed = confirm_registration

        if registration_completed == True:
            LOGED_IN = account_log_in()[0]
            if LOGED_IN == True:
                while LOGED_IN:
                    account_actions = input(p_account_actions)
                    if account_actions == "1":
                        UserBankAccount.payment()
                    elif account_actions == "2":
                        UserBankAccount.loan()
                    elif account_actions == "3":
                        confirm_logout = input(p_confirm_logout)
                        if confirm_logout == "yes":
                            print("You have successfully logged out. See you again soon.")
                            LOGED_IN = False
                        elif confirm_logout == "no":
                            account_actions = input(p_account_actions)
                            
        elif registration_completed == False:
            registration_restarter = input("Looks like you have not completed the registration process,\ndo you want to restart that process? yes or no?: ")
            if registration_restarter == "yes":
                registration()
            else:
                print("Goodbye! Come back soon!")
                LOGED_IN = False

    else:
        print("We noticed that you did not chose a valid option.\nThe program will close now.\nDo come back again but please pay attention to the instructions across the program.\n")


start_program()