#!/usr/bin/env python3

import unittest
import classify
import sys


class Test(unittest.TestCase):
	def test_Candidates(self):
		data = [['AC008128', 71], ['AC019221', 73], ['AB018281', 34], ['AC901913', 24], ['AB023000', 55], ['AB040731', 56], ['AC001001', 54], ['AC008128', 72], ['AC019221', 74], ['AB617113', 89]]
		tCandidates = classify.testRanges(data)
		expectedCandidates = ['AC008128','AC019221','AB018281','AC901913','AB023000','AB040731','AC001001','AC008128','AC019221','AB617113']
		self.assertEqual(tCandidates, expectedCandidates)
		
if __name__=='__main__':
	unittest.main()
