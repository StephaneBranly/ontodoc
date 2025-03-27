from jinja2 import Template
from rdflib import Graph
import rdflib

from ontomdoc.utils import get_object

def render_class(g: Graph, onto, class_object, template: Template):
    class_id = class_object.n3(namespace_manager=g.namespace_manager).split(':')[-1]
    class_label = get_object(g, subject=class_object, predicate=rdflib.RDFS['label'])
    class_comment  = get_object(g, subject=class_object, predicate=rdflib.RDFS['comment'])
    
    results = g.query(f"""
        SELECT ?predicate ?range ?comment ?label
        WHERE {{
            ?predicate rdf:type ?type ;
            rdfs:domain {class_object.n3()} ;
            rdfs:range ?range .
            OPTIONAL {{ ?predicate rdfs:comment ?comment }} .
            OPTIONAL {{ ?predicate rdfs:label ?label }} .
            VALUES ?type {{ owl:DatatypeProperty owl:ObjectProperty }}
        }}""")

    class_md = template.render(
        onto=onto,
        classe={'id':class_id, 'label': class_label, 'comment': class_comment},
        triples=[{
            'id': index,
            'predicate': row.predicate.n3(g.namespace_manager),
            'range': row.range.n3(g.namespace_manager),
            'label': row.label.n3(g.namespace_manager) if row.label else None,
            'comment': row.comment.n3(g.namespace_manager).replace('\n',' ') if row.comment else None,
            'link': row.range.n3(g.namespace_manager).split(':')[1] if row.range.n3(g.namespace_manager).startswith(':') else None
        } for index, row in enumerate(results)]
    )
    
    return class_id, class_md
    