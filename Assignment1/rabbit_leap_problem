class RabbitLeapState:
    def __init__(self, layout, target):
        self.layout = layout
        self.target = target 

    def is_goal(self):
        return self.layout == self.target

    def generate_moves(self):
        moves = []
        stones = self.layout
        empty_idx = stones.index('_')
        length = len(stones)

        if empty_idx > 0 and stones[empty_idx-1] == 'E':
            new_layout = list(stones)
            new_layout[empty_idx], new_layout[empty_idx-1] = new_layout[empty_idx-1], new_layout[empty_idx]
            moves.append(RabbitLeapState(''.join(new_layout), self.target))

        if empty_idx > 1 and stones[empty_idx-2] == 'E' and stones[empty_idx-1] in 'W':
            new_layout = list(stones)
            new_layout[empty_idx], new_layout[empty_idx-2] = new_layout[empty_idx-2], new_layout[empty_idx]
            moves.append(RabbitLeapState(''.join(new_layout), self.target))

        if empty_idx < length - 1 and stones[empty_idx + 1] == 'W':
            new_layout = list(stones)
            new_layout[empty_idx], new_layout[empty_idx + 1] = new_layout[empty_idx + 1], new_layout[empty_idx]
            moves.append(RabbitLeapState(''.join(new_layout), self.target))

        if empty_idx < length - 2 and stones[empty_idx + 2] == 'W' and stones[empty_idx + 1] in 'E':
            new_layout = list(stones)
            new_layout[empty_idx], new_layout[empty_idx + 2] = new_layout[empty_idx + 2], new_layout[empty_idx]
            moves.append(RabbitLeapState(''.join(new_layout), self.target))

        return moves

    def __eq__(self, other):
        return self.layout == other.layout

    def __hash__(self):
        return hash(self.layout)

    def __repr__(self):
        return self.layout


def filter_new_states(new_states, open_list, closed_list):
    open_states = [state for state, _ in open_list]
    closed_states = [state for state, _ in closed_list]
    return [s for s in new_states if s not in open_states and s not in closed_states]


def backtrace_path(node_pair, closed_nodes):
    path = []
    parents_map = {node: parent for node, parent in closed_nodes}
    node, parent = node_pair
    path.append(node)
    while parent:
        path.append(parent)
        parent = parents_map[parent]
    path.reverse()
    return path


def bfs_search(initial_state):
    OPEN = [(initial_state, None)]
    CLOSED = []

    while OPEN:
        current, parent = OPEN.pop(0)
        if current.is_goal():
            solution_path = backtrace_path((current, parent), CLOSED)
            print("Solution Found (BFS):")
            for step in solution_path:
                print(step)
            return
        CLOSED.append((current, parent))
        successors = current.generate_moves()
        new_successors = filter_new_states(successors, OPEN, CLOSED)
        OPEN.extend([(s, current) for s in new_successors])

def dfs_search(initial_state):
    OPEN = [(initial_state, None)]
    CLOSED = []

    while OPEN:
        current, parent = OPEN.pop(0)
        if current.is_goal():
            solution_path = backtrace_path((current, parent), CLOSED)
            print("Solution Found (DFS):")
            for step in solution_path:
                print(step)
            return
        CLOSED.append((current, parent))
        successors = current.generate_moves()
        new_successors = filter_new_states(successors, OPEN, CLOSED)
        OPEN = [(s, current) for s in new_successors] + OPEN 


if __name__ == "__main__":
    start = RabbitLeapState("EEE_WWW", "WWW_EEE")
    bfs_search(start)
    print()
    dfs_search(start)
