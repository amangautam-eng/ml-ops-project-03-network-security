from pathlib import Path
from box import ConfigBox
import yaml
import os
import mlflow as ml

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

def log_metrics(metric_name:str,metric_val:float):
    with ml.start_run():
        ml.log_metric(metric_name,metric_val)

def log_params(param_name:str,param_val:dict):
    try:
        ml.log_metrics(param_name,param_val)
    except Exception as e:
        print(f"failed to log parameters : {e}")
        raise e

def log_model(model_name:str,model):
    try:
        ml.sklearn.log_model(
            sk_model=model,
            registered_model_name=model_name
        )
    except Exception as e:
        print(f"failed to log model: {e}")
        raise e