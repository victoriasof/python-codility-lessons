"""

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. 
The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) 
prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. 
These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), 
...

For example, consider an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

        (1, 26) is 10,
        (4, 10) is 4,
        (16, 20) is 0.

Write a function:

    def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M elements specifying the consecutive answers 
to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..50,000];
        M is an integer within the range [1..30,000];
        each element of arrays P, Q is an integer within the range [1..N];
      ...

"""

"""
#FIRST SOLUTION 

#Firstly use the sieve of Eratosthenes to workout what is prime.

def get_sieve(n):
    # Use the sieve or Eratosthenes to produce an array of primes 
    # where factor[n] == 0 indicates a prime number
    factors = [0] * (n+1)
    i=2
    i2 = i*i

    while (i2 <= n):
        if not factors[i]:
            k = i2
            while k <= n:
                if not factors[k]:
                    factors[k] = i
                k += i
        i += 1
        i2 = i*i
    return factors

#Next, determine if the number is semi prime. If both its factors are prime its semiprime.

def is_semi_prime(n, factors):
    if factors[n]: # Check its not a prime
        for r in range(int(n**.5)+1, 1, -1):
            if not n%r:
                d = n//r
                return (not factors[d]) and (not factors[r])
    return False

#Then scan the range up to N numbers to count slope of increasing semi primes. 
#simply measure the slope within a slice to see how many semi primes occur during that slice.

def solution(N, P, Q):
    # produce a slope of increasing semi primes
    factors = get_sieve(N)
    slope = [0] * (N+1)
    for i in range(1, N+1):
        slope[i] = slope[i-1] + is_semi_prime(i, factors) # Auto casting!! :-)
    # Optimus Prime!
    # print(list(enumerate(slope)))
    return [slope[Q[j]] - slope[P[j]-1] for j in range(len(P))]
"""

#SECOND SOLUTION:

def make_primes(N):

    primes=[-1]*N
    c=2

    while c*c < N:
        ii=2*c
        while(ii<N):
            primes[ii]=c
            ii+=c
        c+=1
    return primes

def solution(N, P, Q):
    N=N+1
    primes=make_primes(N)
    prefix=[0]*N

    for x in xrange(1,N):
        prefix[x]=prefix[x-1]
        first_factor=primes[x]
        second_factor=x/first_factor

        if(primes[x]!=-1 and primes[first_factor]==-1 and primes[second_factor]==-1):
            prefix[x]+=1
    results=[]

    for r in xrange(len(P)):
        results.append(prefix[Q[r]]-prefix[P[r]-1])

    return results


N = 26
P = [1, 4, 16] 
Q = [26, 10, 20]  
print(solution(N, P, Q))


#https://codesays.com/2014/solution-to-count-semiprimes-by-codility/
#https://stackoverflow.com/questions/53902549/count-the-semiprime-numbers-in-the-given-range-a-b