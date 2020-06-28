#Richard Cheung
#U30429525
#cs330 PA6

def Kruskal(n, weight_start_end):
    return_val = [[] for x in range(n)] #initialize our return
    vertices = [x for x in range(n)]  #index corresponds with our vertices/nodes
    head = [1 for x in range(n)]  #initialize head to 1 for all
    for weight, start, end in weight_start_end:
        start_node = find(vertices, start)  #helper
        end_node = find(vertices, end)      #helper
        #print(start_node)
        #print(end_node)
        if(start_node != end_node):
            if(head[start_node] < head[end_node]):  
               vertices[start_node] = end_node
               head[start_node] += head[end_node]
            else:
               vertices[end_node] = start_node
               head[end_node] += head[start_node]
            return_val[start].append(end)
            return_val[end].append(start)
    return return_val

def find(vertices, node):  #helper
    if(vertices[node] == node):
       return node
    else:
       head = find(vertices, vertices[node])
       vertices[node] = head
       return head
       



def main():
    f = open('04_input', 'r')
    n = int(f.readline())  #number of vertices
    m = int(f.readline())  #number of edges
    read_f = f.readlines()
    #print(read_f)
    for i in range(len(read_f)):  #strip \n
        read_f[i] = read_f[i].strip()
    weight_start_end = []  #going to be list of lists, each list is weight, start node, end node
    for j in read_f:
        split_up = j.split(',')
        weight_start_end.append([int(split_up[2]), int(split_up[0]), int(split_up[1])])
    #print(weight_start_end)
    weight_start_end.sort()
    answer = Kruskal(n, weight_start_end)
    #print(answer)
    output = open('output', 'w+')
    for x in answer:
        x = str(x)
        x = x.strip('[]')
        #print(x)
        x = x.replace(' ', '')
        #print(x)
        output.write(x + '\n')
    output.close()




if __name__ == "__main__":
    main()
