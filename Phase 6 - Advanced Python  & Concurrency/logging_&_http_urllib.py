# ==============================================================================
# FILE: 26_logging_and_http_urllib.py
# TOPIC: Structured logging Module (Replacing print) & HTTP API Calls via urllib
# ==============================================================================

import logging
import json
import urllib.request
import urllib.error
from pathlib import Path

# ==============================================================================
# PART A: PRODUCTION LOGGING (Never rely on print() in real applications!)
# ==============================================================================
# Severity Levels (lowest to highest):
#   DEBUG (10) -> INFO (20) -> WARNING (30) -> ERROR (40) -> CRITICAL (50)

log_path = Path("sample_workspace") / "app_runtime.log"
log_path.parent.mkdir(exist_ok=True)

# Configure logging to write to BOTH the console AND a log file simultaneously:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                  # Prints to terminal
        logging.FileHandler(log_path, mode="a", encoding="utf-8")  # Appends to file
    ]
)

logger = logging.getLogger("APIClient")

logger.debug("Debug diagnostics initialized.")
logger.info("Starting HTTP verification check.")
logger.warning("Response latency threshold set to 2000ms.")

# ==============================================================================
# PART B: BUILT-IN HTTP CLIENT (urllib.request — Zero External Dependencies)
# ==============================================================================
# Note: In third-party projects, 'requests' or 'httpx' is popular,
# but urllib.request works out-of-the-box in every Python installation.

def fetch_json_get(url: str, timeout_sec: int = 5) -> dict | None:
    """Performs a clean HTTP GET request and parses the JSON response."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "PythonCurriculumClient/1.0", "Accept": "application/json"},
        method="GET"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as response:
            status_code = response.getcode()
            raw_body = response.read().decode("utf-8")
            logger.info(f"GET {url} -> HTTP {status_code}")
            return json.loads(raw_body)
    except urllib.error.HTTPError as http_err:
        logger.error(f"HTTP Error {http_err.code} on {url}: {http_err.reason}")
    except urllib.error.URLError as url_err:
        logger.error(f"Network unreachable for {url}: {url_err.reason}")
    return None

# Example call against a public test JSON API:
post_data = fetch_json_get("https://jsonplaceholder.typicode.com/posts/1")
if post_data:
    logger.info(f"Fetched Post Title: '{post_data.get('title')}'")
