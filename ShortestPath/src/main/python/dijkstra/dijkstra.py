import heapq

MAX_N = 150005
MAX_M = 150005
ver = [[] for i in range(MAX_N)]
edge = [[] for i in range(MAX_N)]
v = [False for i in range(MAX_N)]


def add(x, y, z):
    ver[x].append(y)
    edge[x].append(z)


def func(n):

    dist = [float("inf") for i in range(n + 1)]
    dist[1] = 0
    # q = [(0, 1)]
    q = []
    heapq.heappush(q, (0, 1))

    while len(q) != 0:
        x = heapq.heappop(q)[1]

        if v[x]:
            continue
        v[x] = True

        for i in range(len(ver[x])):
            y = ver[x][i]
            z = edge[x][i]
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                heapq.heappush(q, (dist[y], y))

    if dist[n] == float("inf"):
        print("-1")

    else:
        print(dist[n])


if __name__ == "__main__":
    # n, m = [int(i) for i in input().split()]

    # # 初始化邻接表
    # neighbor_list = []

    n, m = 3, 3
    neighbor_list = [
        [1, 2, 2],
        [2, 3, 1],
        [1, 3, 4],
    ]
    for i in range(m):
        # add(input().split())
        add(*neighbor_list[i])

    func(n)
