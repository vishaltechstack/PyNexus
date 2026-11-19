# ==============================================================================
# FILE: 01_hello_and_io.py
# TOPIC: First Program, Comments, Print Formatting, and User Input
# ==============================================================================

# 1. COMMENTS IN PYTHON
# Single-line comments start with the '#' symbol. Python ignores them at runtime.

"""
Multi-line strings (enclosed in triple quotes) are used as docstrings
to document modules, classes, and functions.
"""

# 2. STANDARD OUTPUT USING print()
# The print() function sends text or variables to the console.
print("Hello, World! Welcome to Python.")

# You can print multiple items separated by commas.
# By default, Python separates them with a single space (' ').
print("Python", "is", "clean", "and", "readable.")

# Customizing 'sep' (separator) and 'end' (line ending):
# Normally, print() adds a newline (\n) at the end. Changing 'end' overrides this.
print("2026", "11", "19", sep="-")          # Output: 2026-11-19
print("Loading system", end="... ")         # Stays on the same line
print("Ready!")                             # Output: Loading system... Ready!

# 3. STANDARD INPUT USING input()
# input() pauses program execution and waits for the user to type something.
# IMPORTANT: input() ALWAYS returns data as a String (str), even if numbers are typed.
user_name = input("\nEnter your name: ")

# 4. STRING FORMATTING (f-strings)
# Prefixing a string with 'f' allows embedding variables directly inside {}.
# This is the modern, fastest, and cleanest way to format strings in Python.
print(f"Welcome aboard, {user_name}! Let's master Python step by step.")
