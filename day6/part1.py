"""Advent of Code 2021 - Day 6 - Part 1"""
from functools import reduce
from pathlib import Path
from typing import Callable, Iterable, List

def update_fish_counts(
        fish_prod_counts_day_wise: List[int],
        new_fish_prod_day_indices: Iterable[int],
        num_fish_per_prod_day: int)->List[int]:
    """Update the fish counts.
    We return a new list and avoid mutation of input array. So, use this API with confidence."""

    new_fish_prod_counts_day_wise = fish_prod_counts_day_wise.copy()
    for day_idx in new_fish_prod_day_indices:
        new_fish_prod_counts_day_wise[day_idx] += num_fish_per_prod_day
    return new_fish_prod_counts_day_wise

def initial_fish_prod_counts_day_wise(initial_timers: Iterable[int], num_days: int)->List[int]:
    """Compute the days on which the initial_timers will produce their offspring."""
    initial_lst_int: List[int] = []
    prod_day_indices_for_timer: Callable[[int], List[int]] =\
         lambda timer: list(range(timer, num_days, 7))
    initial_fish_prod_day_indices: List[int] = reduce(
        lambda lst_till_now, new_lst: lst_till_now+new_lst,
        [
            prod_day_indices_for_timer(timer)
            for timer in initial_timers
        ],
        initial_lst_int
    )
    return initial_fish_prod_day_indices

def prod_days_for_fish_born_on_day_index(day_idx: int, max_num_days: int)->List[int]:
    """Generate the days on which the fish born on day_idx will produce its offspring."""
    return list(range(day_idx+9, max_num_days, 7))

def total_fishes_after_num_days(initial_fish_timers: List[int], num_days: int)->int:
    """Compute the total number of fishes after n days starting with initial_fish_timers."""
    fishes_created_daywise = update_fish_counts(
        [0]*num_days,
        initial_fish_prod_counts_day_wise(initial_fish_timers, num_days),
        1
    )
    for day_idx in range(num_days):
        num_fishes_born_at_day_idx = fishes_created_daywise[day_idx]
        fishes_created_daywise = update_fish_counts(
            fishes_created_daywise,
            prod_days_for_fish_born_on_day_index(day_idx, num_days),
            num_fishes_born_at_day_idx)
    return sum(fishes_created_daywise)+len(list(initial_fish_timers))

if __name__ == "__main__":
    with open(Path(__file__).parent/"day6_input") as f:
        init_fish_timers = list(map(int, f.readline().strip().split(",")))
        NUM_DAYS = 80
        print(total_fishes_after_num_days(init_fish_timers, NUM_DAYS))
