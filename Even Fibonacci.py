QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges?filters%5Bstatus%5D%5B%5D=solved


SOLUTION:-

def fibonacci_sum_even(n):
    s = 0
    a, b = 1, 1
    while a <= n:
        if a % 2 == 0:
            s += a
        a, b = b, a + b
    return s

t = int(input())

for _ in range(t):
    n = int(input())
    print(fibonacci_sum_even(n))
