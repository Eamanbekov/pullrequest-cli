import unittest
from urllib.error import HTTPError, URLError
from src import cli
from tests import mock_data


class TestCli(unittest.TestCase):

    def test_get_id_list(self):
        self.assertEqual(cli.get_id_list('bookinman', 'test-repo'), [3, 1])

        with self.assertRaises(HTTPError):
            cli.get_id_list('DoesntExist', 'DoesntExist')

    def test_get_pr_by_id(self):
        self.assertEqual(cli.get_pr_by_id('bookinman', 'test-repo', 3), mock_data.pr_by_id)

        with self.assertRaises(HTTPError):
            cli.get_pr_by_id('DoesntExist', 'DoesntExist', 0)


if __name__ == '__main__':
    unittest.main()
