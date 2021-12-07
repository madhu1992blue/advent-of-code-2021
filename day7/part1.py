"""Advent of Code 2021 - Day 7 - Part 1"""
from pathlib import Path
from typing import List

def cheapest_fuel_consumption_to_align(crab_positions: List[int])->int:
    """Returns the least fuel consumed to align the crab positions."""
    # A web search for "minimize absolute sum of differences"
    # revealed that the median does precisely that.
    # It might be useful to align everything towards the median value.
    median_crab_pos = sorted(crab_positions)[len(crab_positions)//2]
    fuel_needed_by_crabs_to_move_to_median_pos =\
        [abs(median_crab_pos - crab_pos) for crab_pos in crab_positions]
    return sum(fuel_needed_by_crabs_to_move_to_median_pos)

if __name__ == "__main__":
    with open(Path(__file__).parent/"day7_input") as f:
        ip_crab_positions = list(map(int, f.readline().strip().split(",")))
        print(cheapest_fuel_consumption_to_align(ip_crab_positions))
