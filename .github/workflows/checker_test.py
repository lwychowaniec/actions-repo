import unittest
import bad_commit_message_blocker as checker


class TestCommitChecker(unittest.TestCase):

    def test_detects_review_leftovers(self):
        test_messages = ['cr', 'Cr', 'poprawki po CR', 'wip fancy functionality', 'WIP']
        for message in test_messages:
            with self.subTest():
                self.assertTrue(checker.contains_review_leftover(message))

    def test_cr_and_wip_are_fine_as_part_of_word(self):
        test_messages = ['Add crone', 'CrockAndRoll', 'nowipSense', 'wiproom']
        for message in test_messages:
            with self.subTest():
                self.assertFalse(checker.contains_review_leftover(message))

    def test_detects_too_short_messages(self):
        message = 'short'
        self.assertTrue(checker.is_suspiciously_short(message))

    def test_title_does_not_start_with_capital_letter(self):
        test_messages = ['API-6666: delete all tests',
                         'API-6667:fix sth',
                         'no tags here',
                         'API-5555:No space after colon']
        for message in test_messages:
            with self.subTest():
                self.assertFalse(checker.doesnt_start_with_capital_letter(message))

    def test_title_starts_with_capital_letter(self):
        test_messages = ['API-6666: Im fine',
                         'No tags here']
        for message in test_messages:
            with self.subTest():
                self.assertTrue(checker.doesnt_start_with_capital_letter(message))


    def test_fetch_title(self):
        test_messages = ['API-6666: Commit title',
                         'Commit title']
        for message in test_messages:
            with self.subTest():
                self.assertEqual(checker.fetch_title(message), "Commit title")


if __name__ == '__main__':
    unittest.main()
