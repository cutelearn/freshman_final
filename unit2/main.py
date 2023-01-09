"""期末作業第二題"""
import csv
import re

import matplotlib.pyplot as plt


def read_csv(filename):
    """讀取 CSV 檔案"""
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def regular_year_and_mouth(data, row, year, mouth):
    """將年份和月份帶入正規表達式"""
    num = []
    date_pattern = rf"{year}/{mouth}/\d+"
    for pattern in data:
        date = re.search(date_pattern, pattern[0])
        if date:
            for i, sublist in enumerate(data):
                if date.group(0) in sublist:
                    num.append(float(data[i][row]))
    return int(sum(num))


def calculation_date(data, row, year):
    """計算每個月的確診人數"""
    mouth_date = []
    for mouth in range(1, 13):
        mouth_date.append(regular_year_and_mouth(data, row, year, mouth))

    return mouth_date


def covid19_chart_generation(year, **kwargs):
    """繪製圖表"""
    month = range(1, 13)
    line1 = plt.plot(month, kwargs['date'][0], "-o")
    line2 = plt.plot(month, kwargs['date'][1], "-o")
    line3 = plt.plot(month, kwargs['date'][2], "-o")
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.legend((line1[0], line2[0], line3[0]), ("法定傳染病通報", "居家檢疫送驗", "擴大監測送驗"))
    plt.xlabel('Month')
    plt.title(f'{year}年度的確診人數')
    plt.show()


def main():
    """主程式"""
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
