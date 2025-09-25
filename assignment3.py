#Fectorial use function
 
# def fectorial(p):
#     if n<0 or n==0:
#         print("Please enter positive number")
#     fect=1
#     for i in range (1,n+1):
#         fect=i*fect
#     return fect
# n=int(input("Enter number: "))
# k=(fectorial(n))
# print (k)


#Task2  
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n*factorial(n-1))
# n=int(input("Enter Number: "))
# print("Factorial of",n,"is",factorial(n))





import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate square root
sqrt_result = math.sqrt(num)

# Calculate natural logarithm (log base e)
# Note: log is undefined for non-positive numbers
if num > 0:
    log_result = math.log(num)
else:
    log_result = "undefined (logarithm only defined for positive numbers)"

# Calculate sine (in radians)
sine_result = math.sin(num)

# Display results
print(f"\nResults for the number {num}:")
print(f"Square root: {sqrt_result}")
print(f"Natural logarithm: {log_result}")
print(f"Sine (in radians): {sine_result}")
