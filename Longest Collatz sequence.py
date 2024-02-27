QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem?isFullScreen=true

# This problem is a programming version of Problem 14 from projecteuler.net

SOLUTION:-

def collatz(n: int, lookup: list) -> int:
    if n <= 1:
        return 1  
    if n < len(lookup) and lookup[n] != 0:
        return lookup[n]    
    c = collatz(n // 2 if n % 2 == 0 else n * 3 + 1, lookup) + 1
    if n < len(lookup): 
        lookup[n] = c
    return c
def compute_collatz_numbers(n: int) -> list:
    lookup = [0] * (n + 1)
    longest = [0] * (n + 1)
    max_number = max_chain = -1
    for i in range(1, n + 1):
        c = collatz(i, lookup)
        if max_chain <= c:
            max_chain = c
            max_number = i
        longest[i] = max_number
    return longest
if __name__ == "__main__":
    T = int(input().strip())
    ns = [int(input().strip()) for _ in range(T)]
    longest = compute_collatz_numbers(max(ns))
    for n in ns: 
        print(longest[n])
