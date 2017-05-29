# -*- coding: utf-8 -*-

import os,shutil,sys
import platform
import re

thissys = platform.system()

def checkpath(path):
    if path == '.':
        print('如过你是Windows')
        print('文件夹创建失败,在python环境中未找到'
                +'...\\Lib\\site-packages 或者 ...\\Lib\\dist-packages')
        print('如过你是Liunx')
        print('文件夹创建失败,在python环境中未找到'
                +'.../Lib/site-packages 或者 .../Lib/dist-packages')
        sys.exit
    else:
        if os.path.exists(path):
            if os.path.isfile(path)==False:
                return path
            else:
                raise ValueError('文件夹创建失败，存在同名文件。')
        else:
            os.makedirs(path)
            return path

sitepath="."
for x in sys.path:
    ## 使用正则表达式寻找 .../site-packages 
    ##               或者 .../dist-packages
    ix = re.search('((site|dist)-packages)$',x)
    if ix != None:
        sitepath = x
        break

## creat zh_CN language folder
zh_CN = os.path.join(sitepath, 'spyder', 'locale', 'zh_CN', 'LC_MESSAGES')
checkpath(zh_CN)

shutil.copyfile("spyder.mo", os.path.join(zh_CN,'spyder.mo'))

## base.py add zh_CN
configpath = os.path.join(sitepath, 'spyder', 'config', 'base.py')
# print(configpath)

## write information to base.py
newpath = os.path.join(sitepath,'base.py')

if thissys == 'Windows':
    newf = open(newpath, 'w', encoding='utf-8')
    with open(configpath, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        islanguage = 0
        for i in range(len(lines)):
            line = lines[i]
            newf.writelines(line)
            if "LANGUAGE_CODES = {'en': u'English'," in line:
                #print(line)
                islanguage = 1
                mystr = "                  'zh_CN': u'简体中文',\n"
                newf.writelines(mystr)



else:
    newf = open(newpath, 'w')
    with open(configpath, 'r') as f:
        lines = f.readlines()
        islanguage = 0
        for i in range(len(lines)):
            line = lines[i]
            newf.writelines(line)
            if "LANGUAGE_CODES = {'en': u'English'," in line:
                #print(line)
                islanguage = 1
                mystr = "                  'zh_CN': u'简体中文',\n"
                newf.writelines(mystr)
newf.close()

## rename old base.py
if os.path.exists(os.path.join(sitepath, 'spyder', 'config', 'base_bak.py')):
    os.remove(os.path.join(sitepath, 'spyder', 'config', 'base_bak.py'))
os.rename(configpath,os.path.join(sitepath, 'spyder', 'config', 'base_bak.py')) 
## remove new base.py
shutil.move(newpath,configpath) 

try:
    raw_input('中文语言包安装完毕，请重启后配置语言选项即可。\n请尽情享用~\n\n 按ENTER键退出。')
except:
    input('中文语言包安装完毕，请重启后配置语言选项即可。\n请尽情享用~\n\n 按ENTER键退出。')