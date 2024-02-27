QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true

#Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.

SOLUTION:-
import sys
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6
def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2
if __name__ == "__main__":
    t = int(input())  
    for _ in range(t):
        n = int(input())  
        sum_squares = sum_of_squares(n)
        square_sum = square_of_sum(n)
        difference = abs(sum_squares - square_sum)
        print(difference)

