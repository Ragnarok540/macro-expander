from datetime import datetime as dt
import json
import os
import os.path
import sys


def file_names(directory: str, extension: str) -> list[str]:
    result = []

    for root, _, files in os.walk(directory):
        for name in files:
            _, ext = os.path.splitext(name)

            if ext == extension:
                result.append(os.path.join(root, name))

    return result


def process_file(path: str, macro_rules: dict, new_path: str):
    result = []

    with open(path, 'r') as f:
        for line in f:
            current_line = line
            for old, new in macro_rules.items():
                current_line = current_line.replace(old, new)

            result.append(current_line)

    _, file_name = os.path.split(path)

    with open(os.path.join(new_path, file_name), 'w') as f:
        for line in result:
            f.write(line)


if __name__ == '__main__':
    try:
        path = sys.argv[1]  # './test.txt'
    except IndexError:
        print("[ERROR] no path provided")
        sys.exit()

    try:
        rules = sys.argv[2]  # './macro_rules_a.json'
    except IndexError:
        print("[ERROR] no macro rules provided")
        sys.exit()

    directory = False

    if os.path.isdir(path):
        try:
            ext = sys.argv[3]  # 'txt'
            directory = True
        except IndexError:
            print("[ERROR] no extension provided")
            sys.exit()

    with open(rules, 'r') as f:
        macro_rules = json.load(f)

    date_time = dt.now().strftime('%Y%m%d%H%M%S')
    new_path = f'./expanded_{date_time}'

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    if directory:
        names = file_names(path, ext)
        for name in names:
            process_file(name, macro_rules, new_path)
    else:
        process_file(path, macro_rules, new_path)
