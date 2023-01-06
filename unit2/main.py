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
                    num.append(float(data[i][row]))
    return int(sum(num))



def calculation_date(data,row,year):
    mouthDate = []
    for mouth in range(1,13):
        mouthDate.append(regular_year_and_mouth(data, row, year, mouth))

    return mouthDate

def covid19_chart_generation(**kwargs):
    pass

def main():
    year = int(input("請輸入要查詢的年度:(目前有2020-2022)"))
    data = read_csv('covid19_tw_specimen.csv')
    # i = regular_year_and_mouth(data,1,2021,6)
    # print(i)
    j = calculation_date(data, 1, year)
    print(j)
    # regular_year_and_mouth(data)
    # sublist = next(sublist for sublist in data if "2020/12/2" in sublist)
    # print(sublist.index("2020/12/2"))
    # for i, sublist in enumerate(data):
    #     if "2020/12/5" in sublist:
    #         j = sublist.index("2020/12/5")
    #         print(f'[{i}][{j}]')


if __name__ == '__main__':
    main()