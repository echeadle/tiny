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

    parser.add_argument("item", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic Program Entry Point"""

    args = get_args()
    items = args.item
    num_items = len(items)

    if args.sorted:
        items.sort()

    bringing = ""
    if num_items == 1:
        bringing = items[0]
    elif num_items == 2:
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")
    # print(f'items = "{items}"')
    # print(f"Is list sorted? {args.sorted}")
    # print(f'Number of items in list: {num_items}')


# --------------------------------------------------
if __name__ == "__main__":
    main()
