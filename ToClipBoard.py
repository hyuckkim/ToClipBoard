# coding=utf-8
import os.path
import pyperclip

MY_PATH = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(MY_PATH, 'Database.txt')

datafile = open(path,'r')
Data = datafile.readlines()
cells = []
for x in Data:
    if x[-2] == '|':
        cells.append([x[:-2],''])
    else:
        cells[-1][1] += x
while(True):
    n = 0
    for y in cells:
        n += 1
        print(str(n) + ' : ' + y[0])
    k = int(input('복사할 링크를 선택해 주세요.'))
    print(cells[k - 1][1])
    pyperclip.copy(cells[k - 1][1])

