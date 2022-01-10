#!/usr/bin/env python3
# All pairs shortest paths by Floyd-Warshall
# jill-jenn vie et christoph durr - 2014-2015



# snip{
def floyd_warshall(weight):
    """All pairs shortest paths by Floyd-Warshall

    :param weight: edge weight matrix
    :modifies: weight matrix to contain distances in graph
    :returns: true if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    V = range(len(weight))
    for k in V:
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v],
                                   weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:      # cycle négatif détecté
            return True
    return False
# snip}

