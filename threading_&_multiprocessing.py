# ==============================================================================
# FILE: 27_threading_and_multiprocessing.py
# TOPIC: Understanding the GIL, ThreadPoolExecutor (I/O) vs ProcessPoolExecutor (CPU)
# ==============================================================================

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ==============================================================================
# THE GOLDEN RULE OF PYTHON CONCURRENCY & THE GIL:
# ==============================================================================
# CPython has a Global Interpreter Lock (GIL): only ONE thread executes Python
# bytecode at a time inside a single process.
#
#   1. I/O-Bound Tasks (APIs, DB queries, file downloads, Selenium waits):
#      -> Use 'threading' or 'asyncio'. Threads release the GIL while waiting on I/O!
#
#   2. CPU-Bound Tasks (heavy math, image processing, data crunching):
#      -> Use 'multiprocessing'. Each process gets its own Python interpreter & GIL,
#         running truly in parallel across multiple CPU cores!
# ==============================================================================

# 1. I/O-BOUND WORKER (Ideal for ThreadPoolExecutor)
def simulated_network_call(task_id: int) -> str:
    time.sleep(0.5)                               # Simulates 500ms network latency
    return f"API_Task_{task_id}_Done"

# 2. CPU-BOUND WORKER (Ideal for ProcessPoolExecutor)
# Must be defined at top-level of module so child processes can pickle/import it!
def heavy_cpu_computation(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    # --- DEMO A: Multithreading for 6 I/O Tasks ---
    # Sequential time would be 6 * 0.5s = 3.0s. With 6 threads, it takes ~0.5s!
    start_io = time.perf_counter()
    with ThreadPoolExecutor(max_workers=6) as thread_pool:
        io_results = list(thread_pool.map(simulated_network_call, range(1, 7)))
    io_elapsed = time.perf_counter() - start_io

    print(f"[Threading] {len(io_results)} I/O tasks finished in {io_elapsed:.2f}s")

    # --- DEMO B: Multiprocessing for 4 Heavy CPU Tasks ---
    workloads = [5_000_000, 5_000_000, 5_000_000, 5_000_000]

    start_cpu = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as process_pool:
        cpu_results = list(process_pool.map(heavy_cpu_computation, workloads))
    cpu_elapsed = time.perf_counter() - start_cpu

    print(f"[Multiprocessing] {len(cpu_results)} CPU tasks finished in {cpu_elapsed:.2f}s")
