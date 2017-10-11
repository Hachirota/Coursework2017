def abc_formatter(song):
    output_format = str.splitlines(song)
    print(output_format[0]+" ",end='')
    print("... " + output_format[1][2:],end='')
    for line in output_format:
        if line [0:2] == "M:":
            print(" ... Time sig: " + line[2:] + " ",end='')
        if line [0:2] == "K:":
            print("... Key sig: " + line[2:])

input_file = open('hnr1.abc','r')

music = input_file.read()
output = str.split(music,'X:')

output.pop(0)

filelength = len(output)

for item in output:
    abc_formatter(item)

print("-"*65)
print("There are", (filelength), "tunes in the file.")
print("-"*65)
