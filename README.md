# North Sussex Judo Cost Calculator

A Python console-based application developed as part of an academic programming assignment for the BSc (Hons) Information Technology programme.

The application calculates monthly training fees for athletes enrolled at North Sussex Judo based on their training plan, competition entries, private coaching hours, and competition weight category.

## Project Overview

North Sussex Judo required a simple program to calculate monthly athlete training costs. The program allows users to enter athlete details, select a training plan, add competition details, include private coaching hours, and generate an itemised monthly cost summary.

## Features

- Add new athlete records
- Select training plans: Beginner, Intermediate, or Elite
- Calculate monthly training fees based on weekly plan prices
- Calculate private coaching costs
- Calculate competition entry fees
- Restrict competition entry to Intermediate and Elite athletes
- Store and view previous athlete records
- Display costs formatted as currency
- Validate user input and handle invalid entries
- Compare athlete weight against selected competition weight category

## Technologies Used

- Python
- Console-based application development
- Functions and modular programming
- Dictionaries and data structures
- Input validation
- Conditional logic
- Cost calculation algorithms

## Business Rules Implemented

- Beginner plan: £25 per week
- Intermediate plan: £30 per week
- Elite plan: £35 per week
- Private tuition: £9.50 per hour
- Competition fee: £22 per competition
- Maximum private coaching: 5 hours per week
- Only Intermediate and Elite athletes can enter competitions
- One month is calculated as 4 weeks

## Weight Categories

| Category | Upper Weight Limit |
|---|---:|
| Heavyweight | Over 100kg |
| Light-Heavyweight | 100kg |
| Middleweight | 90kg |
| Light-Middleweight | 81kg |
| Lightweight | 73kg |
| Flyweight | 66kg |

## Learning Outcomes

This project helped strengthen my understanding of Python programming fundamentals, algorithm design, data handling, user input validation, conditional logic, and applying business rules within a working application.

## Future Improvements

- Add a graphical user interface
- Save athlete records to a file or database
- Add edit and delete record functionality
- Improve weight category comparison logic
- Generate printable monthly reports
