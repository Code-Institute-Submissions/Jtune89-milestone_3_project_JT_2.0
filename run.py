import gspread
from google.oauth2.service_account import Credentials
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('House Budget')

#managing household budgets by inputting amounts spent on household/entertainment costs, showing remaining balance

get_date = input ("Enter the date: ")

day, month, year = get_date.split('/')

isValidDate = True
try:
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False

if(isValidDate):
    print("The date is valid ..")
else:
    print("The date you have input is not valid..")

