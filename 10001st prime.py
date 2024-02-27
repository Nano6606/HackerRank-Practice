QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true

# By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
# What is the Nth prime number?

SOLUTION:-

result = [2]
for x in range(3, 110000, 2):
    m=True
    for i in range(3, int(x**0.5)+1, 2):
        if x %i==0:
            m=False
            break
    if m:
        result.append(x)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(result[n-1])
