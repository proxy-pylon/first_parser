import xlsxwriter
from generator import array

address_to_save = r'D:\Python projects\parser\data.xlsx'


def writer(array):
    book = xlsxwriter.Workbook(address_to_save)
    page = book.add_worksheet("Merchandise")

    row = 0
    column = 0

    for item in array():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()

writer(array)