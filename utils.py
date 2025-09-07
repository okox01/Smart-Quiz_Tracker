import json
import os

def load_json(filepath):
    """Load JSON file if exists, else return empty dict. Handles empty files."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                # file exists but is empty or invalid
                return {}
    else:
        return {}  # file doesn't exist

def save_json(data, filepath):
    """Save JSON data to file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
