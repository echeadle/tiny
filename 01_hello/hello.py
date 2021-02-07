#!/usr/bin/env python3
"""
# Original Author: Ken Youens-Clark <kyclark@gmail.com>
# Purpose: Say hello
"""
import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Program Entry Point"""

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
