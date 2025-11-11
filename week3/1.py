# Method 1: Using readlines()
def count_items_readlines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)
    return 0

# Method 2: Using a loop
def count_items_loop(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    return count

# Example usage:
filename = 'shopping_list.txt'
item_count_readlines = count_items_readlines(filename)
item_count_loop = count_items_loop(filename)
print(f"Number of items (using readlines): {item_count_readlines}")
print(f"Number of items (using loop): {item_count_loop}")