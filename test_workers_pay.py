import unittest
from worker import Worker


class MyTestCase(unittest.TestCase):
    def test_pay_per_day(self):
        w = Worker('Tihomir', 'Tiankov', 40, 30)
        self.assertEqual(w.name, 'Tihomir')  # add assertion here
        self.assertEqual(w.surname, 'Tiankov')


if __name__ == '__main__':
    unittest.main()
