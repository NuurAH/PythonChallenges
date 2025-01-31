#Given 2 positive integers a and b, return the sum of all odd integers from a to b inclusively
a = 50
b = 100

#all values between a and b, checked to see if it is divisble by 2 using modulus operator. If it isn't then it is added to sum

sum = 0 
while a < b:
    a += 1  
    if a%2 !=0 :
        sum += a

print(sum)

#challenge value is 144

