from core.detector import ThreatDetector

def test_detector_sql_injection():
    lines = ["SELECT * FROM users WHERE username = 'admin'"]
    d = ThreatDetector()
    result = d.scan_log(lines)
    assert result[0]['threat'] == 'SQL Injection'

def test_detector_no_threat():
    lines = ["User logged in successfully"]
    d = ThreatDetector()
    result = d.scan_log(lines)
    assert result == []
