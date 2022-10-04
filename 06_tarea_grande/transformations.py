import numpy as np


def translation_along_zaxis(a):
    T = [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, a], [0, 0, 0, 1]
    return T


def rotation_around_zaxis(q):
    R = (
        [np.cos(q), -np.sin(q), 0, 0],
        [np.sin(q), np.cos(q), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    )
    return R


def rotation_around_yaxis(q):
    R = (
        [np.cos(q), 0, -np.sin(q), 0],
        [0, 1, 0, 0],
        [np.sin(q), 0, np.cos(q), 0],
        [0, 0, 0, 1],
    )
    return R
