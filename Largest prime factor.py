QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true


SOLUTION:-

import math
def largest_prime_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n // i
    if n > 2:
        max_prime = n
    return max_prime
t = int(input())
for _ in range(t):
    n = int(input())
    print(largest_prime_factor(n))
