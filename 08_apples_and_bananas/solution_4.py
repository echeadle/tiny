#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-09
Purpose: Apples and Bananas: Solution 4  List Comprehension
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
    """Program entry point"""
    args = get_args()
    vowel = args.vowel
    text = [
        vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
        for c in args.text
    ]
    print(''.join(text))


# --------------------------------------------------
if __name__ == "__main__":
    main()
