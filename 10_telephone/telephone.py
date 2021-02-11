#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-10
Purpose: Telephone Game
"""

import argparse
import os
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="seed",
        type=int,
        default=None,
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text.read().rstrip())

    return args


# --------------------------------------------------
def main():
    """ Main program entry point """

    args = get_args()


# --------------------------------------------------
if __name__ == "__main__":
    main()
