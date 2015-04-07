def readJobs(filename):
    f = open(filename)
    
    N = int(f.readline().strip())
    #print N
    
    jobsDiff = []
    jobsRatio = []
    
    jobs = []
    
    for line in f:
        weight, length = int(line.strip().split(" ")[0]), int(line.strip().split(" ")[1])
        #print line + "; " + str(weight) + "; " + str(length)
        
        jobs.append((weight, length))
        
    jobsDiff = sorted(jobs, key = lambda x: (x[0] - x[1], x[0]), reverse = True)
    jobsRatio = sorted(jobs, key = lambda x: (float(x[0]*1.0/x[1])), reverse = True)
    
    return jobsDiff, jobsRatio
    
def calcWeightedSum(sortedjobs):
    wtsum = 0
    C = 0
    for job in sortedjobs:
        C = C + job[1]
        wtsum = wtsum + job[0]*C
    return wtsum
        
if __name__ == "__main__":
    jobsDiff, jobsRatio = readJobs('jobs.txt')
    
    #print str(len(jobsRatio)) + "; " + str(len(jobsDiff))
    
    print calcWeightedSum(jobsDiff)
    print calcWeightedSum(jobsRatio)
    
    
    