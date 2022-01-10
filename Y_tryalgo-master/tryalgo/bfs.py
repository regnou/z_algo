#!/usr/bin/env python3
# Breadth-first-search, bfs and OurQueue
# christoph dürr - jill-jênn vie - 2015

# snip{
from collections import deque


def bfs(graph, start=0):
    """Shortest path in unweighted graph by BFS

       :param graph: adjacency list or adjacency dictionary of a directed graph
       :param start: source vertex
       :returns: distance table, precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = deque()
    dist = [float('inf')] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:              # une file vide évalue à Faux
        node = to_visit.pop()
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec
# snip}

