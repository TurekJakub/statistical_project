#!/usr/bin/env python3

from regular import perform_regular_season_tests
from playoff import perform_playoff_tests

def main():
    print("=== Test results ===", end="\n\n")
    print("=== Regular season ===", end="\n\n")

    perform_regular_season_tests()

    print("\n=== Play off ===", end="\n\n")

    perform_playoff_tests()

main()