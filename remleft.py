def remove_left_recursion(grammar):
    non_terminals = list(grammar.keys())
    for A in non_terminals:
        productions = grammar[A]
        alpha = []
        beta = []
        for prod in productions:
            if prod[0] == A:
                alpha.append(prod[1:])
            else:
                beta.append(prod)
        if alpha:
            # Adding a new non-terminal A' for left recursion
            A_prime = A + "'"
            # Updating beta productions
            grammar[A] = [tuple(b + (A_prime,)) for b in beta]
            # Generating new productions for A' based on alpha
            grammar[A_prime] = [tuple(a + (A_prime,)) for a in alpha] + [('ε',)]
    return grammar

# Example grammar
grammar = {
    'S': [('(', 'L', ')'), ('x',)],
    'L': [('L',  'S'), ('S',)]
}

# Removing left recursion
modified_grammar = remove_left_recursion(grammar)

# Displaying the modified grammar
print("Modified Grammar:")
for non_terminal, productions in modified_grammar.items():
    print(non_terminal, '->', '|'.join([' '.join(prod) for prod in productions]))
