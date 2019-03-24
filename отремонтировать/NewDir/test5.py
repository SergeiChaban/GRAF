import os
import psutil
import sys
import multiprocessing
import shutil
from shutil import copyfileobj
# print (dir())
# print (psutil.Process())
# print(dir(psutil))
# print(help(psutil.pids()))
# print(psutil.pids())
# print (os.name)
# print (multiprocessing.cpu_count())
#print(os.getcwd() + "\n")
# # print (os.uname())
# print (os.getlogin())
# print (help(os))
# print (sys.getfilesystemencoding())

# allFile = os.listdir()
# print (allFile)



# shutil.copy(fileName in os.listdir()

# вариант 1, копирование этого файла в уже сущесвтвующий, который укажет пользователь.

# print(os.path.basename(__file__))
# fileName = ''
# fileName = input('Привет {} \nУкажи Имя файла'.format(os.getlogin(), fileName))
# try:
#     with open(fileName + '.py') as infile:
#
# # в какой из какого
#         with open(fileName + '.py', 'w+') as output, open(os.path.basename(__file__), 'r') as in_put:
#             copyfileobj(in_put, output)
#         print('ВСе хорошо ', fileName)
# except IOError:
#      print ('Неверно указано имя')

#черновики
 # shutil.copyfile(os.path.basename(__file__), (fileName + '.py'))
 # if (fileName + '.py') in allFile:
    # os.path.isfile(fileName + '.py')

# вариант 2, дублирование файла, который укажет пользователь (создание нового файла с содержимым выбранного с
# окончанием .dipl

# file_name = ''
# file_name = input('Привет {} \nУкажи Имя файла, который ты хочешь копировать'.format(os.getlogin(), file_name))
# my_file = open(file_name)
# my_file.read()
# try:
#     f = open(file_name + '.dupl', 'w+')
#
# except IOError:
#     print ('Такой файл уже сущесвтвует, создавать не буду просто копирую')
# copyfileobj(file_name, f)
# f.close()

# def create_file_copy():
#     filename = sys.argv[0]  # __file__
#
#     with open(filename, 'rb') as f:
#         name, extension = filename.split('.')
#         with open(name + '_copy.' + extension, 'wb') as destination_f:
#             destination_f.write(f.read())
def dupl_move (file_list):

    for f in file_list:
        fullname = str(f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
file_name = ''


file_list = os.listdir()
file_name = input('Привет {} \nУкажи Имя файла, который ты хочешь копировать'.format(os.getlogin(), file_name))
print(file_list)

if os.path.isfile(file_name):
    newfile = file_name + '.dupl'
    shutil.copy(file_name, newfile)
    if os.path.isfile(newfile):
        print('File {} is exist'. format(newfile))
    else:
        print ('не получилось')
        sys.exit()

# dupl_move(file_list)
#     try:
#         with open (file_name + '.dupl') as newfile:
#             shutil.copy(file_name, newfile)
#     except  :
#         print('не получилось')
#         sys.exit()
# i += 1




