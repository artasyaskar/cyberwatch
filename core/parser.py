def parse_log_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]
