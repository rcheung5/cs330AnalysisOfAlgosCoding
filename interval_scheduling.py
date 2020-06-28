#cs330 Programming Assignment
#Richard Cheung
#U30429525


def interval_scheduling(start_times, finish_times, n):
    jobs_finish_start = list(zip(finish_times, start_times))  #jobs zipped together by finish and start time where index 0 has the first job
    sorted_by_finish = sorted(jobs_finish_start)   #previous list but sorted
    answer = [jobs_finish_start.index(sorted_by_finish[0])]
    #print(answer)
    i = 1
    while(i < n):
        #if(start_times[jobs_finish_start.index(sorted_by_finish[i])] > finish_times[answer[-1]]):  #if the start time of the job we're up to has a finish time after the last job we've added to our job list
        if(jobs_finish_start[jobs_finish_start.index(sorted_by_finish[i])][1] > finish_times[answer[-1]]):
            answer.append(jobs_finish_start.index(sorted_by_finish[i]))                  
        i += 1
    #print(answer)
    return answer


def main():
    f = open('03_input', 'r')
    n = int(f.readline())   #amount of requests
    read_f = f.readlines()
    print(read_f)
    start_times = []
    finish_times = []
    for i in range(len(read_f)):     #strip \n
        read_f[i] = read_f[i].strip()
    for j in read_f:                 #make two lists, one of start_time, one of finish_time
        print(j)
        start_fin = j.split(',')
        print(start_fin)
        start_times.append(int(start_fin[0]))
        finish_times.append(int(start_fin[1]))
    #print(start_times)
    #print(finish_times)
    answer = interval_scheduling(start_times, finish_times, n)
    output = open('output', 'w+')
    for x in answer:
        output.write(str(x) + '\n')
    output.close()


if __name__ == "__main__":
    main()
