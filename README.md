# Sudoku

Classes that help in create sudoku game, solve or validate.

## Getting Started

### Prerequisites

- [Python3.6](https://www.python.org/downloads/) or later

## Running

### example of the output

``` python
>>> from pprint import pprint
>>> sudoku = Sudoku()
>>> game = sudoku.generateGame(blankNum=50)
>>> pprint(game)
[[0, 0, 0, 0, 3, 0, 0, 1, 0],
 [0, 0, 0, 4, 6, 9, 0, 0, 5],
 [0, 3, 6, 7, 0, 0, 0, 0, 0],
 [0, 5, 2, 1, 4, 8, 9, 6, 0],
 [8, 6, 4, 9, 7, 0, 1, 5, 2],
 [7, 0, 1, 2, 5, 6, 0, 0, 4],
 [2, 8, 3, 6, 9, 4, 0, 7, 1],
 [9, 0, 0, 5, 8, 1, 0, 2, 3],
 [6, 0, 5, 0, 0, 0, 0, 4, 0]]
>>> solved = sudoku.solveBoard(game)
>>> pprint(solved)
[[0, 0, 0, 0, 3, 0, 0, 1, 0],
 [0, 0, 0, 4, 6, 9, 0, 0, 5],
 [0, 3, 6, 7, 0, 0, 0, 0, 0],
 [0, 5, 2, 1, 4, 8, 9, 6, 0],
 [8, 6, 4, 9, 7, 0, 1, 5, 2],
 [7, 0, 1, 2, 5, 6, 0, 0, 4],
 [2, 8, 3, 6, 9, 4, 0, 7, 1],
 [9, 0, 0, 5, 8, 1, 0, 2, 3],
 [6, 0, 5, 0, 0, 0, 0, 4, 0]]
>>> v = SudokuValidation()
>>> print(f'valid: {v.validateBoard(solved)}')
valid: True
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
