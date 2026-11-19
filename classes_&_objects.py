# ==============================================================================
# FILE: 16_classes_and_objects.py
# TOPIC: Classes, Objects, __init__, self, Class vs. Instance State, Method Types
# ==============================================================================

class TestCase:
    """
    A class is a blueprint for creating objects (instances).
    Naming convention: Use PascalCase (e.g., TestCase, BrowserDriver).
    """

    # 1. CLASS ATTRIBUTE
    # Shared across ALL instances created from this class.
    framework_name = "PyAutoSuite"
    total_tests_created = 0

    # 2. CONSTRUCTOR METHOD (__init__)
    # Automatically invoked when a new object is instantiated.
    # 'self' refers to the specific object instance being created/operated on.
    def __init__(self, test_id: str, title: str, priority: str = "Medium"):
        # INSTANCE ATTRIBUTES: Unique to each individual object
        self.test_id = test_id
        self.title = title
        self.priority = priority
        self.status = "NOT_RUN"

        # Increment the shared class counter every time a new object is created
        TestCase.total_tests_created += 1

    # 3. INSTANCE METHOD
    # Operates on instance data via 'self'.
    def execute(self, passed: bool) -> None:
        self.status = "PASS" if passed else "FAIL"
        print(f"[{self.test_id}] '{self.title}' executed -> {self.status}")

    # 4. CLASS METHOD (@classmethod)
    # Receives the class itself ('cls') instead of an instance ('self').
    # Commonly used as alternative constructors (factory methods).
    @classmethod
    def from_string(cls, raw_record: str) -> "TestCase":
        """Factory constructor: builds a TestCase from 'TC_03|Logout Flow|High'."""
        tid, title, prio = raw_record.split("|")
        return cls(tid.strip(), title.strip(), prio.strip())

    # 5. STATIC METHOD (@staticmethod)
    # Utility function bundled inside the class namespace.
    # Takes neither 'self' nor 'cls'—cannot modify object or class state.
    @staticmethod
    def is_valid_id(test_id: str) -> bool:
        return test_id.startswith("TC_") and len(test_id) >= 5


# --- Instantiating and Using Objects ---
tc1 = TestCase("TC_01", "Verify Valid Login", priority="High")
tc2 = TestCase.from_string("TC_02 | Add Item to Cart | Medium")

tc1.execute(passed=True)
tc2.execute(passed=False)

print(f"\nFramework: {TestCase.framework_name}")
print(f"Total TestCase objects created: {TestCase.total_tests_created}")
print(f"Is 'TC_99' valid format? {TestCase.is_valid_id('TC_99')}")
