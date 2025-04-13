import argparse
from jinja2 import Environment, FileSystemLoader, Template
import rdflib.namespace
from ontodoc import __version__
import pathlib
from rdflib import Graph
import rdflib
import json

from ontodoc.classes.Class import Class
from ontodoc.classes.Footer import Footer
from ontodoc.classes.Ontology import Ontology
from ontodoc.generate_page import generate_page

def concat_templates_environment(default_env: Environment, custom_env: Environment = None):
    if custom_env == None:
        return {
            t: default_env.get_template(t) for t in default_env.list_templates()
        }
    custom_env_templates = custom_env.list_templates()
    return {
       t: default_env.get_template(t) if t not in custom_env_templates else custom_env.get_template(t) for t in default_env.list_templates()
    }

parser = argparse.ArgumentParser(prog='OntoDoc', epilog='Python module to easily generate ontology documentation in markdown or html')

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
    "-m", "--model", help='Model type for the documentation. markdown, gh_wiki'
)

# add languages settings
# add footer and navigation settings

def main():
    args = parser.parse_args()

    # Load markdown templates
    default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.resolve().__str__()+'/templates'))
    custom_env = Environment(loader=FileSystemLoader(args.templates)) if args.templates else None
    templates = concat_templates_environment(default_env, custom_env)

    g = Graph(bind_namespaces='none')
    g.parse(args.input)

    ontos = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
    if not len(ontos):
        raise Exception('Ontology not found')
    onto = ontos[0]

    if args.footer:
        footer = Footer(onto, templates['footer.md']).__str__()
        if args.model == 'gh_wiki':
            generate_page(footer, f'{args.output}/_Footer.md', onto)
            footer = None
    else:
        footer = None

    ontology = Ontology(g, onto, templates)

    import json

    class OntoDocEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Graph):
                return None
            if isinstance(obj, Template):
                return None
            if isinstance(obj, Class):
                return obj.__dict__
            if isinstance(obj, Ontology):
                return None
            return super(OntoDocEncoder, self).default(obj)

    if args.model == 'json':
        generate_page(json.dumps(ontology.__dict__, indent=2, cls=OntoDocEncoder), f'{args.output}/ontology.json', add_signature=False)
        for c in ontology.classes:
            generate_page(json.dumps(c.__dict__, indent=2, cls=OntoDocEncoder), f'{args.output}/class/{c.id}.json', add_signature=False)
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
                
if __name__ == '__main__':
    main()
