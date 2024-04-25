def optimization():
    codes = []
    new_codes = []
    subexpressions = {}  # Dictionary to store seen subexpressions and their corresponding left-hand sides
    print("Enter the equations : ")
    for i in range(5):
        code = input()
        codes.append(code)
    print("After Code Optimization : ")
    for code in codes:
        lhs, rhs = code.split("=")
        # CONSTANT FOLDING
        if not any(char.isalpha() for char in rhs):
            rhs = eval(rhs)
            new_codes.append(f"{lhs}={rhs}")
        # COPY PROPAGATION
        elif '+' not in str(rhs) and '-' not in str(rhs) and '*' not in str(rhs) and '/' not in str(rhs) and any(char.isalpha() for char in str(rhs)):
            codes.remove(code)  # Remove the equation from the original list
            for i in range(len(codes)):
                if lhs in codes[i]:
                    codes[i] = codes[i].replace(lhs, rhs)
                    new_codes.append(codes[i])
        # COMMON SUB-EXPRESSION ELIMINATION
        else:
            for subexpr, result in subexpressions.items():
                if subexpr in rhs:
                    rhs = rhs.replace(subexpr, result)  # Replace subexpression with its corresponding result
            if any(char.isalpha() for char in rhs):
                subexpressions[rhs] = lhs  # Update subexpressions if rhs is not a constant value
            new_codes.append(f"{lhs}={rhs}")

    for code in new_codes:
        print(code)

if __name__ == "__main__":
    optimization()