#!/usr/bin/python3
"""calculates the fewest number of operations needed
   to result in exactly n H characters in the file."""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # While n is divisible by the factor
        while n % factor == 0:
            operations += factor
            # We perform `factor` operations (copy + multiple pastes)
            n //= factor  # Reduce n
        factor += 1  # Check the next factor

    return operations
