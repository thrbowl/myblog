Jmeter中如何设置合理的Ramp-Up Period值
########################################

:date: 2016-03-06 15:25
:modified: 2016-03-06 15:25
:tags: Jmeter, Jmeter参数
:category: 测试
:slug: jmeter-rampup-value
:authors: yunlong


使用Jmeter进行性能测试，我们需要在Thread Group中设置各种选项来模拟真实的场景。

.. image:: pictures/jmeter_thread_group_options.png
   :scale: 80
   :alt: Thread Group Options

这里面 *Ramp-Up Period* 表示在多长时间内启动 *Number of Threads* 所指定的用户数（线程数）。

.. PELICAN_END_SUMMARY

例如上图所示中::

    Number of Threads: 100
    Ramp-Up Period: 10

JMeter 将每隔 *10/100=0.1* 秒建立一个用户(线程)。如果 *Ramp-Up Period* 空为，或者为0，将立即创建所有的用户数（线程数）。


什么时候使用该选项，以及设置多少合理？
=========================================

在网上查了些文档，结合别人的一些意见，整理如下:

1. 如果要测试并发递增的情况，需要 *Ramp-Up Period* 。比如想查看5，10，20，50并发情况下的状态，就可以通过设置 *Ramp-Up Period* 来实现。
#. 如果要模拟用户 *Think Time*，需要 *Ramp-Up Period* 。比如用户填写表单，查看内容的在暂停时间。
#. 如果要测试极限性能的时候，不需要 *Ramp-Up Period* 。比如某个文件下载支持的最大值，某个接口并发调用的最大值。
#. 如果测试缓存的有效性，不需要 *Ramp-Up Period* ，比如应该第一个请求后就会创建缓存，测试创建的缓存效果。

摘抄的内容:

    For e.g. Suppose your application deadlocks sometimes and you need to
    simulate this. In this case you might not want a ramp up time , you actually
    do want your application to be hit at the same time . On the other hand if
    you are simulating actual user flows with think times then you dont want 500
    threads to be created at the exact same moment  since this probably isnt
    normal for your application. Or say you are caching data on the first
    request and the cache load is synchronized, then you might want to access
    the page in multiple threads at the same time to check the synchronized
    behavior. so no ramp up. Or perhaps you want to see how many people can
    download a  large file at exactly the same time , you probably want to check
    with no rampup.

    b. If your test is a short test , then the results may be skewed negatively
    without ramp-up (because both your client and server have to be able to
    handle the initial burst of sockets/traffic). A ramp up also adds a certain
    degree of randomness that your threads will be reasonably distributed across
    requests.

    Most tests where you want to measure the performance would want ramp up.
    Most analysis sort of tests (like the deadlock/ cache tests) would not want
    a ramp up.


*Ramp-Up Period* 设置多少合适呢?
====================================

答案是需要根据场景而定。如果设置的太大，后面的线程还没起来，前面的线程已经结束了,
如果设置的太小，又起不到模拟用户真实操作的场景。这种在某些场景下可能都不是我们需要的。

如果为了模拟用户真实的操作场景，我们应该让 *Number of Threads/Ramp-Up Period* 的值尽量接近真实用户的操作频率。

我们可以通过使用 **HTTP代理服务器** 录制脚本获取到相应的数据。



参考资料
========

1. Jmeter文档: http://meter.apache.org/usermanual/test_plan.html
2. JMeter技巧集锦: http://www.knowsky.com/367353.html
