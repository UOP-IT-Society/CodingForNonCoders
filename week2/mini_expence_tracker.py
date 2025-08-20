
expenses = []
total = 0
largest = 0
smallest = 0

for i in range(5):
    expense = float(input("Enter expense amount: "))
    expenses.append(expense)
    total = total + expense
    if expense > largest:
        largest = expense
    if expense < smallest:
        smallest = expense

average = total / len(expenses)
print("Total expenses:", total)
print("Average expense:", average)
print("Largest expense:", largest)
print("Smallest expense:", smallest)



# cleaner way 
expenses = []
for i in range(5):
    expense = float(input("Enter expense amount: "))
    expenses.append(expense)

total = sum(expenses)
average = total / len(expenses)
largest = max(expenses)
smallest = min(expenses)
print("Total expenses:", total)
print("Average expense:", average)
print("Largest expense:", largest)
print("Smallest expense:", smallest)
