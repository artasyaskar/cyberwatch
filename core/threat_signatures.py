KNOWN_THREATS = {
    "SQL Injection": r"(SELECT|INSERT|DELETE|UPDATE).*FROM",
    "XSS Attempt": r"<script>.*</script>",
    "Path Traversal": r"\.\.\/",
    "Suspicious IP": r"192\.168\.1\.\d{1,3}"
}
