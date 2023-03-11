# Game-of-Life-Simulator
Simulates Conway's Game of Life and other life-like cellular automata on a square grid.

To play the game, a board must be initialized using the Plane constructor, which takes a list of lists whose length is the same as each of its elements, and a Rule instance.
The Rule constructor takes two parameters, 'birth' and 'survival'. The former is a list containing the numbers of adjacent living cells necessary for a dead cell to become alive, and the latter is a list containing the numbers of adjacent living cells necessary for a living cell to stay alive.
As an example, the variable 'board' initializes a 21x21 board with the rules for Conway's Game of Life.
The code afterwards displays the board and then enters a loop, prompting the user for input, and then updating each cell on the board and displaying the result, until the user submits a response other than the empty string.
