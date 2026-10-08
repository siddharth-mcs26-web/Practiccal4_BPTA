def greedy_vc(edges):
    cover = set()
    E = set(edges)
    M = []
    while(len(E) != 0):
        u,v = E.pop()
        
        cover.add(u)
        cover.add(v)
        
        M.append((u,v))
        
        edges_to_remove = set()
        
        for edge in E:
            if u in edge or v in edge:
                edges_to_remove.add(edge)
        
        E = E - edges_to_remove
        
    return cover