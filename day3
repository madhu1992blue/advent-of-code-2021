"""Advent of code 2021 - Day 3 - Part 1"""
from typing import List, Tuple
from functools import reduce
from pathlib import Path

def bin_to_decimal(binary_str: str)->int:
    """Convert a given binary string to Decimal number."""
    decimal = 0
    for ele in binary_str:
        decimal = decimal*2 + int(ele)
    return decimal

def gamma_epsilon_bit(zeros: int, ones: int)->Tuple[str, str]:
    """Return the gamma and epsilon bits based on number of zeros and number of ones."""
    if zeros < ones:
        return "1", "0"
    return "0", "1"

def zeros_and_ones(diagnostics: List[str], bit_pos: int)->Tuple[int, int]:
    """Return a tuple which contains the no. of zeros and no. of ones at the given bit pos
    across all diagnostics."""
    def update_zeros_and_ones(zeros_ones: Tuple[int, int], diagnostic: str):
        zeros, ones = zeros_ones
        if diagnostic[bit_pos] == "0":
            return zeros + 1, ones
        return zeros, ones + 1
    return reduce(update_zeros_and_ones, diagnostics, (0, 0))

def gamma_epsilon(diagnostics: List[str])->Tuple[str, str]:
    """ Computes the full gamma and epsilon values for the diagnostics. """
    num_bits: int = len(diagnostics[0])
    gamma = "0"*num_bits
    epsilon = "0"*num_bits
    for bit_pos in range(num_bits):
        zeros, ones = zeros_and_ones(diagnostics, bit_pos)
        gamma_bit, epsilon_bit = gamma_epsilon_bit(zeros, ones)
        gamma += gamma_bit
        epsilon += epsilon_bit
    return gamma, epsilon

with open(Path(__file__).parent / "day3_input") as f:
    ip_diagnostics = list(map(lambda s: s.strip(), f.readlines()))
    op_gamma, op_epsilon = gamma_epsilon(ip_diagnostics)
    print(bin_to_decimal(op_gamma)*bin_to_decimal(op_epsilon))
