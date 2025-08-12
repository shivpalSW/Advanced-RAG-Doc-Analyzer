import yaml


def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    print("Configuration loaded successfully.", config)
    return config

load_config("config/config.yaml")