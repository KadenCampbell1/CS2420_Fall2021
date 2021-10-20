from stack import Stack


def eval_postfix(expr):
    """takes expression and returns calculation as float

    arguments:
    expr -- type string
    """
    if not isinstance(expr, str):
        raise ValueError

    stack = Stack()

    for i in range(len(expr)):
        if expr[i] == "+":
            value1 = stack.pop()
            value2 = stack.pop()
            result = float(value2.get_item()) + float(value1.get_item())

        elif expr[i] == "-":
            value1 = stack.pop()
            value2 = stack.pop()
            result = float(value2.get_item()) - float(value1.get_item())

        elif expr[i] == "*":
            value1 = stack.pop()
            value2 = stack.pop()
            result = float(value2.get_item()) * float(value1.get_item())

        elif expr[i] == "/":
            value1 = stack.pop()
            value2 = stack.pop()
            result = float(value2.get_item()) / float(value1.get_item())

        else:
            stack.push(expr[i].strip())

    return result


def in2post(expr):
    """takes infix expression and returns postfix as string

    arguments:
    expr -- type string
    """
    if not isinstance(expr, str):
        raise ValueError

    stack = Stack()

    for i in range(len(expr)):
        if expr[i] == "+":
            # add to stack with priority
            pass

        elif expr[i] == "-":
            # add to stack with priority
            pass

        elif expr[i] == "*":
            # add to stack with priority
            pass

        elif expr[i] == "/":
            # add to stack with priority
            pass

        else:
            # stack.push(expr[i].strip())
            # store value in result
            pass

    return expr


def main():
    with open("data.txt") as DATA_FILE:
        data_lyst = [x.strip() for x in DATA_FILE.readlines()]

    print(eval_postfix("34+"))

    # for i in data_lyst:
    #     # write to outfile
    #     print(f"infix: {i}")
    #     postfix = in2post(i)
    #     print(f"postfix: {postfix}")
    #     print(f"answer: {eval_postfix(postfix)}\n")


if __name__ == "__main__":
    main()
