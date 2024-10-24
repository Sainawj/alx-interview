#!/usr/bin/python3
import sys
import signal
import re

# Initialize the variables
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

line_count = 0

# Regex pattern to match the log format
log_pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
)


def print_stats():
    """Print the current statistics of file size and status code counts."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle the Ctrl+C signal by printing stats before exiting."""
    print_stats()
    sys.exit(0)


# Set up the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        match = log_pattern.match(line)

        # Check if the line matches the expected format
        if not match:
            print("DEBUG: Skipping line due to incorrect format")
            continue

        # Extract the necessary values from regex match
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))

        # Update the total file size
        total_file_size += file_size

        # Update the status code count if valid
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            print(f"DEBUG: Status code {status_code} "
                  "not in known status codes")

            line_count += 1

        # Every 10 lines, print the stats
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # If interrupted by keyboard, print the stats
    print_stats()
    sys.exit(0)
