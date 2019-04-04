import math


def normalize_vector(vector):
    if all(t == 0 for t in vector):
        return vector
    norm = math.sqrt(sum(map(lambda x: x*x, vector)))
    return list(map(lambda x: x / norm, vector))
