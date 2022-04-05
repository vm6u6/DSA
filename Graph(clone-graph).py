"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class solution( object ):
    def cloneGraph ( self, node ):
        visited = {}
        def dfs ( node ):
            if not node:
                return None

            if node in visited:
                return visited[node]
            copy = Node( node.val )
            visited[node] = copy

            for nd in node.neighbors:
                print(nd)
                copy.neighbors.append( dfs(nd) )
            return copy

        copy = dfs(node)
        return copy      