QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem?isFullScreen=true

# 29 = 512 and the sum of its digits is 5+1+2 =8. 
# What is the sum of the digits of the number 2N?

SOLUTION:-

def sum_of_digits_of_power_of_2(exponent):
    power_of_2 = 2 ** exponent
    digit_sum = 0
    while power_of_2 > 0:
        digit_sum += power_of_2 % 10
        power_of_2 //= 10
    return digit_sum
if __name__ == "__main__":
    for _ in range(int(input())):
        exponent = int(input())
        print(sum_of_digits_of_power_of_2(exponent))
