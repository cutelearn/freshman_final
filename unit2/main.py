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

def covid19_chart_generation(year, **kwargs):
    month = range(1, 13)
    h1 = plt.plot(month, kwargs['date'][0], "-o")
    h2 = plt.plot(month, kwargs['date'][1], "-o")
    h3 = plt.plot(month, kwargs['date'][2], "-o")
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.legend((h1[0], h2[0], h3[0]), ("法定傳染病通報", "居家檢疫送驗", "擴大監測送驗"))
    plt.xlabel('Month')
    plt.title(f'{year}年度的確診人數')
    plt.show()

def main():
    while True:
        try:
            year = int(input("請輸入要查詢的年度:(目前有2020-2022)"))
            if year in range(2020, 2023):
                break
        except ValueError:
            print("請輸入數字")
    data = read_csv('covid19_tw_specimen.csv')

    date = []

    for i in range(1, 4):
        j = calculation_date(data, i, year)
        date.append(j)

    covid19_chart_generation(year, date=date)


if __name__ == '__main__':
    main()