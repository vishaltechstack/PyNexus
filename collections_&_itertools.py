# ==============================================================================
# FILE: 25_collections_and_itertools.py
# TOPIC: collections (Counter, defaultdict, deque, namedtuple) & itertools
# ==============================================================================

from collections import Counter, defaultdict, deque, namedtuple
import itertools

# ==============================================================================
# PART A: THE collections MODULE
# ==============================================================================

# 1. Counter: Fast frequency counting for any iterable
statuses = ["PASS", "FAIL", "PASS", "PASS", "SKIP", "FAIL", "PASS"]
counts = Counter(statuses)

print("Status Counts:", counts)                   # Counter({'PASS': 4, 'FAIL': 2, 'SKIP': 1})
print("Most common status:", counts.most_common(1))  # [('PASS', 4)]

# 2. defaultdict: Dictionary that auto-initializes missing keys (no KeyError!)
# Ideal for grouping records into lists without checking 'if key not in dict'.
grouped_tests: dict[str, list[str]] = defaultdict(list)

test_records = [
    ("Auth", "TC_01_Login"),
    ("Cart", "TC_02_AddItem"),
    ("Auth", "TC_03_ResetPwd"),
    ("Cart", "TC_04_Checkout"),
]

for module, test_name in test_records:
    grouped_tests[module].append(test_name)       # Automatically creates [] if missing

print("\nGrouped Tests:", dict(grouped_tests))

# 3. deque (Double-Ended Queue): O(1) fast appends/pops from BOTH ends
# (Regular lists take O(n) time when inserting/popping from index 0!)
recent_logs: deque[str] = deque(maxlen=3)         # Automatically drops oldest item when full
for step in ["Step 1", "Step 2", "Step 3", "Step 4"]:
    recent_logs.append(step)

print("Last 3 Logs (bounded deque):", list(recent_logs))  # ['Step 2', 'Step 3', 'Step 4']

# 4. namedtuple: Lightweight, immutable, memory-efficient object with named fields
Endpoint = namedtuple("Endpoint", ["method", "path", "expected_status"])
login_api = Endpoint("POST", "/api/v1/login", 200)
print(f"NamedTuple -> {login_api.method} {login_api.path} ({login_api.expected_status})")

# ==============================================================================
# PART B: THE itertools MODULE (Memory-Efficient Iteration Building Blocks)
# ==============================================================================

# 5. itertools.product(): Cartesian product (great for generating test data matrices!)
browsers = ["Chrome", "Firefox"]
environments = ["QA", "Staging"]

print("\nCross-Browser Test Matrix:")
for browser, env in itertools.product(browsers, environments):
    print(f"  Running suite on {browser} @ {env}")

# 6. itertools.combinations() & permutations()
items = ["A", "B", "C"]
print("2-item Combinations (order doesn't matter):", list(itertools.combinations(items, 2)))
print("2-item Permutations (order matters):", list(itertools.permutations(items, 2)))
