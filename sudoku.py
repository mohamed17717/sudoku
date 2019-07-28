
from math import ceil
import random

class Board:
  """ Contain abstracted methods """
  numClms = 9
  numRows = 9
  blank = 0

  def createBlankBoard(self):
    """getBlankBoard()

      return:
        9*9 board with blank boxes
    """
    return [[self.blank for clm in range(self.numClms)] for row in range(self.numRows)]

  def getPointRow(self, point):
    row, clm = point
    return [(row, clm) for clm in range(self.numClms)]

  def getPointClm(self, point):
    row, clm = point
    return [(row, clm) for row in range(self.numRows)]

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

    inClm = self.getPointClm(point)
    inRow = self.getPointRow(point)
    inSquare = self.getPointSquare(point)

    relatedPoints = set(inRow + inClm + inSquare)
    relatedPoints.remove(point)

    return relatedPoints

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
        if board[row][clm] == self.blank:
          blanks.append( (row, clm) )
    return blanks

  def getBoardRows(self, board):
    rows = board
    return rows

  def getBoardClms(self, board):
    clms = [[] for i in range(len(board[0]))]
    for row in board:
      for i, clm in enumerate(row):
        clms[i].append(clm)
    return clms

  def getBoardSquares(self, board):
    squares = []

    # index for all middle points always changes between those 3 nums
    # ex: (1,1) (1,4) (1,7) (4,1) etc...
    x = [1, 4, 7]
    for i in x:
      for j in x:
        middleSquareIndex = (i , j)
        # convert the point to its value
        square = []
        for point in self.getPointSquare(middleSquareIndex):
          row,clm = point
          square.append(board[row][clm])
        squares.append(square)
    return squares


class SudokuValidation(Board):
  def checkRules(self, arr):
    minimum = min(arr) == 1
    maximum = max(arr) == 9
    summition = sum(arr) == 45
    length = len(set(arr)) == len(arr) == 9
    return all([minimum, maximum, summition, length])

  def checkLoop(self, items):
    for item in items:
      if not self.checkRules(item): 
        return False
    return True

  def validateBoard(self, board):
    # validate rows
    for func in [self.getBoardRows, self.getBoardClms, self.getBoardSquares]:
      items = func(board)
      if not self.checkLoop(items): return False
    return True


class Sudoku (SudokuValidation):
  """ generate and solve sudoku game """

  def getRemainingChoices(self, board, point):
    choices = list(range(1, self.numRows + 1))

    relatedPoints = self.getRelatedPoints(point)

    for relatedPoint in relatedPoints:
      row, clm = relatedPoint
      value = board[row][clm]
      if value in choices:
        choices.remove(value)

    assert choices, 'choices is empty, and this is invalid board'
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

  def getLessPosibilityPoint(self, possibleMap):
    point = None
    possible = 10

    for p, value in possibleMap.items():
      pPossibles = value['length']
      assert pPossibles != 0, 'possible some where === 0, its invalid board'
      
      if pPossibles < possible:
        point = p
        possible = pPossibles
    
    return point

  def affectRelatedPoints(self, possibleMap, point, number):
    relatedPoints = self.getRelatedPoints(point)
    for relatedPoint in relatedPoints:
      data = possibleMap.get(relatedPoint)
      try:
        data['choices'].remove(number)
        data['length'] -= 1
        possibleMap[relatedPoint] = data
      except: pass
    return possibleMap

  def generateBoard(self):
    board = self.createBlankBoard()
    possibleMap = self.createPossibleMap(board)

    try:
      for i in range(len(possibleMap)):
        point = self.getLessPosibilityPoint(possibleMap)
        value = possibleMap.pop(point)
        choice = random.choice(value['choices'])

        row, clm = point
        board[row][clm] = choice

        possibleMap = self.affectRelatedPoints(possibleMap, point, choice)
    except: return self.generateBoard()
    return board

  def generateGame(self, blankNum):
    assert blankNum <= 50, 'max blank points is 50'
    board = self.generateBoard()

    for i in range(blankNum):
      row, clm = random.randint(1, 9)-1, random.randint(1, 9)-1
      board[row][clm] = 0
    
    try : 
      b = [i.copy() for i in board]
      self.solveBoard(b)
    except: 
      return self.generateGame(blankNum)

    return board

  def solveBoard(self, board):
    possibleMap = self.createPossibleMap(board)

    for i in range(len(possibleMap)):
      point = self.getLessPosibilityPoint(possibleMap)
      value = possibleMap.pop(point)
      choice = random.choice(value['choices'])

      row, clm = point
      board[row][clm] = choice

      possibleMap = self.affectRelatedPoints(possibleMap, point, choice)

    return board

if __name__ == '__main__':
  from pprint import pprint
  sudoku = Sudoku()
  game = sudoku.generateGame(blankNum=50)
  pprint(game)

  solved = sudoku.solveBoard(game)
  pprint(solved)

  v = SudokuValidation()
  print(f'valid: {v.validateBoard(solved)}')
