#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics."""

import sys

def printStatus(dic, size):
    """Prints accumulated file size and status code counts."""
    print("File size: {:d}".format(size))
    for code in sorted(dic.keys()):
        if dic[code] != 0:
            print("{}: {:d}".format(code, dic[code]))

statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        count += 1
        stlist = line.split()

        try:
            # Add the file size (last item in the line)
            size += int(stlist[-1])
        except (IndexError, ValueError):
            pass

        try:
            # Update status code count if it exists in our dictionary
            if stlist[-2] in statusCodes:
                statusCodes[stlist[-2]] += 1
        except IndexError:
            pass

        # Print status every 10 lines
        if count % 10 == 0:
            printStatus(statusCodes, size)

    # Print final stats if remaining lines after the last multiple of 10
    printStatus(statusCodes, size)

except KeyboardInterrupt:
    # Print stats on manual interruption
    printStatus(statusCodes, size)
    raise

