"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: 
...

The difference between the two parts is ...
the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
A = [3, 1, 2, 4, 3]

We can split this tape in four places:
...

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, 
returns the minimal difference that can be achieved.

For example, given:
A = [3, 1, 2, 4, 3]

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];

"""

def solution(A):  

    left_sum = 0
    array_sum = sum(A)
    minval = float('inf')
    
    for i in A[:-1]: #It slices the string to omit the last character
        left_sum += i
        #minval = min(abs(array_sum - 2*left_sum), minval)
        minval = min(abs(left_sum + (left_sum - array_sum)), minval)
        #rewrote above line to make it more understandable for me 
    
    return minval

A = [3, 1, 2, 4, 3]
print(solution(A))    

#https://stackoverflow.com/questions/48030130/codility-tape-equilibrium-training-using-python
#https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
#float('inf') acts as an unbounded upper value for comparison. 
#This is useful for finding lowest values for something. 