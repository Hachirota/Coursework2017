import readurl

headers, body = readurl.get_url('http://mf2.dit.ie/googleprices.csv')

def sharePriceFormatter(line):
    a = line.split(",")
    Date.append(a[0])
    Open.append(a[1])
    High.append(a[2])
    Low.append(a[3])
    Close.append(a[4])
    AdjClose.append(a[5])
    Volume.append(a[6])


Date = []
Open = []
High = []
Low = []
Close = []
AdjClose = []
Volume = []

csv = body.split('\n')
csv.pop(0)
csv.pop(-1)
for line in csv:
    sharePriceFormatter(line)

OpenDict = dict(zip(Date,Open))
HighDict = dict(zip(Date,High))
LowDict = dict(zip(Date,Low))
CloseDict = dict(zip(Date,Close))
AdjCloseDict = dict(zip(Date,AdjClose))
VolumeDict = dict(zip(Date,Volume))


