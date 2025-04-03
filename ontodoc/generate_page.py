from pathlib import Path

from ontodoc.classes.Ontology import Ontology

def generate_page(content: str, path: Path, onto: Ontology, footer: str = None):
    if type(path) != Path: path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode='w') as f:
        f.write(content)

        if footer:
            f.write(footer)

        f.write('\n\nGenerated with [ontodoc](https://github.com/StephaneBranly/ontodoc)')