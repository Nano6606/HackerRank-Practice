QUESTION LINK:-
https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem?isFullScreen=true

# This problem is a programming version of Problem 12 from projecteuler.net on hackerrank

SOLUTION:-

def prime_factorizer(n):
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    p = 3
    while p * p <= n:
        while n % p == 0:
            n //= p
            factors.append(p)
        p += 2
    if n > 1:
        factors.append(n)
    return factors
def no_of_divisors(n):
    count = 1
    p = 2
    while p * p <= n:
        exp = 0
        while n % p == 0:
            exp += 1
            n //= p
        count *= (exp + 1)
        p += 1 if p == 2 else 2
    if n > 1:
        count *= 2
    return count
def find_triangle_number(N):
    x = 1
    while True:
        if x % 2 == 0:
            if no_of_divisors(x // 2) * no_of_divisors(x + 1) > N:
                break
        else:
            if no_of_divisors(x) * no_of_divisors((x + 1) // 2) > N:
                break
        x += 1
    return x * (x + 1) // 2
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        result = find_triangle_number(n)
        print(result)
