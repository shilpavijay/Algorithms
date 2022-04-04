'''
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap. 

Example: 

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.
'''

class Job:
    def __init__(self,st,et,weight):
        self.start_time = st
        self.end_time = et
        self.weight = weight

def job_scheduling(n,jlist):   
        sorted_jlist = sorted(jlist,key=lambda x: x.weight,reverse=True)
        start_time, end_time, max_weight=sorted_jlist[0].start_time, sorted_jlist[0].end_time,sorted_jlist[0].weight
        l = [sorted_jlist[0]]
        for i in range(1,n-1):
            if start_time < sorted_jlist[i].start_time < end_time or end_time < sorted_jlist[i].end_time < end_time:
                continue
            else:
                l.append(sorted_jlist[i])
        return l


j1 = Job(1,2,50)
j2 = Job(3,5,20)
j3 = Job(6,19,100)
j4 = Job(2,100,200)

for each in job_scheduling(4,[j1,j2,j3,j4]):
    print(each.weight)
