import argparse
from jinja2 import Environment, FileSystemLoader, Template
from ontomdoc import __version__
import pathlib
from rdflib import Graph
import rdflib

from ontomdoc.node_class import render_class
from ontomdoc.utils import get_object

def concat_templates_environment(default_env: Environment, custom_env: Environment = None):
    if custom_env == None:
        return {
            t: default_env.get_template(t) for t in default_env.list_templates()
        }
    custom_env_templates = custom_env.list_templates()
    return {
       t: default_env.get_template(t) if t not in custom_env_templates else custom_env.get_template(t) for t in default_env.list_templates()
    }

parser = argparse.ArgumentParser(prog='OntoMDoc', epilog='Python module to easily generate markdown ontology documentation')

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
    "-m", "--mermaid", help="Display mermaid schemas", action=argparse.BooleanOptionalAction, default=True
)
# add languages settings
# add footer and navigation settings

def main():
    args = parser.parse_args()

    # Load markdown templates
    default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.resolve().__str__()+'/templates'))
    custom_env = Environment(loader=FileSystemLoader(args.templates)) if args.templates else None
    templates = concat_templates_environment(default_env, custom_env)
    template_homepage = templates['homepage.md']

    print('concate', args.concatenate)
    print('footer', args.footer)

    g = Graph()
    g.parse(args.input)

    ontos = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
    if not len(ontos):
        raise Exception('Ontology not found')
    onto = ontos[0]

    classes = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Class']) if type(s) == rdflib.URIRef and s.n3(g.namespace_manager).startswith(':')]
    
    onto_dict = {
            'label': get_object(g, onto, rdflib.RDFS['label']),
            'comment': get_object(g, onto, rdflib.RDFS['comment']),
        }
    
    for c in classes:
        class_id, class_md = render_class(g,onto_dict, c, templates['class.md'])
        try:
            with open(f'{args.output}/class/{class_id}.md', mode='w') as f:
                f.write(class_md)
        except:
            print('Error for class ', class_id)

    md = template_homepage.render(
        onto=onto_dict, 
        contributors=[o.n3() for o in g.objects(subject=onto, predicate=rdflib.DCTERMS['contributor'])],
        classes=[{'name': c.n3(namespace_manager=g.namespace_manager), 'link':  c.n3(namespace_manager=g.namespace_manager).split(':')[-1]} for c in classes]
    )

    with open(f'{args.output}/homepage.md', mode='w') as f:
        f.write(md)


if __name__ == '__main__':
    main()
