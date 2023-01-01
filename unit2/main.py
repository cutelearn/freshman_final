import csv
import re

def read_csv(filename):
    data = []
    with open(filename, "r", encoding= "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def regular_mouth(data):
    for day in data:
        mouth = re.search(r"/(\d+)/", day[0]).group(1)

def calculation_date(data):
    date = []
    for i in range(1, len(data)):
        date.append(data[i][0])
    return date

def main():
    pass

if __name__ == '__main__':
    data = read_csv('covid19_tw_specimen.csv')
    print(data)
