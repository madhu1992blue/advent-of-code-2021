"""Advent of code 2021 - Day 4 - Part 1"""
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, List, Optional, Tuple, TypeVar

@dataclass
class Board:
    """Board Data class."""
    rows: List[List['Cell']]

    def __get_pos(self, num: int)->Optional[Tuple[int, int]]:
        for row_num, row in enumerate(self.rows):
            for col_num, ele in enumerate(row):
                if ele.value == num:
                    return row_num, col_num
        return None

    def mark_num(self, num: int)->'Board':
        """Creates a new board with the current number marked."""
        coordinates = self.__get_pos(num)
        if coordinates is None:
            return self
        row_idx, _ = coordinates
        return Board([
            (row if row != self.rows[row_idx] else \
            [(ele if ele.value != num else Cell(num, True)) for ele in row])
            for row in self.rows
        ])

    def __col_won(self, col: int)->bool:
        for row in self.rows:
            if not row[col].marked:
                return False
        return True

    def __row_won(self, row_num: int)->bool:
        return all([ele.marked for ele in self.rows[row_num]])

    def has_won(self)->bool:
        """Determines if a board has won."""
        return \
            any([self.__row_won(row_num) for row_num in range(len(self.rows))]) or \
            any([self.__col_won(col_num) for col_num in range(len(self.rows[0]))])

    def unmarked(self)->List[int]:
        """Provides a list of all unmarked values in a board."""
        res: List[int] = []
        for row in self.rows:
            res.extend([ele.value for ele in row if not ele.marked])
        return res

@dataclass
class Cell:
    """Cell representing the board cell."""
    value: int
    marked: bool

def cells_from_line_bounds(input_lines: List[str], start_line_num: int, end_line_num: int):
    """Creates a matrix of cells for the board from input lines, start line num and end line num.
    end_line_num is an excluded bound"""
    return [[Cell(int(ele), False) for ele in line.strip().split(" ") if ele != ""]
            for line in input_lines[start_line_num : end_line_num]]

def parse_input(input_lines: List[str])->Tuple[Iterable[int], Iterable[Board]]:
    """Parses input and returns the numbers called and the list of boards."""
    numbers_called = map(int, input_lines[0].strip().split(","))
    num_lines = 5
    boards = [
        Board(
            cells_from_line_bounds(input_lines, start_line_num, start_line_num + num_lines)
        )
        for start_line_num in range(2, len(input_lines), 6)
    ]
    return numbers_called, boards


TV = TypeVar("TV")
def find_first(a_s: Iterable[TV], pred: Callable[[TV], bool])->Optional[TV]:
    """Determines the first ele of the iterable which matches the predicate, pred."""
    for ele in a_s:
        if pred(ele):
            return ele
    return None

def first_winner_and_last_num(
        boards: Iterable[Board], numbers_called: Iterable[int]
    )->Optional[Tuple[Board, int]]:
    """Determines the first winner and last num that created the winner."""
    for num in numbers_called:
        boards = [board.mark_num(num) for board in boards]
        winner_board = find_first(boards, lambda board: board.has_won())
        if winner_board is not None:
            return winner_board, num
    return None

with open(Path(__file__).parent / "day4_input") as f:
    ip_lines = f.readlines()
    ip_boards: Iterable[Board]
    ip_numbers_called: Iterable[int]
    ip_numbers_called, ip_boards = parse_input(ip_lines)
    earliest_winner_last_num = first_winner_and_last_num(ip_boards, ip_numbers_called)
    if earliest_winner_last_num is not None:
        earliest_winner, last_num = earliest_winner_last_num
        print(sum(earliest_winner.unmarked())*last_num)
