# ==============================================================================
# FILE: 08_comprehensions.py
# TOPIC: List, Dictionary, and Set Comprehensions (Clean, Concise Transformations)
# ==============================================================================

# Comprehensions provide a concise, readable, and faster way to build collections
# from existing iterables without writing multi-line 'for' loops with .append().

# 1. LIST COMPREHENSION
# Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional loop way:
squares_loop = []
for n in numbers:
    if n % 2 == 0:
        squares_loop.append(n ** 2)

# Pythonic comprehension way (Same result in 1 readable line):
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)            # [4, 16, 36, 64, 100]

# 2. LIST COMPREHENSION WITH IF-ELSE (Conditional Transformation)
# Note: When using 'else', the if-else goes BEFORE the 'for' keyword!
labels = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 6)]
print("Labels:", labels)                        # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# 3. FLATTENING A 2D MATRIX (Nested Comprehension)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [cell for row in matrix for cell in row]
print("Flattened matrix:", flattened)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. DICTIONARY COMPREHENSION
# Syntax: {key_expr: value_expr for item in iterable if condition}
languages = ["Python", "Java", "SQL", "JavaScript"]
name_lengths = {lang: len(lang) for lang in languages}
print("Language lengths:", name_lengths)        # {'Python': 6, 'Java': 4, 'SQL': 3, 'JavaScript': 10}

# Inverting keys and values of an existing dictionary:
status_codes = {"OK": 200, "NOT_FOUND": 404, "SERVER_ERROR": 500}
code_to_name = {code: name for name, code in status_codes.items()}
print("Inverted dict:", code_to_name)           # {200: 'OK', 404: 'NOT_FOUND', 500: 'SERVER_ERROR'}

# 5. SET COMPREHENSION
# Syntax: {expression for item in iterable if condition}
# Automatically removes duplicates while transforming data:
raw_emails = ["Admin@Test.com", "user@test.com", "ADMIN@test.com", "qa@test.com"]
unique_domains_or_emails = {email.strip().lower() for email in raw_emails}
print("Normalized unique emails:", unique_domains_or_emails)
