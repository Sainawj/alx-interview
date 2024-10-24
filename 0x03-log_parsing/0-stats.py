#!/usr/bin/python3

import sys

def print_metrics(status_codes_count, total_file_size):
    """
    Prints the total file size and the count of different HTTP status codes.

    Args:
        status_codes_count (dict): contains status codes and their counts.
        total_file_size (int): Total size of the files processed.

    Returns:
        None
    """
    print("Total File Size: {}".format(total_file_size))
    # Print each status code with a count, if the count is greater than zero
    for code in sorted(status_codes_count.keys()):
        count = status_codes_count[code]
        if count > 0:
            print("{}: {}".format(code, count))


# Initialize total file size, status code counter, and the number of lines processed
total_file_size = 0
line_count = 0

# Dictionary to hold counts of different HTTP status codes
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    # Read lines from standard input
    for line in sys.stdin:
        # Parse the line according to the specified format
        parts = line.split()
        
        # Check if the line matches the expected format
        if len(parts) >= 6 and parts[1].startswith('-') and parts[3].startswith('"') and parts[4].startswith('HTTP/'):
            # Extract relevant fields
            status_code = parts[-2]
            file_size = parts[-1]

            # Update metrics only if the status code is valid and the file size is an integer
            if status_code in status_codes_count and file_size.isdigit():
                total_file_size += int(file_size)
                status_codes_count[status_code] += 1
                line_count += 1

                # Print metrics for every 10 lines processed
                if line_count == 10:
                    print_metrics(status_codes_count, total_file_size)
                    line_count = 0  # Reset line count for the next batch

except KeyboardInterrupt:
    # Handle keyboard interruption to print final metrics
    print_metrics(status_codes_count, total_file_size)

finally:
    # Print the results for any remaining lines processed
    if line_count > 0:
        print_metrics(status_codes_count, total_file_size)
