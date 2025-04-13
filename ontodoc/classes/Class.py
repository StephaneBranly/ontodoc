import typing
from jinja2 import Template
from rdflib import Graph, Node
import rdflib
import re
from ontodoc.ontology_properties import COMMENT, LABEL
from ontodoc.utils import get_object
    
class Class:
    def __init__(self, g: Graph, onto, class_node: Node, template: Template):
        self.template = template
        self.onto = onto
        self.id = re.sub(r'[^a-zA-Z\-_0-0]+', '_', class_node.n3(namespace_manager=g.namespace_manager).split(':')[-1])
        
        self.label = get_object(g, class_node, LABEL)
        if not self.label:
            self.label = self.id
        self.comment = get_object(g, class_node, COMMENT)

        results = g.query(f"""
        SELECT ?predicate ?range ?comment ?label
        WHERE {{
            ?predicate rdf:type ?type ;
            rdfs:domain {class_node.n3()} ;
            rdfs:range ?range .
            OPTIONAL {{ ?predicate rdfs:comment ?comment }} .
            OPTIONAL {{ ?predicate rdfs:label ?label }} .
            VALUES ?type {{ owl:DatatypeProperty owl:ObjectProperty }}
        }}""")

        self.triples = [{
            'id': index,
            'predicate': row.predicate.n3(g.namespace_manager),
            'range': row.range.n3(g.namespace_manager),
            'label': row.label.n3(g.namespace_manager) if row.label else None,
            'comment': row.comment.n3(g.namespace_manager).replace('\n',' ') if row.comment else None,
            'link': row.range.n3(g.namespace_manager).split(':')[1] if row.range.n3(g.namespace_manager).startswith(':') else None
        } for index, row in enumerate(results)]

    def __str__(self):
        return self.template.render(classe=self.__dict__, onto=self.onto.__dict__)
