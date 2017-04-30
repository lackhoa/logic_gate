from enum import Enum


# Since I need to sort theme later, the value of the enums are not default

class Const(Enum):
    """Represents a boolean constant"""
    ZERO = 0
    ONE = 1

class Var(Enum):
    """Represents a variable"""
    A = 2
    B = 3
    C = 4


class Op(Enum):
    """Represents an operation"""
    AND = 5
    XOR = 6


