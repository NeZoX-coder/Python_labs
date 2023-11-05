import matplotlib.pyplot as plt
import networkx as nx


def get_network_topology():
    topology = []
    print(
        "Enter the network topology with attributes, format 'Node1 Node2 ModSpeed NumChannels RecoveryTime FailureProb PacketLength', type 'done' when finished:")

    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        try:
            parts = entry.split()
            if len(parts) != 7:
                print("Invalid input. Please enter the information in the specified format.")
                continue
            node1, node2, mod_speed, num_channels, recovery_time, failure_prob, packet_length = parts
            channel_data = {
                'nodes': (int(node1), int(node2)),
                'modulation_speed': float(mod_speed),
                'num_channels_in_bundle': int(num_channels),
                'recovery_time': float(recovery_time),
                'failure_probability': float(failure_prob),
                'average_packet_length': float(packet_length)
            }
            topology.append(channel_data)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter the information in the specified format.")

    return topology


# Example of how to use the function
network_topology = get_network_topology()
print(type(network_topology), network_topology, sep='\n')
# Now the network_topology variable contains the 2D list representing the channels and nodes
# for channel, nodes in enumerate(network_topology, start=1):
#     print(f"Channel {channel} connects nodes {nodes[0]} and {nodes[1]}")



# def add_nodes_from_input(G):
#     print("Enter the edges and channels, format 'Node1 Node2 Channel', type 'done' when finished:")
#     while True:
#         edge = input()
#         if edge.lower() == 'done':
#             break
#         parts = edge.split()
#         if len(parts) != 3:
#             print("Invalid input format. Please enter in 'Node1 Node2 Channel' format.")
#             continue
#         node1, node2, channel = parts
#         G.add_edge(int(node1), int(node2), channel=channel)
#
#
# def draw_graph(G, pos):
#     edge_labels = nx.get_edge_attributes(G, 'channel')
#     plt.figure(figsize=(8, 8))  # Set the size of the plot
#     nx.draw_networkx_nodes(G, pos_inverted_triangle, node_size=700, node_color='white', edgecolors='black')
#     nx.draw_networkx_edges(G, pos_inverted_triangle, width=2)
#     nx.draw_networkx_labels(G, pos_inverted_triangle, font_size=20, font_weight='bold')
#     nx.draw_networkx_edge_labels(G, pos_inverted_triangle, edge_labels=edge_labels, font_color='red')
#     plt.axis('off')
#     plt.show()
#
#
# G = nx.Graph()
#
# add_nodes_from_input(G)
#
# pos_inverted_triangle = {
#     1: (-0.866, 0.5),
#     2: (0.866, 0.5),
#     3: (0, -1),
#     4: (0, 0)
# }
