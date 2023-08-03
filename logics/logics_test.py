from collections import Counter, defaultdict
import unittest

from logics import prepare_post

class Test_prepare_post(unittest.TestCase):
    fake_archive = defaultdict(Counter)
    fake_archive["hi"]["my"] = 1
    fake_archive["my"]["dear"] = 2
    fake_archive["dear"]["friend"] = 3

    empty_archive = defaultdict(Counter)
    
    def test_empty_archive(self):
        reply = prepare_post(self.empty_archive, 0)
        self.assertEqual(reply, "empty archive")

    def test_create_post_success(self):
        reply = prepare_post(self.fake_archive, 4)
        self.assertEqual(reply, "hi my dear friend")

if __name__ == '__main__':
    unittest.main()