QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler018/problem?isFullScreen=true

# This problem is a programming version of Problem 18 from projecteuler.net

SOLUTION:

def maximum_total(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

T = int(input())
for _ in range(T):
    N = int(input())
    triangle = []
    for _ in range(N):
        row = list(map(int, input().split()))
        triangle.append(row)
    
    print(maximum_total(triangle))
