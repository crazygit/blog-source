Windows环境下搭建python开发环境
###############################

:date: 2013-11-25 23:14:34
:tags: windows, python, pypi mirrors,
:keywords: windows, python, pypi, mirrors,
:slug: install-python-on-windows
:author: crazygit
:summary: install python on windows
:description:


1. 从 `Python官网下载 <http://www.python.org/download/>`_  下载自己所需版本的windows安装包并进行安装。

2. 将安装包的路径添加到系统环境变量,  :code:`C:\Python27` ， 同时为了后面使 :code:`easy_install` ，也 :code:`C:\Python27\Scripts` 添加到环境变量里（现在这个目录还不存在). 

3. 安装python包管理工具 *setuptools* , 安装方法如下:

    a. 下载 `ez_setup.py <https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py>`_  脚本，并运行 :code:`python easy_install.py` .
    b. 如果cmd命令支持curl命令(如机器上安装过git或一些带linux命令的包时），则可以直接执 :code:`curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python` 进行安装.

4. 安装另一个python包的管理工具 *pip* , :code:`easy_install pip` .

5. 让pip使用国内的pypi源。我们在使用pip进行包安装的时候，默认是从官方下载包的，下载速度相当地慢，而且经常还会出现一些包无法下载的情况。这个时候，让pip使用国内原则能解决这个问题。在这里我选择使用 `清华大学的源 <http://e.pypi.python.org/>`_  。使用pip命令的时候，只需要加 :code:`-i 源地址即可` 。如 :code:`pip install flask -i http://e.pypi.python.org/simple` .也可以进行如下配置， 让以后每次安装的时候都自动使用指定的源

    ::

        使用pip的用户可以如下配置：

        在unix和macos，配置文件为：$HOME/.pip/pip.conf
        在windows上，配置文件为：%HOME%\pip\pip.ini

        需要在配置文件内加上：

        [global]
        index-url=http://e.pypi.python.org/simple

    使用清华大学的源之后，下载安装python包时真是可以体会到飞一般的感觉。

6. 如果有需要，也可以在本地自己做pypi的镜像。具体方法可以参考 `PyPI Mirrors <https://pypi.python.org/mirrors>`_  .

7. 好了，现在可以开始python之旅了。
