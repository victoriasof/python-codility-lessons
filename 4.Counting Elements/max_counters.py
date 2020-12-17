"""
You are given N counters, initially set to 0, and you have two possible operations on them:
        ...
A non-empty array A of M integers is given. This array represents consecutive operations:
      ...
For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

    def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, 
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].

"""

def solution(counters, array):

    output = [0 for _ in range(counters)]
    #value of counters (0, 0, 0, 0, 0)

    for element in array:
    
        if element <= counters: 
            output[element-1] += 1 
            #indexes start at 0, but counters start at 1
            #value of counters after first operation (0, 0, 1, 0, 0)

        else: #if element>counters(6 in this example) then all counters take value of max counter 
            output = [max(output) for i in range(len(output))] 
    
    return output

counters = 5
array = [3, 4, 4, 6, 1, 4, 4]
#we max out at 6

print(solution(counters, array))

