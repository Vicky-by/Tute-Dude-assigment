#task 1 check if a number is even or odd

no=int(input("Enter Number: "))
if(no%2==1):
    print(no,"is an odd  number.")

else:
    print(no,"is an even number.")



#task2 
# sum of 1 to 50  use loop

total=0
for i in range(1,51):
    total += i
print("The sum of integers from 1 to 50 is:", total)
