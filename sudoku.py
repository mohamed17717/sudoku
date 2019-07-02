
from math import ceil


class Sudoku:
  """ generate and solve sudoku game """

  def __init__ (self):
    self.numClms = 9
    self.numRows = 9

  def createBlankBoard(self):
    """getBlankBoard()

      return:
        9*9 board with blank boxes
    """
    return [[0 for clm in range(self.numClms)] for row in range(self.numRows)]

  def getBlankPoints(self, board):
    """getBlankPoints(board) --> get blank points form a board
    
      Parameters:
        board: 9*9 board
      return:
        indexes of blank points
    """
    blanks = []
    for row in range(self.numRows):
      for clm in range(self.numClms):
        if not board[row][clm]:
          blanks.append( (row, clm) )
    return blanks

  def getPointSquare(self, point):
    """getPointSquare(point)

      Parameter;
        point: (row, clm) : 0 <= row,clm < 9
      Return:
        3*3 square contain this point
    """
    row, clm = point

    row_end = ceil( (row+1) / 3) * 3
    clm_end = ceil( (clm+1) / 3) * 3

    row_start = row_end - 3
    clm_start = clm_end - 3
    
    square = []

    for r in range(row_start, row_end):
      for c in range(clm_start, clm_end):
        square.append( (r,c) )

    return square

  def getRelatedPoints(self, point):
    """getRelatedPoints(point) -->

      Parameters:
        point: (row, clm) : 0 <= row,clm < 9
      Reutrn:
        points with a relation to this specific point
    """
    row, clm = point

    inClm = [(row, i) for i in range(self.numClms)]
    inRow = [(i, clm) for i in range(self.numRows)]
    inSquare = self.getPointSquare(point)

    return set(inRow + inClm + inSquare).remove(point)

  def getLessPosibilityPoint(self, map):
    pass

  def getRemainingChoices(self, board, point):
    choices = [i for i in range(1, self.numRows + 1)]

    relatedPoints = self.getRelatedPoints(point)
    
    # row, clm = point
    # assert not board[row][clm], 'you get choices for a point which is already have value.'

    for relatedPoint in relatedPoints:
      row, clm = relatedPoint
      value = board[row][clm]
      if value:
        choices.remove(value) ## if error happen then its not valid board

    assert choices, 'choices is empty, and this is envalid board'
    return choices

  def createPossibleMap(self, board):
    possibleMap = {}

    blankPoints = self.getBlankPoints(board)
    for point in blankPoints:
      choices = self.getRemainingChoices(board, point)

      possibleMap[point] = {
        'choices': choices,
        'length': len(choices)
      }

    return possibleMap

  def generate(self):
    pass