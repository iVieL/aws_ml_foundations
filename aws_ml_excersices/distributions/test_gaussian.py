import unittest
from .gaussian import Gaussian

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result')

    def test_meancalculation(self):
        self.gaussian.read_data_file('../resources/numbers.txt')
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.gaussian.read_data_file('../resources/numbers.txt')
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 92.87, 'sample standard deviation incorrect')
        self.gaussian.read_data_file('../resources/numbers.txt')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 88.55, 'population standard deviation incorrect')


tests = TestGaussianClass()
tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)
unittest.TextTestRunner().run(tests_loaded)