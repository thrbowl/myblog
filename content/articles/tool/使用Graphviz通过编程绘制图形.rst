使用Graphviz通过编程绘制图形
###############################

:date: 2016-03-01 07:26
:tags: Graphviz, 流程图
:category: 工具
:slug: draw-flow-with-graphviz
:authors: yunlong


Graphviz是大名鼎鼎的贝尔实验室的几位牛人开发的一个画图工具，它提供了“所想即所得”的理念，通过dot语言来编写脚本并绘制图形，简单易懂。

具体使用方法可以参考 `官方文档 <http://www.graphviz.org/doc/info/lang.html>`_ ，但是估计很少会有人直接用dot手动绘图，
所以它的优势更体现在通过程序自动生成图形。

例如:

* `PHP中xhprof + graphviz <https://segmentfault.com/a/1190000003042147>`_
* `Python PyCallGraph <http://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script>`_

.. PELICAN_END_SUMMARY

所以在性能分析，自动生成调用层级和自动生成拓扑等方面可以考虑将其应用在项目中。


安装Graphviz
=============

1. Archlinux安装: ``sudo pacman -S graphviz``
#. Fedora 23: ``dnf install graphviz``
#. 源码安装

.. code-block:: bash

    wget http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.38.0.tar.gz
    tar zxf graphviz-2.38.0.tar.gz
    cd graphviz-2.38.0
    ./configure --prefix=/usr/local/graphviz
    make&make install


简单示例
=========

.. code-block:: dot

    digraph G {
        size = "4, 4"
        a->b->c;
        b->d;

        a[shape = polygon, sides = 5, peripheries=3, color = lightblue, style = filled];
        //我的形状是多边形, 有五条边, 3条边框, 颜色的淡蓝色, 样式为填充
        c[shape = polygon, sides = 4, skew= 0.4, lable = "hello world"];
        //我的形状是4变形, 角的弯曲度0.4, 里面的内容为"hello world"
        d[shape = invtriange];
        //我是三角形
        e[shape = polygon, side = 4, distortion = .7];
        //我是梯形啊
    }

将上述内容保存成 *g.gv*


生成图形
========

``dot -Tgif -og.png g.gv``


参考资料
========

1. 使用 Graphviz 生成自动化系统图: https://www.ibm.com/developerworks/cn/aix/library/au-aix-graphviz/
#. 使用graphviz绘制流程图: http://www.cnblogs.com/CoolJie/archive/2012/07/17/graphviz.html
