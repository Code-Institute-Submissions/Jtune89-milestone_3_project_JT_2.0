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
SHEET = GSPREAD_CLIENT.open('House Budget')

#managing household budgets by inputting amounts spent on household/entertainment costs, showing remaining balance

def get_rent_mortgage_data():
    """
    gets the householder to input the data required
    """
    print ("Enter the month for data you want to input data for")
    print ("i.e. January or February etc\n")

    data_str = input ("Enter the month: ")
    print(f"The data provided is {data_str}")

get_rent_mortgage_data()