# Forward Chaining in First-Order Logic (FOL)
# Example: Prove "Criminal(Robert)"

# Knowledge Base (KB)
KB = [
    # Rule 1: It is a crime for an American to sell weapons to hostile nations
    {"if": ["American(p)", "Weapon(q)", "Sells(p, q, r)", "Hostile(r)"], "then": "Criminal(p)"},

    # Rule 2: Country A owns some missiles (T1)
    {"fact": "Owns(A, T1)"},
    {"fact": "Missile(T1)"},

    # Rule 3: Missiles are weapons
    {"if": ["Missile(x)"], "then": "Weapon(x)"},

    # Rule 4: All missiles owned by A were sold by Robert
    {"if": ["Missile(x)", "Owns(A, x)"], "then": "Sells(Robert, x, A)"},

    # Rule 5: Enemies of America are hostile
    {"if": ["Enemy(x, America)"], "then": "Hostile(x)"},

    # Rule 6: Robert is an American
    {"fact": "American(Robert)"},

    # Rule 7: Country A is an enemy of America
    {"fact": "Enemy(A, America)"}
]

# Function to extract all current known facts
def get_facts(kb):
    return {rule["fact"] for rule in kb if "fact" in rule}

# Function to perform variable substitution
def substitute(expr, var, val):
    return expr.replace(f"({var})", f"({val})").replace(f"{var},", f"{val},").replace(f",{var})", f",{val})")

# Forward chaining algorithm
def forward_chain(kb, query):
    inferred = set()
    facts = get_facts(kb)
    new_inference = True

    print("Initial Facts:", facts)
    print("Goal:", query)
    print("\n--- Forward Chaining Process ---")

    while new_inference:
        new_inference = False
        for rule in kb:
            if "if" in rule:
                conditions = rule["if"]
                result = rule["then"]

                # Check if all conditions are satisfied
                satisfied = True
                temp_result = result
                substitution = {}

                for cond in conditions:
                    matched = False
                    for fact in facts:
                        if cond.split("(")[0] == fact.split("(")[0]:
                            # Try variable substitution
                            c_args = cond[cond.find("(") + 1:-1].split(",")
                            f_args = fact[fact.find("(") + 1:-1].split(",")

                            if len(c_args) == len(f_args):
                                for i in range(len(c_args)):
                                    if c_args[i].islower():
                                        substitution[c_args[i]] = f_args[i]
                                    elif c_args[i] != f_args[i]:
                                        break
                                else:
                                    matched = True
                                    break
                    if not matched:
                        satisfied = False
                        break

                if satisfied:
                    for var, val in substitution.items():
                        temp_result = substitute(temp_result, var, val)

                    if temp_result not in facts:
                        facts.add(temp_result)
                        inferred.add(temp_result)
                        new_inference = True
                        print(f"Inferred: {temp_result}")

                    if temp_result == query:
                        print("\n✅ Goal Reached!")
                        return True

    print("\n❌ Goal Not Reached.")
    return False


# Main Execution
if __name__ == "__main__":
    query = "Criminal(Robert)"
    result = forward_chain(KB, query)
    print("\nFinal Result:", "Robert is a Criminal" if result else "Cannot prove Robert is Criminal")
