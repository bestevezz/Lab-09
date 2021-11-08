def factorial(n):
    # an iterative example of the factorial function
    total = 1
    for i in range(0, n, 1):
        # i < n ensures that i will never reach n
        total = total * (n - i)
        # and therefore we never multiply by 0
        print("Current value of i is : ", i)
        print("Current value of total is : ", total)
    return total


userString = input("number please! ")
usernum = int(userString, 10)

print((usernum), ("! is "), factorial(usernum))
# if you use commas, you dont need to convert to a str
