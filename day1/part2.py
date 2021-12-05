"""Advent of code 2021 - Day 1 - Part 2"""
from typing import List
from pathlib import Path

def increasing_window_sum_depths(depths: List[int], win_size: int):
    """ Returns the no. of times window sum increased from previous window sum."""
    previous_window_sum: int = sum(depths[0:win_size])
    window_start = 1
    count = 0
    while window_start + win_size <= len(depths):
        window_end = window_start + win_size - 1
        curr_window_sum = previous_window_sum - depths[window_start-1] + depths[window_end]
        count = count + 1 if curr_window_sum > previous_window_sum else count
        previous_window_sum = curr_window_sum
        window_start += 1
    return count

if __name__ == "__main__":
    with open(Path(__file__).parent / "day1_input") as f:
        ip_depths = list(map(int, f.readlines()))
        print(increasing_window_sum_depths(ip_depths, 3))
        
