# ==============================================================================
# FILE: 19_dunder_methods_and_dataclasses.py
# TOPIC: Dunder (Double-Underscore) Magic Methods & Modern @dataclass
# ==============================================================================

from dataclasses import dataclass, field

# 1. DUNDER (MAGIC) METHODS
# Methods surrounded by double underscores (__name__) let your custom objects
# integrate with Python's built-in syntax (+, ==, len(), print(), indexing).
class TestSuite:
    def __init__(self, name: str, tests: list[str] | None = None):
        self.name = name
        self.tests = tests if tests is not None else []

    # __str__: Human-readable representation used by print() and str()
    def __str__(self) -> str:
        return f"TestSuite('{self.name}', {len(self.tests)} tests)"

    # __repr__: Unambiguous developer representation used in debuggers & lists
    def __repr__(self) -> str:
        return f"TestSuite(name={self.name!r}, tests={self.tests!r})"

    # __len__: Enables len(suite_obj)
    def __len__(self) -> int:
        return len(self.tests)

    # __add__: Enables combining two suites with the '+' operator!
    def __add__(self, other: "TestSuite") -> "TestSuite":
        if not isinstance(other, TestSuite):
            return NotImplemented
        return TestSuite(f"{self.name}+{other.name}", self.tests + other.tests)

    # __getitem__: Enables indexing/iterating like a list (suite_obj[0])
    def __getitem__(self, index: int) -> str:
        return self.tests[index]


smoke = TestSuite("Smoke", ["TC_01_Login", "TC_02_Dashboard"])
regression = TestSuite("Regression", ["TC_03_Reports", "TC_04_Export"])

combined = smoke + regression                   # Calls __add__
print("String output:", combined)               # Calls __str__
print("Total tests:", len(combined))            # Calls __len__
print("First test in combined:", combined[0])   # Calls __getitem__

# 2. @dataclass (Python 3.7+)
# Automatically generates __init__, __repr__, and __eq__ (value-based equality)
# without writing repetitive boilerplate code!
@dataclass
class BugTicket:
    ticket_id: str
    summary: str
    severity: str = "Major"
    # Use field(default_factory=list) for mutable defaults inside dataclasses!
    labels: list[str] = field(default_factory=list)

bug1 = BugTicket("BUG-401", "Search filter ignores case", labels=["UI", "Search"])
bug2 = BugTicket("BUG-401", "Search filter ignores case", labels=["UI", "Search"])

print("\nDataclass repr:", bug1)
print("Value equality (bug1 == bug2):", bug1 == bug2)  # True! (Regular classes compare memory IDs)
