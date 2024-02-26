QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true

SOLUTION:

def largest_palindrome_less_than(n):
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < n and product > largest_palindrome:
                product_str = str(product)
                if product_str == product_str[::-1]:
                    largest_palindrome = product
    return largest_palindrome

# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    print(largest_palindrome_less_than(n))
