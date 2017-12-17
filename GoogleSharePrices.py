import read_url  # importing the external readurl
import operator  # importing the operator module used in sorting the list of averages


def printformatter(tup1):  # function to format the output of the program as a table
    a, b = tup1
    print('{0:9} =>   {1}'.format(a,b))

headers, body = read_url.get_url('http://mf2.dit.ie/googleprices.csv') #importing the data from an external site

input_data = body.split('\n')  # splitting the data on the newline characters

entries = []
input_data.pop(0)  # removing the first entry in the list (column headers)

for item in input_data:
    l = []  # opening a new list to allow creation of a list of lists
    w = item.split(",")  # splitting line on the comma
    for item in w:
        if w.index(item) > 0:
            item = float(item)  # turning every element of the new list except the date into a float
        l.append(item)
    entries.append(l)  # adding the created list to the overall list

entries.pop(-1)  # removing the empty list at the end of our list

# declaring the starting date variables
current_year = '2004'
current_month = '01'

# declaring all the counts and lists used in the next section of code
list_of_yearly_averages = []
yearly_average = 0
yearly_price = 0
yearly_volume = 0
list_of_monthly_averages = []
monthly_average = 0
monthly_price = 0
monthly_volume = 0

# for every list in the list of lists:
for item in entries:
    if current_month != item[0][5:7]:  # check to see if the month being totalled has ended
        if monthly_price != 0:  # prevent divide by zero errors
            monthly_average = monthly_price / monthly_volume  # calculate the average
            yearly_price = yearly_price + monthly_price  # add the monthly price to the yearly total
            yearly_volume = yearly_volume + monthly_volume # same with volume
            monthly_price = 0  # reset both price & volume variables
            monthly_volume = 0
            list_of_monthly_averages.append((current_year + "-" + current_month,monthly_average))  # add the calculated
            # average to our list of averages
        current_month = item[0][5:7]  # set the month to the month of the current entry

    if current_year != item[0][:4]:  # check to see if the year being totalled has ended
        if yearly_price != 0:  # prevent divide by zero errors
            yearly_average = yearly_price / yearly_volume  # calculate the average for the year
            list_of_yearly_averages.append((current_year,(yearly_average)))  # add to list of yearly averages
            yearly_price = 0  # reset price and volume variables
            yearly_volume = 0
        current_year = item[0][:4]  # set year to the year of the current entry

    # now if the current month and current year match
    daily_price = item[6] * item[5]  # calculate the daily price
    monthly_price = monthly_price + daily_price  # add this daily price to the monthly running total
    monthly_volume = monthly_volume + item[6]  # add the volume to the monthly running total

# The loop through the list of lists would does not calculate the final monthly and yearly averages as
# the final current year and month variables will never be able to not match the final entry in the list.
# This block of code addresses that
monthly_average = monthly_price / monthly_volume
yearly_price = yearly_price + monthly_price
yearly_volume = yearly_volume + monthly_volume
list_of_monthly_averages.append((current_year + "-" + current_month,monthly_average))
yearly_average = yearly_price / yearly_volume
list_of_yearly_averages.append((current_year,yearly_average))


# Sort our lists in ascending order
list_of_yearly_averages = sorted(list_of_yearly_averages,key=operator.itemgetter(1))
list_of_monthly_averages = sorted(list_of_monthly_averages,key=operator.itemgetter(1))


worst_six_months = list_of_monthly_averages[:6]
best_six_months = list_of_monthly_averages[-6:]

worst_six_years = list_of_yearly_averages[:6]
best_six_years = list_of_yearly_averages[-6:]

print()
print("The worst six months by average price are:")
print()
print('{0:15}{1}'.format('Period', 'Price'))
for item in worst_six_months:
    printformatter(item)
print()

print("The best six months by average price are:")
print()
print('{0:15}{1}'.format('Period', 'Price'))
for item in best_six_months:
    printformatter(item)
print()

print("The worst six years by average price are:")
print()
print('{0:15}{1}'.format('Period', 'Price'))
for item in worst_six_years:
    printformatter(item)
print()

print("The best six years by average price are:")
print()
print('{0:15}{1}'.format('Period', 'Price'))
for item in best_six_years:
    printformatter(item)
