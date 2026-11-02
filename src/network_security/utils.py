from pathlib import Path
from box import ConfigBox
import yaml
import os


def read_yaml(path: Path) -> ConfigBox:
    with open(path) as f:
        content = yaml.safe_load(f)
    # Wrapping the dictionary in a ConfigBox before returning it
    return ConfigBox(content)

def create_dir(path: Path):
    """
    Creates a directory if it doesn't exist. 
    If a full file path is passed, it extracts and creates the parent directory.
    """
    # If it's a file path (e.g., has an extension like .csv), get its parent directory
    path=Path(path)
    if path.suffix:
        directory = path.parent
    else:
        directory = path

    # Create the directory (handles absolute paths or relative paths from current working dir)
    directory.mkdir(parents=True, exist_ok=True)
