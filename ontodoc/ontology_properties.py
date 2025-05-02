from rdflib import DC, OWL, RDF, RDFS, SKOS, SDO, DCTERMS, VANN

class ONTOLOGY_PROP:
    array = False

class LABEL(ONTOLOGY_PROP):
    predicates = [
        RDFS.label,
        DC.title,
        SKOS.prefLabel,
        SDO.name,
        DCTERMS.title
    ]

class COMMENT(ONTOLOGY_PROP):
    predicates = [
        RDFS.comment,
        DCTERMS.description,
        SKOS.definition,
        SDO.description,
        DC.description
    ]


class TYPE(ONTOLOGY_PROP):
    predicates = [
        OWL.Class,
        OWL.ObjectProperty,
        OWL.DatatypeProperty,
        OWL.AnnotationProperty,
        OWL.FunctionalProperty,
        RDF.Property,
    ]

class RESTRICTION(ONTOLOGY_PROP): 
    predicates = [
        OWL.allValuesFrom,
        OWL.someValuesFrom,
        OWL.hasValue,
        OWL.onProperty,
        OWL.onClass,
        OWL.cardinality,
        OWL.qualifiedCardinality,
        OWL.minCardinality,
        OWL.minQualifiedCardinality,
        OWL.maxCardinality,
        OWL.maxQualifiedCardinality,
    ]

class CREATOR(ONTOLOGY_PROP):
    array = True
    predicates = [ DCTERMS.creator ]

class CONTRIBUTOR(ONTOLOGY_PROP):
    array = True
    predicates = [  DCTERMS.contributor ]
    
class ONTOLOGY(ONTOLOGY_PROP): 
    predicates =  [
        DCTERMS.publisher,
        CREATOR,
        CONTRIBUTOR,
        DCTERMS.created,
        DCTERMS.dateAccepted,
        DCTERMS.modified,
        DCTERMS.issued,
        DCTERMS.license,
        DCTERMS.rights,
        SDO.category,
        OWL.versionIRI,
        OWL.versionInfo,
        OWL.priorVersion,
        SDO.identifier,
        VANN.preferredNamespacePrefix,
        VANN.preferredNamespaceUri,
        SKOS.historyNote,
        SKOS.scopeNote,
        DCTERMS.source,
        DCTERMS.provenance,
        SKOS.note,
        COMMENT,
        LABEL
    ]

class EQUIVALENTCLASS(ONTOLOGY_PROP):
    array = True
    predicates = [
        OWL.equivalentClass
    ]

class SUBCLASSOF(ONTOLOGY_PROP):
    array = True
    predicates = [
        RDFS.subClassOf,
    ]

class CLASS(ONTOLOGY_PROP):
    predicates  = [
        RDFS.isDefinedBy,
        SKOS.scopeNote,
        SKOS.example,
        DCTERMS.source,
        DCTERMS.provenance,
        SKOS.note,
        SUBCLASSOF,
        EQUIVALENTCLASS,
        COMMENT,
        LABEL
    ]