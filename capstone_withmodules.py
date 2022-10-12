#Module list_______________________________________________________________________________________________________________
from datetime import date, datetime
import time
import re
from tkinter import END
import mysql.connector
import pymysql
from pprint import pp
import decimal
from variables import *
from cpsfunctions import *
from tkinter import *

def start_program():

    opening_message = input(p_opening_message)
    
    if opening_message == "1":
        account_login_function = account_log_in()
        logged_in = account_login_function[0]
        if logged_in == True:
            while logged_in:
                account_actions = input(p_account_actions)
                if account_actions == "1":
                    UserBankAccount.payment()
                elif account_actions == "2":
                    UserBankAccount.loan()
                elif account_actions == "3":
                    confirm_logout = input(p_confirm_logout)
                    if confirm_logout == "yes":
                        print("You have successfully logged out. See you again soon.")
                        logged_in = False
                    elif confirm_logout == "no":
                        account_actions = input(p_account_actions)

    elif opening_message == "2":
        confirm_registration = registration()
        registration_completed = confirm_registration

        if registration_completed == True:
            account_login_function = account_log_in()
            logged_in = account_login_function[0]
            if logged_in == True:
                while logged_in:
                    account_actions = input(p_account_actions)
                    if account_actions == "1":
                        UserBankAccount.payment()
                    elif account_actions == "2":
                        UserBankAccount.loan()
                    elif account_actions == "3":
                        confirm_logout = input(p_confirm_logout)
                        if confirm_logout == "yes":
                            print("You have successfully logged out. See you again soon.")
                            logged_in = False
                        elif confirm_logout == "no":
                            account_actions = input(p_account_actions)
                            
        elif registration_completed == False:
            registration_restarter = input("Looks like you have not completed the registration process,\ndo you want to restart that process? yes or no?: ")
            if registration_restarter == "yes":
                registration()
            else:
                print("Goodbye! Come back soon!")
                logged_in = False

    else:
        print("We noticed that you did not chose a valid option.\nThe program will close now.\nDo come back again but please pay attention to the instructions across the program.\n")


start_program()