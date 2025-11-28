#!/usr/bin/env python3
"""
mhkji — tiny CLI stub that echoes arguments and supports a few helper flags.

Usage examples:
  py mhkji.py hello world
  py mhkji.py --version

This file is intentionally small and dependency-free so it can serve as a placeholder
until you replace it with a real utility.
"""
import sys
import argparse

VERSION = "0.1.0"

parser = argparse.ArgumentParser(prog="mhkji", description="mhkji - small CLI stub")
parser.add_argument("args", nargs="*", help="Arguments to echo back")
parser.add_argument("-v", "--version", action="store_true", help="Print version and exit")

if __name__ == '__main__':
    ns = parser.parse_args()
    if ns.version:
        print(VERSION)
        sys.exit(0)

    if not ns.args:
        print("mhkji: no args provided — printing usage message:\n")
        parser.print_help()
        sys.exit(1)

    # Example behaviour: echo the arguments and show a small message
    print("mhkji: received arguments ->", " ".join(ns.args))
    # If the user passed a single subcommand, show a friendly stubbed response
    if len(ns.args) == 1 and ns.args[0].lower() == 'jj':
        print("mhkji: you called the 'jj' subcommand — stub executed successfully.")

    sys.exit(0)
