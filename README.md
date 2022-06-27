# Sudoku Solver

Basically in Sudoku, we want to solve a sudoku puzzle given an input of n*n matrix, known as sudoku board.

Here, we take 9*9 sudoku board. In our board, empty cells are presented by -1.

Our objective is to find the value for each empty cell and replace them with digits between 1 to such that it follows the below mentioned 3 rules.

Rule 1 :
Each 9 place in a row should have a unique value between 1 to 9.
Rule 2 :
Each 9 place along a column should have a unique value between 1 to 9.
Rule 3 :
if we devide the larger 9*9 cube into 9 (3*3) small cubes.
Each 9 place in each small cube should have a unique value between 1 to 9.

Now, our goal is to solve our sudoku puzzle using Python!

Reference : https://www.youtube.com/watch?v=8ext9G7xspg&t=6715s&ab_channel=freeCodeCamp.org
