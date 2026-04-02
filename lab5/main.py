# Question 1
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# Question 2
term = lambda x, n: (x ** n) / factorial(n)

def exp_x(x, n):
    total = 0
    i = 0
    while i <= n:
        total = total + term(x, i)
        i = i + 1
    return total


# Question 3
total_sum = 0

def alternating_series(n):

    global total_sum

    if n == 0:
        return

    alternating_series(n - 1)

    if n % 2 == 1:
        total_sum = total_sum + (1 / n)
    else:
        total_sum = total_sum - (1 / n)


# MAIN PART
print("1. Factorial")
num = int(input("Enter a number for factorial: "))
print("Factorial =", factorial(num))

print()

print("2. e^x calculation")
x = int(input("Enter x: "))
n = int(input("Enter n: "))
print("Result =", exp_x(x, n))

print()

print("3. Alternating series")
n2 = int(input("Enter n: "))
alternating_series(n2)
print("Series result =", total_sum)