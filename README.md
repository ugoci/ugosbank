# ugosbank

Capstone project for CodingNomads
* Project title: The Bank of Ugo (The BU)
* Thanks to my mentor Deniz Y. and the CodingNomads team
_________________________

## Overview

This ReadMe provides an overview of a Fintech program that I wrote as my capstone project for the CodingNomads python bootcamp. Digital currencies are a great way to transfer value in a digital world. Right now, there's a big focus on digital currencies (especially crypto currencies) as stores of value. I think that as a means of exchange, digital currencies could be one of the best tools we use to overcome poverty (in its current form). Think about informal economies where value is created everyday but not captured. With a digital currency that can be deployed easily on mobile devices, you create opportunities for a huge percentage of the world's population. Mobile Money is the perfect example of this in reality. I'm exploring digital currency models that could serve as a reliable means of exchange. This program is still a long way from that, but this is the backstory to why I started working on it. 

## How the program works  

The program works by taking a set of user inputs to create each unique user profile. These profiles are then registered unto a MySQL database. Based on each users background, they are able to earn a native currency that varies by user. Once users are registered, they have a bank account that allows them to transact with other registered users. The program is built using python 3, tkinter and mysql databases.

## Requirements 

* greenlet==2.0.0
* mysql==0.0.3
* mysql-connector==2.2.9
* mysql-connector-python==8.0.31
* mysqlclient==2.1.1
* prettyprint==0.1.5
* protobuf==3.20.1
* PyMySQL==1.0.2
* tk==0.1.0

## Installation and running the program

* Use the package manager [pip] to install the packages listed in the requirements.
* Use the file start_fintech_program.py to run the program

## Usage

Additional files needed to run the program are:
* accessing_database_class.py
* central_bank_class.py
* dialogue_box_opening_functions.py
* security_authentication_functions.py
* user_bank_account_class.py
* user_functions.py
* variables.py

## Creating databases in MySQL

###### Notes on the database

Create two tables. The first just holds the username and password. The second holds all the other info that is collected as part of the registration process.

###### Creating the tables in MySQL

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
