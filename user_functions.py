#Module list_______________________________________________________________________________________________________________
from datetime import date, datetime
import re
import mysql.connector
from variables import p_welcome_message
from variables import p_name
from variables import p_location
from variables import p_contact_number
from variables import p_contact_email
from variables import p_check_skill_database
from variables import list_of_skills
from variables import skill_coefficient_list
from variables import p_education_training
from variables import p_set_password
from variables import USER_NAME
from dialogue_box_opening_functions import open_skilldatabase_window
from dialogue_box_opening_functions import open_privacystatement_window
from accessing_database_class import AccessDatabase


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
                name = get_name() 
                age = check_age()
                the_date = get_date() 
                location = get_location()
                contact_number = get_contact_number()
                contact_email = get_email()

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
                
                USER_NAME = name                            
                user_password = input(p_set_password)       

                each_profile = (name, age, the_date, location, account_balance, contact_number, contact_email, main_skill, education_training,education_coefficient, skill_coefficient)
                AccessDatabase.accessing_userprofiles_database()
                accesser = AccessDatabase.accessing_userprofiles_database()
                establish_sql_connection = accesser[0]
                mycursor = accesser[1]
                insert_to_userprofiles_table = "INSERT INTO user_profiles (Name, Age, Date, Location, Account_balance, Contact_number, Contact_email, Main_skill, Skill_coefficient, Education_training, Education_coefficient) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(insert_to_userprofiles_table, each_profile)
                establish_sql_connection.commit()

                insert_to_logindata_table = "INSERT INTO user_login_data (Name, Password) VALUES (%s,%s)"
                value_to_insert = (f"{USER_NAME}", f"{user_password}")
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



#Get name function gets the users name___________________________________________________________________________________________________
def get_name():
    name = input(p_name) 
    name = name.lower()
    return name   


#cehck age function gets the users age_____________________________________________________________________________________________________
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
    return age


#Get date function gets the current date___________________________________________________________________________________________________
def get_date():
    current_date = date.today()
    the_date = current_date.strftime("%Y-%m-%d") 
    return the_date


#Get location gets the current location_____________________________________________________________________________________________________
def get_location():
    location = input(p_location) 
    location = location.lower()
    return location


#Get contact number gets the uers contact number____________________________________________________________________________________________
def get_contact_number():
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
    return contact_number


#Get email gets the users email address___________________________________________________________________________________________________
def get_email():
    contact_email = input(p_contact_email) 
    contact_email = contact_email.lower()
    ce = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', contact_email)   
    if ce == object:
        pass 
    elif ce == None:
        print("please input a valid email address")   
        contact_email = input(p_contact_email) 
    return contact_email