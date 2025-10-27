### Question 1: Gradebook Analyzer

Write a **function** named `analyze_grades` that takes one argument: a **dictionary** where keys are student names (strings) and values are **lists** of their integer scores.

Your function must:
1.  **Loop** through the dictionary.
2.  For each student, use **operations** to calculate their average score.
3.  Use **conditionals** to assign a letter grade ('A' for >= 90, 'B' for >= 80, 'C' for >= 70, 'F' otherwise).
4.  Store these results in **variables**.
5.  Return a new **dictionary** where each student's name maps to a **tuple** containing `(average_score, letter_grade)`.

---

### Question 2: Shopping Cart Calculator

Write a **function** named `calculate_total` that takes two arguments:
* `cart`: A **list** of item names (strings) a customer wants to buy.
* `prices`: A **dictionary** mapping item names (strings) to their prices (floats).

Your function must:
1.  Initialize a **variable** for the total cost.
2.  **Loop** through the `cart` **list**.
3.  For each item, use **conditionals** to check if it exists in the `prices` **dict**. If it does, use **operations** to add its price to the total.
4.  After the loop, use a **conditional** to apply a 10% discount (`total * 0.9`) *only if* the total is over $100.
5.  Return a formatted **f-string** showing the final price, e.g., `"Your total is: $123.45"`.

---

### Question 3: Unique Activity Logger

Write a **function** named `get_active_users` that takes one argument: a **list** of **tuples**. Each tuple represents a user action, formatted as `(user_id, action_type)`.

Your function must:
1.  Initialize an empty **set** to store unique user IDs.
2.  **Loop** through the **list** of tuples.
3.  Inside the loop, use **conditionals** to check if the `action_type` is exactly `'login'`.
4.  If it is, add the `user_id` to your **set**.
5.  After the loop, return the **set** of unique users who logged in.

---

### Question 4: Inventory Management

Write a **function** named `update_inventory` that takes two arguments:
* `inventory`: A **dictionary** where keys are item names (strings) and values are the stock count (integers).
* `sales`: A **list** of items (strings) that were sold.

Your function must:
1.  **Loop** through the `sales` **list**.
2.  For each sold item, use **conditionals** to check if the item is a key in the `inventory` **dict**.
3.  If it is, use **operations** to decrease its stock count in the `inventory` **dict** by 1.
4.  After processing all sales, create a new **list** containing the names of all items in the `inventory` **dict** whose stock is now 0.
5.  Return this "out of stock" **list**.

---

### Question 5: Profile Summary Generator

Write a **function** named `create_summary` that takes a single **dictionary** called `profile` as an argument. This dictionary will contain:
* `'name'`: A string.
* `'age'`: An integer.
* `'hobbies'`: A **list** of strings (which may contain duplicates).

Your function must:
1.  Use **variables** to store the 'name' and 'age' from the `profile` **dict**.
2.  Use a **set** to find the *number* of *unique* hobbies.
3.  Use **conditionals** and **operations** to create a `status` **variable**:
    * 'Active' if `age` < 65 AND they have 3 or more unique hobbies.
    * 'Relaxed' if `age` >= 65.
    * 'Casual' for all other cases.
4.  Return a single **f-string** that combines all this information, e.g., `"{name}, age {age}, has {num_unique_hobbies} unique hobbies. Status: {status}."`
