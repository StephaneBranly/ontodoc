from __future__ import annotations
from jinja2 import Template
from rdflib import RDFS, Literal, Node

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
from ontodoc.ontology_properties import COMMENT, LABEL
from ontodoc.utils import compute_link, generate_clean_id_from_term, get_object, serialize_subset
    
class Property:
    def __init__(self, onto: Ontology, property_node: Node, template: Template):
        self.template = template
        self.onto = onto
        g = onto.graph
        self.property_node = property_node
        self.id = generate_clean_id_from_term(g, property_node)

        self.serialized = serialize_subset(g, property_node)
        
        self.label = get_object(g, property_node, LABEL)
        if not self.label:
            self.label = Literal(self.id)
        self.comment = get_object(g, property_node, COMMENT)

        self.range = get_object(g, property_node, RDFS['range'])
        self.domain = get_object(g, property_node, RDFS['domain'])

        self.range_link = compute_link(g, self.property_node, self.range, onto.onto_prefix) if self.range else None
        self.domain_link = compute_link(g, self.property_node, self.domain, onto.onto_prefix) if self.domain else None

        self.range_label = generate_clean_id_from_term(g, self.range) if self.range else None
        self.domain_label = generate_clean_id_from_term(g, self.domain) if self.domain else None

    def __str__(self):
        return self.template.render(property=self.__dict__, onto=self.onto.__dict__)
