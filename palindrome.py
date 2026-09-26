n = int(input("enter your number:"))
number = n
reverse_no = 0
while (n > 0):
    last_digit = n % 10 
    n = n//10
    reverse_no = (reverse_no*10)+ last_digit
print(reverse_no)

if number == reverse_no:
    print("the number is palindrome...")

else:
    print("it is not palindrome...")



    
