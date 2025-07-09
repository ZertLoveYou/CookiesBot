# Cookies on the clouds ☁️💤
# ==========================
# config.py - check config.json

import os
import sys
import time
import json

def createconfig(path='data/config.json'):
    default_config = {
        "TOKEN": "your bot token here",
        "PREFIX": "your bot prefix here",
        "CLIENT_ID": "your bot client id here",
        "BOT_NAME": "your bot name here"
    }

    os.makedirs(os.path.dirname(path), exist_ok=True)

    if not os.path.exists(path):
        print('[❌] config.json not found!')
        time.sleep(1)
        print('[ℹ️ ] Creating config.json...')
        time.sleep(1)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(default_config, file, indent=4)
        print('[✅] config.json created!\n     👉 Fill it before restarting the bot!')
        time.sleep(2)
        sys.exit()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            config = json.load(file)

            for key, placeholder in default_config.items():
                if config.get(key) == placeholder:
                    print(f"[❌] Please update your {key} in config.json!")
                    sys.exit(f"     🛑 Bot stopped due to missing config: {key}")

            print('[✅] config.json is valid and ready to use!')
            return config

    except json.JSONDecodeError:
        print('[❌] config.json contains invalid JSON.')
    except Exception as e:
        print(f'[❌] Failed to read config.json: {e}')

    time.sleep(2)
    sys.exit()
