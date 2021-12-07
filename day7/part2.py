"""Advent of Code 2021 - Day 7 - Part 2"""
from pathlib import Path
from typing import List

def fuel_consumed_for_num_steps(num: int)->int:
    """Fuel consumed by a crab for taking n steps."""
    # 1+2+3+....num = num*(num+1)/2
    return num*(num+1)//2

def fuel_consumed_for_crab_positions_to_reach_target_pos(
        crab_positions: List[int],
        target_pos: int)->int:
    """Returns the total fuel consumption for crabs
    at crab_positions to reach the target_pos."""

    def num_steps_taken_to_reach_target(crab_pos: int):
        return abs(target_pos - crab_pos)

    return sum([
        fuel_consumed_for_num_steps(num_steps_taken_to_reach_target(crab_pos))
        for crab_pos in crab_positions
    ])

def cheapest_fuel_consumption_to_align(crab_positions: List[int])->int:
    """Returns the least fuel consumed to align the crab positions."""
    return min([
        fuel_consumed_for_crab_positions_to_reach_target_pos(crab_positions, pos)
        for pos in range(min(crab_positions), max(crab_positions)+1)
    ])

if __name__ == "__main__":
    with open(Path(__file__).parent/"day7_input") as f:
        ip_crab_positions = list(map(int, f.readline().strip().split(",")))
        print(cheapest_fuel_consumption_to_align(ip_crab_positions))
