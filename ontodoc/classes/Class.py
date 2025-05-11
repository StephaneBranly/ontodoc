from __future__ import annotations
from itertools import chain
from pathlib import Path
from jinja2 import Template
from rdflib import RDFS, Node

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
from ontodoc.classes.Generic import Generic
from ontodoc.ontology_properties import CLASS


from ontodoc.utils import get_subject
    
class Class(Generic):
    def __init__(self, onto: Ontology, class_node: Node, template: Template):
        super().__init__(onto, class_node, template, CLASS, Path('class'))

        g = onto.graph

        self.subclasses = get_subject(g, RDFS.subClassOf, class_node, return_all=True)

        results = [p for p in chain(onto.datatypeProperties, onto.annotationProperties, onto.functionalProperties, onto.objectProperties) if p.domain == class_node]
        self.triples = results

    def update_internal_links(self):
        if self.subclasses:
            self.subclasses = [c for c in self.onto.classes if c.node in self.subclasses]
        if self.subclassof:
            self.subclassof = [c for c in self.onto.classes if c.node in self.subclassof]
