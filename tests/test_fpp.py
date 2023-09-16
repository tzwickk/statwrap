import unittest
from statwrap.fpp import *

class TestStd(unittest.TestCase):

	def setUp(self):
		self.numbers = [-1,0,1]
		self.df = pd.DataFrame('col1': self.numbers)

	def test_sd(self):
		sd_ = sd(self.numbers)
		self.assertFalse(sd_ == 1)
		apply_pd_changes()
		self.assertTrue(self.df.col1.sd() == sd_)

	def tearDown(self):
		pass