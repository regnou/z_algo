#!/usr/bin/env python3
# Reading graphs from files and writing into files
# jill-jênn vie et christoph dürr - 2015


def readval(file, ty):
    """Reads a line from file with an item of type ty"""
    return ty(file.readline())


def readtab(fi, ty):
    """Reads a line from file with a space separated list
       of items of type ty"""
    return tuple(map(ty, fi.readline().split()))


def read_graph(filename, directed=False, weighted=False, default_weight=None):
    """Read a graph from a text file

    :param filename: plain text file. All numbers are separated by space.
              Starts with a line containing n (#vertices) and m (#edges).
              Then m lines follow, for each edge.
              Vertices are numbered from 0 to n-1.
              Line for unweighted edge u,v contains two integers u, v.
              Line for weighted edge u,v contains three integers u, v, w[u,v].

    :param directed: true for a directed graph, false for undirected
    :param weighted: true for an edge weighted graph
    :returns: graph as adjacency list, possibly followed by weight matrix
    :complexity: O(n + m) for unweighted graph,
                 :math:`O(n^2)` for weighted graph
    """
    with open(filename, 'r') as f:
        while True:
            line = f.readline()         # ignore leading comments
            if line[0] != '#':
                break
        nb_nodes, nb_edges = tuple(map(int, line.split()))
        graph = [[] for u in range(nb_nodes)]
        if weighted:
            weight = [[default_weight] * nb_nodes for v in range(nb_nodes)]
            for v in range(nb_nodes):
                weight[v][v] = 0
            for _ in range(nb_edges):
                u, v, w = readtab(f, int)
                graph[u].append(v)
                weight[u][v] = w
                if not directed:
                    graph[v].append(u)
                    weight[v][u] = w
            return graph, weight
        else:
            for _ in range(nb_edges):
                # si le fichier contient des poids, ils seront ignorés
                u, v = readtab(f, int)[:2]
                graph[u].append(v)
                if not directed:
                    graph[v].append(u)
            return graph


def write_graph(dotfile, graph, directed=False,
                node_label=None, arc_label=None, comment="",
                node_mark=set(), arc_mark=set()):
    """Writes a graph to a file in the DOT format

    :param dotfile: the filename.
    :param graph: adjacency list or adjacency dictionary
    :param directed: true if graph is directed, false if undirected
    :param weight: weight matrix or adjacency dictionary or None
    :param node_label: vertex label table or None
    :param arc_label: arc label matrix or None
    :param comment: comment string for the dot file or None
    :param node_mark: set of nodes to be shown in gray
    :param arc_marc: set of arcs to be shown in red
    :complexity: `O(|V| + |E|)`
    """
    with open(dotfile, 'w') as f:
        if directed:
            f.write("digraph G{\n")
        else:
            f.write("graph G{\n")
        if comment:
            f.write('label="%s";\n' % comment)
        V = range(len(graph))
        #                              -- vertices
        for u in V:
            if node_mark and u in node_mark:
                f.write('%d [style=filled, color="lightgrey", ' % u)
            else:
                f.write('%d [' % u)
            if node_label:
                f.write('label="%u [%s]"];\n' % (u, node_label[u]))
            else:
                f.write('shape=circle, label="%u"];\n' % u)
        #                              -- edges
        if isinstance(arc_mark, list):
            arc_mark = set((u, arc_mark[u]) for u in V)
        for u in V:
            for v in graph[u]:
                if not directed and u > v:
                    continue   # don't show twice the edge
                if arc_label and arc_label[u][v] == None:
                    continue   # suppress arcs with no label
                if directed:
                    arc = "%d -> %d " % (u, v)
                else:
                    arc = "%d -- %d " % (u, v)
                if arc_mark and ( (v,u) in arc_mark or (not directed and (u,v) in arc_mark) ):
                    pen = 'color="red"'
                else:
                    pen = ""
                if arc_label:
                    tag = 'label="%s"' % arc_label[u][v]
                else:
                    tag = ""
                if tag and pen:
                    sep = ", "
                else:
                    sep = ""
                f.write(arc + "[" + tag + sep + pen + "];\n")
        f.write("}")


# snip{ tree_representations
def tree_prec_to_adj(prec, root=0):
    """Transforms a tree given as predecessor table into adjacency list form

    :complexity: linear
    """
    n = len(prec)
    graph = [[prec[u]] for u in range(n)]   # ajouter les prédécesseurs
    graph[root] = []
    for u in range(n):                      # ajouter les descendants
        if u != root:
            graph[prec[u]].append(u)
    return graph


def tree_adj_to_prec(graph, root=0):
    """Transforms a tree given as adjacency list into predecessor table form

    if graph is not a tree: will return a DFS spanning tree

    :complexity: linear
    """
    n = len(graph)
    prec = [None] * len(graph)
    prec[root] = root            # marquer pour ne pas revisiter la racine
    to_visit = [root]
    while to_visit:              # parcours DFS
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    prec[root] = None            # mettre la marque standard pour la racine
    return prec
# snip}


# snip{ add_reverse_arcs
def add_reverse_arcs(graph, capac):
    """Utility function for flow algorithms that need for every arc (u,v),
    the existence of an (v,u) arc with zero capacity."""
    for u in range(len(graph)):
        for v in graph[u]:
            if u not in graph[v]:
                graph[v].append(u)
                capac[v][u] = 0
# snip}



def weight_to_graph(weight):
    """transforms a squared weight matrix in a adjacency table
    encoding the directed graph corrsponding to the entries of the matrix
    different from None """
    graph = [[] for _ in range(len(weight))]
    for u in range(len(graph)):
        for v in range(len(graph)):
            if weight[u][v] != None:
                graph[u].append(v)
    return graph


def graph_weight_to_sparse(graph, weight=None):
    """Transforms the weighted adjacency list representation of a graph into
    the adjacency dictionnary representation"""
    if weight:
        return [{v:weight[u][v] for v in graph[u]} for u in range(len(graph))]
    else:
        return [{v:None for v in graph[u]} for u in range(len(graph))]


def sparse_to_graph_weight(sparse):
    """Transforms the adjacency dictionnary representation of a graph into
    the weighted adjacency list representation"""
    V = range(len(sparse))
    graph = [[] for _ in V]
    weight = [[None for v in V] for u in V]
    for u in V:
        for v in sparse[u]:
            graph[u].append(v)
            weight[u][v] = sparse[u][v]
    return graph, weight


def extract_path(prec, v):
    """extracts a path in form of vertex list from source to vertex v
       given a precedence table prec leading to the source"""
    L = []
    while v is not None:
        L.append(v)
        v = prec[v]
        assert v not in L   # prevent infinite loops for a bad formed table prec
    return L[::-1]


def make_flow_labels(graph, flow, capac):
    """Generate arc labels for a flow in a graph with capacities.

    :param graph: adjacency list or adjacency dictionary
    :param flow:  flow matrix or adjacency dictionary
    :param capac: capacity matrix or adjacency dictionary
    """
    V = range(len(graph))
    arc_label = [{v:"" for v in graph[u]} for u in V]
    for u in V:
        for v in graph[u]:
            if flow[u][v] >= 0:
                arc_label[u][v] = "%s/%s" % (flow[u][v], capac[u][v])
            else:
                arc_label[u][v] = None   # do not show negative flow arcs
    return arc_label
