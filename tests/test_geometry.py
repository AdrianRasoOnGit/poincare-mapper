import numpy as np
import pytest

from poincare_mapper.geometry import plane_basis, project_to_plane


def test_plane_basis_is_orthonormal():
    normal = np.array([0.0, 1.0, 0.0])

    u, v = plane_basis(normal)

    assert np.dot(u, normal) == pytest.approx(0.0)
    assert np.dot(v, normal) == pytest.approx(0.0)
    assert np.dot(u, v) == pytest.approx(0.0)

    assert np.linalg.norm(u) == pytest.approx(1.0)
    assert np.linalg.norm(v) == pytest.approx(1.0)


def test_project_to_plane_returns_2d_coordinates():
    points = np.array(
        [
            [1.0, 0.0, 2.0],
            [3.0, 0.0, 4.0],
        ]
    )

    projected = project_to_plane(points, normal=[0.0, 1.0, 0.0])

    assert projected.shape == (2, 2)


def test_zero_normal_raises():
    with pytest.raises(ValueError):
        plane_basis([0.0, 0.0, 0.0])
