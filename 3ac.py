def generate3ac(statement):
    operator=None
    operands=[]
    result=None
    parts=statement.split('=')
    if parts!=2:
        print("Invalid statement")
        return
    
    left,right = parts[0],parts[1]

    if '+' in right:
        operator = '+'
        operands = right.split('+')
    
    if '-' in right:
        operator = '-'
        operands = right.split('-')

    if '*' in right:
        operator = '*'
        operands = right.split('*')

    if '/' in right:
        operator = '/'
        operands = right.split('/')

    quadruples=[(operator,operands[0],operands[1],result)]

    return quadruples

def main():
    num_stat = int(input("Enter the number of statements:- "))
    statements=[]
    for i in range (num_stat):
        statement=input("Enter the statement: ")
        statements.append(statement)
    
    print("\nQuadruple")
    print("\n1:Operator , Operan1, Operand2, Result")

    for statement in statements:
        quadruple = generate3ac(statement)
        print("\nFor statement:", statement)
        print("Quadruples:")
        for quad in quadruples:
            print(quad)


if __name__ == "__main__":
    main()



