
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
final_price = price - (price * discount / 100)
print(f"The final price after discount is: {final_price}")
