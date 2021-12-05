"""Advent of code - Day 3 - Part 2"""
from pathlib import Path
from typing import List

def to_decimal(binary: str)->int:
    """Returns a decimal for a given binary string."""
    decimal = 0
    for ele in binary:
        decimal = decimal*2 + int(ele)
    return decimal

def gen_rating(diagnostics: List[str], invert_significant: bool):
    """Generate rating for diagnostics, val when no. 0s lte no. of 1s and
    val when no. of 0s > no. of 1s"""
    def next_diagnostics(diagnostics: List[str], bit_pos: int):
        zeros = sum([1 for diag in diagnostics if diag[bit_pos] == "0"])
        ones = len(diagnostics) - zeros
        most_significant = "0" if invert_significant else "1"
        least_significant = "1" if invert_significant else "0"
        if zeros <= ones:
            return [diag for diag in diagnostics if diag[bit_pos] == most_significant]
        return [diag for diag in diagnostics if diag[bit_pos] == least_significant]

    bit_pos = 0
    while len(diagnostics) != 1:
        diagnostics = next_diagnostics(diagnostics, bit_pos)
        bit_pos = bit_pos + 1
    return diagnostics[0]


def co2_scrubber_rating(diagnostics: List[str])->str:
    """Gives the CO2 scrubber rating."""
    return gen_rating(diagnostics, True)

def o2_gen_rating(diagnostics: List[str]):
    """Gives the O2 scrubber rating."""
    return gen_rating(diagnostics, False)


with open(Path(__file__).parent / "day3_input") as f:
    ip_diagnostics = list(map(lambda line: line.strip(), f.readlines()))
    print(to_decimal(o2_gen_rating(ip_diagnostics))*to_decimal(co2_scrubber_rating(ip_diagnostics)))
