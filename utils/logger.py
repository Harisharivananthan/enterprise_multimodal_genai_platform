import logging
import logging.config
from pathlib import Path
import yaml

def setup_logging():
    config_path = Path("logging/logging.yaml")

    if config_path.exists():
        with open (config_path,"r") as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = logging.INFO)        