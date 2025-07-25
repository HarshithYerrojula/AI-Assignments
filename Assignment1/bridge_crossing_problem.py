class BridgeCrossingState:
    def __init__(self, left_side, right_side, umbrella_side, elapsed_time, max_time=60):
        self.left = frozenset(left_side)
        self.right = frozenset(right_side)
        self.umbrella = umbrella_side  
        self.time = elapsed_time
        self.max_time = max_time
        self.cross_time = {'A':5, 'M':10, 'GM':20, 'GF':25}

    def is_goal(self):
        return len(self.left) == 0 and self.umbrella == 'R' and self.time <= self.max_time

    def generate_moves(self):
        next_states = []
        if self.umbrella == 'L':
    
            for p1 in self.left:
                new_left = set(self.left)
                new_right = set(self.right)
                new_left.remove(p1)
                new_right.add(p1)
                next_time = self.time + self.cross_time[p1]
                if next_time <= self.max_time:
                    next_states.append(BridgeCrossingState(new_left, new_right, 'R', next_time))
                for p2 in self.left:
                    if p1 != p2:
                        new_left2 = set(self.left) - {p1, p2}
                        new_right2 = set(self.right) | {p1, p2}
                        time2 = self.time + max(self.cross_time[p1], self.cross_time[p2])
                        if time2 <= self.max_time:
                            next_states.append(BridgeCrossingState(new_left2, new_right2, 'R', time2))
        else:
            
            for p in self.right:
                new_left = set(self.left)
                new_right = set(self.right)
                new_left.add(p)
                new_right.remove(p)
                next_time = self.time + self.cross_time[p]
                if next_time <= self.max_time:
                    next_states.append(BridgeCrossingState(new_left, new_right, 'L', next_time))
        return next_states

    def __eq__(self, other):
        return (self.left, self.right, self.umbrella, self.time) == (other.left, other.right, other.umbrella, other.time)

    def __hash__(self):
        return hash((self.left, self.right, self.umbrella, self.time))

    def __repr__(self):
        return f"L:{sorted(self.left)} R:{sorted(self.right)} Umb:{self.umbrella} Time:{self.time}"



if __name__ == "__main__":
    
    start_bridge = BridgeCrossingState(['A', 'M', 'GM', 'GF'], [], 'L', 0)
    print("Bridge Crossing BFS:")
    bfs_search(start_bridge)
    print()
    print("Bridge Crossing DFS:")
    dfs_search(start_bridge)
