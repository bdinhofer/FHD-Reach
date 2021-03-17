
def consecutive_years(filename):
    f = open(filename, 'r')
    consecutive_years_giving = []
    for line in f.readlines()[1:]:
        line = line.split(',')
        consecutive_years_giving.append(line[1])
    total = 0
    years_giving_sorted = sorted(consecutive_years_giving)
    for i in years_giving_sorted:
        total += int(i)
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

                
        
print(consecutive_years('By Amount - Donations - 4K and up.csv'))
print(most_common_donation_date('By Amount - Donations - 4K and up.csv'))