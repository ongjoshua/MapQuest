# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../MAPQUEST')

import unittest
import mapquest

class TestMapQuest(unittest.TestCase):

    def test_checkOrigin(self):
        result = mapquest.configLocation('Washington, D.C.', 'Baltimore, Md')
        self.assertEqual(result[0], 'Washington, D.C.')

    def test_checkDestination(self):
        result = mapquest.configLocation('Washington, D.C.', 'Baltimore, Md')
        self.assertEqual(result[1], 'Baltimore, Md')

if __name__ == '__main__':
    unittest.main()
