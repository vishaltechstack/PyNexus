# ==============================================================================
# FILE: 05_lists.py
# TOPIC: Lists (Ordered, Mutable Sequences), Methods, Iteration, and Copying
# ==============================================================================

# 1. CREATING LISTS
# Lists hold items of any data type (even mixed types) in a defined order.
tools = ["Selenium", "TestNG", "Maven", "Jenkins"]
mixed_list = [101, "Python", 3.14, True]
empty_list = []

# 2. INDEXING & SLICING (Works just like strings)
print("First tool:", tools[0])                  # 'Selenium'
print("Last tool:", tools[-1])                  # 'Jenkins'
print("First two tools:", tools[:2])            # ['Selenium', 'TestNG']

# 3. MUTABILITY (MODIFYING IN PLACE)
# Unlike strings, list elements can be changed directly using their index.
tools[2] = "Gradle"                             # Replaces 'Maven' with 'Gradle'
print("After modification:", tools)

# 4. ADDING ELEMENTS
tools.append("Docker")                          # Adds single item to the END
tools.insert(1, "Pytest")                       # Inserts 'Pytest' at index 1
tools.extend(["Git", "GitHub"])                 # Appends multiple items from another iterable
print("After additions:", tools)

# 5. REMOVING ELEMENTS
tools.remove("Gradle")                          # Removes FIRST matching value (raises ValueError if missing)
popped_item = tools.pop()                       # Removes & returns the LAST item ('GitHub')
popped_at_idx = tools.pop(1)                    # Removes & returns item at index 1 ('Pytest')
del tools[0]                                    # Deletes item at index 0 without returning it
print(f"Popped: {popped_item}, Remaining list: {tools}")

# 6. SORTING, REVERSING & SEARCHING
numbers = [42, 7, 19, 7, 85, 3]

print("Count of 7:", numbers.count(7))          # 2
print("Index of 85:", numbers.index(85))        # 4 (First occurrence)
print("Is 19 in list?", 19 in numbers)          # True (Membership test)

# sorted(list) returns a NEW sorted list (leaves original unchanged).
# list.sort() sorts the list IN-PLACE and returns None.
asc_numbers = sorted(numbers)
numbers.sort(reverse=True)                      # In-place descending sort
print("Original sorted desc:", numbers)
print("New sorted asc copy:", asc_numbers)

# 7. ITERATING WITH enumerate()
# Use enumerate() when you need BOTH the index and the value during a loop.
frameworks = ["Playwright", "Cypress", "Appium"]
for idx, fw in enumerate(frameworks, start=1):
    print(f"Framework #{idx}: {fw}")

# 8. CRITICAL TRAP: REFERENCE ASSIGNMENT VS COPYING
# Doing 'b = a' does NOT create a new list; both variables point to the SAME memory!
original = [[1, 2], [3, 4]]
alias = original                                # Same memory reference
shallow_copy = original.copy()                  # New outer list, but inner lists still shared

import copy
deep_copy = copy.deepcopy(original)             # Completely independent nested copy

original[0][0] = 999
print("Shallow copy affected by nested change:", shallow_copy)  # [[999, 2], [3, 4]]
print("Deep copy stays safe:", deep_copy)                       # [[1, 2], [3, 4]]
