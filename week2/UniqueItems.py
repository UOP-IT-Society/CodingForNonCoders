# Define the two lists of user IDs
list1 = ['user1', 'user2', 'user3', 'user4']
list2 = ['user3', 'user4', 'user5', 'user6']

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Find all unique users across both lists
unique_users = set1 | set2
print("All unique users:", unique_users)
# Find users who are in both lists
common_users = set1 & set2
print("Users in both lists:", common_users)
# Find users who are in the first list but not the second
unique_to_list1 = set1 - set2
print("Users in the first list but not the second:", unique_to_list1)

list1 = ['user1', 'user2', 'user3', 'user4']