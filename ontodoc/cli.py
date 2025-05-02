import argparse
from itertools import chain
from jinja2 import Environment, FileSystemLoader, Template
import pathlib
from rdflib import Graph
import rdflib
import json

from ontodoc import __version__
from ontodoc.classes.JSONOntoDocEncoder import JSONOntoDocEncoder
from ontodoc.classes.Footer import Footer
from ontodoc.classes.Ontology import Ontology
from ontodoc.generate_page import generate_page
from ontodoc.utils import concat_templates_environment


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

    # Load markdown templates
    default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.resolve().__str__()+'/templates'))
    custom_env = Environment(loader=FileSystemLoader(args.templates)) if args.templates else None
    templates = concat_templates_environment(default_env, custom_env)

    # Load graph
    g = Graph(bind_namespaces='none')
    g.parse(args.input)

    # Retrieve ontology node
    ontos = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
    if not len(ontos):
        raise Exception('Ontology not found')
    onto = ontos[0]

    # Generate footer
    if args.footer:
        footer = Footer(onto, templates['footer.md']).__str__()
        if args.model == 'gh_wiki':
            generate_page(footer, f'{args.output}/_Footer.md', onto)
            footer = None
    else:
        footer = None

    # Init ontology reader
    ontology = Ontology(g, onto, templates)

    # Generate pages
    if args.model == 'json':
        generate_page(json.dumps(ontology.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{args.output}/ontology.json', add_signature=False)
        for c in ontology.classes:
            generate_page(json.dumps(c.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{args.output}/class/{c.id}.json', add_signature=False)
        for p in chain(ontology.objectProperties, ontology.annotationProperties, ontology.datatypeProperties, ontology.functionalProperties):
            generate_page(json.dumps(p.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{args.output}property/{p.id}.json', add_signature=False)

    elif args.model in ['markdown', 'gh_wiki']:
        if args.concatenate:
            page = ontology.__str__()
            for c in ontology.classes:
                page += '\n\n' + c.__str__()
            generate_page(page, f'{args.output}/ontology.md', onto, footer)

        else:
            generate_page(ontology.__str__(), f'{args.output}/homepage.md', onto, footer)
            for c in ontology.classes:
                generate_page(c.__str__(), f'{args.output}class/{c.id}.md', onto, footer)
            for p in chain(ontology.objectProperties, ontology.annotationProperties, ontology.datatypeProperties, ontology.functionalProperties):
                generate_page(p.__str__(), f'{args.output}property/{p.id}.md', onto, footer)

    # Copy ontology file
    with open(f'{args.output}ontology.ttl', mode='w', encoding='utf-8') as f:
        f.write(g.serialize(format='ttl'))

if __name__ == '__main__':
    main()
