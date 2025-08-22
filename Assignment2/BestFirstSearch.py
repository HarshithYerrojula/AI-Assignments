
class State:
  def __init__(self, x, y, grid):
    self.x = x
    self.y = y
    self.grid = grid
    self.n = len(grid)
    self.goal = (self.n - 1, self.n - 1)

  
  def goalTest(self):
    return (self.x, self.y) == self.goal

  
  def moveGen(self):
    children = []
    directions = [(-1,0),(1,0),(0,-1),(0,1),
                  (-1,-1),(-1,1),(1,-1),(1,1)]
    for dx, dy in directions:
      nx = self.x + dx
      ny = self.y + dy
      if 0 <= nx < self.n and 0 <= ny < self.n and self.grid[nx][ny] == 0:
        children.append(State(nx, ny, self.grid))
    return children

  
  def h(self):
    gx, gy = self.goal
    return abs(self.x - gx) + abs(self.y - gy)


  def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self.x, self.y))


class BestFirstSearch:
  def removeSeen(self, children, open, closed):
    new_nodes = []
    open_nodes = [node for node, parent in open]
    closed_nodes = [node for node, parent in closed]
    for child in children:
      if child not in open_nodes and child not in closed_nodes:
        new_nodes.append(child)
    return new_nodes

  def reconstructPath(self, node_pair, closed):
    path = []
    node, parent = node_pair
    parent_map = {n: p for n, p in closed}
    path.insert(0, node)
    while parent is not None:
      path.insert(0, parent)
      parent = parent_map.get(parent)
    return path

  def search(self, start):
    
    if start.grid[start.x][start.y] == 1 or start.grid[start.n-1][start.n-1] == 1:
      print("Best First Search → Path length: -1")
      return []

    open = [(start, None)]
    closed = []

    while open:
      best_index = 0
      for i in range(1, len(open)):
        if open[i][0].h() < open[best_index][0].h():
          best_index = i

      node_pair = open.pop(best_index)
      node, parent = node_pair

      print("Expanding:", node, "h=", node.h())
      children = node.moveGen()
      print("Children of", node, ":", [str(c) for c in children])

      if node.goalTest():
        path = self.reconstructPath(node_pair, closed)
        print("Best First Search → Path length:", len(path), "Path:", [str(p) for p in path])
        return path

      closed.append(node_pair)
      new_nodes = self.removeSeen(children, open, closed)
      node_pairs = [(child, node) for child in new_nodes]
      open.extend(node_pairs)

    print("Best First Search → Path length: -1")
    return []



grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]

start_state = State(0,0,grid)
search = BestFirstSearch()
path = search.search(start_state)
