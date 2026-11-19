# ==============================================================================
# FILE: 10_args_and_kwargs.py
# TOPIC: Arbitrary Positional Arguments (*args) & Keyword Arguments (**kwargs)
# ==============================================================================

# 1. *args (ARBITRARY POSITIONAL ARGUMENTS)
# The single asterisk '*' packs any number of extra positional arguments
# into a TUPLE named 'args' (the name 'args' is convention, '*' is the syntax).
def calculate_total(*prices: float) -> float:
    print("Received prices tuple:", prices)     # e.g., (199.0, 49.5, 10.0)
    return sum(prices)

print("Total Bill:", calculate_total(199.0, 49.5, 10.0))

# 2. **kwargs (ARBITRARY KEYWORD ARGUMENTS)
# The double asterisk '**' packs any number of extra key=value arguments
# into a DICTIONARY named 'kwargs'.
def build_api_headers(**headers: str) -> dict[str, str]:
    base_headers = {"Accept": "application/json"}
    base_headers.update(headers)                # Merge dynamic keyword arguments
    return base_headers

custom_headers = build_api_headers(Authorization="Bearer xyz123", User_Agent="PyTestClient")
print("API Headers:", custom_headers)

# 3. COMBINING ALL PARAMETER TYPES IN STRICT ORDER
# Python enforces a strict parameter ordering rule:
# (standard_pos, *args, keyword_only, **kwargs)
def execute_pipeline(pipeline_name: str, *steps: str, retry: int = 1, **env_vars: str) -> None:
    print(f"\n=== Running Pipeline: {pipeline_name} (Retries: {retry}) ===")
    for idx, step in enumerate(steps, start=1):
        print(f"  Step {idx}: {step}")
    print(f"  Environment Variables: {env_vars}")

execute_pipeline(
    "Nightly_Regression",                       # pipeline_name
    "Checkout_Code", "Run_Unit_Tests", "Deploy",# *steps (packed into tuple)
    retry=3,                                    # keyword-only argument
    DB_HOST="localhost", ENV="QA"               # **env_vars (packed into dict)
)

# 4. UNPACKING COLLECTIONS WHEN CALLING FUNCTIONS
# You can also use * and ** in reverse—to unpack a list/dict INTO function arguments!
def create_user(username: str, email: str, is_admin: bool):
    print(f"Created user -> {username} ({email}) | Admin: {is_admin}")

user_data_list = ["vishal_qa", "vishal@example.com", True]
create_user(*user_data_list)                    # Unpacks list into 3 positional args

user_data_dict = {"username": "alex_dev", "email": "alex@example.com", "is_admin": False}
create_user(**user_data_dict)                   # Unpacks dict into keyword args
