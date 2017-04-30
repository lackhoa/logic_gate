from ExtensibleStream import ExtensibleStream
from LogicExp import operation_count
from Enum import Var, Op, Const


class LogicExpStream(ExtensibleStream):
    """
    Represents a logic expression
    Example: [[AND], [A, AND], [B, C]]
    TESTED
    """

    def extend(self):
        """
        TESTED! (BUT THERE IS A BUG) (BUG FIXED!)
        """
        if self.value == []:
            next_level_count = 1
        else:
            last_level = self.value[len(self.value) - 1]
            op_count_last_lvl = operation_count(last_level)
            if op_count_last_lvl is 0:
                raise ValueError('Hey, you cannot extend this. This expression is complete')
            next_level_count = 2 * op_count_last_lvl
        # the next level always contains branches count of  2*branch_count_of_the_last_level (except for the empty case)
        # so you can expand that much
        lvl_str = LevelStream([])
        next_lvl_streams = lvl_str.extend_count(next_level_count)

        result = []
        for level_stream in next_lvl_streams:
            result.append(self._make_child(level_stream.value))

        return result

    def extend_count(self, count: int):
        raise NotImplementedError('This function is not implemented due to complete expressions')


class LevelStream(ExtensibleStream):
    """
    A stream of a level, which is just a list of expressions symbols
    TESTED!
    """

    def extend(self):
        result = []
        exp_symbol_list = list(Const)
        exp_symbol_list.extend(list(Var))
        exp_symbol_list.extend(list(Op))

        for exp_symbol in exp_symbol_list:
            result.append(self._make_child(exp_symbol))
        return result

    def double_extend(self):
        """
        Extend twice using pairs: more efficient
        TESTING!
        """
        result = []
        pair_streams = PairStream([]).extend()

        for pair_stream in pair_streams:
            child = self._make_child(pair_stream.value[0][0])
            child = child._make_child(pair_stream.value[0][1])
            result.append(child)
        return result

    def extend_count(self, count):
        """
        Now using pairs to make this thing cost less memoy
        TESTING!
        """
        if count == 0:
            raise ValueError('Hey, you cannot extend 0 times')
        elif count == 1:
            return self.extend()
        else:  # Now you we use pairs
            current_streams = [self]

            for _ in range(count // 2):
                next_streams = []
                for stream in current_streams:
                    next_streams.extend(stream.double_extend())
                current_streams = next_streams

            if not count % 2 == 0:  # Do another round if the pairs ain't enough
                next_streams = []
                for stream in current_streams:
                    next_streams.extend(stream.extend())
                current_streams = next_streams

            return current_streams


class PairStream(ExtensibleStream):
    """
    + pair: a pair is a tuple (?) of two logical symbols. Though I'm using tuple here, note that the order of the pair doesn't matter, and that two pair with the same symbols ordered differently are identical
    + pair is just a means to save memory during the construction of a level. Aside from that, it isn't used in any other function due to compatibility
    """
    all_pairs = []  # Class variable to store the pairs since it only has to extend once

    def extend(self):
        """
        Returns: a list of pairs
        TESTING
        """
        if self.all_pairs == []:
            exp_symbol_list = list(Const)
            exp_symbol_list.extend(list(Var))
            exp_symbol_list.extend(list(Op))

            result = []
            for exp_symbol1 in exp_symbol_list:
                for exp_symbol2 in exp_symbol_list:
                    if exp_symbol1.value <= exp_symbol2.value:  # For symmetric reason
                        self.all_pairs.append(self._make_child((exp_symbol1, exp_symbol2)))

        return self.all_pairs
