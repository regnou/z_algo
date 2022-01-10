#!/usr/bin/env python3
# Bipartie maximum matching
# jill-jenn vie et christoph durr - 2014-2015

__all__ = ["max_bipartite_matching"]


# snip{
def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v],  bigraph, visit, match):
                match[v] = u       # chemin augmentant trouvé
                return True
    return False


def max_bipartite_matching(bigraph):
    """Bipartie maximum matching

    :param bigraph: adjacency list, index = vertex in U,
                                    value = neighbor list in V
    :assumption: U = V = {0, 1, 2, ..., n - 1} for n = len(bigraph)
    :returns: matching list, match[v] == u iff (u, v) in matching
    :complexity: `O(|V|*|E|)`
    """
    n = len(bigraph)               # même domaine pour U que pour V
    match = [None] * n
    for u in range(n):
        augment(u, bigraph, [False] * n, match)
    return match
# snip}

