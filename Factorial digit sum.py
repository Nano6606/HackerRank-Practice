QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem?isFullScreen=true

#  This problem is a programming version of Problem 20 from projecteuler.net

SOLUTION:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
T = int(input())
for _ in range(T):
    N = int(input())
    factorial_N = factorial(N)
    print(sum_of_digits(factorial_N))
