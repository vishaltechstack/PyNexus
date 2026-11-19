<div align="center">

# 🐍 Python Mastery Curriculum

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-28%20Files-2EA44F?style=for-the-badge&logo=files&logoColor=white)](#-repository-structure)
[![Code Style](https://img.shields.io/badge/Documentation-Line--by--Line%20Comments-F59E0B?style=for-the-badge&logo=bookstack&logoColor=white)](#-design-philosophy)
[![Packaging](https://img.shields.io/badge/Standard-PEP%20621%20%7C%20Type%20Hinted-8B5CF6?style=for-the-badge&logo=pypi&logoColor=white)](#-environment--packaging-setup)

**An end-to-end, modular Python engineering codebase spanning 7 progressive phases and 28 self-contained files—from fundamental I/O and memory models to OOP, asynchronous event loops, SQLite persistence, and GIL-aware concurrency.**

</div>

---

## 🎯 Design Philosophy

* **Self-Contained Execution:** Every `.py` file runs independently with zero external third-party dependencies required for Phases 1–6.
* **Line-by-Line Inline Annotations:** Concepts, edge cases, time/space trade-offs, and common runtime traps are documented directly inside the source code.
* **Production Standards:** Uses modern Python 3.10+ idioms including structural pattern matching (`match-case`), `pathlib.Path`, type annotations (`list[str]`, `X | None`), parameterized SQL queries, context managers (`with`), and `logging`.

---

## 📂 Repository Structure

```text
Python_Mastery_Curriculum/
├── 📄 README.md                                  # Curriculum documentation & technical reference
│
├── 🟦 Phase 1: Foundations
│   ├── 01_hello_and_io.py                        # Standard I/O, print(sep/end), input(), f-strings
│   ├── 02_variables_and_types.py                 # Dynamic typing, memory IDs, swapping, type casting
│   ├── 03_operators_and_strings.py               # Operators, 'is' vs '==', string slicing & methods
│   └── 04_control_flow.py                        # if/elif/else, match-case, while/for loops, loop-else
│
├── 🟩 Phase 2: Core Data Structures
│   ├── 05_lists.py                               # Dynamic arrays, slicing, enumerate(), shallow vs. deep copy
│   ├── 06_tuples_and_sets.py                     # Immutability, extended unpacking (*), O(1) sets & set math
│   ├── 07_dictionaries.py                        # Hash maps, safe .get(), dict union (|), frequency counters
│   └── 08_comprehensions.py                      # List, dict, and set comprehensions; matrix flattening
│
├── 🟨 Phase 3: Functions & Modularity
│   ├── 09_functions_and_scope.py                 # Type hints, mutable default trap, LEGB scope resolution
│   ├── 10_args_and_kwargs.py                     # Parameter ordering, *args, **kwargs, call-site unpacking
│   ├── 11_lambda_map_filter.py                   # Anonymous functions, custom sorting keys, map/filter/zip
│   └── 📁 12_modules_and_packages/
│       ├── math_utils.py                         # Reusable module & __name__ == "__main__" guard
│       └── 12_main_app.py                        # Standard library & custom module imports with aliases
│
├── 🟧 Phase 4: Error Handling & File Operations
│   ├── 13_exception_handling.py                  # try/except/else/finally, custom Exception subclasses
│   ├── 14_file_io_and_pathlib.py                 # Context managers (with), UTF-8 I/O, pathlib.Path
│   └── 15_csv_and_json.py                        # csv.DictReader/DictWriter, json.dump/load serialization
│
├── 🟪 Phase 5: Object-Oriented Programming (OOP)
│   ├── 16_classes_and_objects.py                 # Blueprints, __init__, self, @classmethod, @staticmethod
│   ├── 17_encapsulation_and_properties.py        # Access conventions, name mangling, @property getters/setters
│   ├── 18_inheritance_and_polymorphism.py        # Inheritance, super(), method overriding, ABCs, MRO
│   └── 19_dunder_methods_and_dataclasses.py      # __str__, __repr__, __len__, __add__, __getitem__, @dataclass
│
├── 🟥 Phase 6: Advanced Python & Concurrency
│   ├── 20_iterators_and_generators.py            # Lazy evaluation, yield, generator expressions, memory profiling
│   ├── 21_decorators_and_closures.py             # Lexical closures, @functools.wraps, parameterized decorators
│   ├── 22_regex_with_re.py                       # Raw strings, named capture groups, re.sub, compiled regex
│   ├── 23_async_programming.py                   # Coroutines, async/await, event loop, asyncio.gather()
│   ├── 24_sqlite_database.py                     # Embedded SQLite, transactional context managers, SQLi prevention
│   ├── 25_collections_and_itertools.py           # Counter, defaultdict, deque, namedtuple, product/combinations
│   ├── 26_logging_and_http_urllib.py             # Dual-handler logging, standard library HTTP GET via urllib
│   └── 27_threading_and_multiprocessing.py       # CPython GIL internals, ThreadPoolExecutor vs ProcessPoolExecutor
│
└── ⚙️ Phase 7: Environments & Packaging
    └── 📁 28_virtual_envs_and_packaging/
        ├── requirements.txt                      # Pinned dependency lockfile
        ├── pyproject.toml                        # PEP 621 project metadata & Pytest configuration
        └── venv_commands.sh                      # Isolated virtual environment (.venv) lifecycle commands
```

---

## 🧠 Technical Architecture & Internals Covered

### 1. Memory Model & Copy Semantics (`02`, `05`, `20`)
* **Object Identity vs. Value Equality:** Distinguishes reference comparison (`is` via `id()`) from structural equality (`==`).
* **Shallow vs. Deep Copy:** Demonstrates why `list.copy()` shares nested mutable references while `copy.deepcopy()` recursively duplicates object graphs.
* **Lazy Streaming (`yield`):** Contrasts eager $O(n)$ memory list comprehensions against $O(1)$ constant-memory generator expressions using `sys.getsizeof()`.

### 2. Data Structure Time Complexity (`05` – `07`, `25`)
| Structure | Lookup | Append / Push | Insert / Pop Left | Internal Backing |
| :--- | :--- | :--- | :--- | :--- |
| `list` | $O(1)$ by index / $O(n)$ search | $O(1)$ amortized | $O(n)$ | Contiguous pointer array |
| `deque` | $O(n)$ middle | $O(1)$ | $O(1)$ | Doubly-linked block list |
| `set` / `dict` | $O(1)$ average | $O(1)$ average | — | Open-addressed hash table |

### 3. Concurrency & The CPython GIL (`23`, `27`)
* **Single-Threaded Event Loop (`asyncio`):** Uses cooperative multitasking (`async`/`await`) to overlap network/I/O waits without thread context-switching overhead.
* **Multi-Threaded I/O (`ThreadPoolExecutor`):** Threads release the Global Interpreter Lock (GIL) during blocking I/O operations.
* **True CPU Parallelism (`ProcessPoolExecutor`):** Spawns independent OS processes—each with its own Python interpreter and GIL—to saturate multi-core CPUs.

### 4. Security & Reliability Guardrails (`13`, `14`, `24`, `26`)
* **SQL Injection Prevention:** Enforces `?` parameter binding in `sqlite3` instead of string interpolation.
* **Resource Leak Prevention:** Uses context managers (`with open(...)`, `with sqlite3.connect(...)`) for deterministic cleanup and automatic transaction commits/rollbacks.
* **Structured Observability:** Replaces ad-hoc `print()` calls with severity-leveled `logging` (`DEBUG` through `CRITICAL`) routed to console and disk handlers.

---

## 🚀 Environment & Packaging Setup

```bash
# 1. Clone the repository
git clone [https://github.com/vishaltechstack/Python-Mastery-Curriculum.git](https://github.com/vishaltechstack/Python-Mastery-Curriculum.git)
cd Python-Mastery-Curriculum

# 2. Create and activate an isolated virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.\.venv\Scripts\Activate.ps1     # Windows PowerShell

# 3. Install optional development dependencies
pip install -r 28_virtual_envs_and_packaging/requirements.txt

# 4. Run any lesson file directly
python 01_hello_and_io.py
```

---

## 👨‍💻 Author

**Vishal Sharma**
* **GitHub:** [@vishaltechstack](https://github.com/vishaltechstack)
* **Focus Areas:** Software Quality Assurance, Test Automation Frameworks (Java, Selenium, Playwright, Python), SQL & Backend Engineering
