#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-09
Purpose: Lookup tables
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "letter", nargs="+", metavar="letter", help="Letter(s)", type=str
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program Entry Point"""

    args = get_args()

    lookup = {}
    lookup = {line[0].upper(): line.rstrip() for line in args.file}
   # for line in args.file:
   #     lookup[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
