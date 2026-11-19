# ==============================================================================
# FILE: 24_sqlite_database.py
# TOPIC: Built-in SQLite Database, Parameterized Queries, and Transactions
# ==============================================================================

import sqlite3
from pathlib import Path

db_path = Path("sample_workspace") / "qa_tracking.db"
db_path.parent.mkdir(exist_ok=True)

# 1. CONNECTING & USING A CONTEXT MANAGER FOR TRANSACTIONS
# Using 'with sqlite3.connect(...)' automatically commits changes if no error
# occurs, or rolls back the transaction if an exception is raised!
with sqlite3.connect(db_path) as conn:
    # Setting row_factory to sqlite3.Row lets you access columns by name like a dict
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 2. CREATING A TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_executions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            status TEXT NOT NULL,
            duration_ms INTEGER NOT NULL
        )
    """)

    # Clean table for repeatable demo runs
    cursor.execute("DELETE FROM test_executions")

    # 3. INSERTING RECORDS SAFELY (PARAMETERIZED QUERIES)
    # CRITICAL SECURITY RULE: NEVER use f-strings to build SQL queries (prevents SQL Injection!).
    # Always use '?' placeholders and pass values as a tuple.
    sample_runs = [
        ("test_user_login", "PASS", 340),
        ("test_create_lead", "PASS", 510),
        ("test_export_invoice", "FAIL", 1820),
        ("test_delete_contact", "PASS", 290),
    ]
    cursor.executemany(
        "INSERT INTO test_executions (test_name, status, duration_ms) VALUES (?, ?, ?)",
        sample_runs
    )

    # 4. QUERYING & FILTERING DATA
    print("=== Failed Test Executions ===")
    cursor.execute(
        "SELECT id, test_name, duration_ms FROM test_executions WHERE status = ?",
        ("FAIL",)                               # Note trailing comma for single-item tuple!
    )
    for row in cursor.fetchall():
        print(f"  ID #{row['id']}: {row['test_name']} took {row['duration_ms']}ms")

    # 5. AGGREGATE SQL QUERY
    cursor.execute("SELECT COUNT(*) AS total, AVG(duration_ms) AS avg_ms FROM test_executions")
    summary = cursor.fetchone()
    print(f"\nTotal Runs: {summary['total']} | Average Duration: {summary['avg_ms']:.1f}ms")
