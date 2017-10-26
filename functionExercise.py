import ast

def gcd(tup1):
    a, b = tup1
    while b != 0:
        c = b
        b = a % b
        a = c
    return a


def lcm(tup1):
    a,b = tup1
    output = (a * b) / gcd(tup1)
    return output


def addfrac(tup1, tup2):
    a, b = tup1
    c, d = tup2
    cd = lcm((b,d))
    e = a * (cd / b)
    f = c * (cd / d)
    output = (int(e + f), int(cd))
    return output


def subfrac(tup1, tup2):
    a, b = tup1
    c, d = tup2
    cd = lcm((b,d))
    e = a * (cd / b)
    f = c * (cd / d)
    output = (int(e - f), int(cd))
    return output


def reduce(tup1):
    a, b = tup1
    c = gcd(tup1)
    output = (int(a / c), int(b/c))
    return output


print("""Please select the function you wish to use:
1: Greatest Common Divisor
2: Least Common Multiple
3: Add Two Fractions
4: Subtract Two Fractions
5: Simplify Two Fractions\n""")

option = input("")

if option == "1":
     print("Please enter your numbers in the format: 'Biggest, Smallest'")
     gcdtuple = ast.literal_eval(input(""))
     print(gcd(gcdtuple))

elif option == "2":
    print("Please enter your numbers in the format 'num1, num2'")
    lcmtuple = ast.literal_eval(input(""))
    print(int(lcm(lcmtuple)))

elif option == "3":
    print("Please enter the first fraction to be added in the format: 'Numerator, Denominator")
    addfractup1 = ast.literal_eval(input(""))

    print("Please enter the second fraction to be added in the format: 'Numerator, Denominator")
    addfractup2 = ast.literal_eval(input(""))

    print(addfrac(addfractup1,addfractup2))

elif option == "4":
    print("Please enter the first fraction in the format: 'Numerator, Denominator")
    subfractup1 = ast.literal_eval(input(""))

    print("Please enter the fraction to be subtracted in the format: 'Numerator, Denominator")
    subfractup2 = ast.literal_eval(input(""))

    print(subfrac(subfractup1,subfractup2))

elif option == "5":
    print("Please enter a fraction to be simplified in the format: 'Numerator, Denominator")
    simplifytup = ast.literal_eval(input(""))

    print(reduce(simplifytup))

else:
    print("Invalid Option")