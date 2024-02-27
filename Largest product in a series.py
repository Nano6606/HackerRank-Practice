QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true

# Find the greatest product of K consecutive digits in the N digit number.

SOLUTION:-

import sys
def max_product_of_consecutive_digits(n, k, num):
    max_product = 0
    for i in range(n - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= int(num[j])
        max_product = max(max_product, product)
    return max_product
if __name__ == "__main__":
    t = int(input().strip())  
    for _ in range(t):
        n, k = map(int, input().strip().split()) 
        num = input().strip() 
        result = max_product_of_consecutive_digits(n, k, num)
        print(result)
