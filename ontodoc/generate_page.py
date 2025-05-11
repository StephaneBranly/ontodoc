from pathlib import Path

from ontodoc import __version__
from ontodoc.classes.Generic import Generic

def generate_page(content: str = None, path: Path = None, node: Generic = None, footer: str = None, add_signature: bool = True):
    if type(path) != Path: path = Path(path)
    if node != None:
        path = path / node.pagename
        path = path.with_suffix('.md')
    path.parent.mkdir(parents=True, exist_ok=True)
    if content == None:
        content = node.__str__()
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)

        if footer:
            f.write(footer)

        if add_signature:
            f.write(f'\n\nGenerated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v{__version__}*')