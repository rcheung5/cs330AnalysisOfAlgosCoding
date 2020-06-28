#Richard Cheung
#cs330
def BFS(adj, s, t, p):
    visited = [False for x in range(len(adj))]
    visited[s] = True
    q = []
    q.append(s)
    while(q):
        i = q[0]
        q = q[1:]
        for j in adj[i]:
            if not visited[j] and adj[i][j] > 0:
                q.append(j)
                visited[j] = True
                p[j] = i
    return visited[t]

def FF(n, s, t, edges):
    adj = [{} for x in range(n)]
    for i, j, k in edges:
        adj[i][j] = k
        adj[j][i] = 0
    p = [-1 for x in range(n)]
    maxFlow = 0
    while(BFS(adj, s, t, p)):
        pathFlow = float('inf')
        a = t
        while(a != s):
            pathFlow = min(pathFlow, adj[p[a]][a])
            a = p[a]
        maxFlow += pathFlow
        j = t
        while(j != s):
            i = p[j]
            adj[i][j] -= pathFlow
            adj[j][i] += pathFlow
            j = i
    returnVal = []
    for i in edges:
        if(len(i) == 3):
            i, j, k = i
            returnVal.append([i, j, adj[j][i]])
    return returnVal
                

def main():
    f = open('input', 'r')
    n = int(f.readline())
    m = int(f.readline())
    s = int(f.readline())
    t = int(f.readline())
    read_f = f.readlines()
    edges = []
    for line in read_f:
        edges.append(list(map(int, line.split(','))))
    answer = FF(n, s, t, edges)
    output = open('output', 'w+')
    for edge in answer:
        output.write(str(edge).strip('[]').replace(' ', '') + '\n')
    output.close()

if __name__ == "__main__":
    main()
