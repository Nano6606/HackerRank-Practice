QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem?isFullScreen=true

# Work out the first ten digits of the sum of N 50 - digit numbers.

SOLUTION:-

def first_10_digits_of_sum(numbers):
    total = sum(int(num) for num in numbers)
    return str(total)[:10]
if __name__ == "__main__":
    n = int(input().strip())
    numbers = [input().strip() for _ in range(n)]
    result = first_10_digits_of_sum(numbers)
    print(result)
