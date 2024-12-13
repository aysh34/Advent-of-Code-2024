""" Given a lot of equations, each equation has a test value (before colon) and a series of numbers (after colon) like 
190: 19 10
324: 18 19

What to do?
1. Check each equation to see if it's possible to produce the test value by inserting operators(+,*) between the numbers.
2. At the end return the sum of all valid test values.

"""


def pares_input(eq):  # eq = "190: 10 19"
    val, num = eq.split(":")  # val=["190"],num=["10 19"]
    testVal = int(val)
    num = list(map(int, num.split()))
    return testVal, num


with open("Day 7\\input1.txt") as f:
    equations = f.readlines()
    for i in range(len(equations)):
        # print(type(lines[0]))
        t, n = pares_input(equations[i])
        print(t,n)
