# ontomdoc

A python module to generate markdown documentation for ontologies.

Based on `rdflib` and `jinja2`.

## Installation

`pip install ontomdoc`

## Usage

### Command line usage

`python -m ontomdoc`

By default, the file named `ontology.ttl` will be used to generate your documentation in the `build` destination folder.
You can easily change settings as you need.

### Automatically generate your documentation

You can explore `github actions` to automatically generate and publish your documentation.
