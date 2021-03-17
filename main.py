"""

main.py

"""

from stack import Stack

def parenthesis(expr):
    """checks for an inbalance in parenthesis"""
    stk = Stack()
    balanced = True
    i = 0
    while i < len(expr) and balanced:
        sym = expr[i]
        if sym == '(':
            stk.push(sym)
        elif sym == ')':
            if stk.is_empty():
                balanced = False
            else:
                stk.pop()
        i += 1

    if balanced and stk.is_empty():
        return True
    else:
        return False

def concurrent_Op(expr):
    """checks number of operands & operators"""
    sym_count = 0
    non_sym_count = 0
    i = 0
    while i < len(expr):
        if expr[i] in "+-/*":
            sym_count += 1
        elif expr[i] in "0123456789":
            non_sym_count += 1
        i += 1
    if non_sym_count <= sym_count:
        return False

def in2post(expr):
    """converts string to post fix notation"""
    if not isinstance(expr, str):
        raise ValueError
    elif parenthesis(expr) is False:
        raise SyntaxError
    elif concurrent_Op(expr) is False:
        raise SyntaxError

    output = []
    prec = {}
    opstack = Stack()
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    for sym in expr:
        if sym == '(':
            opstack.push('(')
        elif sym == ' ':
            sym == ''
        elif sym in "0123456789":
            output.append(sym)
        elif sym == ')':
            top = opstack.pop()
            while top != '(':
                output.append(top)
                top = opstack.pop()
        else:
            while (not opstack.is_empty() and
                    prec[opstack.top()] >= prec[sym]):
                output.append(opstack.pop())
            opstack.push(sym)

    while not opstack.is_empty():
        output.append(opstack.pop())

    return " ".join(output)

def eval_postfix(expr):
    "evaluates post fix notation and returns value"
    if not isinstance(expr, str):
        raise ValueError
    elif parenthesis(expr) is False:
        raise SyntaxError
    elif concurrent_Op(expr) is False:
        raise SyntaxError

    stk = Stack()
    for char in expr:
        if char in "0123456789":
            stk.push(float(char))
        elif char == " ":
            continue
        else:
            num2 = stk.pop()
            num1 = stk.pop()
            result = calculate(char, num1, num2)
            stk.push(result)
    return stk.pop()

def calculate(char, num1, num2):
    """performs math operation based on char"""
    if char == "/":
        return num1 / num2
    elif char == "+":
        return num1 + num2
    elif char == "-":
        return num1 - num2
    else:
        return num1 * num2

def main():
    """main function opens file & prints to console"""
    with open('data.txt', 'r') as file:
        infix = []
        for line in file:
            fixed_line = line.rstrip("\n")
            infix.append(fixed_line)

    for val in infix:
        print("infix:", val)
        print("postfix:", in2post(val))
        print("answer: ", eval_postfix(in2post(val)))

if __name__ == "__main__":
    main()
