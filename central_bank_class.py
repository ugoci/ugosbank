#Module list_______________________________________________________________________________________________________________
from datetime import date, datetime
import time
import mysql.connector
import decimal
from variables import USER_NAME
from variables import LOGED_IN
from accessing_database_class import AccessDatabase


#Central bank class_______________________________________________________________________________________________
#This class represents the central bank. This class includes the functions needed to run the central bank.

class CentralBank():            

    def __init__(self):                           
        pass

    def __str__(self):
        print("The Central Bank is responsible for all monetary policy\nand is the only institution to issue loans.\nAll loan requests will come from the banks total reserves,\n and will only be approved if there are sufficient reserves.")

    def unit_currency():                    
        #This function generates each individual unit of the native currency based on the individuals background.  
        USER_NAME = "ana"
        currency_multiplier = 3.142
        currency_multiplier = decimal.Decimal(currency_multiplier)
        AccessDatabase.accessing_userprofiles_database()
        accesser = AccessDatabase.accessing_userprofiles_database()
        mycursor = accesser[1]
        point_to_cell = mycursor.execute(f"SELECT Education_coefficient FROM user_profiles WHERE Name = '{USER_NAME}'")
        mycursor.execute(point_to_cell)
        the_cell = mycursor.fetchall()
        
        edco = the_cell
        for x in edco[0]:
            education_coefficient = x
            education_coefficient = decimal.Decimal(education_coefficient)     
        point_to_cell = mycursor.execute(f"SELECT Skill_coefficient FROM user_profiles WHERE Name = '{USER_NAME}'")
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


    def bank_reserves():
        #this function generates the total bank reserves for the central bank.
        total_users = 0
        today = datetime.today()                                                        
        each_unit = CentralBank.unit_currency()
        each_unit_currency = each_unit[0]
        AccessDatabase.accessing_userprofiles_database()
        accesser = AccessDatabase.accessing_userprofiles_database()
        mycursor = accesser[1]
        number_of_rows = mycursor.fetchall()
        
        for row in number_of_rows:
            print(row)
            total_users = total_users + 1
        total_users
        total_reserves = (total_users * each_unit_currency) + 1000               
        return total_reserves

