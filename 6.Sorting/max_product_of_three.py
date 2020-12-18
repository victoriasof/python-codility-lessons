"""
A non-empty array A consisting of N integers is given. 
...

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        ...
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

    ...

"""

def solution(A):
    
  #A = sorted(A)
  A.sort()

  return max(A[-3]*A[-2]*A[-1] , A[0]*A[1]*A[-1])
  #split array into two sections and return max of either section 
  #If an index has a negative value, it counts backward from the end of the list
  #numbers[-1] is the last element of the list, numbers[-2] is the second to last...
  #remember that two negatives equal positive

A = [-3, 1, 2, -2, 5, 6]
print(solution(A))

#https://codesays.com/2014/solution-to-max-product-of-three-by-codility/
#https://www.youtube.com/watch?v=vslRM80lvrY




