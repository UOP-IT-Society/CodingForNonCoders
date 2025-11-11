def create_summary(profile):
    name = profile.get('name', 'Unknown')
    age = profile.get('age', 0)
    hobbies = profile.get('hobbies', [])
    
    unique_hobbies = set(hobbies)
    num_unique_hobbies = len(unique_hobbies)
    
    if age < 65 and num_unique_hobbies >= 3:
        status = 'Active'
    elif age >= 65:
        status = 'Relaxed'
    else:
        status = 'Casual'
    
    return f"{name}, age {age}, has {num_unique_hobbies} unique hobbies. Status: {status}."

# Example usage:
profile = {
    'name': 'John Doe',
    'age': 70,
    'hobbies': ['reading', 'gardening', 'reading', 'traveling']
}
summary = create_summary(profile)
print(summary)  # Output: "John Doe, age 70, has 3 unique hobbies. Status: Relaxed."