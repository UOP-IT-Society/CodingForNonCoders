def analyze_grades(grades_dict):
    results = {}
    for student, scores in grades_dict.items():
        average_score = sum(scores) / len(scores) if scores else 0
        if average_score >= 90:
            letter_grade = 'A'
        elif average_score >= 80:
            letter_grade = 'B'
        elif average_score >= 70:
            letter_grade = 'C'
        else:
            letter_grade = 'F'
        results[student] = (average_score, letter_grade)
    return results

# Example usage:
grades = {
    "Alice": [95, 85, 92],
    "Bob": [78, 82, 80],
    "Charlie": [60, 65, 70]
}

results = analyze_grades(grades)
print(results)