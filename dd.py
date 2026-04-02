print("Hello my fucked physic exam")
#정창욱씨발새끼야


def dfs(v):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)

visited = [False]*10001
g = [[], [2,3],[3,4],[1,2],[2]]