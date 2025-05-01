
from itertools import chain
import re

from jinja2 import Environment
from rdflib import OWL, RDF, RDFS, Graph, Node

from ontodoc.ontology_properties import ONTOLOGY_PROP

def concat_templates_environment(default_env: Environment, custom_env: Environment = None):
    if custom_env == None:
        return {
            t: default_env.get_template(t) for t in default_env.list_templates()
        }
    custom_env_templates = custom_env.list_templates()
    return {
       t: default_env.get_template(t) if t not in custom_env_templates else custom_env.get_template(t) for t in default_env.list_templates()
    }


def get_object(g: Graph, subject: Node, predicate_list: ONTOLOGY_PROP, return_all=False):
    while type(predicate_list) == type and ONTOLOGY_PROP == predicate_list.__base__:
        return_all = predicate_list.array
        predicate_list = predicate_list.predicates

    if type(predicate_list) == list:
        pass
    else:
        predicate_list = [predicate_list]

    
    objects = list(set(chain(
        [o for p in predicate_list for o in g.objects(subject, p)]
    )))

    if len(objects):
        return objects if return_all else objects[0]

    return None

def get_subject(g: Graph, object: Node, predicate_list: ONTOLOGY_PROP, return_all=False):
    while type(predicate_list) == type and ONTOLOGY_PROP == predicate_list.__base__:
        return_all = predicate_list.array
        predicate_list = predicate_list.predicates

    if type(predicate_list) == list:
        pass
    else:
        predicate_list = [predicate_list]

    
    subjects = list(set(chain(
        [o for p in predicate_list for o in g.subjects(object, p)]
    )))

    if len(subjects):
        return subjects if return_all else subjects[0]

    return None

def get_prefix(graph: Graph, n: Node):
    return n.n3(graph.namespace_manager).split(':')[0]

def get_suffix(graph: Graph, n: Node):
    return n.n3(graph.namespace_manager).split(':')[-1]

def generate_clean_id_from_term(graph: Graph, n: Node):
    return re.sub(r'[^a-zA-Z\-_0-0]+', '_', n.n3(namespace_manager=graph.namespace_manager).split(':')[-1])

def compute_link(graph: Graph, current_node: Node, n: Node, onto_prefix: str = ''):
    if n and n.n3(graph.namespace_manager).startswith(onto_prefix+':'):
        relative_path = './' if get_object(graph, current_node, RDF.type) == OWL.Ontology else '../'
        type = get_object(graph, n, RDF.type)
        page_name = n.n3(graph.namespace_manager).split(onto_prefix+':')[1]+'.md'
        if type and type in [RDFS.Class, OWL.Class]:
            return relative_path + 'class/' + page_name
        return relative_path + 'property/' + page_name
    return n.n3()

def serialize_subset(graph: Graph, n: Node):
    gs = Graph()
    [gs.add(t) for t in graph.triples((n, None, None))]
    return gs.serialize(format='ttl')