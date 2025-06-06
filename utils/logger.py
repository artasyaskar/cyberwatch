from datetime import datetime

def log_threat(threat):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] THREAT DETECTED: {threat['threat']} on line {threat['line']}: {threat['match']}")
