import csv
import pandas as pd
import matplotlib.pyplot as plt

def consecutive_years(filename):
    consecutive_years_giving = []
    df = pd.read_csv(filename, usecols=['Consecutive Years of Giving'])
    years_giving_sorted = sorted(df['Consecutive Years of Giving'])
    total = sum(years_giving_sorted)
    avg_years_giving = total/len(years_giving_sorted)
    midpoint = len(years_giving_sorted)//2
    median_years_giving = years_giving_sorted[midpoint]
    return "Average: " + str(avg_years_giving) + " Median: " + str(median_years_giving)

def most_common_donation_date(filename):
    f = open(filename, 'r')
    month_counts = {}
    dates = []
    for line in f.readlines()[1:]:
        line = line.split(',')
        dates.append((line[2], line[4], line[6]))
    months = []
    for i in dates:
        for j in i:
            if j[1] == '/':
                months.append(j[0])
            else:
                months.append(j[0:2])
    for month in months:
        month_counts[month] = month_counts.get(month, 0) + 1
    return sorted(month_counts.items(), key = lambda x: x[1], reverse = True)

def plotData(filename, var_list):
    df = pd.read_csv(filename, usecols=var_list)
    df.plot(x=var_list[0], y=var_list[1], kind='scatter')
    plt.title(var_list[0] + ' vs ' + var_list[1] + ' 4k up')
    plt.show()

#print(consecutive_years('By Amount - Donations - 4K and up.csv'))
#print(most_common_donation_date('By Amount - Donations - 4K and up.csv'))
plotData('By Amount - Donations - 4K and up.csv', ['Consecutive Years of Giving', 'Largest gift amount'])
plotData('By Amount - Donations - 4K and up.csv', ['Consecutive Years of Giving', 'TG Amount'])
