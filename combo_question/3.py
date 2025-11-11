
def get_active_users(actions):
    active_users = set()
    for user_id, action_type in actions:
        if action_type == 'login':
            active_users.add(user_id)
    return active_users

# Example usage:
actions = [
    (1, 'login'),
    (2, 'logout'),
    (1, 'view'),
    (3, 'login'),
    (2, 'login'),
    (3, 'logout'),
    (4, 'login'),
    (1, 'logout')
]

active_users = get_active_users(actions)
print(active_users)  # Output: {1, 2, 3, 4}