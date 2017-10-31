import readurl

headers, body = readurl.get_url('http://mf2.dit.ie/googleprices.csv')

input_data = body.split('\n')

entries = []
input_data.pop(0)

for item in input_data:
    l = []
    w = item.split(",")
    for item in w:
        if w.index(item) > 0:
            item = float(item)
        l.append(item)
    entries.append(l)


entries.pop(-1)

print(type(entries[1][1]))

current_year = '2004'
current_month = '1'

list_of_yearly_averages = []
yearly_average = 0
count = 0

for item in entries:
    if current_year != item[0][:4]:
        list_of_yearly_averages.append((current_year,(yearly_average/count)))
        current_year = str(int(item[0][:4]))
        current_month = '1'
        count = 0
    if current_month != item[0][5:7]:
        current_month = item[0][5:7]
        count +=1
    yearly_average = yearly_average + (item[6] * item[5])


