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
