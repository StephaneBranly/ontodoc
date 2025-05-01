<p align="center">
<img src='https://raw.githubusercontent.com/StephaneBranly/ontodoc/bb6b704b03c3e470189ebedd3ec0c102dbe4177f/src/logo.png' height='200' alt='ontodoc logo' />
</p>

# ontodoc

![PyPIVersion](https://img.shields.io/pypi/v/ontodoc) ![PyPI - Downloads](https://img.shields.io/pypi/dm/ontodoc) ![GitHub License](https://img.shields.io/github/license/StephaneBranly/ontodoc)

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

| Argument name                         | Default        | Description                                           | Implemented |
| ------------------------------------- | -------------- | ----------------------------------------------------- | ----------- |
| `-i, --input INPUT`                   | `ontology.ttl` | _Input ontology file_                                 | ✅          |
| `-o, --output OUTPUT`                 | `build/`       | _Output directory for the generated documentation_    | ✅          |
| `-t, --templates TEMPLATES`           | `templates/`   | _Custom templates folder_                             | ✅          |
| `-f, --footer, --no-footer`           | `true`         | _Add footer for each page_                            | ✅          |
| `-c, --concatenate, --no-concatenate` | `false`        | _Concatenate documentation into an unique file_       | ❌          |
| `-s, --schema, --no-schema`           | `true`         | _Display schemas_                                     | ❌          |
| `-m, --model MODEL`                   | `markdown`     | _Model type for the documentation. markdown, gh_wiki_ | ❌          |

### Automatically generate your documentation

You can explore `github actions` to automatically generate and publish your documentation. If you need some inspiration to do it, check [our ontodoc github action](https://github.com/StephaneBranly/ontodoc/blob/main/.github/workflows/build_doc.yaml).

## Example 👀

Look at the [example for _foaf_](https://github.com/StephaneBranly/ontodoc/blob/main/example/build/homepage.md) to see what type of documentation you can easily build in 2 lines!

## How does it work ? 🔧

```mermaid
%% THIS IS A SCHEMA, IF YOU CANNOT SEE IT, PLEASE TRY TO CONSULT THIS PAGE ON GITHUB AND ON A DESKTOP WEB NAVIGATOR
flowchart LR
 subgraph s1["Ontodoc"]
        mdhrd["Markdown human readable documentation"]
        mt["Markdown templates"]
        sod["Structured ontology description"]
        cli["Command Line Interface"]
  end
    sod --> mdhrd
    mt --> mdhrd
    on(("Ontology")) --> cli
    cli --> sod
    cli -.-> mt

    sod@{ shape: braces}
    cli@{ shape: text}
```

## Contributing </>

Feel free to contribute to this open source project!

We need help to implement new features, fix bugs listed in [issues](https://github.com/StephaneBranly/ontodoc/issues).

If you have any idea, create your own issue.

## License 🔓

[Apache License 2.0](https://github.com/StephaneBranly/ontodoc/blob/main/LICENCE.txt)

## They already have integrated Ontodoc ♥️

_Comming soon..._
