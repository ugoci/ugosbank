#This program takes in user input, registers them unto a database and allows registered 
#users to transact among themselves. The program includes python, tkinter GUI and mysql databases.
#This file includes all the lines of code needed to run the program, in one place.
#Enjoy, feedback welcome!

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


#Start program_______________________________________________________________________________________________________
#This code block starts the program and manages the users interactions with the program
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


#Function to register new users_____________________________________________________________________________________________
#This code block takes in a set of user inputs to create each unique user profile which is then saved unto a MySQL database. 
#The code code block also provides the user with administrative and support options. 
def registration():                                                              
    account_balance = 0
    opening_questions = True

    while opening_questions == True:   
        try:
            welcome_message = input(p_welcome_message) 

        except ValueError:
            print("Please input a valid character/response to the question.")   

        except NameError:
            print("Please input a valid character/response to the question.")   

        else:
            welcome_message = welcome_message.lower()
            skill_coefficient = 0 
            education_coefficient = 0

            if welcome_message == "yes":
                opening_questions = False
                name = input(p_name) 
                name = name.lower()   
                age = check_age()
                current_date = date.today()
                the_date = current_date.strftime("%Y-%m-%d") 
                location = input(p_location) 
                location = location.lower()
                contact_number = input(p_contact_number) 
                contact_num_length = len(contact_number)                        
                if contact_num_length == 8:
                    cn = re.findall("\d", contact_number)
                    if cn:
                        pass
                    else:
                        print("Please input a valid phone number")
                        contact_number 
                elif contact_num_length != 8:
                    print("Please input a valid phone number")
                    contact_number = input(p_contact_number)
                contact_email = input(p_contact_email) 
                contact_email = contact_email.lower()
                ce = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', contact_email)   
                if ce == object:
                    pass 
                elif ce == None:
                    print("please input a valid email address")   
                    contact_email = input(p_contact_email) 
                check_skill_database = input(p_check_skill_database)
                if check_skill_database == "yes":
                    open_skilldatabase_window()
                    which_skill = int(input("write the number that corresponds to your main skill: "))
                    for key, value in list_of_skills.items():
                        if which_skill == value:
                            main_skill = key
                            for key, value in skill_coefficient_list.items():
                                if key == main_skill:
                                    skill_coefficient = value
                else:
                    check_skill_database = input("Look through the list of skills below and\ncheck the number that corresponds to your main skill.\nType yes when you are ready to see the skill database: ")
                
                education_training = input(p_education_training) 
                education_training = education_training.lower()
                if education_training == "1":
                    education_coefficient = 1
                elif education_training == "2":
                    education_coefficient == 1.5
                elif education_training == "3":
                    education_coefficient = 2
                elif education_training == "4":
                    education_coefficient = 2
                elif education_training == "5":
                    education_coefficient = 3
                elif education_training == "6":
                    education_coefficient = 5
                else:
                    education_coefficient = 1  
                user_name = name                            
                user_password = input(p_set_password)       

                each_profile = (name, age, the_date, location, account_balance, contact_number, contact_email, main_skill, education_training,education_coefficient, skill_coefficient)
                establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                              host='localhost',
                              database='user_profiles')
                mycursor = establish_sql_connection.cursor()
                insert_to_userprofiles_table = "INSERT INTO user_profiles (Name, Age, Date, Location, Account_balance, Contact_number, Contact_email, Main_skill, Skill_coefficient, Education_training, Education_coefficient) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(insert_to_userprofiles_table, each_profile)
                establish_sql_connection.commit()

                insert_to_logindata_table = "INSERT INTO user_login_data (Name, Password) VALUES (%s,%s)"
                value_to_insert = (f"{user_name}", f"{user_password}")
                mycursor.execute(insert_to_logindata_table, value_to_insert)
                establish_sql_connection.commit()
                print("your details have been saved sucessfully to our database")
                confirm_login = True

            elif welcome_message == "no":
                print("Thanks for visiting. Goodbye!")
                opening_questions = False
                confirm_login = False

            elif welcome_message == "help":
                print("Welcome to the program, if you are stuck, here are some pointers:\n - you can start by reading the readme_capstone.txt file\n - this program is not case sensitive so you can type in either small or capital letters")
                confirm_login = False

            elif welcome_message == "privacy":
                open_privacystatement_window()
                confirm_login = False
    
    return confirm_login


#Open a new window with list of skills__________________________________________________________________________________________________
#This code block opens a new window with a list of skills, each with a number assigned to it. The block uses tkinter to create the new window.
def open_skilldatabase_window():
    new_window = Tk()
    new_window.title("Skill Database")
    new_window.geometry("500x500")
    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(new_window, yscrollcommand = scrollbar.set )
    line_counter = 0
    for item in list_of_skills:
        line_counter = line_counter + 1
        mylist.insert(END, item + ": " + str(line_counter))
    mylist.pack(side = LEFT, fill = BOTH)
    scrollbar.config(command = mylist.yview)
    new_window.mainloop() 


#Show privacy statement in a new window_________________________________________________________________________________________________
#This block opens a new window with a privacy statement for the user.
def open_privacystatement_window():
    new_window = Tk()
    new_window.title("Our Privacy Statement")
    canvas = Canvas(new_window, width= 1000, height= 750, bg="White")
    canvas.create_text(500, 505, text=f"{privacy_statment}", fill="black", font=('Helvetica 11'))
    canvas.pack()
    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(new_window, yscrollcommand = scrollbar.set )
    mylist.insert(END, privacy_statment)
    scrollbar.config(command = mylist.yview)
    new_window.mainloop() 


#Check the users age meets requirements______________________________________________________________________________________________
#This block checks the user has input numbers at the right length and that the user is not below the age of 18.
def check_age():
    age_checker = True
    while age_checker:
        p_age = input("Indicate your age: ")
        age_lenth = len(p_age)                       
        if age_lenth == 2:
            al = re.findall("\d", p_age)
            if al:
                age = p_age 
                age = int(age)
                if age < 18:
                    guardian_consent = input("You need a legally recognised adult to approve that we can go ahead to create your profile.\nYour guardian must type yes in the commment box to digitally sign that they give consent: ")
                    guardian_consent = guardian_consent.lower()
                    if guardian_consent == "yes":
                        age
                        continue
                    else:
                        print("Sorry but the conditions to create this profile have not been met at this time,\nwe invite you to please try again as you are important to us.\nThank you for understanding and see you again soon!")
                        age_checker = False
                        SystemExit

                elif age > 18:
                    age = age
                    age_checker = False
                    continue
            else:
                print("Please indicate your correct age")
                p_age

        elif age_lenth != 2:
            print("please indicate your correct age")
            p_age


#Create a log in function_______________________________________________________________________________________________________________
#This code block sets the conditions for the user to log into their account. The details from this process allow the user to interact with 
#other aspects of the program as a whole. Here, the username is assigned and turned into a global variabel so that it can be accesed by other functions.
def account_log_in():
    to_login = input(p_to_login) 
    to_login = to_login.lower()
    global loged_in
    loged_in = False
    login_process = True
    while login_process == True:
        try:
            if to_login == "yes":
                account_login_name = input(p_account_login_name)                      
                account_login_password = input(p_account_login_password)
                global user_name
                user_name = account_login_name
                
                establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                                    host='localhost',
                                    database='user_profiles')
                mycursor = establish_sql_connection.cursor()   
                point_to_username_cell = mycursor.execute(f"SELECT Name FROM user_login_data WHERE Name = '{account_login_name}'")
                mycursor.execute(point_to_username_cell)
                the_name_cell = mycursor.fetchall()
                the_users_username = the_name_cell[0][0]

                point_to_password_cell = mycursor.execute(f"SELECT Password FROM user_login_data WHERE Name = '{account_login_name}'")
                mycursor.execute(point_to_password_cell)
                the_password_cell = mycursor.fetchall()
                the_users_password = the_password_cell[0][0]
                
                if account_login_name == the_users_username and account_login_password == the_users_password:                   

                    loged_in = True
                    login_process = False
                    print(f"Welcome {account_login_name}, You have successfully logged into your account")

                    establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                                    host='localhost',
                                    database='user_profiles')
                    mycursor = establish_sql_connection.cursor()
                    point_to_user = mycursor.execute(f"SELECT * FROM user_profiles WHERE Name = '{user_name}'")
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
                loged_in = False
                user_name =  None 

            else:
                print("Invalid input. Program shutting down for security. Please restart.")
                login_process = False
                user_name = None

        except IndexError:
                print("Oops, looks like you entered a value that is not in our database.\nThe program will close now for security.")
                user_name = None
                login_process = False
                        
        else: 
            pass      
        
    return loged_in, user_name


#Function that generates each unit of currency___________________________________________________________________________________
#This function generates each individual unit of the local currency based on the individuals background. 
def unit_currency():                                                         
    currency_multiplier = 3.142
    currency_multiplier = decimal.Decimal(currency_multiplier)
    establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                            host='localhost',
                            database='user_profiles')
    mycursor = establish_sql_connection.cursor()
    point_to_cell = mycursor.execute(f"SELECT Education_coefficient FROM user_profiles WHERE Name = '{user_name}'")
    mycursor.execute(point_to_cell)
    the_cell = mycursor.fetchall()
    edco = the_cell
    for x in edco[0]:
        education_coefficient = x
        education_coefficient = decimal.Decimal(education_coefficient)     
    point_to_cell = mycursor.execute(f"SELECT Skill_coefficient FROM user_profiles WHERE Name = '{user_name}'")
    mycursor.execute(point_to_cell)
    the_cell = mycursor.fetchall()
    skico = the_cell
    for y in skico[0]:
        skill_coefficient = y
    each_unit =  (skill_coefficient * currency_multiplier * education_coefficient) / 100 
    time_stamp = time.strftime("%H%M%S")
    the_hasher = str(hash(each_unit))
    individual_currency_id = (each_unit,"t",time_stamp,"h",the_hasher)
    return each_unit,"t",time_stamp,"h",the_hasher


#Creating the central bank class_______________________________________________________________________________________________
#This class represents the central bank.
class CentralBank():            

    def __init__(self):                           
        pass

    def __str__(self):
        print("The Central Bank is responsible for all monetary policy\n and is the only institution to issue loans.\nAll loan requests will come from the banks total reserves,\n and will only be approved if there are sufficient reserves.")


#Total central bank reserves________________________________________________________________________________________________
#This code block calculates the total reserves based on the total number of user profiles registered on the database in mysql.
def bank_reserves():
    today = datetime.today()                                                        
    each_unit = unit_currency()
    each_unit_currency = each_unit[0]
    establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                            host='localhost',
                            database='user_profiles')
    establish_sql_connection.ping(reconnect=False, attempts=1, delay=0)
    mycursor = establish_sql_connection.cursor()
    mycursor.execute("SELECT * FROM user_profiles")
    number_of_rows = mycursor.fetchall()
    total_users = 0
    for row in number_of_rows:
        total_users = total_users + 1
    total_users
    total_reserves = (total_users * each_unit_currency) + 1000               
    return total_reserves        


#User bank account for transactions______________________________________________________________________________________
#The bank account block allows each user to conduct transactions using their individual bank accounts. The class also ensures that transactions are
#recorded on all associated accounts on the database in mysql.
class UserBankAccount():
    
    def __init__(self, name, age, the_date, location, account_balance, contact_number, contact_email, main_skill, education_training):   
        self.name = name
        self.age = age
        self.the_date = the_date
        self.location = location
        self.account_balance = account_balance
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.education_training = education_training
        self.main_skill = main_skill
 

    def payment():
        user_payment = True  
        while loged_in and user_payment: 
            payment_request = input(f"Hello {user_name}, do you want to make a payment? yes or no?: ") 
            payment_request = payment_request.lower()

            if payment_request == "yes":
                transaction_identifier = input(p_transaction_identifier)
                transaction_identifier = transaction_identifier.lower()
                payment_amount = input(p_payment_amount)
                payment_amount = decimal.Decimal(payment_amount)
                establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                                host='localhost',
                                database='user_profiles')
                query = "SELECT * FROM user_profiles"
                mycursor = establish_sql_connection.cursor()
                mycursor.execute(query)
                the_profiles = mycursor.fetchall()

                for row in the_profiles:
                    if row[0] == user_name:
                        account_balance = row[4] 
                        updated_payers_account = account_balance - payment_amount
                        table_updater = f"UPDATE user_profiles SET account_balance = '{updated_payers_account}' WHERE name = '{user_name}'"
                        mycursor.execute(table_updater)
                        establish_sql_connection.commit()

                for row in the_profiles:
                    if row[0] == transaction_identifier:
                        account_balance = row[4] 
                        updated_recipient_account = account_balance + payment_amount
                        table_updater = f"UPDATE user_profiles SET account_balance = '{updated_recipient_account}' WHERE name = '{transaction_identifier}'"
                        mycursor.execute(table_updater)
                        establish_sql_connection.commit()

                print(f"{user_name} your payment of {payment_amount} to {transaction_identifier} was successful.")
                user_payment = False

            elif payment_request == "no":
                user_payment = False 
                print("Payment cancelled")     


    def loan():
        user_loan = True
        while loged_in  and user_loan:
            total_reserves = bank_reserves()                                                               
            loan_initiator = input(f"{user_name} do you need a loan from the bank? type yes or no?: ")
            loan_initiator = loan_initiator.lower()

            if loan_initiator == "yes":
                loan_amount = input(p_loan_amount)
                loan_amount = decimal.Decimal(loan_amount)
                if total_reserves > loan_amount:
                    print(f"{user_name} your loan of {loan_amount} has been approved and\nthe funds are now in your account.")
                    establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                                    host='localhost',
                                    database='user_profiles')
                    query = "SELECT * FROM user_profiles"
                    mycursor = establish_sql_connection.cursor()
                    mycursor.execute(query)
                    the_profiles = mycursor.fetchall()
                    
                    for row in the_profiles:
                        if row[0] == user_name:
                            account_balance = row[4] 
                            updated_account_with_loan = account_balance + loan_amount
                            table_updater = f"UPDATE user_profiles SET account_balance = '{updated_account_with_loan}' WHERE name = '{user_name}'"
                            mycursor.execute(table_updater)
                            establish_sql_connection.commit()
                    user_loan = False

                elif total_reserves < loan_amount:
                    print("Unfortunately the amount you are requesting is not available at the moment.")
                    user_loan = False

            elif loan_initiator == "no":
                user_loan = False 
                print("Loan cancelled.")
            print("____________")

############call functions and test runs____________________________________________________________________________
start_program()


