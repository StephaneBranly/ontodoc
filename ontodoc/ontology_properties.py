from rdflib import DC, OWL, RDF, RDFS, SKOS, SDO, DCTERMS


LABEL = {
    'predicates': [
        RDFS.label,
        DC.title,
        SKOS.prefLabel,
        SDO.name,
        DCTERMS.title
    ]
}

COMMENT = {
    'predicates': [
        RDFS.comment,
        DCTERMS.description,
        SKOS.definition,
        SDO.description,
        DC.description
    ]
}

TYPE = {
    'predicates': [
        OWL.Class,
        OWL.ObjectProperty,
        OWL.DatatypeProperty,
        OWL.AnnotationProperty,
        OWL.FunctionalProperty,
        RDF.Property,
    ]
}