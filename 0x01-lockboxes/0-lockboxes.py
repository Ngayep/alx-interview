#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from box 0.

    Args:
        boxes (list of lists): A list where each index represents
        a box and contains a list of keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Set of boxes that have been opened, starting with box 0
    opened_boxes = set([0])
    # Stack to explore keys from box 0
    keys_to_explore = [0]
    # Traverse the boxes using the keys
    while keys_to_explore:
        current_box = keys_to_explore.pop()  # Get a box to explore

        for key in boxes[current_box]:
            # If the key opens a box that hasn't been opened and
            # it's within bounds
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)  # Open the box
                # Add it to the stack to explore further
                keys_to_explore.append(key)
    # If the number of opened boxes is equal to the total number of boxes,
    # return True
    return len(opened_boxes) == len(boxes)
