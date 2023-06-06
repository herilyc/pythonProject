# 处理csv文件中换行符等特殊字符（\r\n,\n,\r,\\,空格）
# python handle_csv_newline_char.py filepath

import os
import sys
import csv
import codecs
import time

# 需要处理的文件 来自参数1（filepath）
filename = sys.argv[1]

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '[', filename, ']开始处理')

with codecs.open(filename, 'r', encoding='utf-8') as srcFile, codecs.open(filename + '.tmp', 'w',
                                                                          encoding='utf-8') as dstFile:
    fileReader = csv.reader(srcFile, delimiter=',', quotechar='"', escapechar='\\')
    fileWriter = csv.writer(dstFile, quoting=csv.QUOTE_ALL, lineterminator='\n')

    for d in list(fileReader):
        for ii, dd in enumerate(d):
            if dd.find('\r\n') != -1:
                dd = dd.replace('\r\n', ' ')
            if dd.find('\n') != -1:
                dd = dd.replace('\n', ' ')
            if dd.find('\r') != -1:
                dd = dd.replace('\r', ' ')
            if dd.find('\\') != -1:
                dd = dd.replace('\\', '')
            if dd.find(' ') != -1:
                dd = dd.replace(' ', '')
            d[ii] = dd
        fileWriter.writerow(d)

    dstFile.close()
    srcFile.close()

# 重命名
os.remove(filename)
os.rename(filename + '.tmp', filename)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '[', filename, ']处理完成')