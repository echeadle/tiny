#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str", help="A positional argument")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    pos_arg = args.positional

    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
