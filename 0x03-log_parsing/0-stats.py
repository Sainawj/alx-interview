#!/usr/bin/python3

import sys


def print_msg(status_codes_count, total_file_size):
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
    for code, count in sorted(status_codes_count.items()):
        if count > 0:
            print("{}: {}".format(code, count))


# Initialize total file size, status code counter
# and the number of lines processed
total_file_size = 0
status_code = 0
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
        # Split the line into parts and reverse it for easier access
        parsed_line = line.split()[::-1]

        # Check if there are enough elements in the parsed line
        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                # Update total file size with the first element (file size)
                total_file_size += int(parsed_line[0])
                status_code = parsed_line[1]  # Get the status code

                # If the status code is in our dictionary, increment its count
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

            # Print messages for every 10 lines processed
            if line_count == 10:
                print_msg(status_codes_count, total_file_size)
                line_count = 0  # Reset line count for the next batch

# Finally, print the results for any remaining lines processed
finally:
    print_msg(status_codes_count, total_file_size)
