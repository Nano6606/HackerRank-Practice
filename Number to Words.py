QUESTION LINK:- 
https://www.hackerrank.com/contests/projecteuler/challenges/euler017/problem?isFullScreen=true

# Given a number, you have to write it in words. First character of each word will be capital letter 

SOLUTION:-

ones = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
thousands = {1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'}
def number_to_words(n):
    if n == 0:
        return 'Zero'
    def number(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n]
        else:
            a = n % 10
            b = n // 10
            return tens[b] + ('' if a == 0 else ' ' + ones[a])
    def number_group(n):
        if n < 100:
            return number(n)
        else:
            a = n % 100
            b = n // 100
            return ones[b] + ' Hundred' + ('' if a == 0 else ' ' + number(a))
    if n < 1000:
        return number_group(n)
    else:
        chunks = []
        while n > 0:
            chunks.append(n % 1000)
            n //= 1000
        result = number_group(chunks[0])
        for i in range(1, len(chunks)):
            if chunks[i] != 0:
                result = number_group(chunks[i]) + ' ' + thousands[i] + ' ' + result
        return result
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num = int(input())
        print(number_to_words(num).capitalize())  # Capitalize the first letter
