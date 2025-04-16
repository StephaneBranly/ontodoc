import typing
from jinja2 import Template
from rdflib import Graph


class Homepage:
    def __init__(self, graph: Graph, onto, template: Template):
        self.graph = graph
        self.onto = onto
        self.template = template
            
    def __str__(self):
        return self.template.render(
            onto=self.onto.__dict__
        )