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
