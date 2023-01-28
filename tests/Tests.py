import unittest
import TxRxModul as modul
import numpy as np

class TestStartStopSymbol(unittest.TestCase):
    def test_StartStopSymbol(self):
        self.assertEqual(modul.StartStopSymbol(2), ("##", '~~'), "Should be ## and ~~")

    def test_StartStopSymbol(self):
        self.assertEqual(modul.StartStopSymbol(8), ("~", '/'), "Should be ~ and /")

class TestToDec(unittest.TestCase):
    def test_ToDecimal(self):
        self.assertEqual(modul.ToDecimal([0,2,0,3], 3, 4), 35, "Should be 35")

class TestNormovani(unittest.TestCase):
    def test_NormReal(self):
        proNorm = np.array((1+1j,2+2j))
        proPorovnani = np.array((0.5+0.5j,1+1j))
        norm = modul.NormovaniReal(proNorm)
        self.assertTrue((norm == proPorovnani).all(), "Should be True")       

if __name__ == '__main__':
    unittest.main()