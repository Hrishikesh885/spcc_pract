class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

class Triple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

def generate_quadruples_and_triples(three_address_code):
    quadruples = []
    triples = []
    res = []
    for line in three_address_code:
        parts = line.split()
        res.append(parts[0])

        if parts[-2] in ['+', '-', '*', '/']:
            if len(parts) == 5:
                quadruples.append(Quadruple(parts[-2], parts[2], parts[-1], parts[0]))
                triples.append(Triple(parts[-2], parts[2], parts[-1], parts[0]))
            else:
                quadruples.append(Quadruple(parts[-2], parts[-1], '', parts[0]))
                triples.append(Triple(parts[-2], parts[-1], '', parts[0]))
        else:
            quadruples.append(Quadruple(parts[1], parts[-1], '', parts[0]))
            triples.append(Triple(parts[1], parts[-1], '', parts[0]))

    return quadruples, triples, res

def display_quadruples_table(quadruples):
    print("{:<4} {:<6} {:<6} {:<6}".format("OP", "ARG1", "ARG2", "RESULT"))
    for quad in quadruples:
        print("{:<4} {:<6} {:<6} {:<6}".format(quad.op, quad.arg1, quad.arg2, quad.result))

def display_triples_table(triples, res):
    print("{:<6} {:<6} {:<6}".format("OP", "ARG1", "ARG2"))
    for triple in triples:
        arg1_str = '(' + str(res.index(triple.arg1)) + ')' if triple.arg1 in res else triple.arg1
        arg2_str = '(' + str(res.index(triple.arg2)) + ')' if triple.arg2 in res else triple.arg2
        print("{:<6} {:<6} {:<6}".format(triple.op, arg1_str, arg2_str))

# Get user input for three-address code
three_address_code = []
n = int(input("Enter the number of statements: "))
for _ in range(n):
    print("Enter the 3AC statement: ")
    three_address_code.append(input())

# Generate quadruples and triples
quadruples, triples, res = generate_quadruples_and_triples(three_address_code)

# Display quadruples table
print("\nQuadruples:")
display_quadruples_table(quadruples)

# Display triples table
print("\nTriples:")
display_triples_table(triples, res)
