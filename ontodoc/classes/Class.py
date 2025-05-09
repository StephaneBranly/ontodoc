from __future__ import annotations
from itertools import chain
from jinja2 import Template
from rdflib import RDFS, Node

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
from ontodoc.classes.Generic import Generic
from ontodoc.ontology_properties import CLASS


from ontodoc.utils import compute_link, generate_clean_id_from_term, get_subject
    
class Class(Generic):
    def __init__(self, onto: Ontology, class_node: Node, template: Template):
        super().__init__(onto, class_node, template, CLASS)

        g = onto.graph

        self.subclasses = get_subject(g, RDFS.subClassOf, class_node, return_all=True)
        if self.subclasses:
            self.subclasses = [generate_clean_id_from_term(g, t) for t in self.subclasses]
        if self.subclassof:
            self.subclassof = [generate_clean_id_from_term(g, t) for t in self.subclassof]

        results = [p for p in chain(onto.datatypeProperties, onto.annotationProperties, onto.functionalProperties, onto.objectProperties) if p.domain == class_node]
        self.triples = [{
            'id': index,
            'predicate': row.node.n3(g.namespace_manager) if row.node else None,
            'predicate_link': compute_link(onto, class_node, row.node) if row.node else None,
            'range': row.range.n3(g.namespace_manager) if row.range else None,
            'range_link': compute_link(onto, class_node, row.range) if row.range else None,
            'label': row.label.n3(g.namespace_manager) if row.label else None,
            'comment': row.comment.n3(g.namespace_manager).replace('\n','<br>') if row.comment else None,
        } for index, row in enumerate(results)]


    def __str__(self):
        return self.template.render(classe=self.__dict__, onto=self.onto.__dict__)
