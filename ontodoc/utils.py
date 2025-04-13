
from itertools import chain

from rdflib import DC, DCTERMS, RDFS, SDO, SKOS, Graph


def get_object(g: Graph, subject, predicate):
    oo = [o for o in g.objects(subject=subject, predicate=predicate)]
    if not len(oo):
        return None
    return oo[0]

def get_object(g: Graph, subject, predicate_list):
    if type(predicate_list) == dict and 'predicates' in predicate_list:
        predicate_list = predicate_list['predicates']
    if type(predicate_list) == str:
        predicate_list = [predicate_list]
    for o in chain(
        [o for p in predicate_list for o in g.objects(subject, p)]
    ):
        return o
    return None
