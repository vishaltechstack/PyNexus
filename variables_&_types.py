# ==============================================================================
# FILE: 02_variables_and_types.py
# TOPIC: Variables, Primitive Data Types, Memory References, and Type Casting
# ==============================================================================

# 1. DYNAMIC TYPING
# Unlike Java or C++, you do NOT declare data types explicitly in Python.
# Python infers the type automatically when a value is assigned.
# Naming convention: Use snake_case (lowercase words separated by underscores).

# 2. CORE PRIMITIVE DATA TYPES
integer_num = 25                    # int: Whole numbers (unlimited precision in Python)
floating_num = 99.95                # float: Decimal numbers (64-bit double precision)
complex_num = 3 + 4j                # complex: Real + Imaginary numbers ('j' is imaginary unit)
text_data = "Automation Engineer"   # str: Sequence of Unicode characters
is_active = True                    # bool: Boolean values (Must be capitalized: True / False)
empty_value = None                  # NoneType: Represents the absence of a value (like null)

# 3. INSPECTING TYPES AND MEMORY ADDRESSES
# type() tells you what class/type an object belongs to.
# id() returns the unique memory address of the object in CPython.
print("Type of integer_num:", type(integer_num))   # <class 'int'>
print("Type of text_data:", type(text_data))       # <class 'str'>
print("Memory ID of integer_num:", id(integer_num))

# 4. MULTIPLE ASSIGNMENT & SWAPPING
# Assign multiple variables in a single line:
x, y, z = 10, 20, "Thirty"

# Swap two variables without needing a temporary third variable:
a = 5
b = 10
a, b = b, a
print(f"After swap -> a: {a}, b: {b}")             # a: 10, b: 5

# 5. TYPE CASTING (EXPLICIT CONVERSION)
# Converting one data type into another using built-in constructor functions.
raw_age = "24"                      # Currently a string (str)
numeric_age = int(raw_age)          # Converted to integer (int)
next_year_age = numeric_age + 1     # Now mathematical addition works!

price_float = 49.99
price_int = int(price_float)        # Truncates decimal part (becomes 49, does NOT round)
price_str = str(price_float)        # Converts float back to string "49.99"

print(f"Next year age: {next_year_age}, Truncated price: {price_int}")

# Truthy & Falsy conversions using bool():
# Empty strings "", 0, 0.0, None, and empty collections evaluate to False.
print("bool(0):", bool(0))          # False
print("bool(''):", bool(""))        # False
print("bool('Hi'):", bool("Hi"))    # True
