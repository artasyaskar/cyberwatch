import tempfile
from utils.hash_tools import calculate_sha256

def test_hash_output_consistency():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
        f.write("testdata")
        path = f.name
    hash1 = calculate_sha256(path)
    hash2 = calculate_sha256(path)
    assert hash1 == hash2
