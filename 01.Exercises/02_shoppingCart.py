# shopping cart program

item=input('What would you like to buy: ')
price=float(input("What is the price: "))
qty=int(input("How many: "))

total=price * qty

print(f'You have bought {qty} X {item}')
print(f"your total {total}")
