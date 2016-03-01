# !/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'loch'
AUTHOR = 'yunlong'
AUTHORDESC = """
本人程序猿一枚，北漂于北京，08年毕业自河北承德石油高等专科学校，关注Linux，Python，测试，系统架构及各种开源技术。
"""
SITENAME = u'花开见我'
SITEWORDS = u"不忘初心, 方见本心"
SITEURL = ''
SITELICENSE = """
本项目源码受 <a target="_blank" href="https://github.com/twbs/bootstrap/blob/master/LICENSE" rel="license">MIT</a>开源协议保护，
文档受 <a target="_blank" href="https://creativecommons.org/licenses/by/3.0/" rel="license">CC BY 3.0</a> 开源协议保护。
"""
ICPLICENSE = '京ICP备14006485号-3'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    (u'大库书', 'http://dakushu.com/'),
)

# Social widget
SOCIAL = ()

# Tools
TOOLS = (
    (u'gist', 'https://gist.github.com/'),
    (u'travis-ci', 'https://travis-ci.org/'),
    (u'Sauce Labs', 'https://saucelabs.com'),
)

DEFAULT_PAGINATION = 10

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    'extra/favicon.ico',
]

DEFAULT_DATE_FORMAT = u'%Y年%m月%d日'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
