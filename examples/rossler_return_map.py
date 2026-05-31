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
    t_span=(0, 5000),
    burn_in=20,
)

crossings = result["crossings"]

print("crossings:", crossings.shape)

if len(crossings) < 2:
    raise RuntimeError("Not enough crossings for return map.")

x = crossings[:, 0]

plt.figure(figsize=(8, 8))
plt.scatter(x[:-1], x[1:], s=2)
plt.title("Rössler First Return Map")
plt.xlabel(r"$x_n$")
plt.ylabel(r"$x_{n+1}$")

save_figure("rossler_return_section.png")
