import re

def parse_log_line(line: str) -> dict:
    pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$'
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
    
def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    log_entry = parse_log_line(line)
                    logs.append(log_entry)
                except ValueError as e:
                    print(f"Error parsing line '{line}': {str(e)}")
    return logs



def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = [log for log in logs if log["level"] == level]
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    log_counts = {}
    for log in logs:
        level = log["level"]
        if level in log_counts:
            log_counts[level] += 1
        else:
            log_counts[level] = 1
    return log_counts

def display_log_counts(counts: dict):
    for level, count in counts.items():
        print(f"{level}: {count}")

log_file = "basic.log"
parsed_logs = load_logs(log_file)
log_counts = count_logs_by_level(parsed_logs)
display_log_counts(log_counts)