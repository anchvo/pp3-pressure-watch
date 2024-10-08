# Imports
import gspread
from google.oauth2.service_account import Credentials
from rich import print

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


# Functions


def get_pressure_data_one():
    """
    Get the systolic blood pressure numbers
    via input from the user.
    """
    while True:
        # First loop for user input to repeat asking for input
        # while first set of data is invalid
        print(("Please enter your [underline]systolic[/underline]"
              "(upper number) blood pressure numbers "
               "for the last seven days."))
        print("[italic]Numbers should be separated by commas.[/italic]")
        print("[italic]Example: 110, 115, 105, 98, 113, 99, 102\n[/italic]")

        data_str_one = input("Enter your systolic numbers here:\n")

        pressure_systolic_data = data_str_one.split(",")

        if validate_pressure_data(pressure_systolic_data):
            # Breaks the loop if data is valid and ends user input
            print("[italic green]Data is valid!\n[/italic green]")
            break
    return pressure_systolic_data
    # Returns valid systolic data after user input was validated


def get_pressure_data_two():
    """
    Get the diastolic blood pressure numbers
    via input from the user.
    """
    while True:
        # Second loop for user input to repeat asking for input
        # while second set of data is invalid
        print(("Please enter your [underline]diastolic[/underline]"
              "(lower number) blood pressure numbers "
               "for the last seven days."))
        print("[italic]Numbers should be separated by commas.[/italic]")
        print("[italic]Example: 79, 82, 75, 72, 80, 71, 76\n[/italic]")

        data_str_two = input("Enter your diastolic numbers here:\n")

        pressure_diastolic_data = data_str_two.split(",")

        if validate_pressure_data(pressure_diastolic_data):
            # Breaks the loop if data is valid and ends user input
            print("[italic green]Data is valid!\n[/italic green]")
            break
    return pressure_diastolic_data
    # Returns valid diastolic data after user input was validated


def validate_pressure_data(values):
    """
    Checks if user input data is valid
    Converts all string values to integers inside the try
    Raises ValueError if strings cannot be converted into int
    or if there aren't exactly 7 values
    """
    try:
        # Code that should work with no errors if data is valid
        [int(value) for value in values]
        if len(values) != 7:
            # Should length of the values list not be seven (for seven days)
            raise ValueError(
                f"[red]Numbers for the last seven days are needed, "
                f"you provided {len(values)}.[/red]"
            )

    except ValueError as e:
        # Common shorthand variable e for error
        print(f"[red]Invalid data: {e}. Please try again.\n[/red]")
        return False
        # Returns False because data is invalid
        # which is picked up by while loop and tells it to continue running
    return True
    # Data is valid and returns true, tells the while loop to break


def update_systolic_data(data_one):
    """
    Updates systolic data in pressure worksheet,
    add a new row with the list data from data_one
    """
    print(
        "[italic yellow]Updating systolic pressure data...\n[/italic yellow]"
        )
    pressure_worksheet = SHEET.worksheet("pressure")
    pressure_worksheet.append_row(data_one, table_range="B2:H2")
    # Table_range refers to multiple cells together,
    # needs to be passed as second argument,
    # using A1 Notation
    print("[italic green]Database updated!\n[/italic green]")


def update_diastolic_data(data_two):
    """
    Updates diastolic data in pressure worksheet,
    add a new row with the list data from data_two
    """
    print(
        "[italic yellow]Updating diastolic pressure data...\n[/italic yellow]"
        )
    pressure_worksheet = SHEET.worksheet("pressure")
    pressure_worksheet.append_row(data_two, table_range="B3:H3")
    # Table_range refers to multiple cells together,
    # needs to be passed as second argument,
    # using A1 Notation
    print("[italic green]Database updated!\n[/italic green]")


def calculate_average_systolic():
    """
    Calculate the average systolic blood pressure
    over the last seven days based on provided data
    stored in worksheet
    """
    print("[italic yellow]Calculating average systolic...\n[/italic yellow]")

    pressure_worksheet = SHEET.worksheet("pressure")
    systolic_data = pressure_worksheet.get("B2:H2")

    systolic_list = sum(systolic_data, [])
    # Removes list from list of lists
    systolic_numbers = [int(num) for num in systolic_list]
    average = sum(systolic_numbers) / 7
    average_systolic = round(average)

    print(
        f"[bold]Your average systolic blood pressure\n"
        f"over the last seven days is {average_systolic}\n[/bold]"
        )
    return average_systolic


def calculate_average_diastolic():
    """
    Calculate the average diastolic blood pressure
    over the last seven days based on provided data
    stored in worksheet
    """
    print("[italic yellow]Calculating average diastolic...\n[/italic yellow]")

    pressure_worksheet = SHEET.worksheet("pressure")
    diastolic_data = pressure_worksheet.get("B3:H3")

    diastolic_list = sum(diastolic_data, [])
    # Removes list from list of lists
    diastolic_numbers = [int(num) for num in diastolic_list]
    average = sum(diastolic_numbers) / 7
    average_diastolic = round(average)

    print(
        f"[bold]Your average diastolic blood pressure\n"
        f"over the last seven days is {average_diastolic}\n[/bold]"
        )
    return average_diastolic


def update_average_systolic_data(average_systolic_pressure):
    """
    Updates average systolic data in average worksheet,
    add a new row with the calculated average
    """
    print("[italic yellow]Updating systolic average data...\n[/italic yellow]")
    average_worksheet = SHEET.worksheet("average")
    average_worksheet.update_acell("B2", average_systolic_pressure)
    # Acell refers to specific cell,
    # needs to be passed as first argument
    # using A1 Notation
    print("[italic green]Database updated!\n[/italic green]")


def update_average_diastolic_data(average_diastolic_pressure):
    """
    Updates average diastolic data in average worksheet,
    add a new row with the calculated average
    """
    print(
        "[italic yellow]Updating diastolic average data...\n[/italic yellow]"
        )
    average_worksheet = SHEET.worksheet("average")
    average_worksheet.update_acell("B3", average_diastolic_pressure)
    # Acell refers to specific cell,
    # needs to be passed as first argument
    # using A1 Notation
    print("[italic green]Database updated!\n[/italic green]")


def check_pressure_classification():
    """
    Compares the calculated average pressure data with
    the classification data in classification worksheet,
    gives result and recommendation to the user
    """
    print(
        "[italic yellow]Checking classification database...\n[/italic yellow]"
        )
    average_worksheet = SHEET.worksheet("average")
    classification_worksheet = SHEET.worksheet("classification")

    systolic_average = average_worksheet.get("B2")
    diastolic_average = average_worksheet.get("B3")
    systolic_pressure = sum(systolic_average, [])
    diastolic_pressure = sum(diastolic_average, [])
    # Removes list from list of lists
    systolic_pressure_number = [int(num) for num in systolic_pressure]
    diastolic_pressure_number = [int(num) for num in diastolic_pressure]

    low_systolic = classification_worksheet.get("B2")
    low_diastolic = classification_worksheet.get("B3")
    high_systolic = classification_worksheet.get("D2")
    high_diastolic = classification_worksheet.get("D3")

    low_systolic_pressure = sum(low_systolic, [])
    low_diastolic_pressure = sum(low_diastolic, [])
    high_systolic_pressure = sum(high_systolic, [])
    high_diastolic_pressure = sum(high_diastolic, [])
    # Removes list from list of lists

    low_systolic_number = [int(num) for num in low_systolic_pressure]
    low_diastolic_number = [int(num) for num in low_diastolic_pressure]
    high_systolic_number = [int(num) for num in high_systolic_pressure]
    high_diastolic_number = [int(num) for num in high_diastolic_pressure]

    if (systolic_pressure_number <= low_systolic_number
       and diastolic_pressure_number <= low_diastolic_number):
        print(("[bold red]Your average blood pressure is too low.\n"
              "You should seek medical advice!\n[/bold red]"))

    elif (systolic_pressure_number >= high_systolic_number
          and diastolic_pressure_number >= high_diastolic_number):
        print(("[bold red]Your average blood pressure is too high.\n"
              "You should seek medical advice!\n[/bold red]"))

    else:
        print(("[bold green]Your average blood pressure is normal.\n"
              "Regular check-ups are still advised!\n[/bold green]"))


def clear_sheet_data():
    """
    Clears input and calculated data from
    pressure and average worksheet after
    program is run through
    """
    pressure_worksheet = SHEET.worksheet("pressure")
    average_worksheet = SHEET.worksheet("average")

    pressure_worksheet.batch_clear(["B2:H2", "B3:H3"])
    average_worksheet.batch_clear(["B2", "B3"])
    # Batch_clear clears a range of multiple cells at once
    # using A1 Notation


def main():
    """
    Run all program functions
    """
    data_one = get_pressure_data_one()
    data_two = get_pressure_data_two()
    pressure_systolic_data = [int(num) for num in data_one]
    pressure_diastolic_data = [int(num) for num in data_two]
    # Converts both data sets from string to integers
    update_systolic_data(pressure_systolic_data)
    update_diastolic_data(pressure_diastolic_data)
    average_systolic_pressure = calculate_average_systolic()
    average_diastolic_pressure = calculate_average_diastolic()
    update_average_systolic_data(average_systolic_pressure)
    update_average_diastolic_data(average_diastolic_pressure)
    check_pressure_classification()
    clear_sheet_data()


print(
    f"[bold magenta]Welcome to Pressure Watch!:red_heart-emoji:\n"
    f"A quick and easy way to check "
    f"if your blood pressure is something to worry about!\n[/bold magenta]"
    )
# Welcome Message

main()

print(
    f"[bold magenta]Thank you for using Pressure Watch!"
    f":red_heart-emoji:[/bold magenta]\n"
    f"[italic]If you want to run again,\n"
    f"click the button 'Run Program' at the top![/italic]"
    )
# End and Restart Message
