QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true

# The sum of the primes below 10 is 2+3+5+7 = 17.
# Find the sum of all the primes not greater than given N.

SOLUTION:-

import math
def prime_sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return primes
def prime_sum(limit):
    primes = prime_sieve(limit)
    cumulative_sum = [0]
    current_sum = 0
    for i in range(1, limit + 1):
        if primes[i]:
            current_sum += i
        cumulative_sum.append(current_sum)
    return cumulative_sum
def main():
    limit = 10**6
    cumulative_sum = prime_sum(limit)
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(cumulative_sum[n])
if __name__ == "__main__":
    main()
