from LogicExpStream import LogicExpStream
from LogicExp import is_complete, evaluate, make_truth_table, operation_count_all
from BitStream import *
import sys


# These are the full adder functions
def full_adder_result(args: list) -> bool:
    """
    Returns the result of full_adder with arguments args
    """
    if args == [0, 0, 0]:
        return False
    elif args == [0, 0, 1]:
        return True
    elif args == [0, 1, 0]:
        return True
    elif args == [0, 1, 1]:
        return False

    elif args == [1, 0, 0]:
        return True
    elif args == [1, 0, 1]:
        return False
    elif args == [1, 1, 0]:
        return False
    elif args == [1, 1, 1]:
        return True
        # That's it! There's no other cases: NO OTHER CASES


def full_adder_carrier(args: list) -> bool:
    """
    Returns the carrier of full_adder with arguments args
    """
    if args == [0, 0, 0]:
        return False
    elif args == [0, 0, 1]:
        return False
    elif args == [0, 1, 0]:
        return False
    elif args == [0, 1, 1]:
        return True

    elif args == [1, 0, 0]:
        return False
    elif args == [1, 0, 1]:
        return True
    elif args == [1, 1, 0]:
        return True
    elif args == [1, 1, 1]:
        return True
        # That's it! There's no other cases: NO OTHER CASES


# compare the results of the two funcitons

# Preparing args:
all_args = []
bit_stream = BitStream([])
for bit_stream_third in bit_stream.extend_count(3):
    all_args.append(tuple(bit_stream_third.value))

# Preparing truth table for the logic gates:
full_adder_result_truth_table = {}  # Yes, the truth table is a dictionary with keys as argument list
for args in all_args:
    full_adder_result_truth_table[args] = full_adder_result(list(args))

full_adder_carrier_truth_table = {}  # Yes, the truth table is a dictionary with keys as argument list
for args in all_args:
    full_adder_carrier_truth_table[args] = full_adder_carrier(list(args))  # turned args to tuples to use them as keys

# Make a empty LogicExpStream
current_exp_stream_pool = [LogicExpStream([])]
# then expand it

# constraints: necessary to run this shit without frying your RAM
operation_constraint = 4 #  Constraint of operation count per expression
level_constraint = 4 # Constraint of the number of level

level_count = 0 #  This is here just for the tracking
while level_count <= level_constraint:
    print('level: ', level_count)
    level_count += 1
    
    # Extending and testing at the same time
    next = []
    _stream_count = 0
    for stream in current_exp_stream_pool:
        print('stream no.: ', _stream_count)
        _stream_count += 1
        exp = stream.value
        if is_complete(exp):
            if make_truth_table(exp, all_args) == full_adder_carrier_truth_table:
                print(exp)
                sys.exit()
        else:
            if operation_count_all(exp) <= operation_constraint:
                    next.extend(stream.extend())

    current_exp_stream_pool = next
                
