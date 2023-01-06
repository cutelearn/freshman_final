import csv
import re
import matplotlib.pyplot as plt

def read_csv(filename):
    with open(filename, "r", encoding= "utf-8") as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

def regular_year_and_mouth(data, row, year, mouth):
    num = []
    date_pattern = rf"{year}/{mouth}/\d+"
    for pattern in data:
        date = re.search(date_pattern, pattern[0])
        if date:
            for i, sublist in enumerate(data):
                if date.group(0) in sublist:
                    # print(f'[{i}][{j}]')
                    num.append(float(data[i][row]))
                    # print(data[i][1])

    print(sum(num))


def calculation_date(data):
    date = []
    for i in range(1, len(data)):
        date.append(data[i][0])
    return date

def chart_generation(**kwargs):
    pass

def main():
    data = read_csv('covid19_tw_specimen.csv')
    regular_year_and_mouth(data,1,2020,1)
    # regular_year_and_mouth(data)
    # sublist = next(sublist for sublist in data if "2020/12/2" in sublist)
    # print(sublist.index("2020/12/2"))
    # for i, sublist in enumerate(data):
    #     if "2020/12/5" in sublist:
    #         j = sublist.index("2020/12/5")
    #         print(f'[{i}][{j}]')
if __name__ == '__main__':
    main()