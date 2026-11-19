# ==============================================================================
# FILE: 11_lambda_map_filter.py
# TOPIC: Lambda Expressions, map(), filter(), zip(), and Custom Sorting
# ==============================================================================

# 1. LAMBDA FUNCTIONS (SINGLE-EXPRESSION ANONYMOUS FUNCTIONS)
# Syntax: lambda parameters: single_expression
# No 'return' keyword is used—the expression's result is returned automatically.
square = lambda x: x ** 2
add = lambda a, b: a + b

print("Square of 6:", square(6))                # 36
print("Add 10 + 15:", add(10, 15))              # 25

# 2. MOST PRACTICAL USE CASE: CUSTOM SORTING WITH key=
# Sorting complex structures like a list of dictionaries or tuples.
test_cases = [
    {"id": "TC_03", "priority": 2, "duration_sec": 12.5},
    {"id": "TC_01", "priority": 1, "duration_sec": 45.0},
    {"id": "TC_02", "priority": 1, "duration_sec": 8.2},
]

# Sort by 'priority' ascending, then by 'duration_sec' ascending:
sorted_cases = sorted(test_cases, key=lambda tc: (tc["priority"], tc["duration_sec"]))
print("\nSorted Test Cases by Priority & Speed:")
for tc in sorted_cases:
    print(" ", tc)

# 3. map(function, iterable)
# Applies a transformation function to EVERY item in an iterable lazily (returns an iterator).
raw_prices = [100, 250, 400, 50]
prices_with_tax = list(map(lambda p: round(p * 1.18, 2), raw_prices))
print("\nPrices with 18% GST:", prices_with_tax)

# 4. filter(function, iterable)
# Keeps ONLY items where the function returns True.
response_times_ms = [120, 850, 95, 1400, 310, 2200]
slow_responses = list(filter(lambda ms: ms > 500, response_times_ms))
print("Slow API responses (>500ms):", slow_responses)

# Note: In modern Python, list comprehensions are often preferred over map/filter
# for readability, e.g.: [ms for ms in response_times_ms if ms > 500]

# 5. zip(*iterables)
# Pairs elements from multiple iterables together index-by-index into tuples.
endpoints = ["/login", "/users", "/orders"]
methods = ["POST", "GET", "DELETE"]
expected_codes = [200, 200, 204]

print("\nAPI Endpoint Matrix:")
for method, path, code in zip(methods, endpoints, expected_codes):
    print(f"  {method:6} {path:8} -> Expect HTTP {code}")
