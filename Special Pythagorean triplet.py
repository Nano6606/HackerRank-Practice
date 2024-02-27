QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true

# Given , Check if there exists any Pythagorean triplet for which a+b+c=n. 
# Find maximum possible value of abc among all such Pythagorean triplets.
# If there is no such Pythagorean triplet print -1.

SOLUTION:-

def lint(n):
    if type(n) == int:
        return n
    else:
        return int(n)+1
t = int(input())
for a0 in range(t):
    n = int(input())
    products=[]
    for a in range(1, lint(n/3)):
        b=(n-a-a**2/(n-a))/2
        if b==int(b):
            b=int(b)
            products.append(a*b*(n-a-b))
    if products:
        print(max(products))
    else:
        print(-1)
