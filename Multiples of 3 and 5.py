QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true


SOLUTION:-

def sum_of_multiples_below_n(n, k):
    if n <= 0:
        return 0
    num_terms = (n - 1) // k
    last_term = num_terms * k
    if last_term == n: 
        num_terms += 1
    return (num_terms * (k + last_term)) // 2

def sum_of_multiples_3_or_5_below_n(n):
    sum_3 = sum_of_multiples_below_n(n, 3)
    sum_5 = sum_of_multiples_below_n(n, 5)
    sum_15 = sum_of_multiples_below_n(n, 15)
    return sum_3 + sum_5 - sum_15

t = int(input())

for _ in range(t):
    num = int(input())
    print(sum_of_multiples_3_or_5_below_n(num))
