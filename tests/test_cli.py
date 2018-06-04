from unittest import TestCase, main
from unittest.mock import patch
from urllib.error import HTTPError
from src import cli
from tests import mock_data


class TestCli(TestCase):

    def test_get_pr_list(self):
        with patch('src.cli.get_request') as mocked_get:
            mocked_get.return_value = mock_data.get_request_response
            # Test without password
            pr_list = cli.get_pr_list('bookinman', 'test-repo', '')
            mocked_get.assert_called_with(mock_data.get_request_url)
            self.assertEqual(pr_list, mock_data.pr_list_response)
            # Test with password
            pr_list = cli.get_pr_list('bookinman', 'test-repo', 'password')
            mocked_get.assert_called_with(mock_data.get_request_url, mock_data.get_request_auth)
            self.assertEqual(pr_list, mock_data.pr_list_response)

        with self.assertRaises(HTTPError):
            cli.get_pr_list('DoesntExist', 'DoesntExist', '')

    def test_beauty_print(self):
        self.assertEqual(cli.beauty_print(mock_data.beauty_print_parameters), mock_data.beauty_print_response)

        self.assertTrue(type(cli.beauty_print(mock_data.beauty_print_parameters)) is str)


if __name__ == '__main__':
    main()
