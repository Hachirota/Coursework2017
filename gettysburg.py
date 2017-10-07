import string
import urllib.request

with urllib.request.urlopen("http://mf2.dit.ie/gettysburg.txt") as response:
    gettysburg_bytes = response.read()

gettysburg = gettysburg_bytes.decode("utf-8")
for char in gettysburg:
    if char in string.punctuation:
        gettysburg = gettysburg.replace(char,'')
gettysburg_list = gettysburg.split()
gettysburg_list = [element.lower() for element in gettysburg_list]

with urllib.request.urlopen("http://mf2.dit.ie/stopwords.txt") as response:
    stopwords_bytes = response.read()

stopwords = stopwords_bytes.decode("utf-8")

stopwords_list = stopwords.split(",")

whitespace = str.split(string.whitespace)

punctuation = str.split(string.punctuation)

wordlist = {}
wordcount = 0

for word in gettysburg_list:
    if not word in stopwords_list:
        wordcount = wordcount + 1
        if not word in wordlist:
            wordlist[word] = 1

        else:
            wordlist[word] = wordlist[word] + 1


print("The number of words in the speech, excluding 'Stop Words' is: ", wordcount)
print ("The number of unique words is: ",len(wordlist))

for k,v in wordlist.items():
    print(k, v)
