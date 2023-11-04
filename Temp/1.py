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


def add_nodes_from_input(G):                        # Ввод узлов и каналов связи

    print("Введите узлы и каналы связи, в формате 'Узел1 Узел2 Канал1', введите 'done', когда всё введете:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        parts = edge.split()
        if len(parts) != 3:
            print("Введен неправильный формат. Попробуйте еще.")
            continue
        node1, node2, channel = parts
        G.add_edge(int(node1), int(node2), channel=channel)


def draw_graph(G, pos):                             # Рисует граф
    edge_labels = nx.get_edge_attributes(G, 'channel')
    plt.figure(figsize=(8, 8))  # Set the size of the plot
    nx.draw_networkx_nodes(G, pos_inverted_triangle, node_size=700, node_color='white', edgecolors='black')
    nx.draw_networkx_edges(G, pos_inverted_triangle, width=2)
    nx.draw_networkx_labels(G, pos_inverted_triangle, font_size=20, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos_inverted_triangle, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    plt.show()


G = nx.Graph()                                      # Создаем пустой граф
add_nodes_from_input(G)

# Топология сети
# 1 2 1
# 2 3 2
# 3 1 3
# 4 1 4
# 4 2 5
# 4 3 6
# done

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
