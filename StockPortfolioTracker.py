# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_investment = 0

print("=== Stock Investment Tracker ===")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
with open("investment_report.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Report saved to investment_report.txt")