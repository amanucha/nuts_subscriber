import unittest
from service.processor import MessageProcessor

class TestMessageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = MessageProcessor()

    def test_valid_message(self):
        self.processor.validate_and_save("Test message")
        count = self.processor.db.count_messages()
        self.assertGreaterEqual(count, 1)

    def test_empty_message(self):
        self.processor.validate_and_save("  ")
        # Should not be saved; no exception = pass

    def test_duplicate(self):
        msg = "Duplicate test"
        self.processor.validate_and_save(msg)
        before = self.processor.db.count_messages()
        self.processor.validate_and_save(msg)
        after = self.processor.db.count_messages()
        self.assertEqual(before, after)

    def tearDown(self):
        self.processor.shutdown()

if __name__ == "__main__":
    unittest.main()

