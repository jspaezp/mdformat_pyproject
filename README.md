# mdformat-pyproject

Adds an interface to mdformat that reads from pyproject.toml

## Implementation

At runtime over-writes the `mdformat._conf.read_toml_opts` that reads your `pyrpoject.toml` instead of their
`.mdformat.toml`.

And then runs the standard cli from the project

## Installation

Right now the package is not published so you will have to clone the repository and either use pip or poetry to install
it.

## Usage

**From the cli**

```shell
mdformat_pyproject
# or
mdformatp
```

**Pre-commit hook**

On the making ....
