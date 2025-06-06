import re
from core.threat_signatures import KNOWN_THREATS

class ThreatDetector:
    def __init__(self):
        self.signatures = KNOWN_THREATS

    def scan_log(self, log_lines):
        threats_found = []
        for line_num, line in enumerate(log_lines, 1):
            for threat_name, pattern in self.signatures.items():
                if re.search(pattern, line):
                    threats_found.append({
                        "line": line_num,
                        "match": line.strip(),
                        "threat": threat_name
                    })
        return threats_found
