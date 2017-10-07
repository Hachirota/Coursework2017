music = open('hnr1.abc','r')

#for line in music:
    #print(line)

for line in music:
     if line[0:2] == "X:":
         print(line)
