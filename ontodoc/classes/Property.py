from __future__ import annotations
from jinja2 import Template
from rdflib import Node

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
from ontodoc.classes.Generic import Generic
from ontodoc.ontology_properties import PROPERTY
from ontodoc.utils import compute_link, generate_clean_id_from_term
    
class Property(Generic):
    def __init__(self, onto: Ontology, property_node: Node, template: Template):
        super().__init__(onto, property_node, template, PROPERTY)

        g = onto.graph

        self.range_link = compute_link(onto, property_node, self.range) if self.range else None
        self.domain_link = compute_link(onto, property_node, self.domain) if self.domain else None

        self.range_label = generate_clean_id_from_term(g, self.range) if self.range else None
        self.domain_label = generate_clean_id_from_term(g, self.domain) if self.domain else None


    def __str__(self):
        return self.template.render(property=self.__dict__, onto=self.onto.__dict__)
