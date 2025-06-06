# cyberwatch

**CyberWatch** is a Python-based modular system to detect and log suspicious activity patterns from simulated log files. It features:
- Pattern-matching for known threat signatures
- File hashing to detect tampering
- A CLI interface for batch log analysis
- Threaded scheduling for periodic log scans
- Pluggable threat signature system

## Features

- Parse raw logs and structure them
- Match known threats using configurable rules
- Compute hash of files to detect tampering
- Multi-threaded scheduled scans
- Modular file system for easy extensions

## Installation

```bash
git clone https://github.com/artasyaskar/cyberwatch.git
cd cyberwatch
pip install -r requirements.txt
