# ==============================================================================
# FILE: 09_functions_and_scope.py
# TOPIC: Functions, Default Arguments, Type Hints, Docstrings, and LEGB Scope
# ==============================================================================

# 1. DEFINING A FUNCTION WITH TYPE HINTS & DOCSTRINGS
# Type hints (e.g., 'name: str', '-> str') are optional metadata that make code
# self-documenting and give you autocomplete/error-checking in VS Code.
def greet_engineer(name: str, role: str = "QA Automation Engineer") -> str:
    """
    Returns a formatted welcome message.
    'role' has a default value, making it an optional argument when calling.
    """
    return f"Hello {name}! Role assigned: {role}."

# Positional argument call (order matters):
print(greet_engineer("Vishal", "SDET"))

# Keyword argument call (order doesn't matter; uses default for 'role'):
print(greet_engineer(name="Vishal"))

# 2. RETURNING MULTIPLE VALUES (Tuple Packing & Unpacking)
def analyze_test_results(results: list[str]) -> tuple[int, int, float]:
    """Calculates passed count, failed count, and pass percentage."""
    passed = results.count("PASS")
    failed = results.count("FAIL")
    total = len(results)
    pass_rate = (passed / total) * 100 if total > 0 else 0.0
    return passed, failed, round(pass_rate, 2)    # Automatically packed into a tuple

# Unpack the returned tuple directly into separate variables:
p_count, f_count, rate = analyze_test_results(["PASS", "PASS", "FAIL", "PASS"])
print(f"Passed: {p_count} | Failed: {f_count} | Pass Rate: {rate}%")

# 3. CRITICAL TRAP: MUTABLE DEFAULT ARGUMENTS
# NEVER use a mutable object (like [] or {}) as a default parameter!
# Default values are evaluated ONLY ONCE when the function is defined, not per call.
def add_bug_safe(bug_id: str, bug_list: list[str] | None = None) -> list[str]:
    if bug_list is None:
        bug_list = []                           # Creates a fresh list on every call
    bug_list.append(bug_id)
    return bug_list

print("Run 1:", add_bug_safe("BUG-101"))        # ['BUG-101']
print("Run 2:", add_bug_safe("BUG-102"))        # ['BUG-102'] (Clean list!)

# 4. VARIABLE SCOPE: THE LEGB RULE
# Python resolves variable names in this strict order:
# L (Local) -> E (Enclosing) -> G (Global) -> B (Built-in)

global_env = "STAGING"                          # G: Global scope

def outer_suite():
    enclosing_browser = "Chrome"                # E: Enclosing scope

    def inner_test():
        local_timeout = 30                      # L: Local scope
        # Can read Local, Enclosing, Global, and Built-in (like len()) freely:
        print(f"Env: {global_env} | Browser: {enclosing_browser} | Timeout: {local_timeout}s")

    inner_test()

outer_suite()
