'''
      NAME : JIBEK GUPTA
      SID : @03066097
'''


class Boggle:
  def __init__(self, grid, dictionary):
     # Initialize the boggle board and dictionary
    self.grid = grid
    self.dictionary = set(dictionary) # Store the dictionary as a set for fast lookup
    self.rows = len(grid)     # Number of rows in the grid
    self.cols = len(grid[0]) if grid else 0  # Number of columns in the grid
    self.result = set()       # Set to store found words

  def setGrid(self,grid):
    self.grid = grid
    self.rows = len(grid)
    self.cols = len(grid[0]) if grid else 0

  def setDictionary(self,dictionary):
    self.dictionary =set(dictionary)


  def is_valid(self, x, y, visited):
    # Check if the the cell (x,y) is valid and not yet visited
    return 0 <= x < self.rows and 0 <= y < self.cols and not visited[x][y]

  def dfs(self, x, y, path, visited):
    # Depth-first search to find words starting sell (x,y)
    if path in self.dictionary:
      self.result.add(path)     # Add the word to the result if it's in the dictionary

    # Early exit if the path length exceeds the length of the longest word in the dictionary
    if self.dictionary and len(path) > max(map(len, self.dictionary)):
      return

    # All 8 possible directions to move in the grid
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # Mark the current cell as visited
    visited[x][y] = True

    # Explore all 8 directions
    for dx, dy in directions:
      nx, ny = x + dx, y + dy     # Compute the new positions
      if self.is_valid(nx, ny, visited):
        # Recusively perform DFS from the positions, appending the char at (nx,ny) to the path
        self.dfs(nx,ny,path+self.grid[nx][ny], visited)
    
    # Unmark the current cell to allow other paths to use it
    visited[x][y] = False


  def solution(self):

    if not self.dictionary:
      return []
      
    # Initialize the visited array to keep track of visited cells
    visited = [[False] * self.cols for _ in range(self.rows)]

    # Start DFS from every cell in the grid
    for x in range(self.rows):
      for y in range(self.cols):
        # Perform DFS starting from cell (x,y)
        self.dfs(x, y, self.grid[x][y], visited)

    # Return the list of all found words
    return list(self.result)


def main():
  # define the Boggle grid and dictionary of valid words
  grid = [['A', 'B', 'C', 'D'],
          ['E', 'F', 'G', 'H'], 
          ['I', 'J', 'K', 'L'], 
          ['A', 'B', 'C', 'D']]

  dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

  # Create a Boggle game instance and find all words in the grid
  mygame = Boggle(grid, dictionary)
  
  # Print the found words
  print(mygame.solution())

# This ensures that the main function is called only when the screipt is excuted directly
if __name__ == "__main__":
  main()
