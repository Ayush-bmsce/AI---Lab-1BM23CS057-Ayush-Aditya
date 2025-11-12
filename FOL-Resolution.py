from itertools import combinations

# Utility: negate a literal
def negate(literal):
    if literal.startswith('~'):
        return literal[1:]
    else:
        return '~' + literal

# Apply resolution on two clauses
def resolve(ci, cj):
    resolvents = set()
    for di in ci:
        for dj in cj:
            if di == negate(dj):
                new_clause = (ci - {di}) | (cj - {dj})
                resolvents.add(frozenset(new_clause))
    return resolvents

def fol_resolution(KB, query):
    clauses = set(KB)
    clauses.add(frozenset([negate(query)]))  # add negation of query

    new = set()
    while True:
        pairs = list(combinations(clauses, 2))
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return True  # empty clause found → proved
            new = new.union(resolvents)

        if new.issubset(clauses):
            return False  # no new clauses → cannot prove
        clauses = clauses.union(new)

# ------------------------
# Knowledge Base in CNF
# ------------------------
KB = [
    frozenset(['~Food(x)', 'Likes(John,x)']),  # John likes all food
    frozenset(['Food(Apple)']),
    frozenset(['Food(Vegetables)']),
    frozenset(['~Eats(x,y)', 'Killed(x)', 'Food(y)']),
    frozenset(['Eats(Anil,Peanuts)']),
    frozenset(['Alive(Anil)']),
    frozenset(['~Eats(Anil,x)', 'Eats(Harry,x)']),
    frozenset(['~Alive(x)', '~Killed(x)']),
    frozenset(['Killed(x)', 'Alive(x)'])
]

query = 'Likes(John,Peanuts)'

# Run the resolution
if fol_resolution(KB, query):
    print("Proved:", query)
else:
    print("Invalid — cannot be proved")
