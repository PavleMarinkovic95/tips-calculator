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
        [float(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Exatcly five values are required, you provided {len(values)}"
            )  
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")  
        return False
    return True

def update_worksheet1(tips):
    #This updates the google spreadsheet
    print("Updating tips worksheet")
    tips_worksheet = SHEET.worksheet("tips")
    tips_worksheet.append_row(tips)
    print("Tips worksheet updated successfully... \n")

def update_worksheet2(tips):
    print("Updating weekly average")
    weekly_avg = SHEET.worksheet("week")
    weekly_avg.append_row(tips)
    print("Updated weekly average successfully...\n")


def calculate_weekly_avg(tips):
    #Calculates the weekly average per day earned in tips
    #Also gives the total of the week in question in dollars
    print("Calculating weekly average and total in $\n")
    this_week = []
    average = sum(tips)/len(tips)
    print(f"The weekly average per day is {average} dollars")
    print(f"The total money earend this week is {sum(tips)} dollars\n")
    this_week = [average, sum(tips)]
    return this_week


def main():
    # Runs all program functions :)
    tips = get_tips_data()
    tips_data = [float(i) for i in tips]
    update_worksheet1(tips_data)
    new_tips_data = calculate_weekly_avg(tips_data)
    update_worksheet2(new_tips_data)
    


print("Welcome to tips calculator\n")
print("The objective of this program is to calculate the weekly average of your tips")
print("If you are in a proffesion, lets say working as a waiter, this app is for you")
print("The app also gives the total cash just in tips that you earned in the last month")
print("For new usesrs it would need atleast 4 seperate inputs to give a accurate reading...\n")
main()
