import csv
import xlwt
import os
import fnmatch
from pprint import pprint
import sys

# def get_source_files():
#     source_files = []
#     for (path, dirs, files) in os.walk('./modified'):
#         for filename in fnmatch.filter(files, '*.csv'):
#             source_files.append(os.path.join(path, filename))
#     return source_files

# for xls in get_source_files():
#     with open(xls, 'r') as f:
#         sources = f.readlines()
#         set_trace()



with open('20120901_20120915_ACCLOG.csv', 'r')  as f:
    sources = f.readlines()
    print(sources)



# class ModifyPaymetn(object):
#     def load_file(self, path):
#         load_workbook(filename = 'empty_book.xlsx')
#         pass
# import csv
# # Do the reading
# file1 = open(file.csv, 'rb')
# reader = csv.reader(file1)
# new_rows_list = []
# for row in reader:
#    if row[2] == 'Test':
#       new_row = [row[0], row[1], 'Somevalue']
#       new_rows_list.append(new_row)
# file1.close()   # <---IMPORTANT

# # Do the writing
# file2 = open(file.csv, 'wb')
# writer = csv.writer(file2)
# writer.writerows(new_rows_list)
# file2.close()