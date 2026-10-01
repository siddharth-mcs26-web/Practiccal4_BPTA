import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(edges, cover_LP, cover_optimal, n):
    nodes = [i for i in range(n)]
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(nodes)
    pos = nx.spring_layout(G, seed=42)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    #nx.draw(G, with_labels=True)

    axes[0].set_title("computed cover LP rouding")
    node_colors = []
    for i in G.nodes():
        if i in cover_LP:
            node_colors.append('red')
        else:
            node_colors.append('lightblue')
    nx.draw(G, pos=pos, node_color=node_colors, with_labels=True, ax=axes[0])
    node_colors = []
    for i in G.nodes():
        if i in cover_optimal:
            node_colors.append('red')
        else:
            node_colors.append('lightblue')

    axes[1].set_title("Computed cover LP Optimal")
    nx.draw(G,pos=pos, node_color=node_colors, with_labels=True, ax=axes[1])
    #plt.title("LP rouding and LP Optimal Vertex Cover Visualisation")
    plt.savefig(f"graphpic{len(edges)}_{n}")
    plt.close()
