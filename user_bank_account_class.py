#Module list_______________________________________________________________________________________________________________
import mysql.connector
import decimal
from variables import p_transaction_identifier
from variables import p_payment_amount
from variables import p_loan_amount
from variables import USER_NAME
from variables import LOGED_IN
from security_authentication_functions import account_log_in
from central_bank_class import CentralBank
from accessing_database_class import AccessDatabase


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
        LOGED_IN = account_log_in()
        while LOGED_IN and user_payment: 
            payment_request = input(f"Hello {USER_NAME}, do you want to make a payment? yes or no?: ") 
            payment_request = payment_request.lower()

            if payment_request == "yes":
                transaction_identifier = input(p_transaction_identifier)
                transaction_identifier = transaction_identifier.lower()
                payment_amount = input(p_payment_amount)
                payment_amount = decimal.Decimal(payment_amount)
                AccessDatabase.accessing_userprofiles_database()
                accesser = AccessDatabase.accessing_userprofiles_database()
                establish_sql_connection = accesser[0]
                mycursor = accesser[1]
                the_profiles = accesser[2]

                for row in the_profiles:
                    if row[0] == USER_NAME:
                        account_balance = row[4] 
                        updated_payers_account = account_balance - payment_amount
                        table_updater = f"UPDATE user_profiles SET account_balance = '{updated_payers_account}' WHERE name = '{USER_NAME}'"
                        mycursor.execute(table_updater)
                        establish_sql_connection.commit()

                for row in the_profiles:
                    if row[0] == transaction_identifier:
                        account_balance = row[4] 
                        updated_recipient_account = account_balance + payment_amount
                        table_updater = f"UPDATE user_profiles SET account_balance = '{updated_recipient_account}' WHERE name = '{transaction_identifier}'"
                        mycursor.execute(table_updater)
                        establish_sql_connection.commit()

                print(f"{USER_NAME} your payment of {payment_amount} to {transaction_identifier} was successful.")
                user_payment = False

            elif payment_request == "no":
                user_payment = False 
                print("Payment cancelled")  


    def loan():
        user_loan = True
        LOGED_IN = account_log_in()
        while LOGED_IN  and user_loan:
            total_reserves = CentralBank.bank_reserves()                                                               
            loan_initiator = input(f"{USER_NAME} do you need a loan from the bank? type yes or no?: ")
            loan_initiator = loan_initiator.lower()

            if loan_initiator == "yes":
                loan_amount = input(p_loan_amount)
                loan_amount = decimal.Decimal(loan_amount)
                if total_reserves > loan_amount:
                    print(f"{USER_NAME} your loan of {loan_amount} has been approved and\nthe funds are now in your account.")
                    AccessDatabase.accessing_userprofiles_database()
                    accesser = AccessDatabase.accessing_userprofiles_database()
                    establish_sql_connection = accesser[0]
                    mycursor = accesser[1]
                    the_profiles = accesser[2]
                    
                    for row in the_profiles:
                        if row[0] == USER_NAME:
                            account_balance = row[4] 
                            updated_account_with_loan = account_balance + loan_amount
                            table_updater = f"UPDATE user_profiles SET account_balance = '{updated_account_with_loan}' WHERE name = '{USER_NAME}'"
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

