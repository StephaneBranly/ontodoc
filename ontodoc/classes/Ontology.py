from jinja2 import Template
from rdflib import Graph
import rdflib

from ontodoc.classes.Class import Class
from ontodoc.classes.Homepage import Homepage
from ontodoc.utils import get_object


class Ontology:
    def __init__(self, graph: Graph, onto_node: rdflib.Node, templates: dict[str, Template]):
        self.graph = graph
        self.templates = templates
        self.onto_node = onto_node
        self.namespaces = [{'prefix': i[0], 'uri': i[1]} for i in graph.namespace_manager.namespaces()]
        self.onto_prefix = [prefix for prefix, uriref in graph.namespace_manager.namespaces() if uriref.n3(graph.namespace_manager) == onto_node.n3(graph.namespace_manager)]
        self.onto_prefix = self.onto_prefix[0] if len(self.onto_prefix) > 0 else None
        self.label =  get_object(self.graph, onto_node, rdflib.RDFS['label'])
        self.comment = get_object(self.graph, onto_node, rdflib.RDFS['comment'])
        self.classes = [Class(self.graph, self, s, self.templates['class.md']) for s in self.graph.subjects(predicate=rdflib.RDF["type"], object=rdflib.OWL['Class']) if type(s) == rdflib.URIRef and s.n3(graph.namespace_manager).split(':')[0] == self.onto_prefix]
        self.contributors = [o.n3() for o in self.graph.objects(subject=self.onto_node, predicate=rdflib.DCTERMS['contributor'])]


    def __str__(self):
        homepage = Homepage(self.graph, self, self.templates['homepage.md'])
        return homepage.__str__()
