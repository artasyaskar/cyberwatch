mport tempfile
from core.parser import parse_log_file

def test_parser_skips_blank_lines():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
        f.write("line1\n\nline2\n")
        path = f.name
    lines = parse_log_file(path)
    assert lines == ['line1', 'line2']
