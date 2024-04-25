def first(grammar,nonterminal):
    first_set=set()
    if nonterminal not in grammar:
        first_set.add(nonterminal)
        return first_set
    for production in grammar[nonterminal]:
        for symbol in production:
            first_symbol=first(grammar,symbol)

            first_set |= (first_symbol-{"ep"})

            if "ep" not in first_symbol:
                break
        else:
            first_set.add("ep")
    
    return first_set

def follow(grammar, start_symbol):
    follow_set = {}
    first_sets = {key: set() for key in grammar.keys()}
    
    for non_terminal in grammar.keys():
        follow_set[non_terminal] = set()
    
    follow_set[start_symbol].add('$')
    
    # Compute FIRST sets for all non-terminals
    for non_terminal in grammar.keys():
        first_sets[non_terminal] = first(grammar, non_terminal)
    
    # Iterate until no changes occur in follow sets
    while True:
        prev_follow_set = {key: value.copy() for key, value in follow_set.items()}
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i in range(len(production)):
                    symbol = production[i]
                    if symbol in grammar.keys():
                        if i < len(production) - 1:
                            next_symbol = production[i + 1]
                            if next_symbol in grammar.keys():
                                follow_set[symbol] |= (first_sets[next_symbol] - {'ε'})
                                if 'ε' in first_sets[next_symbol]:
                                    follow_set[symbol] |= follow_set[non_terminal]
                            else:
                                follow_set[symbol].add(next_symbol)
                        else:
                            follow_set[symbol] |= follow_set[non_terminal]
        if prev_follow_set == follow_set:
            break
    
    return follow_set

if __name__ == "__main__":
    grammar = {
        'E': [['T', "E'"]],
        "E'": [['+', 'T', "E'"], ['ε']],
        'T': [['F', "T'"]],
        "T'": [['*', 'F', "T'"], ['ε']],
        'F': [['(', 'E', ')'], ['id']]
    }
    
    start_symbol = 'E'
    
    follow_result = follow(grammar, start_symbol)
    
    print("Follow sets:")
    for non_terminal, follow_set in follow_result.items():
        print(f"FOLLOW({non_terminal}) = {follow_set}")
