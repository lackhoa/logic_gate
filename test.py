import unittest
from LogicExp import *
from LogicExpStream import *
from ExtensibleStream import *
from LogicExp import _make_linker
from BitStream import BitStream


class Test(unittest.TestCase):
    """
    Testing the BitStream class
    """

    def test_bit_extension(self):
        """
        The real test function. I don't know how it works, but I think it will be cool
        :return: dunno
        """
        bit_stream = BitStream([])
        test1 = bit_stream.extend_count(3)
        test2 = bit_stream.extend_count(4)
        self.assertEqual(len(test1), 8)
        self.assertEqual(len(test2), 16)

    def test_level_stream_extend(self):
        """
        Tests the extend method of level stream class
        """
        lvl_stream_test = LevelStream([])
        self.assertEquals(len(lvl_stream_test.extend_count(1)), 7)
        self.assertEquals(len(lvl_stream_test.extend_count(2)),28)
        self.assertEquals(len(lvl_stream_test.extend_count(3)), 28*7)

    def test_LogicExpStream_extend(self):
        log_exp_str = LogicExpStream([])
        extend_1 = log_exp_str.extend()
        self.assertEquals(len(extend_1), 7)

        extend_2 = []
        for str in extend_1:
            if not is_complete(str.value):
                extend_2.extend(str.extend())
        self.assertEquals(len(extend_2), 56)

    def test_is_complete(self):
        exp1 = [[Op.AND], [Var.A, Op.XOR], [Var.B, Var.C]]
        self.assertEquals(is_complete(exp1), True)

        exp2 = [[Op.AND], [Var.A, Op.XOR], [Const.ONE, Op.AND]]
        self.assertEquals(is_complete(exp2), False)

    def test_evaluate(self):
        exp1 = [[Op.AND], [Var.A, Op.XOR], [Var.B, Var.C]]
        args = [True, False, False]
        self.assertEquals(evaluate(exp1, args), False)

        exp2 = [[Op.AND], [Var.A, Op.XOR], [Const.ZERO, Op.XOR], [Var.A, Var.C]]
        self.assertEquals(evaluate(exp2, args), True)

    def test_make_child(self):
        parent = ExtensibleStream(['mammal', 'chicken'])
        child = parent._make_child('dog')
        self.assertEquals(child.value, ['mammal', 'chicken', 'dog'])

    def test_make_truth_table(self):
        """
        Testing the make_truth_table function in the LogicExp file
        """
        exp = [[Op.AND], [Var.A, Op.XOR], [Const.ZERO, Op.XOR], [Var.A, Var.C]]
        args_tuples = [(False,False,False), (False,False,True), (False,True,False), (False,True,True), (True,False,False), (True,False,True), (True,True,False), (True,True,True)]

        truth_table = make_truth_table(exp, args_tuples)

        compare_table = {(False, False, False): False, (False, False, True): False, (False, True, False): False, (False, True, True): False, (True, False, False): True, (True, False, True): False,(True, True, False): True, (True, True, True): False}

        self.assertEquals(truth_table, compare_table)

    def test_make_linker(self):
        exp = [[Op.XOR], [Op.AND, Op.XOR], [Var.A, Const.ONE, Op.AND, Var.C], [Var.A, Var.A]]
        linker = _make_linker(exp)
        compare_value = {(0, 0): (0, 1), (1, 0): (0, 1), (1, 1): (2, 3), (2, 2): (0, 1)}

        self.assertEquals(linker, compare_value)

    def test_pair_stream_extend(self):
        test_pair_stream = PairStream([])
        self.assertEquals(len(PairStream([]).extend()), 28)

    def test_stream_extend_count(self):
        self.assertEquals(len(LevelStream([]).extend_count(1)), 7)
        self.assertEquals(len(LevelStream([]).extend_count(2)), 28)
        self.assertEquals(len(LevelStream([]).extend_count(4)), 784)

    def test_double_extend(self):
        self.assertEquals(len(LevelStream([]).double_extend()), 28)

    def test_operation_count_all(self):
        exp = [[Op.AND], [Op.XOR, Var.C], [Op.AND, Var.A]]
        self.assertEquals(operation_count_all(exp), 3)

if __name__ == "__main__":
    unittest.main()

