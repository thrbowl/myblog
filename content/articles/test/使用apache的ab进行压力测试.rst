使用apache的ab进行压力测试
############################

:date: 2016-02-28 12:44
:modified: 2016-03-04 07:48
:tags: ab, 压力测试
:category: 测试
:slug: test-apache-ab-usage
:authors: yunlong


ab的全称是ApacheBench，是Apache 附带的一个小工具，它可以模拟多个并发请求，用来进行HTTP的测试。

一般来说如果你安装了Apache，那么ab应该就已经在你的电脑上了，当然如果你想单独安装也可以，
但是它依赖Apache的运行环境，所以你需要先安装apr-utils。

ab的使用很简单，通过 ``ab -h`` ,你能看到它支持的所有参数(下面省略了一下关于结果输出的参数)::

    用法: ab [options] [http[s]://]hostname[:port]/path
    参数:
        -n requests     测试会话中所执行的请求个数，默认时，仅执行一个请求
        -c concurrency  一次产生的请求个数。默认是一次一个
        -t timelimit    测试的时间，单位是秒。默认最大执行50000个请求（测试满足时间要求或者满足最大执行请求数，都会退出）
        -s timeout      每个请求的最大响应时间。默认30秒
        -b windowsize   TCP请求的buffer大小，单位字节
        -p postfile     POST请求时，包含数据的文件。
        -u putfile      PUT请求时，包含数据的文件。
        -T content-type 在POST/PUT请求时，指定请求数据的类型。例如'application/x-www-form-urlencoded',默认'text/plain'
        -i              使用HEAD代替GET
        -X proxy:port   指定使用的代理服务器ip和端口
        -V              输出ab的版本信息
        -k              使用KeepAlive
        -l              指定接受的内容长度(用于动态页面，因为apache是根据页面长度来判断响应的成功或失败)
        -g filename     把结果生成gnuplot格式文件
        -e filename     把结果生成CSV格式文件
        -r              当发生socket错误时，不退出
        -m method       指定请求类型（GET，HEAD，POST，PUT）
        -h              显示帮助

我们对百度进行一下测试, 这里用5个并发，总过50个请求:

.. code-block:: bash

    ab -c 5 -n50 www.baidu.com/


**地址后面的 ``/`` 是不能少的**

测试结果如下::

    This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking www.baidu.com (be patient).....done

    # 被测试web服务软件名称他来自于http响应数据的头信息
    Server Software:        BWS/1.1
    # 表示请求的url中的主机部分名称
    Server Hostname:        www.baidu.com
    # 测试web服务器软件的监听端口
    Server Port:            80

    # 请求的url根的绝对路径
    Document Path:          /
    # 表示http响应数据的正文长度
    Document Length:        98085 bytes

    # 并发的用户数
    Concurrency Level:      5
    # 整个测试持续的时间
    Time taken for tests:   3.273 seconds
    # 完成的请求数量
    Complete requests:      50
    # 失败的请求总数
    Failed requests:        43
       (Connect: 0, Receive: 0, Length: 43, Exceptions: 0)
    # 整个场景中的网络传输量
    Total transferred:      4957926 bytes
    # 整个场景中的HTML内容传输量
    HTML transferred:       4909420 bytes
    # 大家最关心的指标之一，相当于 LR 中的 每秒事务数 ，后面括号中的 mean 表示这是一个平均值
    Requests per second:    15.28 [#/sec] (mean)
    # 大家最关心的指标之二，相当于 LR 中的 平均事务响应时间 ，后面括号中的 mean 表示这是一个平均值
    Time per request:       327.272 [ms] (mean)
    # 每个请求实际运行时间的平均值
    Time per request:       65.454 [ms] (mean, across all concurrent requests)
    # 平均每秒网络上的流量，可以帮助排除是否存在网络流量过大导致响应时间延长的问题
    Transfer rate:          1479.42 [Kbytes/sec] received

    # 请求时间的分解，包括连接，处理，等待时间
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        5   79  37.8     80     136
    Processing:   124  239  51.3    240     338
    Waiting:        7   49  32.3     42     196
    Total:        171  318  47.0    321     429

    # 请求响应时间的百分比
    Percentage of the requests served within a certain time (ms)
      50%    321
      66%    328
      75%    339
      80%    347
      90%    387
      95%    395
      98%    429
      99%    429
     100%    429 (longest request)


参考资料
========

1. ab参数详解 – 压力测试: https://blog.linuxeye.com/124.html
