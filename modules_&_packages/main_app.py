# ==============================================================================
# FILE: 12_main_app.py
# TOPIC: Importing Custom Modules, Standard Library Modules, and Aliases
# ==============================================================================

# 1. IMPORTING STANDARD LIBRARY MODULES (Batteries included with Python)
import math
import random
from datetime import datetime

# 2. IMPORTING YOUR CUSTOM MODULE ('math_utils.py' in the same folder)
import math_utils
from math_utils import calculate_pass_percentage as calc_pct  # Alias with 'as'

# Using standard library tools:
print("Current Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Square root of 144:", math.sqrt(144))
print("Random test ID:", random.randint(1000, 9999))

# Using functions from our custom module:
print("Module Version:", math_utils.APP_VERSION)
print("Suite Pass Rate:", calc_pct(47, 50), "%")
print("Is 29 prime?", math_utils.is_prime(29))
