import matplotlib.pyplot as plt

from poincare_mapper.attractors import lorenz
from poincare_mapper.mapper import PoincareMapper
from poincare_mapper.sections import plane_section

section = plane_section(
    normal=[0, 0, 1],
    offset=27,
    direction=1,
)

mapper = PoincareMapper(
    system=lorenz,
    section=section,
)

result = mapper.run(
    initial_state=[1, 1, 1],
    t_span=(0, 500),
)

crossings = result["crossings"]

plt.figure(figsize=(8, 8))
plt.scatter(
    crossings[:, 0],
    crossings[:, 1],
    s=4,
)

plt.title("Lorenz Poincaré Section (z = 27)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
