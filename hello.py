#!
import sys

print("Nicks addition/subtraction  calculator")

'''add = int(input("input 1 for add or 2 for subtract: "))

num1 = int(input("enter the first Number: "))

num2 = int(input("enter the Second Number: "))


if add == 1:
    print(num1 + num2)
else:
    print(num1 - num2)'''

def add(num1, num2):
    """*SYNOPSIS OF FUNCTION*

    PARAMETER1 DESCRIPTION OF PARAMETER
    PARAMETER2
    .
    .
    .
    PARAMETER...
    """
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def main():
    print(add(1, 1))

    while True:
        cmd = input("input command>")
        cmd = cmd.replace(" ", "")
        print(cmd)
        if cmd.find("+") != -1:
            num = cmd.split("+")
            answer = add(int(num[0]), int(num[1]))
        elif cmd.find("-") != -1:
            num = cmd.split("-")
            answer = subtract(int(num[0]), int(num[1]))
        elif cmd.find("*") != -1:
            num = cmd.split("*")
            answer = multiply(int(num[0]), int(num[1]))
        else:
            num = cmd.split("/")
            answer = divide(int(num[0]), int(num[1]))

        print(answer)

    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)





