n = int(input("enter your number:"))
dup = n
sum = 0

while(n > 0):
    last_digit = n % 10
    n = n//10
    sum = sum + (last_digit**3)

if sum == dup:
    print(sum,"is a ARMSTRONG number...")
else:
    print(sum,"it is not a armstrong number...")