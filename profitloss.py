cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("it is a profit")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("it is a loss")
else:
    print("No profit, no loss.")

