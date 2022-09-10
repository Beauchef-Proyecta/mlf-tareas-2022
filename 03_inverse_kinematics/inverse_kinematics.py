import numpy as np


def position_to_dof(x, y, z):
    q = [0, 0, 0]
    l = [55, 39, 135, 147, 66]

    # Calculations
    q[0] = np.arctan(y / x)

    q[2] = np.arccos(
        (
            (np.sqrt(x**2 + y**2) - l[4]) ** 2
            + (z - l[1] - l[0]) ** 2
            + -l[2] ** 2
            + -l[3] ** 2
        )
        / (2 * l[2] * l[3])
    )

    q[1] = (
        np.pi / 2
        + -np.arctan((z - l[1] - l[0]) / (np.sqrt(x**2 + y**2) - l[4]))
        + -np.arctan((l[3] * np.sin(q[2])) / (l[2] + l[3] * np.cos(q[2])))
    )

    # Formatting
    # El robot solo entiende grados sexagesimales y enteros
    q0 = int(np.round(q[0] * 180 / np.pi, 0))
    q1 = int(np.round(q[1] * 180 / np.pi, 0))
    q2 = int(np.round(q[2] * 180 / np.pi, 0))

    return q0, q1, q2
