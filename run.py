import gspread
from google.oauth2.service_account import Credentials

# Values of variables do not change so they 
# are constant variables written in capital letters

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Lists APIs that the program should access in order to run

CREDS = Credentials.from_service_account_file("creds.json")
# Uses a method from the Credentials class that was imported
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pressure_watch")
# Opens the exel sheet in google account that was set up before, 
# name needs to be exact

def get_pressure_data():
    """
    Get the blood pressure numbers (systolic and diastolic) 
    via input from the user.
    """
    print("Please enter your systolic (upper number) and diastolic (lower number) blood pressure numbers for the last seven days.")
    print("Numbers should be separated by commas.")
    print("Example: 110, 115, 105, 98, 113, 99, 102\n")

    data_str_one = input("Enter your systolic numbers here:\n")

    pressure_systolic_data = data_str_one.split(",")

    print(f"The numbers you entered are: {pressure_systolic_data}")

    data_str_two = input("Enter your diastolic numbers here:\n")

    pressure_diastolic_data = data_str_two.split(",")

    print(f"The numbers you entered are: {pressure_diastolic_data}")



        
def main():
    """
    Run all program functions
    """
    data = get_pressure_data()

main()
