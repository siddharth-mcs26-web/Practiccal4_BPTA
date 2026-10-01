def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    edges = []
    for edge in lines:
        edge = edge.strip()
        edge = edge[1:-1]
        edge = edge.split(',')
        edge = (int(edge[0]), int(edge[1]))
        edges.append(edge)
    f.close()
    return edges