#!/usr/bin/env python3
# Shortest path in a 0,1 weighted graph
# jill-jenn vie et christoph durr - 2014-2015

from collections import deque


# snip{
def dist01(graph, weight, source=0, target=None):
    """Shortest path in a 0,1 weighted graph

    :param graph: adjacency list or adjacency dictionary of a directed graph
    :param weight: matrix or adjacency dictionary
    :param int source: vertex
    :param target: exploration stops once distance to target is found
    :returns: distance table, predecessor table
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    black = [False] * n
    dist[source] = 0
    gray = deque([source])
    while gray:
        node = gray.pop()
        black[node] = True
        if node == target:
            break
        for neighbor in graph[node]:
            ell = dist[node] + weight[node][neighbor]
            if black[neighbor] or dist[neighbor] <= ell:
                continue
            dist[neighbor] = ell
            prec[neighbor] = node
            if weight[node][neighbor] == 0:
                gray.append(neighbor)
            else:
                gray.appendleft(neighbor)
    return dist, prec
# snip}

