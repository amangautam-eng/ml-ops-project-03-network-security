from pathlib import Path
from box import ConfigBox
import yaml
import os


def read_yaml(path: Path) -> ConfigBox:
    with open(path) as f:
        content = yaml.safe_load(f)
    # Wrapping the dictionary in a ConfigBox before returning it
    return ConfigBox(content)


def create_dir(path:list[str]):
    current_dir=os.getcwd()
    for paths in path:
        os.makedirs(os.path.join(current_dir,Path(paths)),exist_ok=True)
        
