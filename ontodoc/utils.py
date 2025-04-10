
from itertools import chain

from rdflib import DC, DCTERMS, RDFS, SDO, SKOS, Graph


def get_object(g: Graph, subject, predicate):
    oo = [o for o in g.objects(subject=subject, predicate=predicate)]
    if not len(oo):
        return None
    return oo[0]

def get_label(g: Graph, subject):
    for o in chain(
        g.objects(subject, RDFS.label),
        g.objects(subject, DC.title),
        g.objects(subject, SKOS.prefLabel),
        g.objects(subject, SDO.name),
        g.objects(subject, DCTERMS.title),
    ):
        return o
    return None

def get_comment(g: Graph, subject):
    for o in chain(
        g.objects(subject, RDFS.comment),
        g.objects(subject, DCTERMS.description),
        g.objects(subject, SKOS.definition),
        g.objects(subject, SDO.description),
        g.objects(subject, DC.description),
    ):
        return o
    return None