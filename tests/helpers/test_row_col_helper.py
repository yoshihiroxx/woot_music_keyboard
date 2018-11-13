import os, sys, unittest

from src.helpers.row_col_helper import key_mat, getMatIdByName, getMatIdByNoteNum, isLeft
import numpy as np
import time

class RowColHelperTest(unittest.TestCase):

    def test_key_mat(self):
        self.assertEqual("SCAN_Pause", key_mat[0][15])
        self.assertEqual("SCAN_NumpadMinus", key_mat[1][20])
        self.assertEqual("SCAN_NumpadPlus", key_mat[2][20])
        self.assertEqual("SCAN_Numpad4", key_mat[3][17])
        self.assertEqual("SCAN_Up", key_mat[4][15])
        self.assertEqual("SCAN_Right", key_mat[5][16])

    def test_getMatIdByName(self):
        start = time.time()
        print(getMatIdByName("Hoge")[0])
        elapsed_time = time.time() -start
        print("elapsed time:{0}". format(elapsed_time) + "[sec]")
        self.assertEqual(getMatIdByName("SCAN_ModifierLeftAlt").tolist(), [5,2])
        self.assertEqual(getMatIdByName("SCAN_NumpadMinus").tolist(), [1,20])
        self.assertEqual(getMatIdByName("SCAN_NumpadPlus").tolist(), [2,20])
        self.assertEqual(getMatIdByName("SCAN_Numpad4").tolist(), [3,17])
        self.assertEqual(getMatIdByName("SCAN_Up").tolist(), [4,15])
        self.assertEqual(getMatIdByName("SCAN_Right").tolist(), [5,16])

    def test_getMatIdByNoteNum(self):
        self.assertEqual(getMatIdByNoteNum(60).tolist(), [[5,2],[1,8]])
        self.assertEqual(getMatIdByNoteNum(48).tolist(), [[3,0]])

    def test_isLeft(self):
        print("TODO")
        self.assertTrue(isLeft(0, 6))
        self.assertTrue(isLeft(1, 5))
        self.assertTrue(isLeft(2, 0))
        self.assertTrue(isLeft(3, 3))
        self.assertTrue(isLeft(4, 6))
        self.assertFalse(isLeft(4, 19))
        self.assertFalse(isLeft(2, 19))

if __name__ == '__main__':
    unittest.main()
