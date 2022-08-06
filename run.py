import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Quiz Results')


# Welcome message to Quiz
print("Welcome to the most AMAZING quiz that ever was or will be \n")

#user_information
input ("What is your name? \nName: ")
print ("\nWelcome (name) & good luck!  Lets start with question 1:")

# QUESTION 1
input ("\n What is the capital of India? \n a. New Delhi \n b. Mumbai \n c. Jaipur \n d. Kolkata \n Answer: ")
print (input)
