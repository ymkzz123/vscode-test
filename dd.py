from collections import deque

def dfs(v):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)


def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                res += 1
                q.append((nx, ny))
    
visited = [False]*10001
g = [[], [2,3],[3,4],[1,2],[2]]
N = int(input())
res = 0