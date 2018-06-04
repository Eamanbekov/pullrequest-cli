import unittest
from urllib.error import HTTPError, URLError
from src import cli
from tests import mock_data


class TestCli(unittest.TestCase):

    def test_get_pr_list(self):
        self.assertEqual(cli.get_pr_list('bookinman', 'test-repo', ''), mock_data.pr_list_response)

    def test_get_id_list(self):
        self.assertEqual(cli.get_id_list('bookinman', 'test-repo', ''), [3, 1])

        with self.assertRaises(HTTPError):
            cli.get_id_list('DoesntExist', 'DoesntExist', '')

    def test_get_pr_by_id(self):
        self.assertEqual(cli.get_pr_by_id('bookinman', 'test-repo', 3, ''), mock_data.pr_by_id_response)

        with self.assertRaises(HTTPError):
            cli.get_pr_by_id('DoesntExist', 'DoesntExist', 0, '')

    def test_beauty_print(self):
        self.assertEqual(cli.beauty_print(mock_data.beauty_print_parameters), mock_data.beauty_print_response)

        self.assertTrue(type(cli.beauty_print(mock_data.beauty_print_parameters)) is str)


if __name__ == '__main__':
    unittest.main()
