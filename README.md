# DomainWeight批量查询百度权重

在一些SRC平台提交漏洞的时候，必须要求网站百度权重大于1以上，所以经常需要我们先手动取查询确认。

于是乎，花了一些时间，写了一个简陋的自动化脚本，以便批量查询

## 安装依赖包

```
pip3 install -r requireme.txt
```

## 参数

只有一个-f参数

```
options:
  -h, --help  show this help message and exit
  -f FILE     Input file directory

example:python DomainWeight.py -f url.txt
```

## 使用

```
使用较为简单（暂时没做其他的功能）
python3 DomainWeight.py -f url.txt
```

![image-20220801180005655](https://i0.hdslb.com/bfs/album/97c365fdec4321e34ceea38c69e18d4a28434f2d.png)

## 不足之处

只支持域名查询权重，不支持IP反查功能（查询结果默认为0）

没有对异常结果做处理，程序运行可能出现报错

代码冗余，正则表达不怎么会，先实现效果，后期再学习

有时间再改进吧

## 公众号

欢迎关注“零威胁”

不定时分享Web渗透、漏洞复现、工具使用等文章内容

希望我们在成为信安大牛的路上携手共进

![qrcode_for_gh_494d3ed85514_258](https://i0.hdslb.com/bfs/album/8f884764fff25ddedfce375656d995056f78094c.jpg)