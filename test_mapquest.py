import unittest
import mapquest

class TestMapQuest(unittest.TestCase):

    def test_checkValidOriginnDest(self):
        result = mapquest.configLocation('Washington, D.C.', 'Baltimore, Md')
        self.assertTrue(len(result[9]))

    def test_checkMissingDest(self):
        result = mapquest.configLocation('Washington, D.C.', '')
        self.assertEqual(result[1], 'Missing an entry for one or both locations.')

    def test_checkSameOriginnDest(self):
        result = mapquest.configLocation('Washington, D.C.', 'Washington, D.C.')
        self.assertTrue(len(result[9]))

    def test_checkUnreachDest(self):
        result = mapquest.configLocation('Manila, Philippines', 'Tokyo Japan')
        self.assertEqual(result[1], 'Invalid user inputs for one or both locations.')

    def test_checkQuit(self):
        result = mapquest.configLocation('q', 'q')
        self.assertIsNone(result)
    # def test_checkDestination(self):
    #     result = mapquest.configLocation('Washington, D.C.', 'Baltimore, Md')
    #     self.assertEqual(result[2], 'Missing an entry for one or both locations.')

    # def test_checkDestination(self):
    #     result = mapquest.configLocation('Washington, D.C.', 'Baltimore, Md')
    #     self.assertEqual(result[1], 'Baltimore, Md')

if __name__ == '__main__':
    unittest.main()
