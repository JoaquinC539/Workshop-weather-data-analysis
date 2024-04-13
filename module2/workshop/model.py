from datascience import *

"""
The game state and logic (model component) of 512, 
a game based on 2048 with a few changes. 
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event 
notifications to trigger view updates. 
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random as rd
import unittest
import model

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixme:  We need a constructor, and __add__ method, and __eq__.

    def __init__(self, row, column) -> None:
        self.x = row
        self.y = column

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Vec') -> bool:
        return ((self.x == other.x) and (self.y == other.y))

         # pos = Vec(1,2) #
     # We could access a tile as #
    # tile = board.tiles[pos.x][pos.y] #

class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self, pos: Vec, value: int):
        super().__init__()
        self.row = pos.x
        self.col = pos.y
        self.value = value

    def __repr__(self):
        """Not like constructor --- more useful for debugging"""
        return f"Tile[{self.row},{self.col}]:{self.value}"

    def __str__(self):
        return str(self.value)

class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, columns=4):
        super().__init__()
        # FIXME: a grid holds a matrix of tiles
        self.rows = rows
        self.cols = columns
        self.tiles = [ ]
        for i in range(rows):
            row_tiles = [ ]
            for j in range(self.cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles)

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        # FIXME: Should return True if there is some element with value None
        board_list = Board(self.rows, self.cols)._empty_positions()

        if len(board_list) == 0:
            return False
        else:
            return True
    
    def place_tile(self, value=None):
        """Place a tile on a randomly chosen empty square."""
        #FIXME
        empties = self._empty_positions()
        assert len(empties) > 0
        choice = rd.choice(empties)
        row, col = choice.x, choice.y
        if value is None:
            if rd.random() > 0.1:
                value = 4
            else:
                value = 2
        new_tile = Tile(Vec(row, col), value)
        self.tiles[row][col] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))

    def _empty_positions(self) -> list:
        empty = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tiles[i][j] is None:
                    empty.append((Vec(i,j)))
        return empty
                
    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]

    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = [ ]
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result  

    def from_list(self, values: List[List[int]]) -> 'Board':
        """Test scaffolding: set board tiles to the
        given values, where 0 represents an empty space.
        """
        rows = len(values)
        cols = len(values[0])
        result = Board(rows=rows, columns=cols)
        for i in range(rows):
            for j in range(cols):
                result.tiles[i][j] = values[i][j]
        return result
    
    def in_bounds(self, pos: 'Vec') -> bool:
        """Is position (pos.x, pos.y) a legal position on the board?"""
        return (pos.x >= 0 and pos.x < len(self.tiles[0])) and (pos.y >= 0 and pos.y < len(self.tiles))
    
    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME

class TestBoundsCheck(unittest.TestCase):

    def test_bounds_default_shape(self):
        board = model.Board(4,4)
        self.assertTrue(board.in_bounds(Vec(0,0)))
        self.assertTrue(board.in_bounds(Vec(3,3)))
        self.assertTrue(board.in_bounds(Vec(1,2)))
        self.assertTrue(board.in_bounds(Vec(0,3)))
        self.assertFalse(board.in_bounds(Vec(-1,0))) # off the top
        self.assertFalse(board.in_bounds(Vec(1,-1))) # off the left
        self.assertFalse(board.in_bounds(Vec(4,3)))  # off the bottom
        self.assertFalse(board.in_bounds(Vec(1,4)))  # off the right

TestBoundsCheck().test_bounds_default_shape()



# print(Board(4,5).place_tile())
# print(Board(4,4).tiles)

