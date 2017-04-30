from Enum import Op, Var, Const


# This file deals with the real logical expressions, it has all necessary functions

def _evaluate(exp: list, x: int, y: int, args: list, linker: dict) -> bool:
    """
    This function is to evaluate an expression.
    Input: x is the level count, y is the count horizontally, and args is the list of variable's value
    Added: linker (see explanation in 'make_linker' function)
    TESTING!
    """
    current = exp[x][y]

    if current in list(Var):
        result = args[current.value - 2]
    elif current in list(Const):
        if current == Const.ONE:
            result = True
        else:  # current = Const.ZERO
            result = False

    else:  # If it is an operation
        # Finding y_guider by counting the number of operations that appear before exp[x][y]
        # y_guider = 0
        # if not y == 0:  # Yeah we can't count if there's nothing before that
        #    for yy in range(y):
        #        if exp[x][yy] in list(Op):
        #            y_guider += 1

        # getting left and right children
        # left = _evaluate(exp, x + 1, y_guider * 2, args)
        # right = _evaluate(exp, x + 1, y_guider * 2 + 1, args)

        # getting left and right children:
        left = _evaluate(exp, x + 1, linker[(x, y)][0], args, linker)
        right = _evaluate(exp, x + 1, linker[(x, y)][1], args, linker)

        if current == Op.AND:
            result = left and right
        else:  # If it's XOR
            result = (left != right)  # Now you know that != is XOR

    return result


def evaluate(exp: list, args: list) -> bool:
    """
    This function is to evaluate an expression.
    Evaluates the root node of the expression tree
    TESTING!
    """
    linker = _make_linker(exp)
    return _evaluate(exp, 0, 0, args, linker)


def make_truth_table(exp: list, args_tuples: list) -> dict:
    """
    This does the same thing as 'evaluation', but with many combinations of arguments stored in tuples
    remarks: DON'T feed it incomplete expressions
    return a dictionary with args_tuples as keys and boolean value of the expression as value
    TESTING
    """
    result = {}

    linker = _make_linker(exp)
    for args in args_tuples:
        result[args] = _evaluate(exp, 0, 0, args, linker)

    return result


def _make_linker(exp: list) -> dict:
    """
    Linker is a mapping tool to evaluate an expression faster
    Why faster? It can receive a location of a node (operation) and spit out the y value of the location of its children
     remarks: DON'T feed it incomplete expression!
    return: a linker as a dictionary with the (x, y) value of the parent nodes in tuples as keys and the two y values of their children nodes in tuples as values
    TESTING!
    """
    linker = {}
    x = 0
    for level in exp:
        y_slider = 0
        y = 0

        for exp_symbol in level:
            if exp_symbol in list(Op):
                linker[(x, y)] = (y_slider, y_slider + 1)
                y_slider += 2

            y += 1
        x += 1

    return linker


def operation_count(level: list) -> int:
    """
    Counts the number of operations of the last level from a list of levels
    TESTED!
    """
    count = 0
    for i in level:
        if type(i) is Op:  # Op means 'operation'
            count += 1

    return count

def operation_count_all(exp) -> int:
    """
    Counts the number of operations of an expression
    Returns 0 if the expression is empty
    """
    count = 0
    if not exp == []:
        for level in exp: 
            for i in level:
                if type(i) is Op: 
                    count += 1
    else:
        count = 0

    return count

def is_complete(exp: list) -> bool:
    """
    Check if an expression under the form of list of levels a complete expression
    TESTED
    """
    result = False

    if not exp == []:
        last_level = exp[len(exp) - 1]
        result = True
        for exp in last_level:
            if type(exp) is Op:
                result = False
                break
    return result
