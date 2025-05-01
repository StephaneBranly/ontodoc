import json
from jinja2 import Template
from rdflib import Graph

from ontodoc.classes.Class import Class
from ontodoc.classes.Ontology import Ontology
from ontodoc.classes.Property import Property


class JSONOntoDocEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Graph):
            return None
        if isinstance(obj, Template):
            return None
        if isinstance(obj, Class):
            return obj.__dict__
        if isinstance(obj, Property):
            return obj.__dict__
        if isinstance(obj, Ontology):
            return None
        return super(JSONOntoDocEncoder, self).default(obj)