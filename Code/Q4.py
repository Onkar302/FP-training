#4. roundOff a float number having only one decimal place (3.2 = 3; 4.8 =5 etc)
#Note: It is not allowed to use any inbuilt language function.

def roundOff(x):
    frac = (x*10)%10
    if(frac >= 5):
        return int((x*10)//10 + 1)
    else:
        return int((x*10)//10)

print(roundOff(4.8))
print(roundOff(3.2))
print(roundOff(101.1))
print(roundOff(101.5))
print(roundOff(29.4))

        
