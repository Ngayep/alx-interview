#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics."""

import sys
import re

def print_stats(total_size, status_counts):
    """Prints the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

# Dictionary to store the count of each status code
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

# Regular expression to match the expected log line format
log_pattern = re.compile(
    r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)$'
)

try:
    for line in sys.stdin:
        line_count += 1
        match = log_pattern.match(line.strip())
        
        # Process line if it matches the expected format
        if match:
            status_code = match.group("status")
            file_size = int(match.group("size"))

            # Update total file size
            total_size += file_size

            # Update status code count if valid
            if status_code in status_codes:
                status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    # Print statistics if interrupted
    print_stats(total_size, status_codes)
    raise

# Final print after EOF
print_stats(total_size, status_codes)

