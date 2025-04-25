from pathlib import Path
from jinja2 import Template
from rdflib import Graph, Node

from ontodoc.ontology_properties import COMMENT, LABEL
from ontodoc.utils import compute_link, generate_clean_id_from_term, get_object, serialize_subset
    
class Class:
    def __init__(self, g: Graph, onto, class_node: Node, template: Template):
        self.template = template
        self.onto = onto
        self.class_node = class_node
        self.id = generate_clean_id_from_term(g, class_node)
        
        self.label = get_object(g, class_node, LABEL)
        if not self.label:
            self.label = self.id
        self.comment = get_object(g, class_node, COMMENT)

        self.serialized = serialize_subset(g, class_node)

        results = [p for p in onto.datatypeProperties if p.domain == class_node.n3(g.namespace_manager)]
        self.triples = [{
            'id': index,
            'predicate': row.property_node.n3(g.namespace_manager),
            'range': row.range.n3(g.namespace_manager) if row.range else None,
            'label': row.label.n3(g.namespace_manager) if row.label else None,
            'comment': row.comment.n3(g.namespace_manager).replace('\n','<br>') if row.comment else None,
            'link': compute_link(g, row.range, onto.onto_prefix, 1) if row.range else None
        } for index, row in enumerate(results)]

    def __str__(self):
        return self.template.render(classe=self.__dict__, onto=self.onto.__dict__)
