import sys
from pathlib import Path
import re

def parse_log_line(line: str) -> dict:
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$' #  setting pattern to recognize message format
    match = re.match(pattern, line)
    if match:
        timestamp = match.group(1)
        level = match.group(2)
        message = match.group(3)
        return {
            'timestamp': timestamp,
            'level': level,
            'message': message
        }
    else:
        raise ValueError(f"Invalid log line format: {line}")

def load_logs(file_path: str) -> list:  #   extracting and storing timestamp, log level, and message in the dictionary
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        log_entry = parse_log_line(line)
                        logs.append(log_entry)
                    except ValueError as e:
                        print(f"Error parsing line '{line}': {str(e)}")
    except FileNotFoundError:
        print(f"Error: '{file_path}' - not found")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    log_counts = {}    #  Returns a filtered list of log entries (dictionaries) where each log has a level key that matches with specified level

    for log in logs:
        level = log["level"]
        if level in log_counts:
            log_counts[level] += 1
        else:
            log_counts[level] = 1
    return log_counts

def display_log_counts(counts: dict, logs: list, detailed_level: str = None):
    #   prints header in a format given in exercise
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    total = sum(counts.values())
    for level, count in counts.items():
        print(f"{level:<17} | {count}")
    
    if detailed_level:
        print(f"\nДеталі логів для рівня '{detailed_level}':")
        filtered_logs = filter_logs_by_level(logs, detailed_level)
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <path_to_log_file> <log_level>")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2].upper()

    parsed_logs = load_logs(log_file)
    log_counts = count_logs_by_level(parsed_logs)
    display_log_counts(log_counts, parsed_logs, detailed_level=log_level)


# script check: 
# python3 /Users/volodymyrmikhidenko/Documents/HW05/goit-pycore-hw-05/ex03/main.py /Users/volodymyrmikhidenko/Documents/HW05/goit-pycore-hw-05/ex03/basic.log error
