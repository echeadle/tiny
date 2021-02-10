#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-09
Purpose: Apples and Bananas: Solution 3
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file", type=str)
    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel(s) allowed",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    trans = str.maketrans("aeiouAEIOU", vowel * 5 + vowel.upper() * 5)
    text = args.text.translate(trans)
    print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
