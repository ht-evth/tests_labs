import unittest
from main import *
from numpy import array_equal, unicode_


class test_makeRiskMatrix(unittest.TestCase):
    """
   Тест: функция получения матрицы рисков
    """

    def test1_makeRiskMatrix(self):
        input_matrix = [
            [4, 5, 7, 9],
            [6, 7, 3, 4],
            [11, 4, 12, 3]
        ]

        real_result = [
            [7, 2, 5, 0],
            [5, 0, 9, 5],
            [0, 3, 0, 6]
        ]

        test_result = makeRiskMatrix(input_matrix)

        assert array_equal(real_result, test_result) == True

    def test2_makeRiskMatrix(self):
        input_matrix = [
            [5, 25, 15],
            [20, 12, 8],
            [9, 15, 11],
            [30, 14, 2]
        ]

        real_result = [
            [25, 0, 0],
            [10, 13, 7],
            [21, 10, 4],
            [0, 11, 13]
        ]

        test_result = makeRiskMatrix(input_matrix)

        assert array_equal(real_result, test_result) == True


class test_probsCriterion(unittest.TestCase):
    """ Тест на известных вероятностях """

    def test1_probsCriterion(self):
        input_matrix = [
            [0, 12, 6, 0],
            [7, 4, 2, 1],
            [12, 0, 0, 2]
        ]

        probs = [0.25, 0.25, 0.25, 0.25]

        real_result = [2, 3]

        test_result = probsCriterion(input_matrix, probs)

        assert array_equal(real_result, test_result) == True

    def test2_probsCriterion(self):
        input_matrix = [
            [25, 0, 0],
            [10, 13, 7],
            [21, 10, 4],
            [0, 11, 13]
        ]

        probs = [0.1, 0.4, 0.5]

        real_result = [1]

        test_result = probsCriterion(input_matrix, probs)

        assert array_equal(real_result, test_result) == True


class test_ValdCriterion(unittest.TestCase):
    """ Тест критерия Вальда """

    def test1_ValdCriterion(self):
        input_matrix = [
            [4, 5, 7, 9],
            [6, 7, 3, 4],
            [11, 4, 12, 3]
        ]

        real_result = [1]

        test_result = ValdCriterion(input_matrix)

        assert array_equal(real_result, test_result) == True

    def test2_ValdCriterion(self):
        input_matrix = [
            [5, 25, 15],
            [20, 12, 8],
            [9, 15, 11],
            [30, 14, 2]
        ]

        real_result = [3]

        test_result = ValdCriterion(input_matrix)

        assert array_equal(real_result, test_result) == True


class test_GurvicCriterion(unittest.TestCase):
    """ Тест критерия Гурвица выигрыш"""

    def test1_GurvicCriterion(self):
        input_matrix = [
            [4, 5, 7, 9],
            [6, 7, 3, 4],
            [11, 4, 12, 3]
        ]

        E = 0.2

        real_result = [3]

        test_result = GurvicCriterion(input_matrix, E)

        assert array_equal(real_result, test_result) == True

    def test2_GurvicCriterion(self):
        input_matrix = [
            [5, 25, 15],
            [20, 12, 8],
            [9, 15, 11],
            [30, 14, 2]
        ]

        E = 0.7

        real_result = [2]

        test_result = GurvicCriterion(input_matrix, E)

        assert array_equal(real_result, test_result) == True


class test_gurvicRisk(unittest.TestCase):
    """ Тест критерия Гурвица риск """

    def test1_gurvicRisk(self):
        input_matrix = [
            [4, 5, 7, 9],
            [6, 7, 3, 4],
            [11, 4, 12, 3]
        ]

        L = 0.2

        real_result = [2]

        test_result = gurvicRisk(input_matrix, L)

        assert array_equal(real_result, test_result) == True

    def test2_gurvicRisk(self):
        input_matrix = [
            [5, 25, 15],
            [20, 12, 8],
            [9, 15, 11],
            [30, 14, 2]
        ]

        L = 0.7

        real_result = [3]

        test_result = gurvicRisk(input_matrix, L)

        assert array_equal(real_result, test_result) == True


class test_SavidgeCriterion(unittest.TestCase):
    """ Тест критерия Севиджа """

    def test1_SavidgeCriterion(self):
        input_matrix = [
            [4, 5, 7, 9],
            [6, 7, 3, 4],
            [11, 4, 12, 3]
        ]

        real_result = [2]

        test_result = SavidgeCriterion(input_matrix)

        assert array_equal(real_result, test_result) == True

    def test2_SavidgeCriterion(self):
        input_matrix = [
            [5, 25, 15],
            [20, 12, 8],
            [9, 15, 11],
            [30, 14, 2]
        ]

        real_result = [3]

        test_result = SavidgeCriterion(input_matrix)

        assert array_equal(real_result, test_result) == True


if __name__ == '__main__':
    unittest.main()
