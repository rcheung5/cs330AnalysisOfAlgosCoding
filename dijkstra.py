#Richard Cheung
#U30429525
import queue

def dijkstras(n, m, s, adj):
    priority = queue.PriorityQueue()
    returnList = [[float('infinity'), None] for i in range(n)]
    returnList[s] = [0,None]
    priority.put([0,s], 0)
    while(not priority.empty()):
        distance, vertex = priority.get()
        for (weight, end) in adj[vertex]:
            if returnList[end][0] > (distance + weight):
                returnList[end] = [distance + weight, vertex]
                priority.put([distance + weight, end], distance + weight)
    return returnList



def main():
    f = open('input', 'r')
    n = int(f.readline())  
    m = int(f.readline())  
    s = int(f.readline())
    read_f = f.readlines()
    adj = [[] for i in range(n)]
    for line in read_f:
        values = line.split(',')
        start, end, weight = (map(int, values))
        adj[start].append([weight,end])
    answer = dijkstras(n,m,s,adj)
    output = open('output', 'w+')
    for thing in answer:
        output.write(str(thing[0]) + ',')
        if thing[1] == None:
            output.write('-\n')
        else:
            output.write(str(thing[1]) + '\n')
    output.close()

if __name__ == "__main__":
    main()
    
