import matplotlib.pyplot as plt
import networkx as nx


def add_nodes_from_input(G):
    print("Enter the edges and channels, format 'Node1 Node2 Channel', type 'done' when finished:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        parts = edge.split()
        if len(parts) != 3:
            print("Invalid input format. Please enter in 'Node1 Node2 Channel' format.")
            continue
        node1, node2, channel = parts
        G.add_edge(int(node1), int(node2), channel=channel)


def draw_graph(G, pos):
    edge_labels = nx.get_edge_attributes(G, 'channel')
    plt.figure(figsize=(8, 8))  # Set the size of the plot
    nx.draw_networkx_nodes(G, pos_inverted_triangle, node_size=700, node_color='white', edgecolors='black')
    nx.draw_networkx_edges(G, pos_inverted_triangle, width=2)
    nx.draw_networkx_labels(G, pos_inverted_triangle, font_size=20, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos_inverted_triangle, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    plt.show()


G = nx.Graph()

add_nodes_from_input(G)

pos_inverted_triangle = {
    1: (-0.866, 0.5),
    2: (0.866, 0.5),
    3: (0, -1),
    4: (0, 0)
}
