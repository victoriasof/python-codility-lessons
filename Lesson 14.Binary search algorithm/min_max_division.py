"""
You are given integers K, M and a non-empty array A consisting of N integers. 
Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. 
The size of the block is any integer between 0 and N. 
Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. 
The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

    def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, 
returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and K are integers within the range [1..100,000];
        M is an integer within the range [0..10,000];
        each element of array A is an integer within the range [0..M].

"""

def blockSizeIsValid(A, max_block_cnt, max_block_size):

    block_sum = 0
    block_cnt = 0
 
    for element in A:
        if block_sum + element > max_block_size:
            block_sum = element
            block_cnt += 1

        else:
            block_sum += element

        if block_cnt >= max_block_cnt:
            return False
 
    return True
 
def binarySearch(A, max_block_cnt, using_M_will_give_you_wrong_results):

    lower_bound = max(A)
    upper_bound = sum(A)
 
    if max_block_cnt == 1:      
      return upper_bound
      
    if max_block_cnt >= len(A): 
      return lower_bound
 
    while lower_bound <= upper_bound:

        candidate_mid = (lower_bound + upper_bound) // 2

        if blockSizeIsValid(A, max_block_cnt, candidate_mid):
            upper_bound = candidate_mid - 1

        else:
            lower_bound = candidate_mid + 1
 
    return lower_bound
 
def solution(K, M, A):

    return binarySearch(A,K,M)


K = 3
M = 5

A = [2, 1, 5, 1, 2, 2, 2]

print(solution(K, M, A))

#https://www.martinkysel.com/codility-minmaxdivision-solution/