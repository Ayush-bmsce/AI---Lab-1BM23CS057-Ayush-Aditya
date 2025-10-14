import itertools

# Evaluate a propositional logic sentence in a given model (dictionary of symbol → True/False)
def pl_true(expr, model):
    if isinstance(expr, str):  # atomic symbol
        return model[expr]
    op = expr[0]
    if op == 'not':
        return not pl_true(expr[1], model)
    elif op == 'and':
        return pl_true(expr[1], model) and pl_true(expr[2], model)
    elif op == 'or':
        return pl_true(expr[1], model) or pl_true(expr[2], model)
    elif op == 'implies':
        return (not pl_true(expr[1], model)) or pl_true(expr[2], model)
    elif op == 'iff':
        return pl_true(expr[1], model) == pl_true(expr[2], model)
    else:
        raise ValueError("Unknown operator: " + op)

# The truth table enumeration function
def tt_entails(kb, query, symbols):
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if pl_true(kb, model):
            if not pl_true(query, model):
                return False  # Found a counterexample
    return True

# Example Knowledge Base and Query
# Example: (P ∧ Q) → R, and (P ∧ Q) is true, does R follow?

symbols = ['P', 'Q', 'R']

# Knowledge Base: (P ∧ Q) → R
kb = ('implies', ('and', 'P', 'Q'), 'R')

# Query: R
query = 'R'

# Check entailment
result = tt_entails(kb, query, symbols)

print("Does KB entail Query? →", result)
