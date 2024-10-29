#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines if a data set represents a valid UTF-8 encoding."""

    num_bytes = 0  # Tracks the number of continuation bytes expected

    # Masks for different patterns
    mask_1_byte = 0b10000000  # 128, checks for single-byte (0xxxxxxx)
    mask_2_bytes = 0b11100000  # 224, checks for two-byte starter (110xxxxx)
    mask_3_bytes = 0b11110000  # 240, checks for three-byte starter (1110xxxx)
    mask_4_bytes = 0b11111000  # 248, checks for four-byte starter (11110xxx)
    mask_cont = 0b11000000  # 192, checks continuation (10xxxxxx)

    for byte in data:
        # Check if we’re expecting continuation bytes
        if num_bytes == 0:
            # Determine how many bytes in this UTF-8 character
            if (byte & mask_1_byte) == 0:
                continue  # 1-byte character (0xxxxxxx), move to next
            elif (byte & mask_2_bytes) == 0b11000000:
                num_bytes = 1  # 2-byte character
            elif (byte & mask_3_bytes) == 0b11100000:
                num_bytes = 2  # 3-byte character
            elif (byte & mask_4_bytes) == 0b11110000:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte pattern
        else:
            # Check continuation byte (10xxxxxx)
            if (byte & mask_cont) != 0b10000000:
                return False
            num_bytes -= 1  # Decrement continuation byte count

    return num_bytes == 0  # Valid if no remaining expected bytes
