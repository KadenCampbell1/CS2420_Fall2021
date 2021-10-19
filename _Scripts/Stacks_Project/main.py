from stack import Stack


def eval_postfix(expr):
    """takes expression and returns calculation as float

    arguments:
    expr -- type string
    """
    pass


def in2post(expr):
    """takes infix expression and returns postfix as string

    arguments:
    expr -- type Any
    """
    pass


def main():
    with open("data.txt") as DATA_FILE:
        data_lyst = [x.strip() for x in DATA_FILE.readlines()]

    stack = Stack()
    print(data_lyst[1])
    stack.push(data_lyst[0])
    print(stack)
    stack.push(data_lyst[1])
    stack.push(data_lyst[2])
    print(stack)


if __name__ == "__main__":
    main()
