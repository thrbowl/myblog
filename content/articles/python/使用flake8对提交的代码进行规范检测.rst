使用flake8对提交的代码进行规范检测
###################################

:date: 2016-03-03 23:14
:tags: Python规范, PEP8
:category: Python
:slug: python-source-code-check
:authors: yunlong


一个项目通常都是多人协作的结果，每个人都会有不同的编程习惯，即使使用同一门编程语言，千奇百怪的使用方法，也会让项目看起来显的很 *业余* 。

这时使用一定的规范来限制项目开发者的随心所欲就显的尤为重要，很多公司都有自己的规范，
例如Google, 国内的BAT，都有自己的编程规范，这样大大增加了项目的可维护性。

Python中官方提供PEP8规范，而python的pep8库则实现了自动检查的功能。不过为了更好的使用pep8，我选择了flake8。它封装了三个工具:

* PyFlakes
* pep8
* Ned Batchelder’s McCabe script


使用flake8
============

安装flake8
----------

.. code-block:: bash

    pip install flake8

.. PELICAN_END_SUMMARY

运行flake8
----------

对python模块或者包含pyhton模块的目录直接调用flake8

.. code-block:: bash

    $ flake8 coolproject
    coolproject/mod.py:97:1: F401 'shutil' imported but unused
    coolproject/mod.py:625:17: E225 missing whitespace around operato
    coolproject/mod.py:729:1: F811 redefinition of function 'readlines' from line 723
    coolproject/mod.py:1028:1: F841 local variable 'errors' is assigned to but never used

配置flake8
----------

我们还可以通过一下参数来定制flake8的行为:

* *exclude* : 排除的文件或者目录，使用逗号分割，可以是直接文件名，也可以是正则匹配的文件名，默认：default: .svn,CVS,.bzr,.hg,.git,__pycache
* *filename* : 要进行检测的文件，使用逗号分割，可以是直接文件名，也可以是正则匹配的文件名，默认：\*.py
* *select* : 默认使用的错误和警告，默认关闭
* *ignore* : 忽略的错误或者警告，如果不设置，默认：E123/E133, E226 and E241/E242
* *max-line-length* : 一行最大的字符长度，默认：79
* *format* : 错误的显示格式
* *max-complexity* : McCabe的复杂度阈值


关联flake8与git commit
=======================

要关联flake8与git commit，最直接简单的方式是在git commit的pre-commit钩子中调用flake8。
但是为了预处理的可扩展性，我使用了pre-commit这个基于Yelp的，管理和维护pre-commit钩子的框架。

安装pre-commit
---------------

.. code-block:: bash

    pip install pre-commit

配置关联flake8与git commit
--------------------------

1. 为项目安装钩子

.. code-block:: bash

    pre-commit install

2. 关联flake8与git commit

项目中添加.pre-commit-config.yaml文件，内容如下：

.. code-block:: yaml

    -   repo: git://github.com/pre-commit/pre-commit-hooks
        sha: 97b88d9610bcc03982ddac33caba98bb2b751f5f
        stages: commit
        hooks:
        -   id: flake8

执行flake8
----------

这时候如果你进行git commit动作就会触发flake8检测，或者你也可以直接调用:

.. code-block:: bash

    pre-commit run flake8


参考资料
========

1. flake8文档: http://flake8.readthedocs.org/en/latest/
#. Google编程规范: http://zh-google-styleguide.readthedocs.org/en/latest/
#. pre-commit文档: http://pre-commit.com/
