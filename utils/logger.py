# Cookies on the clouds ☁️💤
# ==========================
# config.py - logging system

import os
import datetime

def createlog(path='logs'):
    print(f'[ℹ️ ] Checking logs folder and log files...')

    # 1. Tạo folder nếu chưa có
    os.makedirs(path, exist_ok=True)

    # 2. Tạo 2 file log nếu chưa tồn tại
    log_files = {
        'usage.log': "Usage log file created",
        'error.log': "Error log file created"
    }

    full_paths = {}

    for filename, description in log_files.items():
        file_path = os.path.join(path, filename)
        full_paths[filename] = file_path

        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"{description} at {datetime.datetime.now()}\n")
                f.write("-" * 40 + "\n")
            print(f"[✅] {file_path} created!")
        else:
            print(f"[✔️ ] {file_path} exists and ready!")

    return full_paths['usage.log'], full_paths['error.log']

def log_usage(message, usage_path = 'logs/usage.log'):
    timestamp = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    with open(usage_path, 'a', encoding = 'utf-8') as file:
        file.write(f"{timestamp} {message}\n")

def log_error(error: Exception, error_path = 'logs/error.log'):
    timestamp = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    with open(error_path, 'a', encoding = 'utf-8') as file:
        file.write(f"{timestamp} {str(error)}\n")