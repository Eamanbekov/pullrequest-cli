#!/usr/bin/env python3.6
import argparse
import urllib.request
import urllib.error
import json


BASE_URL = 'https://api.bitbucket.org/2.0/'
REPOS_URL = BASE_URL + 'repositories/'
PR_URL = REPOS_URL + '{0}/{1}/pullrequests/'
OPEN_PR_URL = PR_URL + '?state=OPEN'
PR_ID_URL = PR_URL + '{2}'


def main():
    parser = argparse.ArgumentParser(description='Lets you collect all pull requests')
    parser.add_argument('username', type=str, default=1.0,
                        help='Bitbucket username')
    parser.add_argument('repository', type=str, default=1.0,
                        help='Bitbucket repository name')
    parser.add_argument('--password', '-p', type=str, default='',
                        help='Your bitbucket account password. For private repositories only')
    args = parser.parse_args()
    # Handle some errors
    try:
        id_list = get_id_list(args.username, args.repository)
        pr_list = [
            get_pr_by_id(args.username, args.repository, pr_id)
            for pr_id in id_list
        ]
        pr_list = list(filter(lambda pr: any(
            part['role'] == 'REVIEWER' and
            not part['approved'] and
            part['user']['username'] == args.username
            for part in pr['participants']
        ), pr_list))
        print(beauty_print(pr_list))
    except urllib.error.HTTPError:
        print('Wrong username or repository!')
    except urllib.error.URLError:
        print('No internet connection!')


def beauty_print(pr_list):
    """Function for getting formatted print"""
    result = 'There are no PR assigned to you\n'
    if len(pr_list) != 0:
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


def get_id_list(username, repository):
    """Gets all pull request IDs"""
    url = OPEN_PR_URL.format(username, repository)
    data = get_request(url)
    pr_list = data.get('values')
    id_list = [pr.get('id') for pr in pr_list]
    return id_list


def get_pr_by_id(username, repository, pr_id):
    """Gets detailed info about pull request"""
    url = PR_ID_URL.format(username, repository, pr_id)
    data = get_request(url)
    keys = ['title', 'description', 'participants', 'links']
    data = {key: data[key] for key in keys}
    return data


def get_request(url):
    """Function for making get requests"""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = json.load(response)
    return data


if __name__ == '__main__':
    main()
