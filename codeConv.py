def generate_assembly(eq):
    assembly_code = []
    registers = ['R0', 'R1', 'R2', 'R3']  # Available registers
    reg_count = 0  # Register counter

    for line in eq:
        parts = line.split('=')
        lhs = parts[0].strip()
        rhs = parts[1].strip()

        if '-' in rhs:
            op1, op2 = rhs.split('-')
            assembly_code.append(f"MOV {op1},{registers[reg_count]}")
            assembly_code.append(f"SUB {op2},{registers[reg_count]}")
        elif '+' in rhs:
            op1, op2 = rhs.split('+')
            if op1 in registers:
                assembly_code.append(f"ADD {op2},{op1}")
            elif op2 in registers:
                assembly_code.append(f"ADD {op1},{op2}")
            else:
                assembly_code.append(f"MOV {op1},{registers[reg_count]}")
                assembly_code.append(f"ADD {op2},{registers[reg_count]}")

        if lhs not in registers:
            assembly_code.append(f"MOV {registers[reg_count]},{lhs}")
            reg_count = (reg_count + 1) % len(registers)

    return assembly_code


def print_code_table(eq, assembly):
    print("Statements\t\t\t\t\tCode Generated")
    print("--------------------------------------------")
    for i in range(len(eq)):
        if i == len(eq) - 1:
            print(f"{eq[i]:<40}\tMOV R0,{eq[i][0]}")
        else:
            print(f"{eq[i]:<40}\t{assembly[i*3]}\n{'':<40}\t{assembly[i*3 + 1]}")
        print("--------------------------------------------")
    print("--------------------------------------------")


if __name__ == "__main__":
    equations = ["t = a - b", "u = a - c", "v = t + u", "d = v + u"]
    assembly = generate_assembly(equations)
    print_code_table(equations, assembly)
