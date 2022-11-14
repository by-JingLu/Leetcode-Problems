from collections import defaultdict, deque

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(set)
        self.connection = [0] * n

    def addE(self, s, e):
        self.graph[s].add(e)
        self.graph[e].add(s)

        self.connection[s] += 1
        self.connection[e] += 1

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
# Created graph 
g = Graph(n)
for start, end in roads:
    g.addE(start, end)
print(g.graph, g.connection)

all_results = []
for i in range(n):
    for j in range(i+1, n):
        duplicate_connection = i in g.graph[j]
        result = g.connection[i] + g.connection[j] - (1 if duplicate_connection else 0)
        all_results.append(result)
print(all_results)
print(max(all_results))