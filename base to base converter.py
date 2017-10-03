print('Base to Base Converter')

digits = "0123456789ABCDEF"
check = 0
try:
    input_str = input('Give me a base string: ')
    base_from = int(input("Please enter it's base (1 - 16): "))
    while base_from > 16:
        base_from = int(input("Please enter a valid base (1 - 16): "))
    temp = input_str
    new_int = 0
    power = 0
    while len(temp) > 0:
        bit = int(digits.index(temp[-1]))
        new_int = new_int + bit * base_from ** power
        temp = temp[:-1]
        power += 1

    base_to = int(input("Please enter a base to convert to (1 - 16): "))
    while base_to > 16:
        base = int(input("Please enter a valid base (1 - 16): "))
    output_str = ''
    while new_int > 0:
        check = new_int % base_to
        digit = digits[check]
        output_str = digit + output_str
        new_int //= base_to

    print(input_str,'in base',base_from, 'converted to base', base_to, 'is', output_str)



except ValueError as e:
    print("You made an error. Try again.")