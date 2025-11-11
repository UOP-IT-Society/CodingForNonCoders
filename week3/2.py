import csv
def find_hottest_day(filename):
    hottest_day = ""
    max_temp = float('-inf')
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            day = row[0]
            temp = float(row[1])
            if temp > max_temp:
                max_temp = temp
                hottest_day = day
    return hottest_day

# Example usage:
filename = 'week3/temperatures.csv'
hottest_day = find_hottest_day(filename)
print(f"The hottest day is: {hottest_day}")