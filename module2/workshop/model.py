
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
    
    def merge(self, other: "Tile"):
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile.
        other.notify_all(GameEvent(EventKind.tile_removed, other))

class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        # FIXME: a grid holds a matrix of tiles
        self.rows = rows
        self.cols = cols
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
                    tile:Tile=col
                    row_values.append(tile.value) #<-------FIXME
            result.append(row_values)
        return result  

    def from_list(self, values: List[List[int]]) -> 'Board':
        """Test scaffolding: set board tiles to the
        given values, where 0 represents an empty space.
        """
        rows = len(values)
        cols = len(values[0])
        result = Board(rows, cols)
        for i in range(rows):
            for j in range(cols):
                vec:Vec=Vec(i,j)
                value=values[i][j]
                tile:Tile=Tile(vec,value)                
                result.tiles[i][j] = tile
        return result
    
    def in_bounds(self, pos: 'Vec') -> bool:
        """Is position (pos.x, pos.y) a legal position on the board?"""
        return (pos.x >= 0 and pos.x <=  len(self.tiles)-1) and (pos.y >= 0 and pos.y <= len(self.tiles[0])-1)
    
    '''
    [--------------> y
    [None, None, None, None]    ^
    [None, None, None, None]    x
    ]                           |
    '''

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
        rowIndex:int=0
        for row in self.tiles:
            for i in range(len(row),-1,-1):                
                vector = Vec(rowIndex,i)
                tile:Tile=self.tiles[vector.x,vector.y]
                if not (tile is None):
                    direction=Vec(rowIndex,len(row)-1)                
                    self.slide(vector, direction)   
            rowIndex += 1
        return

    def left(self):
        rowIndex:int=0
        for row in self.tiles:
            for i in range(len(row)):                
                vector = Vec(rowIndex,i)
                tile:Tile=self.tiles[vector.x,vector.y]
                if not (tile is None):
                    direction=Vec(rowIndex,len(row)-1)                
                    self.slide(vector, direction)   
            rowIndex += 1
        return

    def down(self):
        """ [ c <-------------------
            [None, None, None , None] r
            [None, None, None , None] ^
            [None, None, None , None] |
            [None, None, None , None] |
            [None, None, None , None] |
            ]
        """

        lastRowIndex:int = len(self.tiles) - 1
        for c in range(len(self.tiles[0]),-1,-1):
            for r in range(lastRowIndex, -1, -1):
                vector:Vec = Vec(c,r)
                tile:Tile = self.tiles[vector.x,vector.y]
                if not (tile is None):
                    direction:Vec = Vec(c,lastRowIndex)                    
                    self.slide(vector,direction)
        return
    
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

        
board:Board=Board()
as_list = [[0, 2, 2, 4], [2, 0, 2, 8], [8, 2, 2, 4], [4, 2, 2, 0]]

class TestScaffolding(unittest.TestCase):

    def test_to_from_list(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        as_list = [[0, 2, 2, 4], [2, 0, 2, 8], [8, 2, 2, 4], [4, 2, 2, 0]]
        board2=board.from_list(as_list) #<------Error FIXME
        self.assertEqual(board.to_list(), as_list)

    def test_from_to(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        board.place_tile()
        board.place_tile(value=32)
        board.place_tile()
        as_list = board.to_list()
        board.from_list(as_list)
        again = board.to_list()
        self.assertEqual(as_list, again)

print(TestScaffolding().test_to_from_list())        

# board:Board=Board(4, 4)
# # x:List[List[int]] = board.tiles
# y = [[0, 2, 2, 4], [2, 0, 2, 8], [8, 2, 2, 4], [4, 2, 2, 0]]
# board2=board.from_list(y)
# print(board2)
# print(type(board2.to_list()))

# class TestBoundsCheck(unittest.TestCase):

#     def test_bounds_default_shape(self):
#         board = model.Board()
#         self.assertTrue(board.in_bounds(Vec(0,0)))
#         self.assertTrue(board.in_bounds(Vec(3,3)))
#         self.assertTrue(board.in_bounds(Vec(1,2)))
#         self.assertTrue(board.in_bounds(Vec(0,3)))
#         self.assertFalse(board.in_bounds(Vec(-1,0))) # off the top
#         self.assertFalse(board.in_bounds(Vec(1,-1))) # off the left
#         self.assertFalse(board.in_bounds(Vec(4,3)))  # off the bottom
#         self.assertFalse(board.in_bounds(Vec(1,4)))  # off the right

#     def test_bounds_odd_shape(self):
#         """Non-square board to make sure we're using row and column
#         correctly.
#         """
#         board = model.Board(rows=2,cols=4)
#         self.assertTrue(board.in_bounds(Vec(0,0)))
#         self.assertTrue(board.in_bounds(Vec(1,3)))
#         self.assertFalse(board.in_bounds(Vec(3,1)))

# print(TestBoundsCheck().test_bounds_odd_shape())
# board = Board(rows=2,cols=4)
# print(board.to_list())
# class TestSlide(unittest.TestCase):

#     def test_slide_left_to_edge(self):
#         """A tile should stop just when it reaches the edge"""
#         board = model.Board()
#         board2= board.from_list([[0, 0, 0, 0],
#                          [0, 0, 2, 0],
#                          [0, 0, 0, 0],
#                          [0, 0, 0, 0]])
#         board2.slide(Vec(1, 2), Vec(1, 0))  # Slide the 2 left
#         board2.to_list() == [[0, 0, 0, 0],
#                           [2, 0, 0, 0],
#                           [0, 0, 0, 0],
#                           [0, 0, 0, 0]]
                         

    # def test_slide_right_to_edge(self):
    #     """A tile should stop just when it reaches the edge"""
    #     board = model.Board()
    #     board.from_list([[0, 0, 0, 0],
    #                      [0, 0, 2, 0],
    #                      [0, 0, 0, 0],
    #                      [0, 0, 0, 0]])
    #     board.slide(Vec(1, 2), Vec(0, 1))  # Slide the 2 right
    #     self.assertEqual(board.to_list(),
    #                      [[0, 0, 0, 0],
    #                       [0, 0, 0, 2],
    #                       [0, 0, 0, 0],
    #                       [0, 0, 0, 0]])

    # def test_slide_already_at_edge(self):
    #     """A tile already at the edge can't slide farther that way"""
    #     board = model.Board()
    #     board.from_list([[0, 0, 0, 0],
    #                      [0, 0, 0, 4],
    #                      [0, 0, 0, 0],
    #                      [0, 0, 0, 0]])
    #     board.slide(Vec(1, 3), Vec(0, 1))  # To the right
    #     self.assertEqual(board.to_list(),
    #                      [[0, 0, 0, 0],
    #                       [0, 0, 0, 4],
    #                       [0, 0, 0, 0],
    #                       [0, 0, 0, 0]])

    # def test_empty_wont_slide(self):
    #     """Sliding an empty position has no effect"""
    #     board = model.Board()
    #     board.from_list([[2, 0, 0, 0],
    #                      [0, 2, 0, 0],
    #                      [0, 0, 2, 0],
    #                      [0, 0, 0, 2]])
    #     board.slide(Vec(1, 0), Vec(0, 1))  # Space 1,0 is empty
    #     self.assertEqual(board.to_list(),
    #                      [[2, 0, 0, 0],
    #                       [0, 2, 0, 0],
    #                       [0, 0, 2, 0],
    #                       [0, 0, 0, 2]])

    # def test_slide_into_obstacle(self):
    #     """A tile should stop when it reaches another tile"""
    #     board = model.Board()
    #     board.from_list([[2, 0, 0, 0],
    #                      [0, 2, 4, 0],
    #                      [0, 0, 2, 0],
    #                      [0, 0, 0, 2]])
    #     board.slide(Vec(1, 1), Vec(0, 1))  # Space 1,0 is empty
    #     self.assertEqual(board.to_list(),
    #                      [[2, 0, 0, 0],
    #                       [0, 2, 4, 0],
    #                       [0, 0, 2, 0],
    #                       [0, 0, 0, 2]])
    

# TestSlide().test_empty_wont_slide()
# TestSlide().test_slide_already_at_edge()
# TestSlide().test_slide_into_obstacle()
# TestSlide().test_slide_left_to_edge()
# TestSlide().test_slide_right_to_edge()


# print(Board(4,5).place_tile())
# print(Board(4,4).tiles)
