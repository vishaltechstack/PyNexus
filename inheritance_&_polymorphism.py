# ==============================================================================
# FILE: 18_inheritance_and_polymorphism.py
# TOPIC: Inheritance, super(), Method Overriding, Polymorphism, and ABCs
# ==============================================================================

from abc import ABC, abstractmethod

# 1. ABSTRACT BASE CLASS (ABC)
# Enforces a contract: any child class inheriting from BaseRunner MUST implement
# all @abstractmethod methods, otherwise Python prevents instantiating it.
class BaseRunner(ABC):
    def __init__(self, suite_name: str):
        self.suite_name = suite_name

    def setup(self) -> None:
        print(f"[{self.suite_name}] Initializing environment...")

    @abstractmethod
    def run_tests(self) -> None:
        """Subclasses MUST override this method."""
        pass


# 2. CHILD CLASS 1 (Inherits from BaseRunner)
class WebUIRunner(BaseRunner):
    def __init__(self, suite_name: str, browser: str):
        # super() calls the parent class's __init__ so we don't repeat code
        super().__init__(suite_name)
        self.browser = browser

    # Method Overriding: providing a specialized implementation
    def run_tests(self) -> None:
        print(f"[{self.suite_name}] Launching {self.browser} and running Selenium UI checks...")


# 3. CHILD CLASS 2 (Inherits from BaseRunner)
class ApiRunner(BaseRunner):
    def __init__(self, suite_name: str, base_url: str):
        super().__init__(suite_name)
        self.base_url = base_url

    def run_tests(self) -> None:
        print(f"[{self.suite_name}] Sending HTTP requests to {self.base_url}...")


# 4. POLYMORPHISM IN ACTION
# Different runner objects respond to the exact same interface (.setup() and .run_tests())
# with their own specialized behavior.
def trigger_ci_pipeline(runners: list[BaseRunner]) -> None:
    for runner in runners:
        runner.setup()
        runner.run_tests()
        print("-" * 50)

pipeline_runners: list[BaseRunner] = [
    WebUIRunner("CRM_UI_Smoke", browser="Chrome"),
    ApiRunner("CRM_REST_Regression", base_url="https://api.example.com/v1")
]

trigger_ci_pipeline(pipeline_runners)

# Check inheritance relationships dynamically:
print("Is WebUIRunner a BaseRunner?", isinstance(pipeline_runners[0], BaseRunner))
print("Method Resolution Order (MRO):", [cls.__name__ for cls in WebUIRunner.__mro__])
