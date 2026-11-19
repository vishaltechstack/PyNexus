# ==============================================================================
# FILE: 20_iterators_and_generators.py
# TOPIC: Iterators (__iter__/__next__), Generators (yield), and Lazy Streams
# ==============================================================================

import sys

# 1. WHY GENERATORS MATTER
# A regular list builds ALL items in memory at once.
# A generator produces ONE item at a time on demand (lazy evaluation),
# using virtually zero memory even when streaming millions of records!

def generate_test_ids(prefix: str, count: int):
    """
    Any function containing the 'yield' keyword becomes a Generator Function.
    When called, it returns a generator object without running the body yet.
    Each next() call runs until 'yield', pauses state, and returns the value.
    """
    current = 1
    while current <= count:
        yield f"{prefix}_{current:04d}"          # Pauses execution & yields value
        current += 1

# Creating the generator object (instant, minimal memory):
id_stream = generate_test_ids("TC", 5)

print("First manual pull:", next(id_stream))    # 'TC_0001'
print("Second manual pull:", next(id_stream))   # 'TC_0002'

print("Remaining items via for-loop:")
for tid in id_stream:                           # Resumes right where next() left off!
    print(" ", tid)

# 2. GENERATOR EXPRESSIONS (Parentheses instead of square brackets)
# Compare memory footprint of 1,000,000 numbers:
list_comp = [n * 2 for n in range(1_000_000)]
gen_expr = (n * 2 for n in range(1_000_000))

print(f"\nList size in memory:      {sys.getsizeof(list_comp):,} bytes")
print(f"Generator size in memory: {sys.getsizeof(gen_expr):,} bytes")

# 3. PRACTICAL PIPELINE: STREAMING LARGE LOG FILES
def stream_error_lines(log_lines: list[str]):
    """Yields only ERROR lines one by one without copying the entire dataset."""
    for line in log_lines:
        if "ERROR" in line:
            yield line.strip()

mock_server_logs = [
    "2026-11-19 INFO Server healthy",
    "2026-11-19 ERROR Connection timeout on /api/v1/orders",
    "2026-11-19 INFO Retrying request",
    "2026-11-19 ERROR Database deadlock detected",
]

print("\nStreamed Errors:")
for err in stream_error_lines(mock_server_logs):
    print(" ->", err)
