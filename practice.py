import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    mxheap, mnheap = [], []
    visited = [False]*(k+1)
    idx = 0
    
    def clean(heap):
        while heap and not visited[heap[0][1]]:
            heapq.heappop(heap)
                
    for i in range(k):
        s, n = input().split();n = int(n)
        
        if s == 'I':
            heapq.heappush(mnheap, (n, idx))
            heapq.heappush(mxheap, (-n, idx))
            visited[idx] = True
            idx += 1
        
        else:
            if n == 1:
                clean(mxheap)
                if mxheap:
                    visited[mxheap[0][1]] = False
                    heapq.heappop(mxheap)
            
            else:
                clean(mnheap)
                if mnheap:
                    visited[mnheap[0][1]] = False
                    heapq.heappop(mnheap)
            
            
    clean(mnheap)
    clean(mxheap)

    if not mnheap:
        print("EMPTY")
    else:
        print(-mxheap[0][0], mnheap[0][0])