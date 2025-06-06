
def test_detect_xss():
    lines = ["<script>alert('hack');</script>"]
    d = ThreatDetector()
    result = d.scan_log(lines)
    assert result[0]['threat'] == 'XSS Attempt'

def test_path_traversal():
    lines = ["GET /../../etc/passwd"]
    d = ThreatDetector()
    result = d.scan_log(lines)
    assert result[0]['threat'] == 'Path Traversal'
