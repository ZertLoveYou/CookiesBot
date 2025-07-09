# Cookies on the clouds ☁️💤
# ==========================
# blacklist.py

import json
import os
import time

BLACKLIST_PATH = 'data/blacklist.json'

def createblacklist(path=BLACKLIST_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if not os.path.exists(path):
        print('[❌] blacklist.json not found!')
        time.sleep(1)
        print('[ℹ️ ] Creating blacklist.json...')
        time.sleep(1)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump({"users": []}, file, indent=4)
        print('[✅] blacklist.json created!')
        time.sleep(1)

def load_blacklist():
    if not os.path.exists(BLACKLIST_PATH):
        return []
    try:
        with open(BLACKLIST_PATH, 'r', encoding = 'utf-8') as file:
            return json.load(file).get("users", [])
    except:
        return []
    
def save_blacklist(user_ids):
    user_ids = list(map(str, user_ids))
    with open(BLACKLIST_PATH, 'w') as file:
        json.dump({"users": user_ids}, file, indent = 4)

def add_to_blacklist(user_id):
    users = load_blacklist()
    user_id = str(user_id)
    if str(user_id) not in users:
        users.append(user_id)
        save_blacklist(users)

    print(f"[✅] Added to blacklist: {user_id}")

def remove_from_blacklist(user_id):
    users = load_blacklist()
    user_id = str(user_id)
    if str(user_id) in users:
        users.remove(user_id)
        save_blacklist(users)
    print(f"[✅] Removed from blacklist: {user_id}")

def is_blacklisted(user_id):
    return str(user_id) in load_blacklist()