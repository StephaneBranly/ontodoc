import argparse
from jinja2 import Environment, FileSystemLoader, Template
from ontomdoc import __version__
import pathlib
import os
from rdflib import Graph
import rdflib

def concat_templates_environment(default_env: Environment, custom_env: Environment):
    custom_env_templates = custom_env.list_templates()
    return {
       t: default_env.get_template(t) if t not in custom_env_templates else custom_env.get_template(t) for t in default_env.list_templates()
    }

def get_object(g, subject, predicate):
    oo = [o for o in g.objects(subject=subject, predicate=predicate)]
    if not len(oo):
        return None
    return oo[0]

def render_class(g: Graph, onto, class_object, template: Template):
    class_label = class_object.n3(namespace_manager=g.namespace_manager).split(':')[-1]
    class_md = template.render(
        onto=onto,
        classe={'label':class_label}
    )
    try:
        with open(f'./build/class/{class_label}.md', mode='w') as f:
            f.write(class_md)
    except:
        print('Error for class ', class_label)

parser = argparse.ArgumentParser()

parser.add_argument(
    "-v", "--version", action="version", version="{version}".format(version=__version__)
)

# add input file
# add output destination folder
# add languages settings
# add custom template folder
# add footer and navigation settings
# add mermaid settings

def main():
    args = parser.parse_args()

    # Load markdown templates
    default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.resolve().__str__()+'/templates'))
    custom_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.parent.resolve().__str__()+'/custom_templates'))
    templates = concat_templates_environment(default_env, custom_env)
    template_homepage = templates['homepage.md']



    g = Graph()
    g.parse('./example/ontology.ttl')

    ontos = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
    if not len(ontos):
        raise Exception('Ontology not found')
    onto = ontos[0]

    classes = [s for s in g.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Class'])]

  

    onto_dict = {
            'label': get_object(g, onto, rdflib.RDFS['label']),
            'comment': get_object(g, onto, rdflib.RDFS['comment']),
        }
    
    for c in classes:
        render_class(g,onto_dict, c, templates['class.md'])
    md = template_homepage.render(
        onto=onto_dict, 
        contributors=[o.n3() for o in g.objects(subject=onto, predicate=rdflib.DCTERMS['contributor'])],
        classes=[{'name': c.n3(namespace_manager=g.namespace_manager), 'link':  c.n3(namespace_manager=g.namespace_manager).split(':')[-1]} for c in classes]
    ) + '\n\nGenerated with [ontomdoc](https://github.com/StephaneBranly/ontomdoc)'

    with open('./build/homepage.md', mode='w') as f:
        f.write(md)


if __name__ == '__main__':
    main()
