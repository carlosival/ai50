import heapq

class Node():
    def __init__(self, state, parent, action, score):
        self.state = state
        self.parent = parent
        self.action = action
        self.score = score
    
    def __lt__(self, other):
        return self


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class HeapFrontier():
    def __init__(self):
        self.frontier = []
        self.lookup = {}

    def add(self, node):
        self.lookup[node.state[1]] = node.state[1]
        heapq.heappush(self.frontier,(node.score,node))

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = heapq.heappop(self.frontier)[1]
            self.lookup.pop(node.state[1])  
            return node
    
    def contains_state(self, state):
        return state in self.lookup