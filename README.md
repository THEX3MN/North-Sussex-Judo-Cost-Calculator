# North Sussex Judo Cost Calculator

A Python console-based application developed as part of an academic programming assignment for the BSc (Hons) Information Technology programme.

The system calculates monthly training fees for athletes at North Sussex Judo by applying training plan costs, private coaching charges, competition fees, eligibility rules, and athlete weight category details.

## Project Overview

North Sussex Judo required a simple application to calculate the monthly cost of training for athletes. The application allows users to register athlete details, select a training plan, enter competition information, add private coaching hours, and generate an itemised monthly cost summary.

The project demonstrates beginner-level software development using Python, including modular programming, data structures, validation, conditional logic, calculations, and menu-driven application design.

## Features

* Add new athlete records
* Select training plans: Beginner, Intermediate, or Elite
* Calculate monthly training fees based on weekly plan prices
* Calculate private coaching costs
* Calculate competition entry fees
* Restrict competition entry to Intermediate and Elite athletes
* Store and view previous athlete records during program execution
* Display itemised monthly cost summaries
* Format all costs as currency
* Validate user input and display suitable error messages
* Display the selected competition weight category for each athlete

## Technologies Used

* Python
* Console-based application development
* Functions and modular programming
* Dictionaries and data structures
* Conditional logic
* Loops and menu-driven programming
* Input validation
* Cost calculation algorithms

## Business Rules Implemented

* Beginner training plan: £25.00 per week
* Intermediate training plan: £30.00 per week
* Elite training plan: £35.00 per week
* Private coaching fee: £9.50 per hour
* Competition fee: £22.00 per competition
* Maximum private coaching allowed: 5 hours per week
* Only Intermediate and Elite athletes can enter competitions
* One month is calculated as 4 weeks
* Costs are displayed to two decimal places

## Weight Categories

| Category           | Upper Weight Limit |
| ------------------ | -----------------: |
| Heavyweight        |         Over 100kg |
| Light-Heavyweight  |              100kg |
| Middleweight       |               90kg |
| Light-Middleweight |               81kg |
| Lightweight        |               73kg |
| Flyweight          |               66kg |

## Screenshots

### Main Menu

![Main Menu](Main%20Menu.png)

### Adding Athlete Record

![Adding Athlete Record](Adding%20Athlete%20Record.png)

### Record Summary

![Record Summary](Record%20Summary.png)

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the Python file using the command below:

```bash
python main.py
```

## Example Workflow

1. Start the program.
2. Select the option to add a new athlete record.
3. Enter the athlete name, training plan, current weight, competition category, competitions entered, and private coaching hours.
4. The program calculates the monthly cost and displays an itemised summary.
5. Previous records can be viewed from the main menu.

## Assignment Brief

The assignment brief is included in this repository as:

```text
Assignment Brief.pdf
```

It contains the original scenario, client requirements, business rules, and development expectations for the application.

## Learning Outcomes

This project helped strengthen my understanding of:

* Python programming fundamentals
* Algorithm design and implementation
* Data handling using dictionaries and lists
* User input validation
* Menu-driven application development
* Applying business rules in a working program
* Formatting output for readability
* Structuring a simple console-based software solution

## Future Improvements

* Add a graphical user interface
* Save athlete records to a file or database
* Add edit and delete functionality for athlete records
* Improve weight category comparison logic
* Add stronger validation for private coaching limits
* Generate printable monthly reports or invoices
* Add automated tests for calculation functions
