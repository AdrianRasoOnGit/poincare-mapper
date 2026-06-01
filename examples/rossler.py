import matplotlib.pyplot as plt

from poincare_mapper.attractors import roessler
from poincare_mapper.geometry import project_to_plane
from poincare_mapper.mapper import PoincareMapper
from poincare_mapper.plotting import save_figure
from poincare_mapper.sections import plane_section

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

projected = project_to_plane(crossings, section.normal)

plt.figure(figsize=(8, 8))
plt.scatter(
    projected[:, 0],
    projected[:, 1],
    s=2,
    color="darkred",
)

plt.title("Rössler Poincaré Section")
plt.xlabel("section coordinate 1")
plt.ylabel("section coordinate 2")

save_figure("rossler_section.png")
