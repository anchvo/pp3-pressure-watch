# Testing

The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome Message | User is given a welcome message | Weclome message presented | Works as expected |
| Instructions | User is given instructuctions | Instruction message presented | Works as expected |
| Examples | User is given a input examples | Instruction message presented | Works as expected |
| Systolic Numbers Input | User is asked to enter their systolic numbers | Systolic numbers input  | Works as expected |
| Systolic Numbers Input | User inputs data other than number | Error message appears | Works as expected |
| Systolic Numbers Input | User inputs numbers less or more than 7 | Error message appears | Works as expected |
| Instructions | User is given instructuctions | Instruction message appears | Works as expected |
| Examples | User is given a input examples | Instruction message appears | Works as expected |
| Diastolic Numbers Input | User is asked to enter their diastolic numbers | Diastolic numbers input  | Works as expected |
| Diastolic Numbers Input | User inputs data other than number | Error message appears | Works as expected |
| Diastolic Numbers Input | User inputs numbers less or more than 7 | Error message appears | Works as expected |
| Information | User is informed that systolic input data is updated | Updating process notice appears | Works as expected |
| Information | User is informed that systolic database was updated | Succesful update notice appears | Works as expected |
| Information | User is informed that diastolic input data is updated | Updating process notice appears | Works as expected |
| Information | User is informed that diastolic database was updated | Succesful update notice appears | Works as expected |
| Information | User is informed that average systolic is calculated | Calculate average systolic notice appears | Works as expected |
| Information Result | User is informed about their average systolic | Message with calculated average systolic appears | Works as expected |
| Information | User is informed that average diastolic is calculated | Calculate average diastolic notice appears | Works as expected |
| Information Result | User is informed about their average diastolic | Message with calculated average diastolic appears | Works as expected |
| Information | User is informed that average systolic data is updated | Updating process notice appears | Works as expected |
| Information | User is informed that average systolic database was updated | Succesful update notice appears | Works as expected |
| Information | User is informed that average diastolic data is updated | Updating process notice appears | Works as expected |
| Information | User is informed that average diastolic database was updated | Succesful update notice appears | Works as expected |
| Information | User is informed that classification database is checked | Checking database notice appears | Works as expected |
| Information | User is informed about the classification of their blood pressure as low and gets recommendations | Low blood pressure message appears | Works as expected |
| Information | User is informed about the classification of their blood pressure as normal and gets recommendations | Normal blood pressure message appears | Works as expected |
| Information | User is informed about the classification of their blood pressure as high and gets recommendations | High blood pressure message appears | Works as expected |
| End Message | User is an ending and thank you message | Ending message appears | Works as expected |
| Information | User is informed about how to start program again | Restart message appears | Works as expected |


## Testing Browsers
The program was tested in the following browsers by myself and others: 

- Firefox 
- Brave
- Safari

It worked without issues in the above browsers

## Testing Google Sheets

The attached Google Sheets was manually tested to check if user input shows up correctly. 
At the start of the program, only the classification worksheet contains data that is set. 

The pressure worksheet contains names but no numbers that can be used. The needed numbers are filled in by the user input for systolic and diastolic data. This works as expected.

The average worksheet also contains names but no numbers. The needed numbers are filled in after a calculation function runs and passed the correct numbers. This works as expected. 

The classification workheet contains all necessary data. The data is used in a calculation function, that compares the average number to the classification numbers. This works as expected.

Data passed to the Sheet are cleared out via a clear function at the end of the program. This works as expected.

## Python Validation

The Python code was run through the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#) and returned no errors.

![Pressure Watch CI Python Linter](assets/screenshots/pressure-watch-ci-python-linter.png)





