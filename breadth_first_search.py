#cs330 Programming Assignment 2
#Richard Cheung
#U30429525

def BFS(n, start_node, our_input):
    discovered_nodes = [False for i in range(len(our_input))]  #if node is discovered, discovered_nodes[i] becomes True
    our_queue = [start_node]   #our queue to keep track of which nodes we have to check
    returnlist = [[] for i in range(len(our_input))]   #our return that will give us the neighbors from our bfs search
    while(our_queue): #keeps running until we have an empty queue
        cur_node = our_queue[0]   #gets the next node we have to check
        our_queue = our_queue[1:] #pops the node we're currently checking
        for x in our_input[cur_node]:  #accesses the neighbors of our current node from our_input
            if(discovered_nodes[x] == False):  #if we haven't found this node yet, add it to our return value
                discovered_nodes[x] = True        #we have no discovered the node, we will now no longer add an useless edge to another later node that might be neighbors with it
                returnlist[cur_node].append(x)    #when we find the new node, add it as a neighbor to our returnlist
                returnlist[x].append(cur_node)    #since cur_node is neighbors with x, x is neighbors with cur_node as well
                our_queue.append(x) #add this new discovered node to the queue of nodes that need to be checked
            #print(returnlist)
    return returnlist
    

def main():
    f = open('input', 'r', encoding = 'utf-8-sig')
    n = int(f.readline())      #number of nodes
    start_node = int(f.readline())   #value of our first node
    #print(n)
    #print(start_node)
    our_input = []  #going to be a list of lists for neighbors for each of our nodes
    read_f = f.readlines()   #rest of the lines
    #print(read_f)
    for i in range(len(read_f)):  #strips the \ns
        read_f[i] = read_f[i].strip()
    for x in read_f:
        if(x != '-'):    #checks for -
            neighbors = x.split(',')  #gets the neighbors of the current node that we're at
            our_input.append(list(map(int, neighbors)))  #for each item we have in neighbors, we're turning it into an int with the map function, all the ints will be a list (list function) which we'll be appending to our_input
        else:  #if the line is empty, append an empty list
            our_input.append([])
    #print(our_input)
    answer = BFS(n, start_node, our_input)
    output = open('output', 'w+')
    p = 0
    while(p < n):
        output.write(str(set(answer[p])).strip('{}') + '\n')    #set orders the list and gets rid of duplicates and uses {} which is why we strip it
        p += 1
    output.close()
        
    
if __name__ == "__main__":
    main()
