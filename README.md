# CodeAlpha_StockPortfolio

A simple **Stock Portfolio Tracker** built in Python as part of my **CodeAlpha Python Programming Internship (Task 2)**.

The program lets you enter the stocks you own along with their quantities, looks up each price from a predefined list, and calculates your total investment value. You can also save the summary to a text or CSV file.

---

## Features

- User enters stock symbols and quantities
- Stock prices are stored in a hardcoded dictionary
- Calculates the value of each holding and the total investment
- Input validation (rejects unknown symbols and invalid quantities)
- Combines duplicate entries automatically
- Optionally saves the result to a `.txt` or `.csv` file

---

## Concepts Used

- Dictionaries
- Input / Output
- Basic arithmetic
- File handling (txt and csv)
- Functions
- Loops and conditionals

---

## Available Stocks

| Symbol | Price per share |
|--------|-----------------|
| AAPL   | $180            |
| TSLA   | $250            |
| GOOGL  | $140            |
| AMZN   | $130            |
| MSFT   | $300            |
| NFLX   | $500            |

---

## How to Run

1. Make sure **Python 3** is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```bash
python stock_tracker.py
```

4. Follow the on-screen prompts to enter your stocks and view the total.

---

## Sample Output

```
========================================
        YOUR PORTFOLIO SUMMARY
========================================
AAPL    10 share(s) x $180 = $1800
TSLA    5 share(s) x $250 = $1250
----------------------------------------
TOTAL INVESTMENT VALUE: $3050
========================================
```

---

## Author

**Aaryan Verma**
CodeAlpha Python Programming Intern

---

## Acknowledgement

Thanks to **CodeAlpha** for the internship opportunity and this project task.
