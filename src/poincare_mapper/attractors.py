"""
Collection of continuous-time dynamical systems.
"""


def roessler(t, state, a=0.2, b=0.2, c=5.7):
    """
    Rössler attractor.

    dx/dt = -y - z
    dy/dt = x + a*y
    dz/dt = b + z*(x - c)
    """
    x, y, z = state

    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)

    return [dxdt, dydt, dzdt]


def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    """
    Lorenz attractor.

    dx/dt = sigma * (y - x)
    dy/dt = x * (rho - z) - y
    dz/dt = x * y - beta * z
    """
    x, y, z = state

    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return [dxdt, dydt, dzdt]


def duffing(t, state, delta=0.2, alpha=-1.0, beta=1.0, gamma=0.3, omega=1.2):
    """
    Forced Duffing oscillator.

    State:
        x = position
        y = velocity

    x' = y
    y' = -delta*y - alpha*x - beta*x^3 + gamma*cos(omega*t)
    """
    import numpy as np

    x, y = state

    dxdt = y
    dydt = (
        -delta * y
        - alpha * x
        - beta * x**3
        + gamma * np.cos(omega * t)
    )

    return [dxdt, dydt]

def chen(t, state, a=35.0, b=3.0, c=28.0):
    """
    Chen attractor.
    """
    x, y, z = state

    dxdt = a * (y - x)
    dydt = (c - a) * x - x * z + c * y
    dzdt = x * y - b * z

    return [dxdt, dydt, dzdt]

def thomas(t, state, b=0.208186):
    """
    Thomas cyclically symmetric attractor.
    """
    import numpy as np

    x, y, z = state

    dxdt = np.sin(y) - b * x
    dydt = np.sin(z) - b * y
    dzdt = np.sin(x) - b * z

    return [dxdt, dydt, dzdt]

def halvorsen(t, state, a=1.4):
    """
    Halvorsen attractor.
    """
    x, y, z = state

    dxdt = -a * x - 4 * y - 4 * z - y**2
    dydt = -a * y - 4 * z - 4 * x - z**2
    dzdt = -a * z - 4 * x - 4 * y - x**2

    return [dxdt, dydt, dzdt]

def aizawa(
    t,
    state,
    a=0.95,
    b=0.7,
    c=0.6,
    d=3.5,
    e=0.25,
    f=0.1,
):
    """
    Aizawa attractor.
    """
    x, y, z = state

    dxdt = (z - b) * x - d * y
    dydt = d * x + (z - b) * y

    dzdt = (
        c
        + a * z
        - (z**3) / 3
        - (x**2 + y**2) * (1 + e * z)
        + f * z * x**3
    )

    return [dxdt, dydt, dzdt]

def dadras(t, state, a=3, b=2.7, c=1.7, d=2, e=9):
    """
    Dadras attractor.
    """
    x, y, z = state

    dxdt = y - a * x + b * y * z
    dydt = c * y - x * z + z
    dzdt = d * x * y - e * z

    return [dxdt, dydt, dzdt]
