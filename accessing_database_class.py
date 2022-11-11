#Module list_______________________________________________________________________________________________________________
import mysql.connector


#Accessing the database class_______________________________________________________________________________________________
#This class includes all the functions needed to access the database and various tables saved in the database.

class AccessDatabase():

    def accessing_userprofiles_database():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM user_profiles"
        mycursor = establish_sql_connection.cursor()
        mycursor.execute(query)
        the_profiles = mycursor.fetchall()
        return establish_sql_connection, mycursor, the_profiles

#the databases below have been created but not yet integrated to the rest of the program

    def accessing_skill_database():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM skill_database"
        skill_db_cursor = establish_sql_connection.cursor()
        skill_db_cursor.execute(query)
        the_skills = skill_db_cursor.fetchall()
        return establish_sql_connection, skill_db_cursor, the_skills
    
    def accessing_user_skills():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM user_skill"
        user_skill_cursor = establish_sql_connection.cursor()
        user_skill_cursor.execute(query)
        users_skill = user_skill_cursor.fetchall()
        return establish_sql_connection, user_skill_cursor, users_skill

    def accessing_education_database():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM education_database"
        education_db_cursor = establish_sql_connection.cursor()
        education_db_cursor.execute(query)
        the_education = education_db_cursor.fetchall()
        return establish_sql_connection, education_db_cursor, the_education

    def accessing_user_education():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM user_education"
        user_education_cursor = establish_sql_connection.cursor()
        user_education_cursor.execute(query)
        users_education = user_education_cursor.fetchall()
        return establish_sql_connection, user_education_cursor, users_education

    def accessing_user_bank_account_database():
        establish_sql_connection = mysql.connector.connect(user='root', password='PASSWORD-TO-CHANGE',
                                host='localhost',
                                database='user_profiles')
        query = "SELECT * FROM user_bank_account"
        account_db_cursor = establish_sql_connection.cursor()
        account_db_cursor.execute(query)
        the_account = account_db_cursor.fetchall()
        return establish_sql_connection, account_db_cursor, the_account

