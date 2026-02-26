import yaml

def load_config(config_path="config.yml"):

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Config {config_path} not found. Using default values.")
        return {
            'source_lang': 'en',
            'target_lang': 'ru',
            'batch_size': 10,
            'sleep_sec': 1.0,
            'xpath': './/phrase'
        }