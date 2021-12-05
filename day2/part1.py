"""Advent of code 2021 - Day 2 - Part 1"""
from typing import Callable, Generator, List
from pathlib import Path
from dataclasses import dataclass

@dataclass
class SubmarineState:
    """Represents the Submarine state"""
    horizontal_pos: int
    depth: int

def on_forward(magnitude: int)->Callable[[SubmarineState], SubmarineState]:
    """Return new state on moving forward."""
    def handler(curr_state: SubmarineState):
        new_horizontal_pos = curr_state.horizontal_pos + magnitude
        new_depth = curr_state.depth
        return SubmarineState(new_horizontal_pos, new_depth)
    return handler

def on_down(magnitude: int)->Callable[[SubmarineState], SubmarineState]:
    """Return new state on moving down."""
    def handler(curr_state: SubmarineState):
        new_horizontal_pos = curr_state.horizontal_pos
        new_depth = curr_state.depth + magnitude
        return SubmarineState(new_horizontal_pos, new_depth)
    return handler

def on_up(magnitude: int)->Callable[[SubmarineState], SubmarineState]:
    """Return new state on moving up."""
    def handler(curr_state: SubmarineState):
        new_horizontal_pos = curr_state.horizontal_pos
        new_horizontal_pos = curr_state.horizontal_pos
        new_depth = curr_state.depth - magnitude
        return SubmarineState(new_horizontal_pos, new_depth)
    return handler


direction_handlers = {
    "up": on_up,
    "down": on_down,
    "forward": on_forward
}


class Submarine:
    """Submarine Object. The submarine can be started with .start()"""

    def __init__(self) -> None:
        self.submarine_state = SubmarineState(0, 0)

    def __handle_movement_event(self, command: str):
        command_parts: List[str] = command.split(" ")
        direction: str = command_parts[0]
        magnitude: int = int(command_parts[1])
        self.submarine_state = direction_handlers[direction](magnitude)(self.submarine_state)

    def start(self)->Generator[None, str, None]:
        """Returns a Generator to which you can send instructions to submarine."""
        while True:
            command: str = yield
            if command == "stop":
                break
            self.__handle_movement_event(command)

    def horizontal_pos(self):
        """Returns the current horizontal postion of the submarine."""
        return self.submarine_state.horizontal_pos

    def depth(self):
        """Returns the current depth of the submarine."""
        return self.submarine_state.depth


with open(Path(__file__).parent / "day2_input") as f:
    instructions = f.readlines()
    submarine = Submarine()
    submarine_channel: Generator[None, str, None] = submarine.start()
    next(submarine_channel)
    for instruction in instructions:
        submarine_channel.send(instruction)
    print(submarine.horizontal_pos()*submarine.depth())
