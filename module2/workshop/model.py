
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
    
    def slide(self, pos: Vec,  dir: Vec)->None:
        """Slide tile at pos.x, pos.y (if any)
        in direction (dir.x, dir.y) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos

    def _move_tile(self, old_pos: Vec, new_pos: Vec)->None:
        # You write this
        if(self.tiles[old_pos.x][old_pos.y] is None):
            return
        
        tile:Tile = self.tiles[old_pos.x][old_pos.y]
        valueTile = tile.value
        self.tiles[old_pos.x][old_pos.y] = None
        newTile:Tile = Tile(new_pos,valueTile)
        self.tiles[new_pos.x][new_pos.y] = newTile
        return

    def right(self):
        
        pass

    def left(self):
        pass

    def down(self):
        pass
    
    def up(self):
        pass
    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME

class TestSlide(unittest.TestCase):

    def test_slide_left_to_edge(self):
        """A tile should stop just when it reaches the edge"""
        board = model.Board()
        board.from_list([[0, 0, 0, 0],
                         [0, 0, 2, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]])
        board.slide(Vec(1, 2), Vec(0, -1))  # Slide the 2 left
        self.assertEqual(board.to_list(),
                         [[0, 0, 0, 0],
                          [2, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])

    def test_slide_right_to_edge(self):
        """A tile should stop just when it reaches the edge"""
        board = model.Board()
        board.from_list([[0, 0, 0, 0],
                         [0, 0, 2, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]])
        board.slide(Vec(1, 2), Vec(0, 1))  # Slide the 2 right
        self.assertEqual(board.to_list(),
                         [[0, 0, 0, 0],
                          [0, 0, 0, 2],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])

    def test_slide_already_at_edge(self):
        """A tile already at the edge can't slide farther that way"""
        board = model.Board()
        board.from_list([[0, 0, 0, 0],
                         [0, 0, 0, 4],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]])
        board.slide(Vec(1, 3), Vec(0, 1))  # To the right
        self.assertEqual(board.to_list(),
                         [[0, 0, 0, 0],
                          [0, 0, 0, 4],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])

    def test_empty_wont_slide(self):
        """Sliding an empty position has no effect"""
        board = model.Board()
        board.from_list([[2, 0, 0, 0],
                         [0, 2, 0, 0],
                         [0, 0, 2, 0],
                         [0, 0, 0, 2]])
        board.slide(Vec(1, 0), Vec(0, 1))  # Space 1,0 is empty
        self.assertEqual(board.to_list(),
                         [[2, 0, 0, 0],
                          [0, 2, 0, 0],
                          [0, 0, 2, 0],
                          [0, 0, 0, 2]])

    def test_slide_into_obstacle(self):
        """A tile should stop when it reaches another tile"""
        board = model.Board()
        board.from_list([[2, 0, 0, 0],
                         [0, 2, 4, 0],
                         [0, 0, 2, 0],
                         [0, 0, 0, 2]])
        board.slide(Vec(1, 1), Vec(0, 1))  # Space 1,0 is empty
        self.assertEqual(board.to_list(),
                         [[2, 0, 0, 0],
                          [0, 2, 4, 0],
                          [0, 0, 2, 0],
                          [0, 0, 0, 2]])
    

TestSlide().test_empty_wont_slide()
TestSlide().test_slide_already_at_edge()
TestSlide().test_slide_into_obstacle()
TestSlide().test_slide_left_to_edge()
TestSlide().test_slide_right_to_edge()


# print(Board(4,5).place_tile())
# print(Board(4,4).tiles)

