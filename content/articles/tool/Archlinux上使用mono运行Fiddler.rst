Archlinux上使用mono运行Fiddler
###############################

:date: 2016-03-01 07:26
:tags: Fiddler, Http抓包
:category: 工具
:slug: archlinux-run-fiddler
:authors: yunlong


Fiddler是一个http协议调试代理工具，它能够记录并检查所有你的电脑和互联网之间的http通讯，设置断点，查看所有的“进出”Fiddler的数据。

Fiddler依赖于.net运行环境，所以在linux无法直接运行，但是可以通过linux上的mono启动运行。


下载Fiddler安装包
==================

* http://fiddler.wikidot.com/mono
* http://ericlawrence.com/dl/MonoFiddler-v4484.zip


安装mono环境
=============

sudo pacman -S mono


运行Fiddler
============

进入到Fiddler目录中，找到Fiddler.exe，执行mono Fiddler.exe

.. PELICAN_END_SUMMARY


设置浏览器
===========

Fiddler默认启动127.0.0.1:8888作为代理端口，只要将浏览器的代理设为改地址和端口，Fiddler就能捕捉到请求中的所有数据了


另外Charles，Burp Proxy，WebScarab，httpry，wireshark都是不错的Fiddler替代工具，只是因为windows上还是Fiddler用的多一些，没必要不同的平台使用不同的工具，具体的还是根据跟人的需求和爱好进行选择使用了。


参考资料
========

1. Fiddler 教程: http://www.cnblogs.com/TankXiao/archive/2012/02/06/2337728.html
#. 从入门到深入Fiddler 2: http://www.cnblogs.com/kingwolf_JavaScript/archive/2012/11/07/FiddlerUI.html
