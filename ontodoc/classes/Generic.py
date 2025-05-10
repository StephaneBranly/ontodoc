from __future__ import annotations
from pathlib import Path
from jinja2 import Template
from rdflib import Literal, Node

from typing import TYPE_CHECKING

from ontodoc.ontology_properties import ONTOLOGY_PROP
from ontodoc.utils import generate_clean_id_from_term, get_object, get_suffix, serialize_subset
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology


class Generic:
    def __init__(self, onto: Ontology, node: Node, template: Template, default_properties: ONTOLOGY_PROP=[], path: Path = Path('./')):
        g = onto.graph

        self.template = template
        self.onto = onto
        self.id = generate_clean_id_from_term(g, node)
        self.node = node
        self.n3 = node.n3(g.namespace_manager)
        self.pagename = path / self.id
        self.serialized = serialize_subset(g, node)
        
        for p in default_properties.predicates:
            setattr(self, p.__name__.lower() if type(p) == type else get_suffix(g, p), get_object(g, node, p))

        if not self.label:
            self.label = Literal(self.id)

    def update_internal_links(self):
        pass

    def __str__(self):
        return self.template.render(**{self.__class__.__name__.lower(): self.__dict__, 'onto': self.onto.__dict__, 'metadata': self.onto.metadata})