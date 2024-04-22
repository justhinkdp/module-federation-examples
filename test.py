from os.path import abspath, dirname, join
print(abspath(__file__))
print(dirname(abspath(__file__)))
data_path = join(dirname(abspath(__file__)),'data')
print(data_path)
import os
 
# 获取当前路径
current_path = './'
 
# 列出当前路径下的所有文件和文件夹
files_and_folders = os.listdir(current_path)
 
# 打印所有文件和文件夹的名称
for item in files_and_folders:
    print(item)