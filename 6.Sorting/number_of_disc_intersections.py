"""
We draw N discs on a plane. ...
An array A of N non-negative integers, specifying the radiuses of the discs, is given. 
The J-th disc is drawn with its center at (J, 0) and radius A[J].

...
have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, 
returns the number of (unordered) pairs of intersecting discs. 
...

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

"""

#stackoverflow solution:
"""
from bisect import bisect_right

def solution(A):
    pairs = 0

    # create an array of tuples, each containing the start and end indices of a disk
    # some indices may be less than 0 or greater than len(A), this is fine!
    # sort the array by the first entry of each tuple: the disk start indices
    intervals = sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )

    # create an array of starting indices using tuples in intervals
    starts = [i[0] for i in intervals]

    # for each disk in order of the *starting* position of the disk, not the centre
    for i in range(len(starts)):

        # find the end position of that disk from the array of tuples
        disk_end = intervals[i][1]

        # find the index of the rightmost value less than or equal to the interval-end
        # this finds the number of disks that have started before disk i ends
        count = bisect_right(starts, disk_end )

        # subtract current position to exclude previous matches
        # this bit seemed 'magic' to me, so I think of it like this...
        # for disk i, i disks that start to the left have already been dealt with
        # subtract i from count to prevent double counting
        # subtract one more to prevent counting the disk itsself
        count -= (i+1)
        pairs += count
        if pairs > 10000000:
            return -1
    return pairs
"""
#more understandable solution for me: 

from bisect import bisect_right
#This module provides support for maintaining a list in sorted order 
# without having to sort the list after each insertion.

def solution(A):
        start = [i-j for i, j in enumerate(A)]
        #use enumarate() to have a variable that changes on each loop iteration. 

        start.sort()
        pairs = 0

        for i in range(0, len(A)):

                end = i + A[i]
                count = bisect_right(start, end)

                count_1 = count-1
                count_2 = count_1-i

                pairs += count_2        

        return pairs


A = [1, 5, 2, 1, 4, 0]
print(solution(A))

#https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
#https://www.youtube.com/watch?v=NYjnoZulqrQ&t=61s
