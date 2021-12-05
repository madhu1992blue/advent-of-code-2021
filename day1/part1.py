"""Advent of code 2021 - Day 1 - Part 1"""
from typing import List
from pathlib import Path

def increasing_counts(depths: List[int]):
    """Given depths, return the no. of times depths increases from its previous value."""
    count, prev_depth, index = 0, depths[0], 1
    while index != len(depths):
        count = count + 1 if prev_depth < depths[index] else count
        prev_depth = depths[index]
        index = index+1
    return count

if __name__ == "__main__":
    with open(Path(__file__).parent / "day1_input") as f:
        ip_depths = list(map(int, f.readlines()))
        print(increasing_counts(ip_depths))
