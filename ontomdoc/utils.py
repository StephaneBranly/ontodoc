
def get_object(g, subject, predicate):
    oo = [o for o in g.objects(subject=subject, predicate=predicate)]
    if not len(oo):
        return None
    return oo[0]
