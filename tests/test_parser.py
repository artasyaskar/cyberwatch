
def test_parse_real_log(tmp_path):
    log_file = tmp_path / "log.txt"
    log_file.write_text("SELECT * FROM users;\n\n<script>alert(1)</script>\n")
    lines = parse_log_file(str(log_file))
    assert len(lines) == 2
    assert lines[0].startswith("SELECT")
