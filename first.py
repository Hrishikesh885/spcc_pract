def first(grammar, nonterminal):
    first_set = set()

    if nonterminal not in grammar:
        first_set.add(nonterminal)
        return first_set
    
    for production in grammar[nonterminal]:
        for symbol in production:
            first_of_symbol = first(grammar, symbol)

            first_set |= (first_of_symbol - {'ε'})

            if 'ε' not in first_of_symbol:
                break
        else:
            first_set.add('ε')

    return first_set

def print_first(grammar):
    for nonterminal in grammar:
        first_set = first(grammar, nonterminal)
        print(f"FIRST({nonterminal}): {first_set}")

# Grammar
grammar = {
    'E': [['T', 'E\'']],
    'E\'': [['+', 'T', 'E\''], ['ε']],
    'T': [['F', 'T\'']],
    'T\'': [['*', 'F', 'T\''], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

print("First sets:")
print_first(grammar)
