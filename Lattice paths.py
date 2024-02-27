QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler015/problem?isFullScreen=true

# This problem is a programming version of Problem 15 from projecteuler.net

SOLUTION:-

import math
for i in range(int(input())):
    n, m=map(int, input().split())
    print(math.comb(n+m, m) %(10**9+7))
