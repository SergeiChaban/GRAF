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
print(os.path.basename(__file__))
fileName = ''
# allFile = os.listdir()
# print (allFile)
fileName = input('Привет {} Укажи Имя файла {}'.format(os.getlogin(), fileName))


# shutil.copy(fileName in os.listdir()

# вариант 1
try:
    with open(fileName + '.py') as infile:
        # shutil.copyfile(os.path.basename(__file__), (fileName + '.py'))
        with open(fileName + '.py', 'w+') as output, open(os.path.basename(__file__), 'r') as input:
            copyfileobj(input, output)
    # if (fileName + '.py') in allFile:
    # os.path.isfile(fileName + '.py')
        print('ВСе хорошо ', fileName)
except IOError:
     print ('Неверно указано имя')

