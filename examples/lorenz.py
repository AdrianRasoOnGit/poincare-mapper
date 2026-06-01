import matplotlib.pyplot as plt

from poincare_mapper.attractors import lorenz
from poincare_mapper.mapper import PoincareMapper
from poincare_mapper.plotting import save_figure
from poincare_mapper.sections import plane_section

section = plane_section(
    normal=[0, 0, 1],
    offset=27,
    direction=1,
)

mapper = PoincareMapper(lorenz, section)

result = mapper.run(
    initial_state=[1, 1, 1],
    t_span=(0, 5000),
    burn_in=100,
)

crossings = result["crossings"]

print("crossings:", crossings.shape)

plt.figure(figsize=(8, 8))

plt.scatter(
    crossings[:, 0],
    crossings[:, 1],
    s=3,
    color="darkred",
)

plt.title("Lorenz Poincaré Section")
plt.xlabel("x")
plt.ylabel("y")

save_figure("lorenz_section.png")
