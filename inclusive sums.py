#Given 2 positive integers a and b, return the sum of all odd integers from a to b inclusively
a = 10
b = 25

#all values between a and b, and no positive integers add +1 to a and then see if it is divisble by 2

sum = 0 
while a < b:
    a += 1  
    if a%2 !=0 :
        sum += a
        print(sum)
    else:
       continue

#Have to print all my values here unsure on how to print only the last value
#challenge value is 144

