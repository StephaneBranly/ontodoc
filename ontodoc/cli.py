import argparse

from ontodoc import __version__
from ontodoc.classes.Documentation import Documentation

parser = argparse.ArgumentParser(prog='OntoDoc', epilog='Python module to easily generate ontology documentation in markdown')

parser.add_argument(
    "-v", "--version", action="version", version="{version}".format(version=__version__)
)
parser.add_argument(
    "-i", "--input", help='Input ontology file', default='./ontology.ttl'
)
parser.add_argument(
    "-o", "--output", help='Output directory for the generated documentation', default='build/'
)
parser.add_argument(
    "-t", "--templates", help="Custom templates folder", default='templates/'
)
parser.add_argument(
    "-f", "--footer", help="Add footer for each page", action=argparse.BooleanOptionalAction, default=True
)
parser.add_argument(
    "-c", "--concatenate", help="Concatenate documentation into an unique file", action=argparse.BooleanOptionalAction, default=False
)
parser.add_argument(
    "-s", "--schema", help="Display schemas", action=argparse.BooleanOptionalAction, default=True
)
parser.add_argument(
    "-m", "--model", help='Model type for the documentation. markdown, gh_wiki or json', default='markdown'
)

def main():
    args = parser.parse_args()
    documentation = Documentation(
        input_graph=args.input,
        output_folder=args.output,
        templates=args.templates,
        footer=args.footer,
        model=args.model,
        concatenate=args.concatenate,
        with_schema=args.schema
    )
    documentation.generate()

if __name__ == '__main__':
    main()
