# Unification Algorithm in First-Order Logic (FOL)

def is_variable(x):
    """Check if the symbol is a variable (starts with lowercase letter)."""
    return x[0].islower() and x.isalpha()

def unify(x, y, subs=None):
    """Main unification function."""
    if subs is None:
        subs = {}
    if x == y:
        return subs

    elif is_variable(x):
        return unify_var(x, y, subs)

    elif is_variable(y):
        return unify_var(y, x, subs)

    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for a, b in zip(x, y):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    elif isinstance(x, str) and isinstance(y, str):
        return None  # constants don't match

    elif isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0]:  # predicate symbols must match
            return None
        return unify(list(x[1]), list(y[1]), subs)

    else:
        return None


def unify_var(var, x, subs):
    """Handle variable substitution logic."""
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    elif occurs_check(var, x, subs):
        return None
    else:
        subs[var] = x
        return subs


def occurs_check(var, x, subs):
    """Prevent infinite recursive substitution."""
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occurs_check(var, xi, subs) for xi in x)
    elif isinstance(x, tuple):
        return occurs_check(var, x[1], subs)
    elif x in subs:
        return occurs_check(var, subs[x], subs)
    else:
        return False


# Example usage
if __name__ == "__main__":
    expr1 = ('Eats', ['x', 'Apple'])
    expr2 = ('Eats', ['Riya', 'y'])

    result = unify(expr1, expr2)
    if result:
        print("Unification Successful!")
        print("Substitutions:", result)
    else:
        print("Unification Failed!")
