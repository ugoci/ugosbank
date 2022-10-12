from datetime import date, datetime
import time

#global variables__________________________________________________________________________________
yes = "yes"
no  = "no"
today = datetime.today()
account_balance = 0

#variables for registration_______________________________________________________________________ 
p_opening_message = "Welcome to The Bank of Ugo!\nFounded in September 2022.\nYou are on the homepage,\nPress 1 to log in if you have an account,\nPress 2 to sign up if you do not already have an account with us: "
p_confirm_logout = "Are you sure that you want to logout? yes or no?"
p_account_actions = "What would you like to do next?\nPress 1 for payment,\nPress 2 for loan,\nPress 3 to logout: "
p_welcome_message = "Welcome to the bank. Do you want to register and start earning? Type out a response\n - 'yes' to register\n - 'no' to exit\n - 'help' for instructions\n - 'privacy' to read our privacy statement: "
p_name = "Pease indicate your first and last name: "
p_age = "Indicate your age: "
p_current_date = date.today()
p_the_date = p_current_date.strftime("%Y-%m-%d")
p_location = "Indicate your location: "
p_contact_number = "Indicate your 8-digit contact phone number: "
p_contact_email = "Please indicate your email address: "         
p_main_skill = "Indicate your main skill by chooing from the options(press 1 for I.T, 2 for Analysis, 3 for Crafts, 4 for Mechanics, 5 for Physical Labour, 6 for Soft Skills): "
p_education_training = "Indicate your highest level of education by choosing from the options (press 1 for No formal education, 2 for primary, 3 for secondary, 4 for vocational, 5 for university, 6 for post graduate: "
p_set_password = "Please set a secure password for your account: "
p_to_login = "Hello, would  you like to log into your account? please type yes or no?: "
p_account_login_name = "Username: "
p_account_login_password = "Password: "
p_transaction_identifier = "Who is receiving the payment?: "
p_payment_amount = "How much is this payment?: "
p_loan_amount = f"What is the loan amount that you are requesting?: "
p_check_skill_database = "Look through the list of skills in the new window and\ncheck the number that corresponds to your main skill.\nType yes when you are ready to see the skill list: "



privacy_statment = """Privacy Policy\n
This Privacy Policy describes Our policies and procedures on the collection, use and disclosure of Your information when You use the Service
and tells You about Your privacy rights and how the law protects You.
We use Your Personal data to provide and improve the Service. By using the Service, You agree to the collection and use of information
in accordance with this Privacy Policy.\n
Interpretation and Definitions\n
Interpretations:
The words of which the initial letter is capitalized have meanings defined under the following conditions.
The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.\n
Definitions:
Account means a unique account created for You to access our Service or parts of our Service.
Business refers to the Company as the legal entity that collects Consumers personal information and determines the purposes and means of the
processing of Consumers personal information, or on behalf of which such information is collected and that alone,
or jointly with others, determines the purposes and means of the processing of consumers personal information, that
does business in the State.
Company (referred to as either 'the Company', 'We', "Us" or "Our" in this Agreement)\n
For the purpose of the GDPR, the Company is the Data Controller.
'Consumer', means a natural person.
"Cookies" are small files that are placed on Your computer, mobile device or any other device by a website, containing the details of Your browsing
history on that website among its many uses.
"Data Controller", for the purposes of the GDPR (General Data Protection Regulation), refers to the Company as the legal person which alone
or jointly with others determines the purposes and means of the processing of Personal Data.
"Device" means any device that can access the Service such as a computer, a cell phone or a digital tablet.
"Do Not Track" (DNT)” is a concept that has been promoted by US regulatory authorities, in particular the U.S. Federal Trade Commission (FTC),
for the Internet industry to develop and implement a mechanism for allowing internet users to control the tracking of their online activities
across websites.
"Personal Data" is any information that relates to an identified or identifiable individual.\n
For the purposes of GDPR, Personal Data means any information relating to You such as a name, an identification number, location data,
online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity.
"Sale", means selling, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating orally,
in writing, or by electronic or other means, a Consumers personal information to another business or a third party for monetary or other
valuable consideration.
"Service" refers to the Website.
"Service Provider" means any natural or legal person who processes the data on behalf of the Company. It refers to third-party companies
or individuals employed by the Company to facilitate the Service, to provide the Service on behalf of the Company, to perform services
related to the Service or to assist the Company in analyzing how the Service is used. For the purpose of the GDPR, Service Providers are
considered Data Processors.
'Usage Data' refers to data collected automatically, either generated by the use of the Service or from the Service infrastructure itself
(for example, the duration of a page visit).
'You' means the individual accessing or using the Service, or the company, or other legal entity on behalf of which such individual is
accessing or using the Service, as applicable.\n
Under GDPR (General Data Protection Regulation), You can be referred to as the Data Subject or as the User as you are the individual
using the Service.\n
Types of Data Collected
While using Our Service, We may ask You to provide Us with certain personally identifiable information that can be used to contact or identify You
Personally identifiable information may include, but is not limited to:
-Email address
-First name and last name
-Phone number
-Address, State, Province, ZIP/Postal code, City
-Usage Data"""

list_of_skills = {
"Accounting": 1,
"Active listening": 2,
"Acute care": 3,
"Adaptability": 4,
"Administration": 5,
"Advanced Cardiac Life Support": 6,
"Assessing":7,
"Attention to detail": 8,
"B2B Marketing": 9,
"Blueprint drafting": 10,
"Brainstorming": 11,
"Brand management": 12,
"Business Development": 13,
"C": 14,
"C++": 15,
"Calculating": 16,
"Coaching": 17,
"Code-switching": 18,
"Collaboration": 19,
"Compassion": 20,
"Conceptual thinking": 21,
"Conflict management": 22,
"Constructing": 23,
"Conversing": 24,
"Copywriting": 25,
"Cost-benefit analyzing": 26,
"CPR": 27,
"Creative thinking": 28,
"Crisis managing": 29,
"Critical thinking": 30,
"Customer service": 31,
"Data analysis": 32,
"Data visualizing": 33,
"Deductive reasoning": 34,
"Delegating": 35,
"Directing": 36,
"Documenting": 37,
"Editing": 38,
"Effective communication": 39,
"Emotional intelligence": 40,
"Evaluating": 41,
"Evidence collecting": 42,
"Experimenting": 43,
"Explaining": 44,
"Extrapolating": 45,
"Extroversion": 46,
"Flexibility": 47,
"Forecasting": 48,
"Goal-setting": 49,
"Graphic designing": 50,
"HTML & CSS": 51,
"Illustrating": 52,
"Inductive reasoning": 53,
"Infection control": 54,
"Inferring": 55,
"Influencing": 56,
"Information processing": 57,
"Innovation": 58,
"Inquiring": 59,
"Inspiring": 60,
"Interior designing": 61,
"Interpreting": 62,
"Investigating": 63,
"Java": 64,
"Languages": 65,
"Leadership": 66,
"Machinery skills": 67,
"Managing": 68,
"Marketing": 69,
"Mathematics": 70,
"Mediating": 71,
"Mentoring": 72,
"Modeling": 73,
"Motivating": 74,
"Negotiating": 75,
"Networking": 76,
"Nonverbal communication": 77,
"Observing": 78,
"Open-mindedness": 79,
"Organization & planning": 80,
"Patience": 81,
"People management": 82,
"Photo and video editing": 83,
"Positivity": 84,
"Presenting": 85,
"Problem-solving": 86,
"Product developing": 87,
"Project/campaign management": 88,
"Proofreading": 89,
"Proposal writing": 90,
"Public speaking": 91,
"Python": 92,
"Reporting": 93,
"Researching": 94,
"Sales": 95,
"SEO/SEM": 96,
"Statistical analysis": 97,
"Storytelling": 98,
"Strategic Management": 99,
"Stress management": 100,
"Supervising": 101,
"Surgery preparation": 102,
"Surveying": 103,
"Teaching": 104,
"Teamwork": 105,
"Time management": 106,
"Training": 107,
"Typography": 108,
"User experience development": 109,
"Web analytics": 110,
"Web designing": 111,
"Wireframing": 112,
"Wordpress": 113,
"Writing": 114,
"Written communication": 115}


skill_coefficient_list = {
"Accounting": 6.2,
"Active listening": 5,
"Acute care": 7,
"Adaptability": 5,
"Administration": 4,
"Advanced Cardiac Life Support": 6,
"Assessing":5.5,
"Attention to detail": 6,
"B2B Marketing": 6,
"Blueprint drafting": 3.5,
"Brainstorming": 3,
"Brand management": 3.7,
"Business Development": 6.5,
"C": 7.5,
"C++": 7.5,
"Calculating": 2,
"Coaching": 3,
"Code-switching": 1.7,
"Collaboration": 3,
"Compassion": 3,
"Conceptual thinking": 6.4,
"Conflict management": 5,
"Constructing": 4,
"Conversing": 2,
"Copywriting": 3,
"Cost-benefit analyzing": 3.7,
"CPR": 7,
"Creative thinking": 7,
"Crisis managing": 5.7,
"Critical thinking": 6.6,
"Customer service": 3,
"Data analysis": 5.3,
"Data visualizing": 5,
"Deductive reasoning": 6,
"Delegating": 1,
"Directing": 5.6,
"Documenting": 3,
"Editing": 3.5,
"Effective communication": 3.8,
"Emotional intelligence": 3,
"Evaluating": 3,
"Evidence collecting": 3,
"Experimenting": 4.6,
"Explaining": 3,
"Extrapolating": 4,
"Extroversion": 1,
"Flexibility": 7,
"Forecasting": 5.9,
"Goal-setting": 2,
"Graphic designing": 6.6,
"HTML & CSS": 7,
"Illustrating": 5,
"Inductive reasoning": 6,
"Infection control": 7,
"Inferring": 5,
"Influencing": 6,
"Information processing": 6.7,
"Innovation": 8,
"Inquiring": 5,
"Inspiring": 7,
"Interior designing": 3,
"Interpreting": 3,
"Investigating": 5,
"Java": 7.5,
"Languages": 7,
"Leadership": 7.8,
"Machinery skills": 6,
"Managing": 6,
"Marketing": 6,
"Mathematics": 7.5,
"Mediating": 5,
"Mentoring": 7,
"Modeling": 6,
"Motivating": 7,
"Negotiating": 6,
"Networking": 7,
"Nonverbal communication": 5,
"Observing": 4,
"Open-mindedness": 4,
"Organization & planning": 6,
"Patience": 4,
"People management": 5,
"Photo and video editing": 5,
"Positivity": 4,
"Presenting": 4,
"Problem-solving": 6.8,
"Product developing": 6,
"Project/campaign management": 6.9,
"Proofreading": 2,
"Proposal writing": 4,
"Public speaking": 4,
"Python": 7.5,
"Reporting": 5,
"Researching": 5.8,
"Sales": 6,
"SEO/SEM": 5,
"Statistical analysis": 7,
"Storytelling": 7.6,
"Strategic Management": 7.9,
"Stress management": 7,
"Supervising": 6.8,
"Surgery preparation": 7,
"Surveying": 5,
"Teaching": 6,
"Teamwork": 6,
"Time management": 5,
"Training": 4,
"Typography": 4,
"User experience development": 5.7,
"Web analytics": 6,
"Web designing": 6.1,
"Wireframing": 5.9,
"Wordpress": 7,
"Writing": 7.3,
"Written communication": 5}



