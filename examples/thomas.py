import matplotlib.pyplot as plt

from poincare_mapper.attractors import thomas
from poincare_mapper.mapper import PoincareMapper
from poincare_mapper.sections import z_equals_zero

mapper = PoincareMapper(
    system=thomas,
    section=z_equals_zero(),
)

result = mapper.run(
    initial_state=[1.0, 1.0, 1.0],
    t_span=(0, 10000),
)

crossings = result["crossings"]

plt.figure(figsize=(8, 8))
plt.scatter(
    crossings[:, 0],
    crossings[:, 1],
    s=1,
)
plt.title("Thomas Attractor Poincaré Section")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()
