# #Greedy algorithm to find the minimum number of coins needed to make a given amount.

# Task 1: Job Scheduling Problem

# Problem Statement: You're a job scheduler, and you have a list of jobs to schedule. Each job has a start time, an end time, and a profit associated with it. Your goal is to select the maximum number of non-overlapping jobs that maximize the total profit.

# Input:

#     n (the number of jobs)

#     For each job, you have a start time, end time, and profit:
#      start[i] end[i] profit[i] (n lines)

# Output: Print the maximum profit that can be earned by selecting jobs without overlap.

# Testcase 1:

# 4

# 1 3 50

# 2 5 20

# 3 6 70

# 5 8 60

# Answer: 120

def job_scheduling( n, job_list):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    
    job_list.sort(key=lambda x: x[1])
    max_profit=0
    prev_end=0
    for i in range(n):
        if job_list[i][0]>=prev_end:
            max_profit+=job_list[i][2]
            prev_end=job_list[i][1]
    return max_profit

n=int(input().strip())
job_list=[]
for i in range(n):
    job_list.append(list(map(int, input().split())))



print(job_scheduling(n,job_list))

