
def update_inventory(inventory, sales):
    for item in sales:
        if item in inventory:
            inventory[item] -= 1
    out_of_stock = [item for item, count in inventory.items() if count == 0]
    return out_of_stock

# Example usage:
inventory = {
    "apple": 5,
    "banana": 2,
    "orange": 0,
    "steak": 3,
    "salmon": 1
}
sales = ["apple", "banana", "banana", "salmon", "steak", "steak", "steak"]
out_of_stock_items = update_inventory(inventory, sales)
print(out_of_stock_items)  # Output: ['banana', 'salmon', 'steak']
