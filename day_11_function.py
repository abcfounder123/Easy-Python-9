
"""

4. Function
   - code reuse
   - call, invoke   => ( )

##########################################

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")
print('-' * 42)

##########################################

Step.1


def m2():
    for r in range(1, 13, 1):
        print(f"2 x {r} = {2 * r}")
    print('-' * 42)


def m3():
    for r in range(1, 13, 1):
        print(f"3 x {r} = {3 * r}")
    print('-' * 42)


def m4():
    for r in range(1, 13, 1):
        print(f"4 x {r} = {4 * r}")
    print('-' * 42)


m2()
m2()
m2()
m3()
m4()

##########################################

Step.2


def m(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=2)
m(l=3)
m(l=4)

##########################################

Step.3

def m12(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


def m10(l):
    for r in range(1, 11, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m12(2)
m10(2)

##########################################

Step.4


def m(l, n):
    for r in range(1, n+1, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=2, n=10)

####################################################################################

"""
