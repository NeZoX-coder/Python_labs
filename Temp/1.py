N = int(input())  # Число узлов сети

P_nodes = list(map(int, input().split()))  # Вероятность отказа соответствующих узлов (P_i)
P_channels = list(map(float, input().split()))  # Вероятность отказа соответствующих каналов связи (P_ik^k)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


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