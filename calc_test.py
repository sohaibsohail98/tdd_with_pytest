import pytest
import unittest2

from calc import *

class Calc_Test(unittest2.TestCase):

    simple_calc = Calc()

    def test_inchtocm(self):
        self.assertEqual(self.simple_calc.inch_cm_values(2), 4)

    def test_cmtoinch(self):
        self.assertEqual(self.simple_calc.cm_inch_values(3), 2)