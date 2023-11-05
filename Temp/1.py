import matplotlib.pyplot as plt
import networkx as nx

# N = int(input())                                    # Число узлов сети
#
# P_nodes = list(map(int, input().split()))           # Вероятность отказа соответствующих узлов (P_i)
# P_channels = list(map(float, input().split()))      # Вероятность отказа соответствующих каналов связи (P_ik^k)

pos_inverted_triangle = {                           # Координаты положения узлов на графике(для красоты)
    1: (-1, 1),
    2: (1, 1),
    3: (0, -1),
    4: (0, 0)
}
network_topology = [                                # Топология сети (чтобы не вводить вручную)
    [1, 2, 1200, 1, 1, 0.1, 1024],
    [2, 3, 4800, 6, 6, 0.05, 4096],
    [3, 1, 9600, 2, 2, 0.2, 8192],
    [1, 4, 1200, 1, 1, 0.1, 1024],
    [2, 4, 4800, 6, 6, 0.05, 4096],
    [3, 4, 1200, 1, 1, 0.2, 1024],
]


# Топология сети
# 2 3 4800 6 6 0.05 4096
# 3 1 9600 2 2 0.2 8192
# 1 4 1200 1 1 0.1 1024
# 2 4 4800 6 6 0.05 4096
# 3 4 1200 1 1 0.2 1024
# done


# def get_network_topology():                       # Ввод узлов и каналов связи для топологии сети вручную
#     topology = []
#     print(
#         "Введите узлы и каналы связи, в формате 'Узел1 Узел2 Канал1', введите 'done', когда всё введете:")
#
#     while True:
#         entry = input()
#         if entry.lower() == 'done':
#             break
#         try:
#             parts = entry.split()
#             if len(parts) != 7:
#                 print("Введен неправильный формат. Попробуйте еще..")
#                 continue
#             node1, node2, mod_speed, num_channels, recovery_time, failure_prob, packet_length = parts
#             channel_data = {
#                 'nodes': (int(node1), int(node2)),
#                 'modulation_speed': float(mod_speed),
#                 'num_channels_in_bundle': int(num_channels),
#                 'recovery_time': float(recovery_time),
#                 'failure_probability': float(failure_prob),
#                 'average_packet_length': float(packet_length)
#             }
#             topology.append(channel_data)
#         except ValueError as e:
#             print(f"Неправильный ввод: {e}. Попробуйте еще раз.")
#
#     return topology


def draw_graph(network_topology, pos):
    G = nx.Graph()
    for i, channel in enumerate(network_topology):
        node1, node2, mod_speed, num_channels, recovery_time, failure_prob, packet_length = channel
        G.add_edge(node1, node2, channel=i + 1)
    plt.figure(figsize=(8, 8))
    edge_labels = nx.get_edge_attributes(G, 'channel')
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='white', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=20, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    plt.show()




# network_topology = get_network_topology()
draw_graph(network_topology, pos_inverted_triangle)











# def find_all_paths(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return [path]
#     if start not in graph:
#         return []
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             new_paths = find_all_paths(graph, node, end, path)
#             for new_path in new_paths:
#                 paths.append(new_path)
#     return paths

# def P_routes(P: list, i: int, j: int, k: int) -> float:  # Вероятность отказа маршрутов (P_ok^ij)
#     result = 1.0
#     n = len(P)
#
#     for m in range(n):
#         if m != i and m != j:
#             result *= (1 - P[i]) * (1 - P[m] if m != k else P[k]) * (1 - P[j])
#
#     return 1 - result
#
# print(P_routes(P))
