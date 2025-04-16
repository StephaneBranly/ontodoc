
from itertools import chain

from rdflib import Graph

from ontodoc.ontology_properties import ONTOLOGY_PROP

def get_object(g: Graph, subject, predicate_list: ONTOLOGY_PROP, return_all=False):
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

def get_prefix(graph: Graph, n):
    return n.n3(graph.namespace_manager).split(':')[0]

def get_suffix(graph: Graph, n):
    return n.n3(graph.namespace_manager).split(':')[-1]