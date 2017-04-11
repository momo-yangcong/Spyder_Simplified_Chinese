

** 请务必忽略截图中的错别字（人工捂脸**

Spyder在3.x版本之后开始支持自定义语言包。

虽然使用无障碍，还是想上一个中文包，毕竟还是好多朋友找这个汉化包。

这就是汉化包的由来啦。

![screenshot](./img/2017-04-07-13-59-16.png)
============================================
该汉化包已pull到Spyder官方，目前等待合并。合并后更新Spyder到最新版即可使用中文语言了，在此之前如果想尝试的话，可以使用一键安装脚本来安装。


### 必备条件：
>1、已安装Spyder
>
>2、Spyder版本在3.X以上。

### Spyder安装：
>1、anaconda下，conda install spyder
>
>2、Python发行版下， pip install spyder

### Spyder升级：
>1、anaconda下，conda update spyder
>
>2、Python发行版下，pip install --upgrade spyder


## 汉化包的安装(文尾有详细方法)：
如果python环境首选路径是anaconda的话，在main.py所在路径打开命令行或者终端，输入一下命令即可：
> python main.py


Ubuntu：

![screenshot](./img/spyder001.png)

Windows:

![screenshot](./img/spyder002.png)


安装完成后，打开或重启Spyder，在偏好设置中，选择简体中文，重启即可。

## 详细安装方法

1、假设已经通过git命令或者直接下载zip文件并解压到目录A。

**目录A下有spyder.mo，main.py，readme.md等文件。

2、如果是windows系统，在目录A下，再选择任何文件的情况下(可以先左键单击空白处)，按住Shift的同时在空白处单击右键，调出菜单
，此时菜单中会出现【在此处打开命令窗口】的选项，打开。

3、在弹出的命令窗口中输入：

>python main.py 

回车执行即可。
（如果是Linux系统，右键打开终端，输入同样命令。）