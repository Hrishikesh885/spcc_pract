def remove_left_factoring(grammar):
    new_grammar = {}

    for nonterminal, productions in grammar.items():
        common_prefixes = {}
        new_productions = []

        # Group productions by their common prefixes
        for production in productions:
            prefix = ""
            for i, symbol in enumerate(production):
                prefix += symbol
                if i < len(production)-1 and all(p.startswith(prefix) for p in productions):
                    continue
                else:
                    # Found the longest common prefix
                    common_prefixes.setdefault(prefix[:-1], []).append(production[i:])
                    break

        for prefix, suffixes in common_prefixes.items():
            if len(suffixes) > 1:
                # Create a new non-terminal for the common prefix
                new_nonterminal = nonterminal + "'"
                new_grammar[new_nonterminal] = suffixes
                new_productions.append(prefix + new_nonterminal)
            else:
                new_productions.extend([prefix + suffix for suffix in suffixes])

        new_grammar[nonterminal] = new_productions

    return new_grammar

# Example grammar
grammar = {
    'A': ['bE+acF', 'bE+F']
}

# Remove left factoring
new_grammar = remove_left_factoring(grammar)

# Print the updated grammar
for nonterminal, productions in new_grammar.items():
    print(f"{nonterminal} -> {' | '.join(productions)}")
