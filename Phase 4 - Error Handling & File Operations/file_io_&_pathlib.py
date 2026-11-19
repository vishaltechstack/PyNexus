# ==============================================================================
# FILE: 14_file_io_and_pathlib.py
# TOPIC: File Input/Output, Context Managers ('with'), and Modern pathlib Paths
# ==============================================================================

from pathlib import Path

# 1. MODERN FILE PATHS WITH pathlib (Preferred over legacy os.path)
# Path objects work identically across Windows (\) and Linux/macOS (/).
base_dir = Path("sample_workspace")
base_dir.mkdir(exist_ok=True)                     # Creates folder if it doesn't exist

log_file = base_dir / "execution.log"             # '/' operator joins paths cleanly!

# 2. WRITING TO A FILE ('w' mode) USING THE 'with' CONTEXT MANAGER
# Why 'with'? It guarantees the file handle is automatically closed even if an
# error occurs mid-write—preventing file locks and memory leaks.
# Common modes:
#   'w' = Write (creates file or OVERWRITES existing content)
#   'a' = Append (adds to the end without erasing existing content)
#   'r' = Read (default mode; raises FileNotFoundError if missing)
# Always specify encoding="utf-8" for cross-platform safety!

with open(log_file, mode="w", encoding="utf-8") as file:
    file.write("2026-11-19 09:00:01 [INFO] Suite started.\n")
    file.write("2026-11-19 09:00:05 [PASS] TC_01 Login verified.\n")

# 3. APPENDING TO AN EXISTING FILE ('a' mode)
with open(log_file, mode="a", encoding="utf-8") as file:
    file.write("2026-11-19 09:00:12 [FAIL] TC_02 Checkout timeout.\n")

# 4. READING FILES SAFELY
# Method A: Read the entire file into a single string (best for small files)
full_content = log_file.read_text(encoding="utf-8")
print("=== Full Log Content ===")
print(full_content)

# Method B: Stream line-by-line (memory-efficient for multi-gigabyte log files!)
print("=== Filtered Failures Only ===")
with open(log_file, mode="r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, start=1):
        clean_line = line.strip()                 # Removes trailing '\n'
        if "[FAIL]" in clean_line:
            print(f"Line {line_num}: {clean_line}")

# 5. INSPECTING FILE METADATA
print(f"\nFile Name: {log_file.name} | Extension: {log_file.suffix} | Size: {log_file.stat().st_size} bytes")
