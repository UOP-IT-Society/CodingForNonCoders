def calculate_total(cart, prices):
    total = 0.0
    for item in cart:
        if item in prices:
            total += prices[item]
    if total > 100:
        total *= 0.9
    return f"Your total is: ${total:.2f}"

# Example usage:
cart = ["apple", "banana", "orange", "steak", "salmon"]
prices = {
    "apple": 1.20,
    "banana": 0.50,
    "orange": 0.80,
    "steak": 25.00,
    "salmon": 30.00,
    "bread": 2.50
}