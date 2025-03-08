from queue import PriorityQueue
from queue import Queue

def main():

    ans = 0
    
    def dfs(current, parent, k, adj):
        h = 1
    
        for to in adj[current]:
            if to == parent:
                continue
    
            h = max(h, dfs(to, current, k, adj) + 1)
    
        # Cada vez que encontramos una altura >= k
        # Añadimos 1 a la respuesta
        if h == k:
            global ans
            ans += 1
    
            # Reiniciamos la altura a 0
            h = 0
    
        return h
    
    n, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
    
        adj[u].append(v)
        adj[v].append(u)
    
    dfs(0, -1, k, adj)
    
    print(ans)

if __name__  == '__main__':
    main()
