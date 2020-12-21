"""
A non-empty array A consisting of N integers is given. 
...
(notice that the slice contains at least two elements). 
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] 
divided by the length of the slice. 
...

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, 
returns the starting position of the slice with the minimal average. 
If there is more than one slice with a minimal average, 
you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        ...

"""
"""
WRONG SOLUTION 
def solution(A):

    min_avg = (A[0]+A[1])/2
    min_idx = 0

    for i in range(0, len(A)-2):
        avg_2 = (A[i]+A[i+1])/2
        avg_3 = (A[i]+A[i+1]+A[i+2])/3
        tmp3 = (A[-2] + A[-1])/2

        if min_avg > avg_2:
            min_idx = i
            min_avg = avg_2
            
        if min_avg > avg_3:
            min_idx = i   
            min_avg = avg_3
             
        #avg_2 = (A[-2] + A[-1])/2

    if min_avg > tmp3:
        idx = len(A)-2
        min_avg = (A[-1] + A[-2])/2    

    return min_idx
"""

def solution(A):
    #if(len(A) < 2):
    #    return 0;

    index=0
    min_avg=(A[0]+A[1])/2
    
    for i in range(1,len(A)-1):
        avg=(A[i]+A[i+1])/2

        if(avg<min_avg):
            min_avg=avg
            index=i   

    for i in range(0,len(A)-2):
        avg=(A[i]+A[i+1]+A[i+2])/3

        if(avg<min_avg):
            min_avg=avg
            index=i        

    return index 


A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))

#https://stackoverflow.com/questions/21635397/min-average-two-slice-codility
#https://www.youtube.com/watch?v=w0eFQwiKY7k
