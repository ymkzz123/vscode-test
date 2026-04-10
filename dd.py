import sys
input = sys.stdin.readline
sys.setrecursionlimit(21900)

def dfs(v, prev):
    for next, c in g[v]:
        if next == prev:
            continue
        d[next] = d[v]+c
        dfs(next, v)

n = int(input())
g = [[] for _ in range(n+1)]
res = 0
d = [0]*(n+1)

for _ in range(n-1):
    p, s, w = map(int, input().split())
    g[p].append((s, w))
    g[s].append((p, w))

dfs(1, 0)

long = d.index(max(d))
d = [0]*(n+1)
dfs(long, 0)

print(max(d))