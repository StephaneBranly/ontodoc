<p align="center">
<img src='./src/logo.png' height='200' alt='ontodoc logo' />
</p>

# ontodoc

A python module to generate markdown documentation for ontologies.

Based on `rdflib` and `jinja2`.

## Getting Started 🚀

### Installation

```shell
pip install ontodoc
```

### Command line usage

```shell
python -m ontodoc
```

By default, the file named `ontology.ttl` will be used to generate your documentation in the `build` destination folder.

You can easily change settings as you need.
Available arguments :

| Argument name                         | Default        | Description                                          |
| ------------------------------------- | -------------- | ---------------------------------------------------- |
| `-i, --input INPUT`                   | `ontology.ttl` | _Input ontology file_                                |
| `-o, --output OUTPUT`                 | `build/`       | _Output directory for the generated documentation_   |
| `-t, --templates TEMPLATES`           | `templates/`   | _Custom templates folder_                            |
| `-f, --footer, --no-footer`           | `true`         | _Add footer for each page_                           |
| `-c, --concatenate, --no-concatenate` | `false`        | _Concatenate documentation into an unique file_      |
| `-s, --schema, --no-schema`           | `true`         | _Display schemas_                                    |
| `-m, --model MODEL`                   | `markdown`     | _Model type for the documentation. markdown or html_ |

### Automatically generate your documentation

You can explore `github actions` to automatically generate and publish your documentation.

## Contributing </>

Feel free to contribute to this open source project!

## License 🔓
