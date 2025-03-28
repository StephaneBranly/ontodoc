from pathlib import Path

from ontodoc.classes.Ontology import Ontology


def generate_page(content: str, path: Path, include_footer: bool, onto: Ontology):
    with open(path, mode='w') as f:
        f.write(content)

        if include_footer:
            f.write('\nFOOTER')