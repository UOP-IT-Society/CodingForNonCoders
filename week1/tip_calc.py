total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you want to give: "))
tip_amount = (tip_percentage / 100) * total_bill
print(f"The tip amount is: {tip_amount}")
