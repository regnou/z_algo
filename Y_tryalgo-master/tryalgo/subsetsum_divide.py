#!/usr/bin/env python3
# Subsetsum by splitting
# c.durr et jill-jênn vie - 2014-2015


# snip{
def part_sum(x, i=0):
    """All subsetsums from x[i:]

    :param x: table of values
    :param int i: index defining suffix of x to be considered
    :iterates: over all values, in arbitrary order
    :complexity: :math:`O(2^{len(x)-i})`
    """
    if i == len(x):
        yield 0
    else:
        for s in part_sum(x, i + 1):
            yield s
            yield s + x[i]


def subset_sum(x, R):
    """Subsetsum by splitting

    :param x: table of values
    :param R: target value
    :returns boolean: if there is a subsequence of x with total sum R
    :complexity: :math:`O(n^{\\lceil n/2 \\rceil})`
    """
    k = len(x) // 2             # diviser l'entrée
    Y = [v for v in part_sum(x[:k])]
    Z = [R - v for v in part_sum(x[k:])]
    Y.sort()                    # test d'intersection Y avec Z
    Z.sort()
    i = 0
    j = 0
    while i < len(Y) and j < len(Z):
        if Y[i] == Z[j]:
            return True
        elif Y[i] < Z[j]:       # incrémenter l'indice du plus petit élément
            i += 1
        else:
            j += 1
    return False
# snip}
