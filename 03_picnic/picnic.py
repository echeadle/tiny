#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-07
Purpose: Picnic Game
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("item",
                        metavar="str",
                        nargs= '+',
                        help="Item(s) to bring")

    parser.add_argument("-s",
                        "--sorted",
                        help="Sort the items",
                        action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic Program Entry Point"""

    args = get_args()
    flag_arg = args.sorted
    pos_arg = args.item

    print(f'items = "{pos_arg}"')
    print(f'Is list sorted? {flag_arg}')


# --------------------------------------------------
if __name__ == "__main__":
    main()
