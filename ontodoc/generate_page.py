from pathlib import Path

from ontodoc import __version__
from ontodoc.classes.Ontology import Ontology

def generate_page(content: str, path: Path, onto: Ontology = None, footer: str = None, add_signature: bool = True):
    if type(path) != Path: path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)

        if footer:
            f.write(footer)

        if add_signature:
            f.write(f'\n\nGenerated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v{__version__}*')