import csv
import pandas as pd 
import matplotlib.pyplot as plt
import os

def getNum(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)

    l = []
    for i in range(1, 31):
        l.append(f'Gift amount {i}')

    df = pd.read_csv(full_path, usecols=l)

    counts_dict = {'1': 0, '2-5': 0, '6-10': 0, '>10': 0}
    for index, row in df.iterrows():
        count = 0
        for col in l:
            if not pd.isnull(row[col]):
                count += 1 
            else:
                if count == 1:
                    counts_dict['1'] += 1
                elif count >= 2 and count <= 5:
                    counts_dict['2-5'] += 1
                elif count >= 6 and count <= 10:
                    counts_dict['6-10'] += 1
                else:
                    counts_dict['>10'] += 1
                break

    plt.bar(counts_dict.keys(), counts_dict.values())
    plt.xlabel('Number of Gifts')
    plt.ylabel('Frequency')
    plt.show()


def moreSpef(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)

    l = []
    for i in range(1, 31):
        l.append(f'Gift amount {i}')

    df = pd.read_csv(full_path, usecols=l)

    counts_dict = {}
    for index, row in df.iterrows():
        count = 0
        for col in l:
            if not pd.isnull(row[col]):
                count += 1 
            else:
                counts_dict[count] = counts_dict.get(count, 0) + 1
                break
    sorted_counts = sorted(counts_dict.items(), key=lambda x: x[0])
    plt.bar([val[0] for val in sorted_counts], [val[1] for val in sorted_counts])
    plt.xlabel('Number of Gifts')
    plt.ylabel('Frequency')
    plt.show()


def showAvg(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)

    l = []
    for i in range(1, 31):
        l.append(f'Gift amount {i}')

    df = pd.read_csv(full_path, usecols=l)

    avg_dict = {}
    for index, row in df.iterrows():
        count = 0
        total = 0
        for col in l:
            if not pd.isnull(row[col]):
                count += 1 
                total += row[col]
            else:
                avg = total / count
                if count == 1:
                    avg_dict['1'] = (avg_dict.get('1', avg) + avg) / 2
                elif count >= 2 and count <= 5:
                    avg_dict['2-5'] = (avg_dict.get('2-5', avg) + avg) / 2
                elif count >= 6 and count <= 10:
                    avg_dict['6-10'] = (avg_dict.get('6-10', avg) + avg) / 2
                else:
                    avg_dict['>10'] = (avg_dict.get('>10', avg) + avg) / 2
                break

    sorted_avg = sorted(avg_dict.items(), key=lambda x: x[0])
    plt.bar([val[0] for val in sorted_avg], [val[1] for val in sorted_avg])
    plt.xlabel('Number of Gifts')
    plt.ylabel('Average Gift Amount')
    plt.show()

def consCount(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)
    df = pd.read_csv(full_path, usecols=['Consecutive Years of Giving'])

    counts_dict = {'0': 0, '1-5': 0, '6-10': 0, '>10': 0}
    for val in df['Consecutive Years of Giving']:
        if val == 0:
            counts_dict['0'] +=1
        elif val >= 1 and val <= 5:
            counts_dict['1-5'] += 1
        elif val >= 6 and val <= 10:
            counts_dict['6-10'] += 1
        else:
            counts_dict['>10'] += 1
    
    plt.bar(counts_dict.keys(), counts_dict.values())
    plt.xlabel('Consecutive Years of Giving')
    plt.ylabel('Frequency')
    plt.show() 


if __name__ == '__main__':
    # getNum('NumGifts.csv')
    # moreSpef('NumGifts.csv')
    # showAvg('NumGifts.csv')
    consCount('NumGifts.csv')