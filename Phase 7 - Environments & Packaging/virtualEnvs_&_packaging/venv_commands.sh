#!/usr/bin/env bash
# ==============================================================================
# FILE: venv_commands.sh
# TOPIC: Virtual Environment (venv) & pip Dependency Management Workflow
# ==============================================================================

# 1. Create an isolated virtual environment inside a '.venv' folder
python -m venv .venv

# 2. Activate the virtual environment:
#    Windows (PowerShell): .\.venv\Scripts\Activate.ps1
#    Windows (CMD):        .\.venv\Scripts\activate.bat
#    macOS / Linux:        source .venv/bin/activate

# 3. Upgrade pip and install packages into .venv ONLY
python -m pip install --upgrade pip
pip install pytest requests

# 4. Freeze exact installed versions into requirements.txt for teammates/CI
pip freeze > requirements.txt

# 5. Recreate the exact same environment on another machine:
pip install -r requirements.txt

# 6. Exit the virtual environment when finished:
deactivate
