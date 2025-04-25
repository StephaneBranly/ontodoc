from jinja2 import Template
from rdflib import RDFS, Graph, Node

from ontodoc.ontology_properties import COMMENT, LABEL
from ontodoc.utils import compute_link, generate_clean_id_from_term, get_object, serialize_subset
    
class Property:
    def __init__(self, g: Graph, onto, property_node: Node, template: Template):
        self.template = template
        self.onto = onto
        self.property_node = property_node
        self.id = generate_clean_id_from_term(g, property_node)

        self.serialized = serialize_subset(g, property_node)
        
        self.label = get_object(g, property_node, LABEL)
        if not self.label:
            self.label = self.id
        self.comment = get_object(g, property_node, COMMENT)

        self.range = get_object(g, property_node, RDFS['range'])
        self.domain = get_object(g, property_node, RDFS['domain'])

        self.range_link = compute_link(g, self.range, onto.onto_prefix) if self.range else None
        self.domain_link = compute_link(g, self.domain, onto.onto_prefix) if self.domain else None

    def __str__(self):
        return self.template.render(property=self.__dict__, onto=self.onto.__dict__)
