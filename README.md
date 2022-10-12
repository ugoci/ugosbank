# ugosbank

Capstone project for CodingNomads
* Project title: The Bank of Ugo (The BU)
* Thanks to my mentor Deniz Y. 
_________________________

This ReadMe provides an overview of a Fintech program that I wrote as my capstone project for the CodingNomads python bootcamp. Digital currencies are a great way to transfer value in a digital world. Right now, there's a big focus on digital currencies (especially crypto currencies) as stores of value. I think that as a means of exchange, digital currencies could be one of the best tools we use to overcome poverty (in its current form). Think about informal economies where value is created everyday but not captured. With a digital currency that can be deployed easily on mobile devices, you create opportunities for a huge percentage of the world's population. Mobile Money is the perfect example of this in reality. I'm exploring digital currency models that could serve as a reliable means of exchange. This program is still a long way from that, but this is the backstory to why I started working on it. 

1. Structure 

	The program works by taking a set of user inputs to create each unique user profile. These profuiles are then registered unto a 
	MySQL database. Based on each users background, they are able to earn a local currency that varies by user. Once users are registered,
	they have a bank account that allows them to transact with other users in the community. 
	The program is built using python 3, tkinter (a GUI and mysql databases.

2. Modules needed to run the program successfully

   - from datetime import date, datetime
   - import time
   - import re
   - from tkinter import END
   - import mysql.connector
   - import pymysql
   - from pprint import pp
   - import decimal
   - from variables import *
   - from cpsfunctions import *
   - from tkinter import *

3. Libraries used in this program including their versions 
   
   - greenlet==1.1.3
   - mysql==0.0.3
   - mysql-connector-python==8.0.30
   - mysqlclient==2.1.1
   - prettyprint==0.1.5
   - protobuf==3.20.1
   - PyMySQL==1.0.2
   - SQLAlchemy==1.4.41
   - tk==0.1.0

4. Functions have been created for the following tasks

   - start_program - This function starts the program and manages the users interactions with the program. 
   - registration - This function allows new users to register with the "bank". This function also saves each user profile on a dedicated database for user profiles.
   - open skill database window - This function opens a new window with a list of skills, each with a number assigned to it. The block uses tkinter to create the new window.
   - open privacy statement window - This function opens a new window with a privacy statement for the user.
   - check age - This block checks the user has input numbers at the right length and that the user is not below the age of 18.
   - account login - This function sets the conditions for the user to log into their account. The details from this process allow the user to interact with other aspects of the program as a whole. Here, the username is assigned and turned into a global variabel so that it can be accesed by other functions.
   - unit_currency - This function generates each unit of currency based on the individuals background. each unit of currency also has a timestamp and a hash nunmber.
   - bank reserves - This function calculates the total reserves based on the total number of user profiles registered on the database in mysql.

5. Classes where created for the following

   - CentralBank class: this class represents the central repository of all currencies 		 
     - UserBankAccount class: this class represents each users account and allows each account to carry out transactions
   - functions under the UserBankAccount class are:
     - payment: this function allows each user to make payments. this class should ideally interact with all accounts impacted by the payment, i.e. the payer and receiver
     - loan: this function allows users to request for loans. loans should be possible from other users or from the CentralBank

6.	Databases were created with the processes below

step 1 establishing the connection to the database:

```	
establish_sql_connection = mysql.connector.connect(user='root', password='Anthropod@2022',
                              host='localhost',
                              database='user_profiles')
```

step 2 creating the cursor:

```
mycursor = establish_sql_connection.cursor()
```

step 3 creating a table:

```
table_headings = '''CREATE TABLE USER_PROFILES(
    Name VARCHAR(255) NOT NULL,
    Age INT,
    Date DATE,
    Location VARCHAR(255),
    Account_balance DEC,
    Contact_number INT,
    Contact_email VARCHAR(255),
    Main_skill VARCHAR(255),
    Skill_coefficient DEC,
    Education_training VARCHAR(255),
    Education_coefficient FLOAT
)'''
mycursor.execute(table_headings)
```

step 4 inserting data to the table:

```insert_to_table = "INSERT INTO user_profiles (Name, Age, Date, Location, Account_balance, Contact_number, Contact_email, Main_skill, Skill_coefficient, Education_training, Education_coefficient) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

value_to_insert = ("a name", age, "year-month-day", "city", int figure, "phone number", "email@testemail.com", "a skill", auto_assigned, "education level", auto_assigned)

mycursor.execute(insert_to_table, value_to_insert)

establish_sql_connection.commit()```

