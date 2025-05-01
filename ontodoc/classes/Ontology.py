from jinja2 import Template
from rdflib import Graph
import rdflib

from ontodoc.classes.Class import Class
from ontodoc.classes.Homepage import Homepage
from ontodoc.classes.Property import Property
from ontodoc.ontology_properties import ONTOLOGY
from ontodoc.utils import get_object, get_prefix, get_suffix


class Ontology:
    def __init__(self, graph: Graph, onto_node: rdflib.Node, templates: dict[str, Template]):
        
        self.graph = graph
        for p in ONTOLOGY.predicates:
            setattr(self, p.__name__.lower() if type(p) == type else get_suffix(self.graph, p), get_object(self.graph, onto_node, p))

        self.templates = templates
        self.onto_node = onto_node
        self.namespaces = [{'prefix': i[0], 'uri': i[1]} for i in graph.namespace_manager.namespaces()]
        self.onto_prefix = [prefix for prefix, uriref in graph.namespace_manager.namespaces() if uriref.n3(graph.namespace_manager) == onto_node.n3(graph.namespace_manager)]
        self.onto_prefix = self.onto_prefix[0] if len(self.onto_prefix) > 0 else None

        self.objectProperties = [Property(self, s, self.templates['property.md']) for s in self.graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.ObjectProperty) if type(s) == rdflib.URIRef and get_prefix(self.graph, s) == self.onto_prefix]
        self.datatypeProperties = [Property(self, s, self.templates['property.md']) for s in self.graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.DatatypeProperty) if type(s) == rdflib.URIRef and get_prefix(self.graph, s) == self.onto_prefix]
        self.annotationProperties = [Property(self, s, self.templates['property.md']) for s in self.graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.AnnotationProperty) if type(s) == rdflib.URIRef and get_prefix(self.graph, s) == self.onto_prefix]
        self.functionalProperties = [Property(self, s, self.templates['property.md']) for s in self.graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.FunctionalProperty) if type(s) == rdflib.URIRef and get_prefix(self.graph, s) == self.onto_prefix]
        self.classes = [Class(self, s, self.templates['class.md']) for s in self.graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.Class) if type(s) == rdflib.URIRef and get_prefix(self.graph, s) == self.onto_prefix]

    def __str__(self):
        homepage = Homepage(self.graph, self, self.templates['homepage.md'])
        return homepage.__str__()
