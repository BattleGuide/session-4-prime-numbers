def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "cant divide by zero"
        return a / b
    else:
        return "wrong operation"


num = int(input("enter number: "))

if is_prime(num):
    print("prime")
else:
    print("not prime")

a = float(input("enter first num: "))
b = float(input("enter second num: "))
op = input("enter operation: ")

print(calculator(a, b, op))

input("press enter to exit")