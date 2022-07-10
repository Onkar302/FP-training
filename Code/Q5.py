#5. Surprisingly there are only three numbers that can be written as the sum of fourth 
#powers of their digits:
#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14
#is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their 
#digits.

def checkFifthPower(x):
    res = 0
    number = x
    while(x > 0):
        digit = x%10
        res += (digit**5)
        x //= 10
    if (res == number):
        return True
    else:
        return False

def sumFifthPowers():
    sum = 0
    for i in range(2, 1000000):
        if(checkFifthPower(i)):
            sum += i
        i += 1
    print("Sum of all the numbers that can be written as the sum of fifth powers is:", sum)

sumFifthPowers()
