# ==============================================================================
# FILE: 13_exception_handling.py
# TOPIC: Runtime Error Handling, Custom Exceptions, and Defensive Programming
# ==============================================================================

# 1. THE COMPLETE try / except / else / finally ANATOMY
def divide_metrics(total_time: float, test_count: int) -> float | None:
    """
    Demonstrates all four exception-handling blocks:
    - try:     Code that might raise an exception.
    - except:  Runs ONLY if a matching exception occurs.
    - else:    Runs ONLY if NO exception occurred in the 'try' block.
    - finally: ALWAYS runs (whether an error occurred or not)—ideal for cleanup.
    """
    try:
        avg_time = total_time / test_count
    except ZeroDivisionError:
        print("[Error] Cannot divide by zero: test_count must be greater than 0.")
        return None
    except TypeError as err:
        # 'as err' captures the exception object so you can inspect its message
        print(f"[Error] Invalid data types provided: {err}")
        return None
    else:
        print("[Success] Calculation completed cleanly.")
        return round(avg_time, 3)
    finally:
        print("[Cleanup] Metric calculation attempt finished.\n")

print("Result 1:", divide_metrics(15.5, 5))       # Runs try -> else -> finally
print("Result 2:", divide_metrics(15.5, 0))       # Runs try -> except -> finally

# 2. CREATING AND RAISING CUSTOM EXCEPTIONS
# Inherit from Python's built-in 'Exception' class to define domain-specific errors.
class InvalidEnvironmentError(Exception):
    """Raised when an unsupported test environment is requested."""
    def __init__(self, env_name: str, allowed: tuple[str, ...]):
        self.env_name = env_name
        super().__init__(f"Environment '{env_name}' is invalid. Allowed: {allowed}")

def connect_to_environment(env: str) -> str:
    allowed_envs = ("DEV", "QA", "STAGING", "PROD")
    normalized = env.strip().upper()

    if normalized not in allowed_envs:
        # 'raise' explicitly triggers an exception
        raise InvalidEnvironmentError(env, allowed_envs)

    return f"Connected successfully to {normalized} database."

# Handling our custom exception:
try:
    print(connect_to_environment("QA"))
    print(connect_to_environment("SANDBOX"))      # This will raise InvalidEnvironmentError
except InvalidEnvironmentError as e:
    print(f"[Custom Exception Caught] {e}")
