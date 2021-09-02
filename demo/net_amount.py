# Display net amount by taking price and qty and applying 10% discount

price = float(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty
discount = amount * 0.10
net_amount = amount - discount

print(f'Net Amount = {net_amount:6.2f}')

