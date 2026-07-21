"""
CodeAlpha - Task 2: Stock Portfolio Tracker
Author: Aaryan Verma

A simple stock portfolio tracker.
- User enters stock names and quantities
- Stock prices come from a hardcoded dictionary
- Calculates and displays the total investment value
- Optionally saves the result to a .txt or .csv file
Concepts used: dictionary, input/output, basic arithmetic, file handling
"""

import csv

# Hardcoded dictionary of stock prices (stock symbol -> price per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300,
    "NFLX": 500,
}


def show_available_stocks():
    # Display the list of stocks the user can choose from
    print("\nAvailable stocks and their prices:")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} -> ${price}")
    print("-" * 35)


def build_portfolio():
    # Collect the user's stocks and quantities into a dictionary
    portfolio = {}   # stock symbol -> quantity owned

    print("\nEnter the stocks you own. Type 'done' when finished.")

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        # Stop asking once the user is done
        if symbol == "DONE":
            break

        # Make sure the stock exists in our price list
        if symbol not in STOCK_PRICES:
            print(f">> '{symbol}' is not in our price list. Please choose from the available stocks.")
            continue

        # Ask for the quantity and validate it
        quantity_input = input(f"Enter quantity of {symbol}: ").strip()
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print(">> Please enter a valid whole number greater than 0.")
            continue

        quantity = int(quantity_input)

        # If the stock was already added, add to the existing quantity
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        print(f">> Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_and_display(portfolio):
    # Calculate the value of each holding and the grand total
    print("\n" + "=" * 40)
    print("        YOUR PORTFOLIO SUMMARY")
    print("=" * 40)

    total_value = 0
    summary_lines = []   # store rows so we can save them to a file later

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity     # basic arithmetic
        total_value += value

        line = f"{symbol:<6}  {quantity} share(s) x ${price} = ${value}"
        print(line)
        summary_lines.append(line)

    print("-" * 40)
    print(f"TOTAL INVESTMENT VALUE: ${total_value}")
    print("=" * 40)

    return total_value, summary_lines


def save_result(portfolio, total_value, summary_lines):
    # Ask the user if they want to save, and in which format
    choice = input("\nDo you want to save the result to a file? (y/n): ").lower().strip()
    if choice != "y":
        print("Result not saved.")
        return

    file_format = input("Save as (txt/csv): ").lower().strip()

    if file_format == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("YOUR PORTFOLIO SUMMARY\n")
            f.write("=" * 30 + "\n")
            for line in summary_lines:
                f.write(line + "\n")
            f.write("-" * 30 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value}\n")
        print(">> Saved to portfolio.txt")

    elif file_format == "csv":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                writer.writerow([symbol, quantity, price, price * quantity])
            writer.writerow(["", "", "TOTAL", total_value])
        print(">> Saved to portfolio.csv")

    else:
        print(">> Unknown format. Result not saved.")


def main():
    print("=" * 40)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    show_available_stocks()
    portfolio = build_portfolio()

    # Handle the case where the user didn't add any stocks
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    total_value, summary_lines = calculate_and_display(portfolio)
    save_result(portfolio, total_value, summary_lines)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
