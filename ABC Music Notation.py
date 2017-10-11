input_file = open('hnr1.abc','r')

music = input_file.read()

output = str.split(music,'X:')
#for line in music:
 #   print(line)

#for line in music:
 #    if line[0:2] == "X:":
  #       print(line)

print(type(output))

print(output)