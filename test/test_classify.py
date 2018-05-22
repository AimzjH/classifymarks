#!/usr/bin/env python3

import unittest
import classify
import sys


class Test(unittest.TestCase):
	def test_ResultLength(self):
		length = 10
		result = classify.getData(fname)
		self.assertEqual(len(result),length)
if __name__=='__main__':
	fname = open(sys.argv[1])
	print(fname)
	unittest.main()
