# ==============================================================================
# FILE: 07_dictionaries.py
# TOPIC: Dictionaries (Hash Maps), Safe Access, Iteration, and Merging
# ==============================================================================

# 1. CREATING DICTIONARIES
# Dictionaries store data as Key: Value pairs.
# Keys must be unique and immutable (strings, ints, tuples). Values can be anything.
user_profile = {
    "username": "vishaltechstack",
    "role": "QA Engineer",
    "experience_years": 1,
    "skills": ["Java", "Selenium", "Python", "SQL"],
    "is_available": True
}

# 2. ACCESSING VALUES SAFELY
print("Username:", user_profile["username"])    # Direct lookup (raises KeyError if key missing)

# .get(key, default) returns None (or your custom default) instead of crashing!
print("Location:", user_profile.get("location", "Not Specified"))

# 3. ADDING, UPDATING & REMOVING KEYS
user_profile["city"] = "Noida"                  # Adds a new key-value pair
user_profile["experience_years"] = 2            # Updates existing key's value

# Merge/update multiple keys at once using update() or '|' operator (Python 3.9+):
extra_info = {"github": "github.com/vishaltechstack", "open_to_work": True}
merged_profile = user_profile | extra_info

# Removing keys:
removed_val = merged_profile.pop("is_available")
print(f"Removed 'is_available' ({removed_val})")

# 4. ITERATING OVER DICTIONARIES
print("\n--- Profile Details ---")
for key, value in user_profile.items():         # .items() yields (key, value) tuples
    print(f"{key}: {value}")

# You can also iterate over .keys() or .values() independently:
print("All keys:", list(user_profile.keys()))

# 5. PRACTICAL PATTERN: FREQUENCY COUNTER WITH .get()
# Counting occurrences of items in a list cleanly:
log_statuses = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL"]
status_counts = {}

for status in log_statuses:
    # Fetch current count (default 0) and add 1
    status_counts[status] = status_counts.get(status, 0) + 1

print("\nTest Execution Summary:", status_counts)  # {'PASS': 3, 'FAIL': 2, 'SKIP': 1}
