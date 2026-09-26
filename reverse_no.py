num = int(input("enter the number:"))
reverse = 0 
# 7789
while(num > 0):
    last_digit = num % 10
    num = num // 10
    reverse = (reverse * 10) + last_digit

print("reverse no is:",reverse)