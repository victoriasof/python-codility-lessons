"""

Two positive integers N and M are given. 
Integer N represents the number of chocolates arranged in a circle, ...

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. 
Then you omit the next ... chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, 
then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. 
You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

    def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..1,000,000,000].

"""

def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def solution(N, M):
    lcm = N * M / gcd(N, M) # Least common multiple
    return lcm / M

N = 10
M = 4
print(solution(N,M))    

#https://codesays.com/2014/solution-to-chocolates-by-numbers-by-codility/

