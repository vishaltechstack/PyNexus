# ==============================================================================
# FILE: 22_regex_with_re.py
# TOPIC: Regular Expressions (re module) for Parsing, Validation & Extraction
# ==============================================================================

import re

# Always use RAW STRINGS (r"...") for regex patterns so Python doesn't treat
# backslashes (\d, \w, \s) as string escape sequences!

# Common Regex Tokens:
#   \d  = Digit (0-9)              \w  = Word char (a-z, A-Z, 0-9, _)
#   \s  = Whitespace               .   = Any character except newline
#   +   = 1 or more                *   = 0 or more
#   ?   = 0 or 1 (optional)        {n,m} = Between n and m repetitions
#   ^   = Start of string          $   = End of string

# 1. EXTRACTING ALL MATCHES WITH re.findall()
log_blob = """
[2026-11-19 10:15:02] Ticket BUG-1042 assigned to vishal.sharma@company.com
[2026-11-19 10:18:45] Ticket BUG-1043 assigned to qa_lead@company.org
"""

ticket_ids = re.findall(r"BUG-\d{4}", log_blob)
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", log_blob)

print("Extracted Tickets:", ticket_ids)         # ['BUG-1042', 'BUG-1043']
print("Extracted Emails:", emails)

# 2. NAMED CAPTURE GROUPS WITH re.search()
# (?P<name>...) lets you extract structured fields by name from a matched string.
api_log = "POST /api/v2/users HTTP/1.1 -> Status: 201 (42ms)"
pattern = r"(?P<method>GET|POST|PUT|DELETE)\s+(?P<path>/\S+).*Status:\s+(?P<status>\d{3})\s+\((?P<latency>\d+)ms\)"

match = re.search(pattern, api_log)
if match:
    print("\nParsed Log Fields:", match.groupdict())
    # {'method': 'POST', 'path': '/api/v2/users', 'status': '201', 'latency': '42'}

# 3. MASKING SENSITIVE DATA WITH re.sub()
raw_text = "User card 4532-8910-2234-9876 charged successfully."
masked_text = re.sub(r"\d{4}-\d{4}-\d{4}-(\d{4})", r"XXXX-XXXX-XXXX-\1", raw_text)
print("\nMasked Card Output:", masked_text)

# 4. PRE-COMPILING PATTERNS FOR HIGH-SPEED REUSE
STRONG_PWD_REGEX = re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

for pwd in ["weakpass", "Strong@2026"]:
    is_valid = bool(STRONG_PWD_REGEX.match(pwd))
    print(f"Password '{pwd}' valid? {is_valid}")
