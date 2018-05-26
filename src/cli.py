#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Lets you collect all pull requests')
    parser.add_argument('username', type=str, default=1.0,
                        help='Bitbucket username')
    parser.add_argument('repository', type=str, default=1.0,
                        help='Bitbucket repository name')
    parser.add_argument('--password', '-p', type=str, default='password',
                        help='Your bitbucket account password. For private repositories only')
    args = parser.parse_args()
    print('Username: %s\n'
          'Repository: %s\n'
          'Password: %s\n' % (args.username, args.repository, args.password))


if __name__ == '__main__':
    main()
