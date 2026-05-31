"""
Poincare section definitions.

A Poincare section is represented as an event function compatible with
scipy.integrate.solve_ivp. The event function returns zero when the
trajectory intersects the section.
"""

from __future__ import annotations

import numpy as np


def plane_section(normal, offset=0.0, direction=1):
    """
    Create a generic hyperplane Poincare section.

    The section is defined by:

        normal · state = offset

    Parameters
    ----------
    normal:
        Normal vector of the section plane.
    offset:
        Scalar offset from the origin.
    direction:
        Crossing direction for scipy event detection.

        direction =  1  detects negative-to-positive crossings
        direction = -1  detects positive-to-negative crossings
        direction =  0  detects crossings in either direction

    Returns
    -------
    callable
        Event function suitable for scipy.integrate.solve_ivp.

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

    normal = np.asarray(normal, dtype=float)

    if normal.ndim != 1:
        raise ValueError("Section normal vector must be one-dimensional.")

    norm = np.linalg.norm(normal)

    if norm == 0:
        raise ValueError("Section normal vector must be non-zero.")

    normal = normal / norm
    offset = float(offset)

    def event(t, state):
        state = np.asarray(state, dtype=float)

        if state.shape[0] != normal.shape[0]:
            raise ValueError(
                "State dimension does not match section normal dimension."
            )

        return float(np.dot(normal, state) - offset)

    event.direction = direction
    event.terminal = False

    return event


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
