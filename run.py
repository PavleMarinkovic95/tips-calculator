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
    while True:
        print("Please enter your tips from monday to friday in dollars \n")
        print("Your data should be 5 numbers, separated by commas")
        print("Example: 9, 5.5, 10.2, 4, 5\n")
        
        data_str = input("Enter your tips here: ")
        
        tips_data = data_str.split(",")
        
        if validate_tips(tips_data):
            print ("Data is valid \n")
            break

    return tips_data
    
def validate_tips(values):
    # Inside the try, we convert the the string values to floats
    # If the value cannot be converted, throw an Error, 
    # If there are not 5 values for 5 days of the week, also throw Error
    try:
        [float(value) for value in values]1
        if len(values) != 5:
            raise ValueError(
                f"Exatcly five values are required, you provided {len(values)}"
            )  
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")  
        return False
    return True

get_tips_data()
