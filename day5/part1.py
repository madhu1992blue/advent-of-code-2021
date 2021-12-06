"""Advent of code 2021 - Day 5 - Part 1"""
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Callable, List, Tuple

@dataclass
class OceanFloor:
    """Represents the map of the Ocean Floor."""
    rows: List[List['Cell']]
    def set_cloud_overlap(self, coordinate: 'Point', count: int) -> None:
        """ Update the coordinate with new cell containing the cloud overlap."""
        self.rows[coordinate.y_c][coordinate.x_c] = Cell(count)

    def get_cell(self, coordinate: 'Point') -> 'Cell':
        """Return the cell at the given coordinate."""
        return self.rows[coordinate.y_c][coordinate.x_c]

    def find_cells(self, criteria: Callable[['Cell'], bool])->List['Cell']:
        """Find cells matching criteria."""
        res: List['Cell'] = []
        for row in self.rows:
            res.extend([ele for ele in row if criteria(ele)])
        return res

@dataclass
class Cell:
    """Represents a state of the given point on the ocean floor."""
    cloud_overlap: int

@dataclass
class Point:
    """Represents a point coordinate of the Ocean Floor."""
    x_c: int
    y_c: int



def range_inclusive_increase(first: int, second: int)->range:
    """Generates a range in ascending order for values between first and second."""
    left, right = (first, second+1) if first <= second else (second, first+1)
    return range(left, right)

@dataclass
class LineSegment:
    """Represents a line segment."""
    start: Point
    end: Point

    def points(self)->List[Point]:
        """Generates the list of points included in the line segment."""
        if self.start.x_c == self.end.x_c:
            return [Point(self.start.x_c, y)
                    for y in range_inclusive_increase(self.start.y_c, self.end.y_c)]
        if self.start.y_c == self.end.y_c:
            return [Point(x, self.start.y_c)
                    for x in range_inclusive_increase(self.start.x_c, self.end.x_c)]
        return []

def floor_with_line_spans(
        line_segments: List[LineSegment],
        ocean_floor_x_size: int,
        ocean_floor_y_size: int)->OceanFloor:
    """Creates a Ocean floor with Cells based on scan."""
    new_ocean_floor = OceanFloor([[Cell(0) for _ in range(ocean_floor_x_size+1)]
                                  for _ in range(ocean_floor_y_size+1)])
    for line_segment in line_segments:
        for point in line_segment.points():
            new_ocean_floor.set_cloud_overlap(
                point,
                new_ocean_floor.get_cell(point).cloud_overlap+1
            )
    return new_ocean_floor

def line_segments_from_raw(input_line: str)->LineSegment:
    """Create line segments from raw line input string."""
    def point_raw_to_point(point_raw: str)->'Point':
        raw_split = point_raw.split(",")
        return Point(int(raw_split[0]), int(raw_split[1]))

    start_point_raw, end_point_raw = input_line.split("->")
    start_point = point_raw_to_point(start_point_raw)
    end_point = point_raw_to_point(end_point_raw)
    return LineSegment(start_point, end_point)

def max_x_y(line_segments: List[LineSegment])->Tuple[int, int]:
    """Calculate the max values in the line segments."""
    x_max = max([ele.x_c
                 for ele in reduce(
                     lambda points, segment: points + [segment.start, segment.end],
                     line_segments,
                     initial_points)])
    y_max = max([ele.y_c
                 for ele in reduce(
                     lambda points, segment: points + [segment.start, segment.end],
                     line_segments,
                     initial_points)])
    return x_max, y_max

if __name__ == "__main__":
    with open(Path(__file__).parent/"day5_input") as f:
        ip_line_segments = [line_segments_from_raw(input_line) for input_line in f.readlines()]
        initial_points: List[Point] = []
        max_x, max_y = max_x_y(ip_line_segments)
        ocean_floor = floor_with_line_spans(ip_line_segments, max_x, max_y)
        print(len(ocean_floor.find_cells(lambda cell: cell.cloud_overlap >= 2)))
