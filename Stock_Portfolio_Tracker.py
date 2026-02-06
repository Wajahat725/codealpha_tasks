import tkinter as tk
from tkinter import messagebox
import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = []
total_investment = 0

def add_stock():
    global total_investment

    stock = stock_entry.get().upper()
    quantity = quantity_entry.get()

    if stock == "" or quantity == "":
        messagebox.showerror("Error", "All fields are required")
        return

    if stock not in STOCK_PRICES:
        messagebox.showerror("Error", "Stock not available")
        return

    try:
        quantity = int(quantity)
    except:
        messagebox.showerror("Error", "Quantity must be a number")
        return

    price = STOCK_PRICES[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append((stock, quantity, price, investment))

    portfolio_list.insert(
        tk.END,
        f"{stock} | Quantity: {quantity} | Price: {price} | Value: {investment}"
    )

    total_label.config(text=f"Total Investment: ${total_investment}")

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def save_portfolio():
    if not portfolio:
        messagebox.showwarning("Warning", "Portfolio is empty")
        return

    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for item in portfolio:
            writer.writerow(item)
        writer.writerow(["", "", "Total", total_investment])

    messagebox.showinfo("Saved", "Portfolio saved as portfolio.csv")

# GUI Setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("500x450")
root.resizable(True, True)

tk.Label(root, text="📈 Stock Portfolio Tracker", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Stock Name:").grid(row=0, column=0, padx=5, pady=5)
stock_entry = tk.Entry(frame)
stock_entry.grid(row=0, column=1)

tk.Label(frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(frame)
quantity_entry.grid(row=1, column=1)

tk.Button(root, text="Add Stock", width=20, command=add_stock).pack(pady=10)

portfolio_list = tk.Listbox(root, width=65, height=10)
portfolio_list.pack(pady=10)

total_label = tk.Label(root, text="Total Investment: $0", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

tk.Button(root, text="Save to CSV", width=20, command=save_portfolio).pack(pady=10)

root.mainloop()
