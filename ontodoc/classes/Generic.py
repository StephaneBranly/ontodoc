from __future__ import annotations
from jinja2 import Template
from rdflib import Literal, Node

from typing import TYPE_CHECKING

from ontodoc.ontology_properties import ONTOLOGY_PROP
from ontodoc.utils import generate_clean_id_from_term, get_object, get_suffix, serialize_subset
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology


class Generic:
    def __init__(self, onto: Ontology, node: Node, template: Template, default_properties: ONTOLOGY_PROP=[]):
        g = onto.graph

        self.template = template
        self.onto = onto
        self.id = generate_clean_id_from_term(g, node)
        self.node = node

        self.serialized = serialize_subset(g, node)
        
        for p in default_properties.predicates:
            setattr(self, p.__name__.lower() if type(p) == type else get_suffix(g, p), get_object(g, node, p))

        if not self.label:
            self.label = Literal(self.id)