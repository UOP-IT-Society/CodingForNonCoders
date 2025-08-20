
inventory = {"cats" : 99999, "bananas": 22, "type_writers":101}
for items in inventory:
    if inventory[items] > 0:
        print(f"Sold one {items}")
        inventory[items] -= 1

        if inventory[items] == 0:
            print(f"Out of stock: {items}")

print("Current inventory:", inventory)