#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-02-10
Purpose: Curse Generator
 In this program, you will learn to
   Use parser.error() from argparse to throw errors
   Control randomness with random seeds
   Take random choices and samples from Python lists
   Iterate an algorithm a specified number of times with a for loop
   Format output strings
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap Abuse", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--insults",
        help="Number of insults",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s",
        "--seed",
        metavar="seed",
        help="Random seed",
        type=int,
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program Entry point"""

    args = get_args()
    random.seed(args.seed)

    adjectives = """
        bankrupt base caterwauling corrupt cullionly detestable dishonest false
        filthsome filthy foolish foul gross heedless indistinguishable infected
        insatiate irksome lascivious lecherous loathsome lubbery old peevish
        rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
        thin-faced toad-spotted unmannered vile wall-eyed
        """.strip().split()

    nouns = """
        Judas Satan ape ass barbermonger beggar block boy braggart butt
        carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
        gull harpy jack jolthead knave liar lunatic maw milksop minion
        ratcatcher recreant rogue scold slave swine traitor varlet villain worm
        """.strip().split()


# --------------------------------------------------
if __name__ == "__main__":
    main()
