#Richard Cheung
#cs330

def BF(n, m, s, edges):
    returnVal = [float('inf') for x in range(n)]
    returnVal[s] = 0
    for i in range(1, n):
        for i, j, k in edges:
            if returnVal[i] + k < returnVal[j] and returnVal[i] != float('inf'):
                returnVal[j] = returnVal[i] + k
    return returnVal

def main():
    f = open('input', 'r')
    n = int(f.readline())
    m = int(f.readline())
    s = int(f.readline())
    edges = []
    for line in f:
        vals = line.split(',')
        edges.append(list(map(int, vals)))
    answer = BF(n, m, s, edges)
    output = open('output', 'w+')
    for line in answer:
        output.write(str(line) + '\n')
    output.close()

if __name__ == "__main__":
    main()
