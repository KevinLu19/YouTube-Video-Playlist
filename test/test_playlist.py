import unittest

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.test_queue_collection = []
        self.test_front_data = 0          # First element of the queue.
        self.test_size = 0                # Current elements inside of the list.
