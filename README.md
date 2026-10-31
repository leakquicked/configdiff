![Python checks](https://github.com/leakquicked/configdiff/actions/workflows/python-checks.yml/badge.svg)

# ConfigDiff

Compare two text configuration files and show changed lines.

## Requirements
Python 3.10+, standard library only.

## Usage
`python configdiff.py --help`

Supply a local text export or copied response headers. This tool is passive: it does not contact websites or alter configuration. Findings are advisory and require review in context.

## Tests
`python -m unittest discover -s tests -v`
