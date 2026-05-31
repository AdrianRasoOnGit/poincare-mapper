# Poincaré Mapper

A lightweight Python toolkit for generating Poincaré sections and first-return maps of continuous dynamical systems.

## Features

- Event-based Poincaré section detection using SciPy
- Arbitrary hyperplane sections
- Rössler attractor
- Lorenz attractor
- Thomas attractor
- First-return maps
- Automatic figure generation

## Installation

Using Micromamba:

```bash
micromamba create -f environment.yml
micromamba activate poincare-mapper
pip install -e .
```

## Project Structure

```text
poincare-mapper/
├── environment.yml
├── README.md
├── .gitignore
├── figures/
├── examples/
├── src/
│   └── poincare_mapper/
│       ├── attractors.py
│       ├── mapper.py
│       ├── plotting.py
│       └── sections.py
└── tests/
```

## Running Examples

Rössler Poincaré section:

```bash
python examples/rossler.py
```

Rössler first-return map:

```bash
python examples/rossler_return_map.py
```

Generated figures are written to:

```text
figures/
```

## Example

A first-return map generated from the Rössler attractor:

![Rössler Return Map](docs/rossler_return_map.png)

## Mathematical Background

Given a continuous dynamical system

\[
\dot{x} = f(x)
\]

a Poincaré section is defined by a hypersurface

\[
g(x)=0
\]

The system trajectory is integrated and each crossing of the section is detected using event-based root finding.

The resulting sequence of intersection points defines the Poincaré map.

## Future Work

- Arbitrary plane coordinate projection
- Interactive parameter exploration
- Additional chaotic attractors
- Lyapunov exponent estimation
- Fractal dimension estimation

## License

MIT
