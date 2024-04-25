import re

def generate_three_address_code(expression):
    # Tokenize the expression
    tokens = re.findall(r'\(|\)|\w+|\S', expression)
    # Stack to hold operators and operands
    stack = []
    # List to store the generated three-address code
    three_address_code = []
    # Temporary variable count
    temp_count = 1
    
    for token in tokens:
        if token.isalnum():
            stack.append(token)
        elif token in {'+', '-', '*', '/'}:
            stack.append(token)
        elif token == ')':
            op2 = stack.pop()
            operator = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            three_address_code.append(f"{operator} {op1} {op2} {temp}")
            stack.append(temp)
            temp_count += 1
        elif token == '(':
            continue
        else:
            print("Invalid token:", token)

    return three_address_code

expression = "(a+b) * (c-d)"
three_address_code = generate_three_address_code(expression)
for instruction in three_address_code:
    print(instruction)
