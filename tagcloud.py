import string
import httplib2


gettysburg = httplib2.Http(".cache")
headers, body = gettysburg.request("http://mf2.dit.ie/gettysburg.txt", "GET")

gettysburg = body.decode()
for char in gettysburg:
    if char in string.punctuation:
        gettysburg = gettysburg.replace(char,'')

gettysburg_list = gettysburg.split()
gettysburg_list = [element.lower() for element in gettysburg_list]

stopwords = httplib2.Http(".cache")
headers, body = stopwords.request("http://mf2.dit.ie/stopwords.txt")
stopwords = body.decode()

stopwords_list = stopwords.split(",")

wordlist = {}
wordcount = 0

for word in gettysburg_list:
    if not word in stopwords_list and len(word) > 3:
        wordcount = wordcount + 1
        if not word in wordlist:
            wordlist[word] = 1

        else:
            wordlist[word] = wordlist[word] + 1

with open("tagcloud.html","w") as f:
    f.write("""<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="UTF-8">
<title>Tag Cloud Generator</title>
</head>
<body>
<div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; 
border:1px solid black">""")
    for k, v in wordlist.items():
        f.write("<span style='font-size: %spx'> %s </span>" % (v * 10, k))
    f.write("""</div>
</body>
</html>""")