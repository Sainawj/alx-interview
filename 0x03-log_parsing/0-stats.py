#!/usr/bin/python3
import sys

# Initialize total file size and a dictionary to store status code counts
total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Function to print the current stats for
    total file size and status codes."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        # Check for valid line format with at least 7 elements
        if len(parts) < 7:
            continue
        try:
            # Extract the file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Increment line counter
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with invalid format
            continue

except KeyboardInterrupt:
    # On keyboard interruption, print the current stats
    print_stats()
    raise

# Ensure final output of stats if not already done
print_stats()
