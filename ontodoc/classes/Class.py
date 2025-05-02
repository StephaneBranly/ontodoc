from __future__ import annotations
from itertools import chain
from jinja2 import Template
from rdflib import RDFS, Literal, Node

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
from ontodoc.ontology_properties import CLASS


from ontodoc.utils import compute_link, generate_clean_id_from_term, get_object, get_subject, get_suffix, serialize_subset
    
class Class:
    def __init__(self, onto: Ontology, class_node: Node, template: Template):
        self.template = template
        self.onto = onto
        g = onto.graph
        self.class_node = class_node
        self.id = generate_clean_id_from_term(g, class_node)

        for p in CLASS.predicates:
            setattr(self, p.__name__.lower() if type(p) == type else get_suffix(g, p), get_object(g, class_node, p))
        
        if not self.label:
            self.label = Literal(self.id)

        self.subclasses = get_subject(g, RDFS.subClassOf, class_node, return_all=True)
        if self.subclasses:
            self.subclasses = [generate_clean_id_from_term(g, t) for t in self.subclasses]
        if self.subclassof:
            self.subclassof = [generate_clean_id_from_term(g, t) for t in self.subclassof]

        self.serialized = serialize_subset(g, class_node)

        results = [p for p in chain(onto.datatypeProperties, onto.annotationProperties, onto.functionalProperties, onto.objectProperties) if p.domain == class_node]
        self.triples = [{
            'id': index,
            'predicate': row.property_node.n3(g.namespace_manager) if row.property_node else None,
            'predicate_link': compute_link(g, self.class_node, row.property_node, onto.onto_prefix) if row.property_node else None,
            'range': row.range.n3(g.namespace_manager) if row.range else None,
            'range_link': compute_link(g, self.class_node, row.range, onto.onto_prefix) if row.range else None,
            'label': row.label.n3(g.namespace_manager) if row.label else None,
            'comment': row.comment.n3(g.namespace_manager).replace('\n','<br>') if row.comment else None,
        } for index, row in enumerate(results)]

    def __str__(self):
        return self.template.render(classe=self.__dict__, onto=self.onto.__dict__)
