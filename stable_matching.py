#cs330 Programming Assignment 1
#Richard Cheung
#U30429525

#in the gs_algorithm, n is the amount of men or women and pref_1 and pref_2 are
#the lists of preferences for said men and women
def gs_algorithm(n, pref_1, pref_2):
    man_free = [-1] * n    #checks if the man is free
    woman_free = [-1] * n    #checks if the woman is free
    man_with = [-1] * n #list index is the man number and what's in the list index is the woman number
    proposal_amount = [0] * n #keeps track of how many times each man has proposed, helps us run in n^2 time as well
    while(-1 in man_free):
        m = man_free.index(-1)
        w = pref_1[m].index(proposal_amount[m])
        if(woman_free[w] == -1):        #if w is free, man is engaged with woman
            man_free[m] = 0
            woman_free[w] = 0
            proposal_amount[m] += 1
            man_with[m] = w
        elif(pref_2[w][m] < pref_2[w][man_with.index(w)]):    #if w isn't free but prefers the man proposing now to her current fiance
            man_free[man_with.index(w)] = -1
            man_with[man_with.index(w)] = -1
            man_free[m] = 0
            man_with[m] = w
            proposal_amount[m] += 1
        else:        #w rejects the proposer, the proposer increases their porposal amount by one
             proposal_amount[m] += 1
    return man_with

          
def main():
    f = open("pref_file_1", "r")
    read_f = f.readlines()
    #read_f = ['3', '2,0,1', '1,0,2', '2,1,0']
    #read_f = ['5', '2,1,3,4,0', '3,4,1,2,0', '2,3,4,0,1', '4,2,0,1,3', '4,1,3,0,2']
    pref_1 = []
    n = 0
    for i in range(len(read_f)):             #gets rid of \n at the end of each string in read_f
       read_f[i] = read_f[i].strip()
    for x in read_f:      #gets the number of people
        n = int(x)
        break
    i = 0
    for x in read_f:      #gives the preferences for the first gender; first n strings is person 1s preferences in order, etc.
        if(x == read_f[0]):     #skips the first line which is n
            pref_1 = pref_1
        else:             #adds each number in current line into our pref_1 list
            pref_1 += [x.split(',')]
            for x in pref_1[i]:
                pref_1[i][int(x)] = int(pref_1[i][int(x)])
            i += 1
    g = open("pref_file_2", "r")
    read_g = g.readlines()
    #read_g = ['3', '2,1,0', '2,1,0', '1,0,2']
    #read_g = ['5', '2,1,3,4,0', '2,1,4,3,0', '2,4,1,0,3', '4,0,1,2,3', '2,1,3,0,4']
    for k in range(len(read_g)):             #gets rid of \n at the end of each string in read_g
       read_g[k] = read_g[k].strip()
    pref_2 = []
    j = 0
    for x in read_g:
        if(x == read_g[0]):
            pref_2 = pref_2
        else:
            pref_2 += [x.split(',')]
            for x in pref_2[j]:
                pref_2[j][int(x)] = int(pref_2[j][int(x)])
            j += 1
    answer = gs_algorithm(n, pref_1, pref_2)
    output = open("output", "w+")
    for x in answer:
        output.write(str(answer.index(x)) + ',' + str(x) + "\n")
    output.close()


if __name__ == "__main__":
    main()
