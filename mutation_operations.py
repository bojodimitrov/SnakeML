import random


def replace_weight(weight):
    """
    Replaces weight
    """
    return random.randint(-1, 1)


def scale(weight):
    """
    Scales weight by some value
    """
    return weight * random.uniform(0.5, 1.5)


def shift(weight):
    """
    Adds random number between -0.8, 0.8
    """
    return weight + random.uniform(-0.5, 0.5)


def swap_sign(weight):
    """
    Swaps sign of weight
    """
    return weight * (-1)


def lesser_shift(weight):
    """
    Narrows the shift
    """
    return shift(weight) * 0.07


def lesser_scale(weight):
    """
    Narrows the scale
    """
    return scale(weight) * 0.3
