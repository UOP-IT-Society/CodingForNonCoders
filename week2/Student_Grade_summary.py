
students = {
    "Alice": [85, 92, 78],
    "Bob": [79, 88, 91],
    "Charlie": [95, 90, 93]
}

for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{student}: {average:.2f}")

    