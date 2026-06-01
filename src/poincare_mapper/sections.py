"""
Poincare section definitions.

A Poincare section is represented as a callable event object compatible
with scipy.integrate.solve_ivp. The event returns zero when the trajectory
intersects the section.
"""

from __future__ import annotations

import numpy as np


class PlaneSection:
    """
    Generic hyperplane Poincare section.

    The section is defined by:

        normal · state = offset
    """

    def __init__(self, normal, offset=0.0, direction=1):
        normal = np.asarray(normal, dtype=float)

        if normal.ndim != 1:
            raise ValueError("Section normal vector must be one-dimensional.")

        norm = np.linalg.norm(normal)

        if norm == 0:
            raise ValueError("Section normal vector must be non-zero.")

        self.normal = normal / norm
        self.offset = float(offset)
        self.direction = direction
        self.terminal = False

    def __call__(self, t, state):
        state = np.asarray(state, dtype=float)

        if state.ndim != 1:
            raise ValueError("State vector must be one-dimensional.")

        if state.shape[0] != self.normal.shape[0]:
            raise ValueError(
                "State dimension does not match section normal dimension."
            )

        return float(np.dot(self.normal, state) - self.offset)


def plane_section(normal, offset=0.0, direction=1):
    """
    Create a generic hyperplane Poincare section.

    Examples
    --------
    z = 0:
        plane_section([0, 0, 1])

    z = 27:
        plane_section([0, 0, 1], offset=27)

    x + y = 5:
        plane_section([1, 1, 0], offset=5)

    x = z:
        plane_section([1, 0, -1])
    """

    return PlaneSection(
        normal=normal,
        offset=offset,
        direction=direction,
    )


def x_equals_zero(direction=1):
    """
    Convenience section for x = 0.
    """
    return plane_section(
        normal=[1.0, 0.0, 0.0],
        offset=0.0,
        direction=direction,
    )


def y_equals_zero(direction=1):
    """
    Convenience section for y = 0.
    """
    return plane_section(
        normal=[0.0, 1.0, 0.0],
        offset=0.0,
        direction=direction,
    )


def z_equals_zero(direction=1):
    """
    Convenience section for z = 0.
    """
    return plane_section(
        normal=[0.0, 0.0, 1.0],
        offset=0.0,
        direction=direction,
    )
