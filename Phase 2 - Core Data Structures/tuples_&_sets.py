# ==============================================================================
# FILE: 06_tuples_and_sets.py
# TOPIC: Tuples (Immutable Sequences) and Sets (Unique Unordered Collections)
# ==============================================================================

# ==============================================================================
# PART A: TUPLES
# ==============================================================================

# 1. CREATING TUPLES
# Tuples are ordered like lists, but IMMUTABLE (cannot add, remove, or change items).
# They use less memory and are faster than lists—ideal for fixed records.
coordinates = (28.6139, 77.2090)

# Single-element tuple trap: MUST include a trailing comma!
not_a_tuple = (50)                              # This is just an int (50)
single_tuple = (50,)                            # This is a tuple of length 1
print("Type of single_tuple:", type(single_tuple))

# Attempting coordinates[0] = 10.0 raises: TypeError: 'tuple' object does not support item assignment

# 2. TUPLE UNPACKING (Very common in Python!)
# Assigning tuple elements directly to multiple variables in one step:
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Extended unpacking using '*' (collects remaining items into a list):
record = ("Vishal", "QA Automation", "Java", "Python", "SQL")
name, role, *tech_stack = record
print(f"Name: {name} | Role: {role} | Skills: {tech_stack}")

# ==============================================================================
# PART B: SETS
# ==============================================================================

# 3. CREATING SETS & AUTOMATIC DEDUPLICATION
# Sets store ONLY unique, hashable items. Duplicates are automatically discarded.
# Note: Use set() for an empty set; {} creates an empty dictionary!
raw_ids = [101, 102, 102, 103, 104, 104, 104]
unique_ids = set(raw_ids)
print("Deduplicated IDs:", unique_ids)          # {101, 102, 103, 104}

# Adding and removing from a set (O(1) average lookup time—extremely fast!):
unique_ids.add(105)
unique_ids.discard(999)                         # Safe remove: does NOT raise error if missing
# unique_ids.remove(999)                        # Raises KeyError if missing

# 4. MATHEMATICAL SET OPERATIONS
# Ideal for comparing datasets, tags, or database records.
backend_devs = {"Amit", "Neha", "Raj", "Priya"}
qa_engineers = {"Raj", "Priya", "Karan", "Sneha"}

# Union (|): Everyone in either team
print("All team members (Union):", backend_devs | qa_engineers)

# Intersection (&): People who belong to BOTH teams
print("Cross-functional (Intersection):", backend_devs & qa_engineers)

# Difference (-): People in backend_devs who are NOT in qa_engineers
print("Only Backend (Difference):", backend_devs - qa_engineers)

# Symmetric Difference (^): People in one team or the other, but NOT both
print("Exclusive to one team:", backend_devs ^ qa_engineers)
