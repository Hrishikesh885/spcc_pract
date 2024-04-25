class Triple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

def generate_triples(three_address_code):
    triples = []
    res = []
    for line in three_address_code:
        parts = line.split()
        res .append(parts[0])
        if parts[-2] in ['+', '-', '*', '/']:
            if len(parts) == 5:
                triples.append(Triple(parts[-2], parts[2], parts[-1], parts[0]))
            else:
                triples.append(Triple(parts[-2], parts[-1], '', parts[0]))
        
        else:
            triples.append(Triple(parts[1], parts[-1], '', parts[0]))
    return triples,res

def display_triples_table(triples, res):
    print("{:<6} {:<6} {:<6}".format("OP", "ARG1", "ARG2"))
    for triple in triples:
        arg1_str = '(' + str(res.index(triple.arg1)) + ')' if triple.arg1 in res else triple.arg1
        arg2_str = '(' + str(res.index(triple.arg2)) + ')' if triple.arg2 in res else triple.arg2
        print("{:<6} {:<6} {:<6}".format(triple.op, arg1_str, arg2_str))

# Example usage
three_address_code = []
n = int(input("Enter the number of statements: "))
for _ in range(n):
    print("Enter the 3AC statement: ")
    three_address_code.append(input())

triples,res = generate_triples(three_address_code)
display_triples_table(triples,res)
