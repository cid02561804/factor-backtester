from pathlib import Path
import yaml


def load_yaml_config(file_path: str) -> dict:
    """
    Load a YAML configuration file into a dictionary.
    """
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)