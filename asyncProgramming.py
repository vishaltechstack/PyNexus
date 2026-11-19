# ==============================================================================
# FILE: 23_async_programming.py
# TOPIC: Asynchronous Concurrency with async, await, and asyncio.gather()
# ==============================================================================

import asyncio
import time

# 1. SYNCHRONOUS VS. ASYNCHRONOUS EXECUTION
# Synchronous code blocks the entire thread while waiting for I/O (APIs, DBs, files).
# Asynchronous code ('async def') yields control back to the Event Loop during
# 'await' pauses so other tasks can progress concurrently on a SINGLE thread!

async def fetch_endpoint(endpoint: str, delay_sec: float) -> dict:
    """Coroutine function simulating a non-blocking HTTP network call."""
    print(f"  [Start] Requesting {endpoint} (est. {delay_sec}s)...")
    await asyncio.sleep(delay_sec)              # Non-blocking sleep (simulates network I/O)
    print(f"  [Done]  Received response from {endpoint}")
    return {"endpoint": endpoint, "status": 200}

async def main() -> None:
    start_time = time.perf_counter()

    print("=== Running 3 API Checks Concurrently ===")
    # asyncio.gather() schedules multiple coroutines on the event loop simultaneously
    # and waits until ALL of them complete, returning results in order.
    results = await asyncio.gather(
        fetch_endpoint("/users", 1.5),
        fetch_endpoint("/orders", 1.0),
        fetch_endpoint("/inventory", 2.0),
    )

    elapsed = time.perf_counter() - start_time
    # Total time is ~2.0s (the slowest single task) instead of 1.5 + 1.0 + 2.0 = 4.5s!
    print(f"\nAll {len(results)} calls completed in {elapsed:.2f} seconds!")
    for res in results:
        print(" ->", res)

# 2. ENTRY POINT TO START THE ASYNCIO EVENT LOOP
if __name__ == "__main__":
    asyncio.run(main())
