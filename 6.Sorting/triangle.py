"""
An array A consisting of N integers is given. 
...
..
For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, 
returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. 

Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Write an efficient algorithm for the following assumptions:

       ...

"""

def solution(A):
  
  A.sort()

  for i in range(len(A)-2):
    if A[i] + A[i+1] > A[i+2]:
      return 1

  else:
    return 0    


A = [10, 2, 5, 1, 8, 20]
print(solution(A))

A = [10, 50, 5, 1]
print(solution(A))


#https://stackoverflow.com/questions/44912099/triangle-determine-if-an-array-includes-a-triangular-triplet-codility
#https://www.youtube.com/watch?v=od90LeHWXPM

