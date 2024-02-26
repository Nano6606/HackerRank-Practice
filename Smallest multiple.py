QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true


SOLUTION:-

import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
def smallest_multiple(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))

