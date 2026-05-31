import matplotlib.pyplot as plt

from poincare_mapper.attractors import roessler
from poincare_mapper.mapper import PoincareMapper
from poincare_mapper.sections import plane_section
from poincare_mapper.plotting import save_figure

section = plane_section(
    normal=[0, 1, 0],
    offset=0,
    direction=1,
)

mapper = PoincareMapper(roessler, section)

result = mapper.run(
    initial_state=[1.0, 1.0, 1.0],
    t_span=(0, 2000),
    burn_in=20,
)

crossings = result["crossings"]

print("crossings:", crossings.shape)

if len(crossings) == 0:
    raise RuntimeError("No crossings found.")

x = crossings[:, 0]
z = crossings[:, 2]

plt.figure(figsize=(8, 8))
plt.scatter(x, z, s=2)
plt.title("Rössler Poincaré Section: y = 0, dy/dt > 0")
plt.xlabel("x")
plt.ylabel("z")

save_figure("rossler_section.png")
