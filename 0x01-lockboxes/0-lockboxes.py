#!/usr/bin/python3
"""
Solution to the lockboxes problem.
This script determines if all boxes can be unlocked given a list of boxes where
each box may contain keys to other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked starting from the first box.
    
    Arguments:
    boxes -- a list of lists, where each inner list contains keys (integers) to other boxes.
    
    Returns:
    True if all boxes can be unlocked, False otherwise.
    """
    
    # Ensure that the input is a valid list
    if not isinstance(boxes, list):
        return False
    
    # If there are no boxes, return False
    if len(boxes) == 0:
        return False
    
    # Iterate through all boxes starting from box 1 (box 0 is always open)
    for box_num in range(1, len(boxes)):
        is_unlocked = False  # Flag to check if the current box can be unlocked
        
        # Check if the current box number can be found as a key in any other box
        for idx in range(len(boxes)):
            # Box can be unlocked if its number is found in any other box (except itself)
            if box_num in boxes[idx] and box_num != idx:
                is_unlocked = True
                break
        
        # If a box cannot be unlocked, return False
        if not is_unlocked:
            return False
    
    # If all boxes can be unlocked, return True
    return True