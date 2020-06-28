#Richard Cheung U30429525
#cs440 LCS

def LCS(length, first, second):
    lcs = [[None for a in range(length + 1)] for b in range(length + 1)]
    for c in range(length + 1):
        for d in range(length + 1):
            if c == 0 or d == 0:
                lcs[c][d] = 0
            elif first[c - 1] == second[d - 1]:
                lcs[c][d] = lcs[c - 1][d - 1] + 1
            else:
                lcs[c][d] = max(lcs[c - 1][d], lcs[c][d - 1])
    returnVal = ''
    i = j = length
    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            returnVal = first[i - 1] + returnVal
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return returnVal

def main():
    f = open('input', 'r')
    length = int(f.readline())
    first = f.readline().strip('\n')
    second = f.readline().strip('\n')
    answer = LCS(length,first,second)
    output = open('output', 'w+')
    output.write(answer)
    output.close()
    
if __name__ == "__main__":
    main()
