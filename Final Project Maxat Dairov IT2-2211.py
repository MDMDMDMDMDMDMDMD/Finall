def generate_assembly_from_prefix(prefix_expression):
    # Operators and their corresponding assembly commands
    operators = {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MUL',
        '/': 'DIV'
    }

    # Split the input string into tokens
    tokens = prefix_expression.split()

    # Use a stack to process the tokens
    stack = []

    # Process tokens from right to left (characteristic of prefix notation)
    for token in reversed(tokens):
        if token in operators:
            # If the token is an operator, pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Generate the assembly command
            assembly = f"{operators[token]} {operand1}, {operand2}"
            # Push the result back onto the stack
            stack.append(assembly)
        else:
            # If the token is an operand (number), push it onto the stack
            stack.append(token)

    # The final result is the only element left in the stack
    return stack[0]


# Main program block
if __name__ == "__main__":
    # Input the prefix expression from the console
    prefix_code = input("Enter a prefix expression (e.g., * + 2 3 4): ")
    try:
        # Generate the assembly code
        assembly_code = generate_assembly_from_prefix(prefix_code)
        print("Generated assembly code:")
        print(assembly_code)
    except IndexError:
        print("Error: Invalid expression. Make sure it is correct.")
