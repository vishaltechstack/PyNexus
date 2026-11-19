# ==============================================================================
# FILE: 21_decorators_and_closures.py
# TOPIC: First-Class Functions, Closures, Decorators, and Parameterized Wrappers
# ==============================================================================

import time
import functools
from typing import Callable, Any

# 1. CLOSURES (Functions that remember variables from their enclosing scope)
def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiply(number: int) -> int:
        return number * factor                  # 'factor' is remembered even after outer finishes
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"Closure test -> double(5): {double(5)}, triple(5): {triple(5)}")

# 2. BUILDING A EXECUTION TIMER DECORATOR
# A decorator takes a function, wraps it with extra behavior (logging, timing, auth,
# retries) without modifying the original function's source code, and returns it.
def measure_time(func: Callable) -> Callable:
    # @functools.wraps preserves the original function's __name__ and __doc__
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)          # Execute the wrapped function
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[Timer] '{func.__name__}' finished in {elapsed_ms:.2f} ms")
        return result
    return wrapper

# Applying the decorator using the '@' syntactic sugar:
@measure_time
def run_heavy_query(record_count: int) -> int:
    """Simulates a database query."""
    total = sum(i for i in range(record_count))
    return total

print("\nQuery Result:", run_heavy_query(500_000))
print("Preserved Function Name:", run_heavy_query.__name__)

# 3. DECORATOR WITH ARGUMENTS (e.g., Auto-Retry for Flaky Tests/APIs)
def retry(max_attempts: int = 3):
    """Outer factory accepts decorator configuration arguments."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"[Retry {attempt}/{max_attempts}] Failed: {exc}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

attempt_counter = 0

@retry(max_attempts=3)
def flaky_api_call() -> str:
    global attempt_counter
    attempt_counter += 1
    if attempt_counter < 3:
        raise ConnectionError("503 Service Unavailable")
    return "200 OK: Payload received!"

print("\nFlaky API Outcome:", flaky_api_call())
