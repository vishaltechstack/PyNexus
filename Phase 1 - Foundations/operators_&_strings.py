# ==============================================================================
# FILE: 03_operators_and_strings.py
# TOPIC: Arithmetic, Comparison, Logical Operators, and String Manipulation
# ==============================================================================

# 1. ARITHMETIC OPERATORS
num1 = 17
num2 = 5

print("Addition (+):", num1 + num2)             # 22
print("Subtraction (-):", num1 - num2)          # 12
print("Multiplication (*):", num1 * num2)       # 85
print("True Division (/):", num1 / num2)        # 3.4 (Always returns a float)
print("Floor Division (//):", num1 // num2)     # 3 (Drops the remainder/decimal)
print("Modulus (%):", num1 % num2)              # 2 (Returns the remainder)
print("Exponentiation (**):", 2 ** 4)           # 16 (2 raised to the power 4)

# 2. COMPARISON & LOGICAL OPERATORS
# Comparison: ==, !=, >, <, >=, <= (Always return True or False)
# Logical: and, or, not (Python uses English words instead of &&, ||, !)
score = 85
attendance = 92

passed = (score >= 50) and (attendance >= 75)
print("Did student pass?", passed)              # True

# Identity Operators ('is' vs '=='):
# '==' checks if VALUES are equal.
# 'is' checks if both variables point to the EXACT SAME object in memory.
val = None
print("Is val None?", val is None)              # Always use 'is' when checking for None

# 3. STRING INDEXING & SLICING
# Strings are immutable (cannot be changed in-place) sequences of characters.
# Positive index:  0   1   2   3   4   5   6   7   8   9  10  11
# Text:            P   y   t   h   o   n   _   C   o   d   e   r
# Negative index: -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

title = "Python_Coder"

print("First character:", title[0])             # 'P'
print("Last character:", title[-1])             # 'r'

# Slicing syntax: string[start : stop : step] ('stop' index is excluded)
print("First 6 chars:", title[0:6])             # 'Python'
print("From index 7 to end:", title[7:])        # 'Coder'
print("Every 2nd character:", title[::2])       # 'Pto_oe'
print("Reversed string:", title[::-1])          # 'redoC_nohtyP'

# 4. ESSENTIAL STRING METHODS
raw_input_str = "   python programming language   "

cleaned = raw_input_str.strip()                 # Removes leading/trailing whitespace
print("Upper:", cleaned.upper())                # 'PYTHON PROGRAMMING LANGUAGE'
print("Title:", cleaned.title())                # 'Python Programming Language'
print("Replace:", cleaned.replace("python", "Java"))

# Splitting a string into a list and joining it back:
words_list = cleaned.split(" ")                 # ['python', 'programming', 'language']
joined_str = "-".join(words_list)               # 'python-programming-language'
print("Joined with hyphen:", joined_str)
