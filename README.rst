基于Pelican的博客源码
######################


环境配置
========

需要系统上已经有python运行环境，版本2.7以上。


安装包管理器pip
---------------

.. code-block:: bash

    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py


克隆项目到本地
--------------

.. code-block:: bash

    git clone https://github.com/thrbowl/myblog.git
    cd myblog
    pip install -r requirements.txt


写日志
======

启动开发服务器
--------------

.. code-block:: bash

    cd myblog
    ./develop_server.sh start


创建文件
--------

使用ReST语法在content目录创建对应的日志文件。


查看日志
--------

浏览器中输入http://localhost:8000, 选择刚创建的日志进行查看。


发布日志
========

修改Makefile文件
-----------------

我们使用rsync来上传文件，所以只需要修改下列选项：

* SSH_HOST=itkeng.com
* SSH_PORT=22
* SSH_USER=root
* SSH_TARGET_DIR=/opt/sites/myblog

**需要本地已经安装了rsync服务**


发布日志到正式服务器
-------------------

.. code-block:: bash

    make rsync_upload
