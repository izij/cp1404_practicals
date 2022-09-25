total_price = 0
number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))

for item in range(number_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price - total_price * 0.1

print(f"Total price for {number_items} is ${total_price:.2f}")
