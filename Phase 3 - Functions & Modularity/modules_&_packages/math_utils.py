# ==============================================================================
# FILE: math_utils.py
# TOPIC: Creating a Custom Reusable Python Module
# ==============================================================================

APP_VERSION = "1.0.0"

def calculate_pass_percentage(passed: int, total: int) -> float:
    """Computes percentage safely without ZeroDivisionError."""
    if total <= 0:
        return 0.0
    return round((passed / total) * 100, 2)

def is_prime(n: int) -> bool:
    """Checks whether an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# THE __name__ == "__main__" GUARD:
# When Python runs this file directly, __name__ is set to "__main__".
# When another file imports this module, __name__ is set to "math_utils".
# Putting test code inside this block prevents it from running during imports!
if __name__ == "__main__":
    print("[Self-Test] Running math_utils directly...")
    assert calculate_pass_percentage(18, 20) == 90.0
    assert is_prime(17) is True
    print("[Self-Test] All assertions passed!")
