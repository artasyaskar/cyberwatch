import argparse
from core.parser import parse_log_file
from core.detector import ThreatDetector
from utils.logger import log_threat

def main():
    parser = argparse.ArgumentParser(description="CyberWatch Threat Scanner")
    parser.add_argument('--scan', type=str, required=True, help='Path to log file')
    args = parser.parse_args()

    lines = parse_log_file(args.scan)
    detector = ThreatDetector()
    threats = detector.scan_log(lines)
    if threats:
        for t in threats:
            log_threat(t)
    else:
        print("No threats detected.")

if __name__ == '__main__':
    main()
