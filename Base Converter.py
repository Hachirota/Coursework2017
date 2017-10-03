print('Int to base')

digits = "0123456789ABCDEF"
check = 0
try:
    int_str = input('Give me an int: ')
    myInt = int(int_str)
    base = int(input("Please enter a valid base (1 - 16): "))
    while base > 16:
        base = int(input("Please enter a valid base (1 - 16): "))
    bin_str = ''
    while myInt > 0:
        check = myInt % base
        digit = digits[check]
        bin_str = digit + bin_str
        myInt //= base

    print(int_str,' in base ',base, ' is', bin_str)

    print('\nBase to int')
    bin_str = input('Give me a base string: ')
    base = int(input("Please enter a valid base (1 - 16): "))
    while base > 16:
        base = int(input("Please enter a valid base (1 - 16): "))
    temp = bin_str
    new_int = 0
    power = 0
    while len(temp) > 0:
        bit = int(digits.index(temp[-1]))
        new_int = new_int + bit * base ** power
        temp = temp[:-1]
        power += 1

    print(bin_str, ' in base',base, 'to integer is', new_int)

except ValueError as e:
    print("You made an error. Try again.")