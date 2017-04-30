from LogicExpStream import *

from LogicExp import *

first_dict = {(0, 1): True, (1, 2): False}
second_dict = {(1, 2): False, (0, 1): True}

print(first_dict == second_dict)
