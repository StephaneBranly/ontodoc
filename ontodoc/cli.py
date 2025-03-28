import argparse
from jinja2 import Environment, FileSystemLoader
from ontodoc import __version__
import pathlib
from rdflib import Graph
import rdflib

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
    "-i", "--input", help='Input ontology file', default='./example/ontology.ttl'
)
parser.add_argument(
    "-o", "--output", help='Output directory for the generated documentation', default='build/'
)
parser.add_argument(
    "-t", "--templates", help="Custom templates folder"
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
    "-m", "--model", help='Model type for the documentation. markdown or html'
)
# add languages settings
# add footer and navigation settings

def main():
    args = parser.parse_args()

    # Load markdown templates
    default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.resolve().__str__()+'/templates'))
    custom_env = Environment(loader=FileSystemLoader(args.templates)) if args.templates else None
    templates = concat_templates_environment(default_env, custom_env)

    g = Graph()
    g.parse(args.input)

    ontos = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
    if not len(ontos):
        raise Exception('Ontology not found')
    onto = ontos[0]

    # for c in classes:
    #     class_id, class_md = render_class(g, onto_dict, c, templates['class.md'])
    #     try:
    #         with open(f'{args.output}/class/{class_id}.md', mode='w') as f:
    #             f.write(class_md)
    #     except:
    #         print('Error for class ', class_id)
    ontology = Ontology(g, onto, templates)
    # homepage = Homepage(g, onto, templates['homepage.md'])
    # for c in homepage.classes:

    generate_page(ontology.__str__(), f'{args.output}/homepage2.md', True, onto)


if __name__ == '__main__':
    main()
