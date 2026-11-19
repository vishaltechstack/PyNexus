# ==============================================================================
# FILE: 04_control_flow.py
# TOPIC: if/elif/else, match-case, while loops, for loops, break & continue
# ==============================================================================

# 1. CONDITIONAL STATEMENTS (if / elif / else)
# Python uses INDENTATION (4 spaces) instead of curly braces {} to define code blocks.
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Marks: {marks} -> Grade: {grade}")

# Ternary Conditional Expression (One-line if-else):
status = "Eligible" if marks >= 40 else "Not Eligible"
print("Exam Status:", status)

# 2. STRUCTURAL PATTERN MATCHING (match-case, Python 3.10+)
# Similar to 'switch' statements in other languages, but much more powerful.
http_code = 404

match http_code:
    case 200:
        print("OK: Request succeeded.")
    case 401 | 403:                             # '|' acts as OR
        print("Auth Error: Access denied.")
    case 404:
        print("Not Found: Resource missing.")
    case _:                                     # '_' is the default wildcard case
        print("Unhandled HTTP status code.")

# 3. WHILE LOOPS (Condition-controlled repetition)
# Runs as long as the condition evaluates to True.
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1                              # Decrement to prevent an infinite loop!
print("Liftoff!\n")

# 4. FOR LOOPS & range() (Sequence-controlled repetition)
# range(start, stop, step) generates numbers up to (but excluding) 'stop'.
print("Even numbers from 2 to 10:")
for num in range(2, 11, 2):
    print(num, end=" ")                         # Output: 2 4 6 8 10
print("\n")

# 5. LOOP CONTROL: break, continue, and for-else
# 'continue' skips the rest of the current iteration and jumps to the next one.
# 'break' exits the loop immediately.
# 'else' on a loop runs ONLY if the loop finished normally (without hitting 'break').

target = 7
for i in range(1, 10):
    if i % 2 == 0:
        continue                                # Skip even numbers
    if i == target:
        print(f"Target {target} found! Breaking out of loop.")
        break
    print(f"Checking odd number: {i}")
else:
    # This block will NOT execute because 'break' was triggered above.
    print("Target was not found in range.")
