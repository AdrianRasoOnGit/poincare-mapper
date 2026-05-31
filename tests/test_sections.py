import numpy as np
import pytest

from poincare_mapper.sections import (
    plane_section,
    x_equals_zero,
    y_equals_zero,
    z_equals_zero,
)


def test_plane_section_zero_crossing():
    event = plane_section([0, 0, 1])

    state = np.array([1.0, 2.0, 0.0])

    assert event(0.0, state) == pytest.approx(0.0)


def test_plane_section_positive_side():
    event = plane_section([0, 0, 1])

    state = np.array([1.0, 2.0, 3.0])

    assert event(0.0, state) > 0.0


def test_plane_section_negative_side():
    event = plane_section([0, 0, 1])

    state = np.array([1.0, 2.0, -3.0])

    assert event(0.0, state) < 0.0


def test_plane_with_offset():
    event = plane_section([0, 0, 1], offset=5.0)

    assert event(0.0, [1, 2, 5]) == pytest.approx(0.0)
    assert event(0.0, [1, 2, 7]) > 0.0
    assert event(0.0, [1, 2, 3]) < 0.0


def test_x_equals_zero():
    event = x_equals_zero()

    assert event(0.0, [0, 10, 20]) == pytest.approx(0.0)
    assert event(0.0, [5, 10, 20]) > 0.0
    assert event(0.0, [-5, 10, 20]) < 0.0


def test_y_equals_zero():
    event = y_equals_zero()

    assert event(0.0, [10, 0, 20]) == pytest.approx(0.0)
    assert event(0.0, [10, 5, 20]) > 0.0
    assert event(0.0, [10, -5, 20]) < 0.0


def test_z_equals_zero():
    event = z_equals_zero()

    assert event(0.0, [10, 20, 0]) == pytest.approx(0.0)
    assert event(0.0, [10, 20, 5]) > 0.0
    assert event(0.0, [10, 20, -5]) < 0.0


def test_direction_is_preserved():
    event = plane_section([0, 0, 1], direction=-1)

    assert event.direction == -1
    assert event.terminal is False


def test_normalization_does_not_change_plane():
    event = plane_section([0, 0, 10])

    assert event(0.0, [1, 2, 0]) == pytest.approx(0.0)
