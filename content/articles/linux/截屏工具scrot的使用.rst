截屏工具scrot的使用
#######################

:date: 2016-03-06 07:26
:tags: Scrot, 截屏, Linux工具
:category: linux
:slug: scrot-screenshot
:authors: yunlong


在Windows下通过 ``PrintScreen`` 键，或者QQ截图快捷键 ``Ctrl + Alt + A`` ,都可以方便的截取屏幕上需要的内容进行保存或者分享。

Linux下可以通过 **Scort** 相似的功能。


安装Scrot
=============

.. code-block:: bash

    $ sudo pacman -S scrot


使用Scrot截屏
===============

1. 截取整个屏幕
------------------

.. code-block:: bash

    $ scrot ~/Pictures/my_desktop.png

直接运行 ``scrot`` 命令，也可以在命令后指定存放截图的目录和文件名。

.. PELICAN_END_SUMMARY

2. 截取特定窗口或矩形区域
----------------------------

.. code-block:: bash

    $ scrot -s

运行这个命令后，继续用你的鼠标单击任意窗口或画出一个矩形，它能够触发对选定窗口/区域的屏幕截取。


3. 延迟截屏
--------------

.. code-block:: bash

    $ scrot -s -d 5

有时候你选定的区域或窗口可能会被桌面的其它窗口部分遮挡, 你可能想要移动一下窗口，激活一下菜单，或是触发特定时间（如通知）等等,
这时候通过 *-d N* 参数，指定延迟N秒截屏会很有用。


4. 调整截屏质量
-----------------

.. code-block:: bash

    $ scrot -q 50

你可以在1到100的范围内调整截取的图像质量（数字越大质量越高）。默认质量设置为75。


5. 调整截屏尺寸
----------------

.. code-block:: bash

    $ scrot -t 10

减小截屏的尺寸到原图的10％, 你可以在1到100的范围内调整截取的图像尺寸（数字越大尺寸越大）。


参考资料
========

1. Linux截屏工具scrot用法详细介绍: http://www.jb51.net/LINUXjishu/284831.html
