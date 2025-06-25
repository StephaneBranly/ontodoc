import datetime
from itertools import chain
import json
import pathlib
from jinja2 import Environment, FileSystemLoader
from rdflib import Graph, Node
import rdflib

from ontodoc import __version__
from ontodoc.classes.Footer import Footer
from ontodoc.classes.JSONOntoDocEncoder import JSONOntoDocEncoder
from ontodoc.classes.Ontology import Ontology
from ontodoc.generate_page import generate_page
from ontodoc.utils import concat_templates_environment


class Documentation:
    def __init__(self, input_graph: Graph, output_folder: str = 'build', onto_node: Node=None, templates: str=None, footer:bool=True, model='markdown', concatenate:bool=False, with_schema:bool=True):
        default_env = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent.parent.resolve().__str__()+'/templates'))
        custom_env = Environment(loader=FileSystemLoader(templates)) if templates else None
        
        self.templates = concat_templates_environment(default_env, custom_env)

        if type(input_graph) == str:
            g = Graph(bind_namespaces='none')
            self.graph = g.parse(input_graph)
        elif type(input_graph) == Graph:
            self.graph = input_graph
        else:
            raise Exception('Graph must be a string or a Graph object')

        if not onto_node:
            ontos = [s for s in self.graph.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Ontology'])]
            if not len(ontos):
                raise Exception('Ontology not found')
            onto_node = ontos[0]
        self.onto = onto_node

        self.footer = footer
        self.model = model
        self.concatenate = concatenate
        self.with_schema = with_schema
        self.output = output_folder
        self.version = __version__

    def generate(self):
        # Generate footer
        if self.footer:
            footer = Footer(self.onto, self.templates['footer.md']).__str__()
            if self.model == 'gh_wiki':
                generate_page(content=footer, path=f'{self.output}/_Footer.md')
                footer = None
        else:
            footer = None

        metadata = {
            **self.__dict__,
            'version': self.version,
            'editionDate': datetime.date.today().strftime('%Y-%m-%d'),
        }
        # Init ontology reader
        ontology = Ontology(self.graph, self.onto, self.templates, metadata)
        path = pathlib.Path(self.output)



        # Generate pages
        if self.model == 'json':
            generate_page(json.dumps(ontology.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{self.output}/ontology.json', add_signature=False)
            for c in ontology.classes:
                generate_page(json.dumps(c.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{self.output}/class/{c.id}.json', add_signature=False)
            for p in chain(ontology.objectProperties, ontology.annotationProperties, ontology.datatypeProperties, ontology.functionalProperties):
                generate_page(json.dumps(p.__dict__, indent=2, cls=JSONOntoDocEncoder), f'{self.output}property/{p.id}.json', add_signature=False)
        elif self.model in ['markdown', 'gh_wiki']:
            if self.concatenate:
                page = ontology.__str__()
                for n in ontology.nodes:
                    page += '\n\n' + n.__str__()
                generate_page(path=path, content=page, node=ontology, footer=footer)

            else:
                generate_page(path=path, node=ontology, footer=footer)
                for n in ontology.nodes:
                    generate_page(path=path, node=n, footer=footer)
        else:
            raise Exception('Model not supported')
        # Copy ontology file
        with open(f'{self.output}/ontology.ttl', mode='w', encoding='utf-8') as f:
            f.write(self.graph.serialize(format='ttl'))

        return self.output