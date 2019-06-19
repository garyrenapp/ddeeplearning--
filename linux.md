
https://www.bilibili.com/video/av18156598/?p=15
### 管道符号 |
用法: command 1 | command 2 他的功能是把第一个命令command 1执行的结果作为command 2的输入传给command 2，例如:
~
### cat -n  显示行号
### tac 倒序显示
### more 分页显示 
* 空格或f翻页 
* enter换行 
* q退出
### less 
* 不仅有more的功能 
* page up 向上翻页 
* 上箭头向上翻一行
* 搜索：输入/关键词，如果当前页面没有你想要的 可以按n查看下一个
### head 
* head -n 100 /etc/services 前100行
### tail 
* tail -n 100 /etc/s        后100行
* tail -f 动态显示，当文件内容变化时显示会更新
### ln 链接文件
* 软连接 ln -s /etc/issue tmp/issue.soft
类似widows的快捷方式
* 硬连接 ln /etc/issue tmp/issue.hard
相当于拷贝cp，跟cp不同的是，两个文件可以同步更新。
源文件即使删除，硬链接依然可以访问。
硬链接不可以跨分区。

### chmod
* chmod
[{ugoa}{+-=}][文件或目录] u-user g-group o-other a-all
[mode=421] [文件或者目录] r-4 w-2 x-1
-R 递归修改
* chmod g+w,o-r t.txt
group 增加写权限
ohter 去掉读权限
这种方式不常用，通常使用数字的方式

### touch 创建文件
### chown 改变文件所有者
### chgrp 改变文件所属组

### find 文件搜索命令
* find [搜索范围] [匹配条件]
* find /etc -name init 在目录/etc中查找文件名为init的文件
* find /etc -name \*init* 文件名中包含init的文件
* find /etc -name init??? 文件名为init后面加上3个任意字符的文件
* find /etc -iname init 不区分大小写
* find /etc -size +204800 查找大于文件大小的文件 一个数据块是512字节=0.5kb
* find /home -user A 查找所有者为A的文件
* find /etc -cmin -5 5分钟内文件属性被改
* find /etc -mmin -5 5分钟内文件内容被改
* find /etc -amin -5 5分钟内文件被访问
* find /etc -size +16380 -a -size -20480 两个条件都满足
* find /etc -size +16380 -o -size -20480 两个条件满足一个
* find /etc -size +16380 -a -type f
-type 根据文件类型 f文件 d目录 l软链接
* find /etc -name inittab -exec ls -l{} \;  -exec后者-ok 后面接一个命令.
-ok有确认的环节
* find -inum 根据i节点查找
* find /etc -inum 31123 -exec rm {} \; 根据i节点删除文件，有时候文件名奇形怪状可以根据i节点删除
### locate 比find速度快
是从系统维护的文件资料库搜索
存在的问题，如果新建的文件还没有更新到文件资料库则查不到
* updatadb 更新文件资料库
如果目录比如tmp没有在文件资料库也搜索不到
* locate -i Ubuntu 不却分大小写
### which 命令所在位置
* which ls 查找ls命令所在位置
### whereis 命令所在目录+帮助目录所在位置
### grep 在文件中搜索字符串匹配的行并输出
* grep mysql /root/install.log
* grep -i mysql /root/install.log 查找msql的行,不区分大小写
* grep -v # /etc/inittab 去除包含#的行
* grep -v ^# /etc/inittab 去掉以#开头的行

### man 帮助命令
man [命令或配置文件]

### help shell内置命令的帮助信息

### 用户管理
* useradd xm
* passw xm 
* who 查看登陆用户
### 压缩解压命令
* gzip gunzip
gzip只能压缩文件，不能压缩目录,不保留原文件
* tar -zcvf tt.tar.gz tt
* tar -zxvf tt.tar.gz
-c 打包
-x 解包
-v 显示详细信息
-f 指定文件名
-z 解压缩
* zip  unzip
能保留原文件，可以压缩目录
zip [-r][压缩后文件名][文件或者目录]
-r 压缩目录
* bzip2 bunzip2 [-k] 保留原文件


### vim

### 软件包安装
#### rpm 离线安装
#### yum 在线安装

### 用户管理
### 环境变量
* env 显示所有环境变量
* echo $PATH 输出环境变量
#### 环境变量配置文件
* source 配置文件 或者 .配置文件
如果修改了环境变量的配置文件，source 可以让立刻生效
##### 常见配置文件
/etc下的对所有用户生效
* /etc/profile
* /etc/profile.d/*.sh
* /etc/bashrc
~下的对自己生效
* ~/.bash_profile
* ~/.bashrc
之前总是 export 环境变量，退出终端后就失效了，原来是要写入文件中才能永久生效


### screen
* screen -ls 列出当前的所有screen
* screen -S name 新建screen
* screen -X -S id quit 删除screen
#### 分屏
* control + a 然后 shfit + s   横屏
* control + a 然后 tab  切换窗口
* control + a 然后 c  新建窗口
* control + a 然后 x  关闭窗口


### conda 
* conda activate name  or source acitvate name 
* conda remove -n name 
* conda create -n name python=verison...
* conda env list 

