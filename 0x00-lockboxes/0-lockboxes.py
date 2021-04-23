#!/usr/bin/python3


def canUnlockAll(boxes):
    """You have n number of locked boxes
    in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each
    box may contain keys to the other boxes.
    """
    if (type(boxes) is not list):
        return False
    if (len(boxes) == 0):
        return False

    keys = [0]
    for num in keys:
        for var in boxes[num]:
            if var not in keys and (var != num) and (var < len(boxes)) and (var != 0):
                keys.append(var)
    if len(keys) == len(boxes):
        return True
    return False
    