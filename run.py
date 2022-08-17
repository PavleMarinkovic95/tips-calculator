from lib2to3.pgen2.token import SLASHEQUAL
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Setup APIs 
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tips_spreadsheet')

def get_tips_data():
    # Gets tips data from the user for the current week
    print("Please enter your tips from monday to friday in dollars \n")
    print("Your data should be 5 numbers, separated by commas")
    print("Example: 9, 5.5, 10.2, 4, 5\n")
    
    data_str = input("Enter your tips here: ")
    
    tips_data = data_str.split(",")
    validate_tips(tips_data)
    


get_tips_data()
