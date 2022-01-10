#!/usr/bin/env python3
# Sweepline algrithm technique
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def max_interval_intersec(S):
    """determine a value that is contained in a largest number of given intervals

    :param S: list of half open intervals
    :complexity: O(n log n), where n = len(S)
    """
    B = ([(left,  +1) for left, right in S] +
         [(right, -1) for left, right in S])
    B.sort()
    c = 0
    best = (c, None)
    for x, d in B:
        c += d
        if best[0] < c:
            best = (c, x)
    return best
# snip}

