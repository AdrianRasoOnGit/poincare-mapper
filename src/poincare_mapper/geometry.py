import numpy as np


def plane_basis(normal):
    normal = np.asarray(normal, dtype=float)

    norm = np.linalg.norm(normal)
    if norm == 0:
        raise ValueError("Normal vector must be non-zero.")

    n = normal / norm

    if abs(n[0]) < 0.9:
        reference = np.array([1.0, 0.0, 0.0])
    else:
        reference = np.array([0.0, 1.0, 0.0])

    u = np.cross(n, reference)
    u = u / np.linalg.norm(u)

    v = np.cross(n, u)
    v = v / np.linalg.norm(v)

    return u, v


def project_to_plane(points, normal):
    points = np.asarray(points, dtype=float)

    if points.ndim != 2:
        raise ValueError("Points must be a 2D array.")

    u, v = plane_basis(normal)

    projected_u = points @ u
    projected_v = points @ v

    return np.column_stack([projected_u, projected_v])
