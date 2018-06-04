#!/usr/bin/env python3.6
import argparse
from base64 import b64encode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from json import loads
from webbrowser import open_new_tab


BASE_URL = 'https://api.bitbucket.org/2.0/'
REPOS_URL = BASE_URL + 'repositories/'
PR_URL = REPOS_URL + '{0}/{1}/pullrequests/'
QUERY_FILTER = 'q=state="OPEN"+AND+reviewers.username="{0}"'
FIELD_FILTER = 'fields=values.title,values.links.html,values.description,' \
                                      'values.participants.role,' \
                                      'values.participants.approved,values.participants.user.username'
FILTER_URL = PR_URL + '?' + QUERY_FILTER + '&' + FIELD_FILTER


def main():
    parser = argparse.ArgumentParser(description='Lets you collect all pull requests')
    parser.add_argument('username', type=str, default=1.0,
                        help='Bitbucket username')
    parser.add_argument('repository', type=str, default=1.0,
                        help='Bitbucket repository name')
    parser.add_argument('--password', '-p', type=str, default='',
                        help='Your bitbucket account password. For private repositories only')
    parser.add_argument('--browser', '-b', help='Open in browser',
                        action='store_true')
    args = parser.parse_args()
    # Handle some errors
    try:
        pr_list = get_pr_list(args.username, args.repository, args.password)
        if len(pr_list) == 0:
            print('There are no PR assigned to you')
        elif args.browser:
            open_browser(pr_list)
        else:
            print(beauty_print(pr_list))
    except HTTPError:
        if args.password == '':
            print('Wrong username or repository!'
                  'May be this repository is private. Try it with --password option.')
        else:
            print('Wrong username, repository or password!')
    except URLError:
        print('No internet connection!')


def open_browser(pr_list):
    """Opens pullrequest in your default browser"""
    for pr in pr_list:
        open_new_tab(pr['links']['html']['href'])


def beauty_print(pr_list):
    """Function for getting formatted print"""
    result = []
    for pr in pr_list:
        pr_print = \
            '_' * 20, \
            'Title: %s' % pr['title'], \
            'Description: %s' % pr['description'], \
            'Link: %s' % pr['links']['html']['href']
        result.append('\n'.join(pr_print))
    result = '\n'.join(result)
    return result


def get_pr_list(username, repository, password):
    """Gets all pull requests assigned to user"""
    url = FILTER_URL.format(username, repository)
    # Making a request
    if password != '':
        auth = get_auth(username, password)
        data = get_request(url, auth)
    else:
        data = get_request(url)
    # Filtering response
    pr_list = list(filter(lambda pr: any(
        part['role'] == 'REVIEWER' and
        not part['approved'] and
        part['user']['username'] == username
        for part in pr['participants']
    ), data['values']))
    return pr_list


def get_auth(username, password):
    """Returns basic authentication object"""
    auth = '{0}:{1}'.format(username, password)
    auth = b64encode(bytes(auth, 'utf-8'))
    auth = str(auth)[2:-1]
    auth = {'Authorization': 'Basic {0}'.format(auth)}
    return auth


def get_request(url, auth=None):
    """Function for making get requests"""
    if auth:
        request = Request(url, None, auth)
    else:
        request = Request(url)
    data = loads(urlopen(request).read())
    return data


if __name__ == '__main__':
    main()
