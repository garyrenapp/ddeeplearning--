
https://www.bilibili.com/video/av18156598/?p=15
### 管道符号 |
用法: command 1 | command 2 他的功能是把第一个命令command 1执行的结果作为command 2的输入传给command 2，例如:

### 同时结束多个进程
* ps -ef|grep jinchengming|grep -v grep|cut -c 9-15|xargs kill -9
管道符“|”用来隔开两个命令，管道符左边命令的输出会作为管道符右边命令的输入。下面说说用管道符联接起来的 
几个命令： 
* “ ps - ef”是Red Hat 里查看所有进程的命令。这时检索出的进程将作为下一条命令“grep LOCAL=NO”的输入。 
* “grep LOCAL=NO”的输出结果是，所有含有关键字“LOCAL=NO”的进程，这是Oracle数据库中远程连接进程的共同特点。 
* “grep -v grep”是在列出的进程中去除含有关键字“grep”的进程。 
* “cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。 
* “xargs kill -9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -9”命令的参数，并执行该令。 
* “kill -9”会强行杀掉指定进程，这样就成功清除了oracle的所有远程连接进程。其它类似的任务，只需要修改“grep LOCAL=NO”中的关键字部分就可以了。

### 端口查看
* netstat -ntlp

### ls
* 统计当前目下的文件个数  ls -l | grep "^-" | wc -l
* ls | head -10 显示前10个
* ls | sort | head -10 
* ls -lt 按时间排序从近到远
* ls -ltr 按时间排序从远到近

### grep 
Linux系统中grep命令是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹 配的行打印出来。grep全称是Global Regular Expression Print.

* 规则表达式

命令 | 解释
----| --- 
^  | ^a 以a开头的行
$  | $a 以a结尾的行

### watch 
* watch [options] command
* watch -n 1 nvidia-smi 一秒显示一次gpu情况


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
* find /etc -name inittab -exec ls -l{} \\;  -exec后者-ok 后面接一个命令.
-ok有确认的环节
* find -inum 根据i节点查找
* find /etc -inum 31123 -exec rm {} \\; 根据i节点删除文件，有时候文件名奇形怪状可以根据i节点删除
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
unzip test.zip -d /tmp
zip [-r][压缩后文件名][文件或者目录]
* zip -r myfile.zip ./my/*
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

* control + a 然后 shfit + s   横屏
* control + a 然后 tab  切换窗口
* control + a 然后 c  新建窗口
* control + a 然后 x  关闭窗口
* control + a 然后 d 退出当前screenss
* screen -xr 5170.pts-21 当前screen attach的时候 再 attach会报错 重新attach * screen 死机
```cpp
ps -A | grep "screen"
kill -9 pid
```

### conda 
* conda activate name  or source acitvate name 
* conda remove -n name 
* conda create -n name python=verison...
* conda create -n name --clone name 
* conda env list 

### shell
http://c.biancheng.net/cpp/view/6999.html
* cat /etc/shells 查看当前系统可用的shell 
* echo &SHELL     查看默认shell

#### 第一个shell脚本
```
echo "hello word"
#!/bin/bash
“#!” 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种Shell。echo命令用于向窗口输出文本。
```
#### 运行Shell脚本有两种方法
* 作为可执行程序
```
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
注意，一定要写成./test.sh，而不是test.sh。运行其它二进制的程序也一样，直接写test.sh，linux系统会去PATH里寻找有没有叫test.sh的，而只有/bin, /sbin, /usr/bin，/usr/sbin等在PATH里，你的当前目录通常不在PATH里，所以写成test.sh是会找不到命令的，要用./test.sh告诉系统说，就在当前目录找。
```
* 作为解释器参数
```
这种运行方式是，直接运行解释器，其参数就是shell脚本的文件名，如：
/bin/sh test.sh
/bin/php test.php
这种方式运行的脚本，不需要在第一行指定解释器信息(#!/bin/bash这种)
```

#### 变量
```
skill="Java"
echo $skill
echo "I am good at ${skill}Script"

#双引号与单引号的区别
以单引号' '包围变量的值时，单引号里面是什么就输出什么
以双引号" "包围变量的值时，输出时会先解析里面的变量和命令
url="http://c.biancheng.net"
website1='open：${url}'
website2="open：${url}"
echo $website1 ->open: ${url}
echo $website2 ->open: http://c.biancheng.net
```
* 将命令的结果赋值给变量
```
variable=`command`
variable=$(command)
第一种方式把命令用反引号包围起来，反引号和单引号非常相似，容易产生混淆，所以不推荐使用这种方式；第二种方式把命令用$()包围起来，区分更加明显，所以推荐使用这种方式。

log=$(cat log.txt)
```
* 只读变量
```
使用readonly 将变量变为只读变量
readonly s_tmp
```
* 删除变量
```
#!/bin/sh
myUrl="http://see.xidian.edu.cn/cpp/u/xitong/"
unset myUrl
echo $myUrl # 没有输出
```
* 特殊变量

特殊变量列表
变量|含义
----|----
$0|当前脚本的文件名
$n|传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数$2。
$#|传递给脚本或函数的参数个数。
$*|传递给脚本或函数的所有参数。
$@|传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。
$?|上个命令的退出状态，或函数的返回值。
$$|当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID。

* 命令行参数
运行脚本时传递给脚本的参数称为命令行参数。命令行参数用 $n 表示，例如，$1 表示第一个参数，$2 表示第二个参数，依次类推。

请看下面的脚本：
```
#!/bin/bash
echo "File Name: $0" #输出脚本文件名
echo "First Parameter : $1"   #输出第一个参数
echo "First Parameter : $2"   #输出第二个参数
echo "Quoted Values: $@"      #输出所有参数
echo "Quoted Values: $*"      #输出所有参数
echo "Total Number of Parameters : $#"   #输出参数个数

运行结果：
$./test.sh Zara Ali
File Name : ./test.sh
First Parameter : Zara
Second Parameter : Ali
Quoted Values: Zara Ali
Quoted Values: Zara Ali
Total Number of Parameters : 2
```

* \$* 和 \$@的区别

* 退出状态
\$? 可以获取上一个命令的退出状态。所谓退出状态就是上一个命令执行后的返回结果

#### 运算符

算术运算符列表
运算符|说明|举例
----|----|----
+	|加法	|`expr $a + $b` 结果为 30。
-	|减法	|`expr $a - $b` 结果为 10。
*	|乘法	|`expr $a \* $b` 结果为  200。
/	|除法	|`expr $b / $a` 结果为 2。
%	|取余	|`expr $b % $a` 结果为 0。
=	|赋值	|a=$b 将把变量 b 的值赋给 a。
==	|相等。用于比较两个数字，相同则返回 true。	|[ \$a == \$b ] 返回 false。
!=	|不相等。用于比较两个数字，不相同则返回 true。	|[ \$a != \$b ] 返回 true。
注意：条件表达式要放在方括号之间，并且要有空格，例如 [\$a==\$b] 是错误的，必须写成 [ \$a == \$b ]。

关系运算符列表
运算符|说明|举例
----|----|----
-eq	|检测两个数是否相等，相等返回 true。	|[ \$a -eq \$b ] 返回 true。
-ne	|检测两个数是否相等，不相等返回 true。	|[ \$a -ne \$b ] 返回 true。
-gt	|检测左边的数是否大于右边的，如果是，则返回 true。	|[ \$a -gt \$b ] 返回 false。
-lt	|检测左边的数是否小于右边的，如果是，则返回 true。	|[ \$a -lt \$b ] 返回 true。
-ge	|检测左边的数是否大等于右边的，如果是，则返回 true。	|[ \$a -ge \$b ] 返回 false。
-le	|检测左边的数是否小于等于右边的，如果是，则返回 true。	|[ \$a -le \$b ] 返回 true。


布尔运算符列表
运算符|说明|举例
----|----|----
!	|非运算，表达式为 true 则返回 false，否则返回 true。	|[ ! false ] 返回 true。
-o	|或运算，有一个表达式为 true 则返回 true。	|[ \$a -lt 20 -o \$b -gt 100 ] 返回 true。
-a	|与运算，两个表达式都为 true 才返回 true。	|[ \$a -lt 20 -a \$b -gt 100 ] 返回 false。
```
a=10
b=20
if [ $a != $b ]
then
   echo "$a != $b : a is not equal to b"
else
   echo "$a != $b: a is equal to b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a -lt 100 -a $b -gt 15 : returns true"
else
   echo "$a -lt 100 -a $b -gt 15 : returns false"
fi
```


#### 字符串
```
单引号
str='this is a string'
单引号字符串的限制：
单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
单引号字串中不能出现单引号（对单引号使用转义符后也不行）。

双引号
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
双引号的优点：
双引号里可以有变量
双引号里可以出现转义字符

拼接字符串
your_name="qinjx"
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1

获取字符串长度
string="abcd"
echo ${#string} #输出 4

提取子字符串
string="alibaba is a great company"
echo ${string:1:4} #输出liba

查找子字符串
string="alibaba is a great company"
echo `expr index "$string" is`
```

#### 数组
bash支持一维数组（不支持多维数组），并且没有限定数组的大小。类似与C语言，数组元素的下标由0开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于0。
* 定义数组
在Shell中，用括号来表示数组，数组元素用“空格”符号分割开。定义数组的一般形式为：
    array_name=(value1 ... valuen)
例如：
```
array_name=(value0 value1 value2 value3)
或者
array_name=(
value0
value1
value2
value3
)

还可以单独定义数组的各个分量：
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
可以不使用连续的下标，而且下标的范围没有限制。
```
* 读取数组
```
读取数组元素值的一般格式是：
    ${array_name[index]}
例如：
valuen=${array_name[2]}
```
```
举个例子：
#!/bin/sh
NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
运行脚本，输出：
$./test.sh
First Index: Zara
Second Index: Qadir
```
* 使用@ 或 * 可以获取数组中的所有元素，例如：
```
${array_name[*]}
${array_name[@]}
```
```
举个例子：
#!/bin/sh
NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"
echo "First Method: ${NAME[*]}"
echo "Second Method: ${NAME[@]}"
运行脚本，输出：
$./test.sh
First Method: Zara Qadir Mahnaz Ayan Daisy
Second Method: Zara Qadir Mahnaz Ayan Daisy
```
* 获取数组的长度
```
获取数组长度的方法与获取字符串长度的方法相同，例如：
纯文本复制
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

#### printf
```
# format-string为双引号
$ printf "%d %s\n" 1 "abc"
1 abc
# 单引号与双引号效果一样 
$ printf '%d %s\n' 1 "abc" 
1 abc
# 没有引号也可以输出
$ printf %s abcdef
abcdef
# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
$ printf %s abc def
abcdef
$ printf "%s\n" abc def
```

#### if 
```
#!/bin/sh
a=10
b=20
if [ $a == $b ]
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi
```

#### case
```
case $aNum in
    1)  echo 'You select 1'
    ;;
    2)  echo 'You select 2'
    ;;
    3)  echo 'You select 3'
    ;;
    4)  echo 'You select 4'
    ;;
    *)  echo 'You do not select a number between 1 to 4'
    ;;
esac
```

#### for
```
#!/bin/bash
for str in 'This is a string'
do
    echo $str
done
```

#### while
```
#!/bin/bash
COUNTER = 0 
while [ $COUNTER -lt 5]
do
    COUNTER = 'expr $COUNTER + 1'
    echo $COUNTER
done
```

#### 函数
在Shell中，调用函数时可以向其传递参数。在函数内部，通过$n的形式获取参数的值。
例如$1代表第一个参数
```
#!/bin/bash
funWithParam(){
    echo "The value of the first parameter is $1 !"
    echo "The value of the second parameter is $2 !"
    echo "The value of the tenth parameter is $10 !" #大于10的失手需要加{}
    echo "The value of the tenth parameter is ${10} !"
    echo "The value of the eleventh parameter is ${11} !"
    echo "The amount of the parameters is $# !"  # 参数个数
    echo "The string of the parameters is $* !"  # 传递给函数的所有参数
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

#### 输入输出重定向
* 输出重定向
```
$ command > file
$ command >> file 
```
* 输入重定向
```
$ wc -l < users
```
一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：
* 标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
* 标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
* 标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
```
$ command >file 2>&1      #输出和错误信息重定向到文件
$ command >>file 2>&1     #输出和错误信息追加到文件
$ command < file1 > file2  #将输入重定向到文件1 输出重定向到文件2
```

* /dev/null 文件
/dev/null 是一个特殊到文件，写入到它到内容都会被丢弃，如果尝试从该文件读取内容，那么什么也读不到，但是该文件非常游泳。将命令到输出重定向到它，起到禁止输出到效果。
```
$command > /dev/null
```

#### 文件包含

#### 接受键盘输入
* read [-option] [variable]
* -p 指定读取值时的提示符
* -t 指定读取时等待时间
* read -p "输入数字：" number

#### 随机抽取文件
```shell
#!/bin/bash

echo "开始执行数据集split..."

read -p "输入文件路径:" path

echo “统计文件数...”

total=$(ls -l $path | grep "^-" | wc -l )xs

#(( ))是整数运算不支持浮点数
train_num=$(( $total * 9 /10 ));
test_num=$(( $total - $train_num ));
echo "文件总数:" $total "训练集" $train_num "测试集" $test_num

test_files=$(find $path -name "*.jpg" | sort --random-sort | head -$test_num)

echo "创建test文件夹"
mkdir ./test
for filename in $test_files
do
    mv $filename ./test
done

echo "处理完成"
```




### git
* 创建分支  git branch issue55分支名字
* 查看分支  git branch  查看本地分支
* 查看远程分支 git branch -a
* checkout 远程分支 git checkout -b issue(本地分支名) origin/dev(远程分支名)
* push 到远程分支
```
git push <远程主机名> <本地分支名>:<远程分支名>
git push origin PSENET:fintune_dip
```
* git rm --cached tt/\*.png 删除缓存区的文件。 有时候添加了忽略文件 add 的时候 依然存在，是因为它在缓存区了 把它删了

* SSH 配置
```cpp
//配置用户
git config --global user.name "ss"
git config --global user.email "a@ee.com"
//生成密钥
ssh-keygen -t rsa -C "humingx@yeah.net"
//将id_rsa.pub的内容复制到github上
cat ~/.ssh/id_rsa.pub
// 认证输出 Agent pid 32524
eval "$(ssh-agent -s)"
//添加生成的 SSH key 到 ssh-agent。
ssh-add ~/.ssh/id_rsa
// 测试
ssh -T git@github.com
```
* 已存在的文件夹或 Git 仓库
```cpp
cd existing_folder
git init
git remote add origin git@code.aliyun.com:mahuichao/test.git
git add .
git commit
git push -u origin master
```

* 放弃本地代码直接将远程代码覆盖到本地
```cpp
git fetch --all
git reset --hard origin/dev (这里master要修改为对应的分支名)
git pull
```

### mysql
* mysql –uroot –hXXX.XXX.XXX.XXX –ppassword    -u -p -h 后面无空格
* show databases;    //查看数据库列表
* show tables;       //查看table列表
* select * from images where id='17';
* select * from images where id in('16','17');
* update images set is_deal=0 where project_id in ('16','17');
* 复制表数据到新表
```cpp
create table biao1 like biao2;
insert into biao1 select * from biao2;
```

### nginx 
* service nginx reload  重新加载配置

### supervisor

#### 安装
```cpp
$ sudo su - #切换为root用户

# yum install epel-release
# yum install -y supervisor
# systemctl enable supervisord # 开机自启动
# systemctl start supervisord # 启动supervisord服务

# systemctl status supervisord # 查看supervisord服务状态
# ps -ef|grep supervisord # 查看是否存在supervisord进程
```

#### 更新配置
* supervisorctl update



### centos 编译tensorflow c++ 动态库

#### 安装bazel
##### Installing Bazel on CentOS 7
* https://docs.bazel.build/versions/master/install-redhat.html
* .repo 下载地址 https://copr.fedorainfracloud.org/coprs/vbatts/bazel/
* 把*.repo 放到 /etc/yum.repos.d/ 下
* yum install bazel
**因为我要编译tensorflow1.10版本的c++ 需要bazel0.15的版本上述方法装的是最新版的bazel行不通** 
* 在git上直接下载二进制文件 bazel-0.15.0-installer-linux-x86_64.sh
* chmod +x bazel-0.15.0-installer-linux-x86_64.sh
* ./bazel-0.15.0-installer-linux-x86_64.sh  --user
* vim ~/.bashrc 配置bazel的环境变量

#### 编译 tensorflow 源文件
* git clone git@github.com:tensorflow/tensorflow.git
* git checkout -b tensorflow origin/r1.10
* [cpu 指令]bazel build --config=opt //tensorflow:libtensorflow_cc.so [gpu指令] bazel build --config=opt --config=cuda //tensorflow:libtensorflow_cc.so
**编译完成后生成libtensorflow_cc.so libtensorflow_framework.so 动态库文件**

#### 编译第三方库文件
* cd tensorflow
* cd tensorflow/contrib/makefile/
* ./bulid_all_linux.sh 


#### 使用cmake 构建程序
```cpp
#include <tensorflow/core/platform/env.h>
#include <tensorflow/core/public/session.h>

#include <iostream>

using namespace std;
using namespace tensorflow;

int main()
{
    Session* session;
    Status status = NewSession(SessionOptions(), &session);
    if (!status.ok()) {
        cout << status.ToString() << "\n";
        return 1;
    }
    cout << "Session successfully created.\n";
}
```

*  创建CMakeLists.txt
```cpp
#设置cmake的最小版本
cmake_minimum_required(VERSION 3.10)
#项目名称
project(demo)
#设置c++编译器
set(CMAKE_CXX_STANDARD 11)
#设置TENSORFLOW_DIR变量，变量内容为安装的tensorflow文件夹路径
set(TENSORFLOW_DIR /home/ma/tensorflow) 
#项目中的include路径
include_directories(${TENSORFLOW_DIR})
include_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/gen/proto)
include_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/gen/protobuf-host/include)
include_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/downloads/eigen)
include_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/downloads/nsync/public)

#项目中lib路径
link_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/gen/lib)
link_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/gen/protobuf-host/lib)
link_directories(${TENSORFLOW_DIR}/tensorflow/contrib/makefile/downloads/nsync/builds/default.linux.c++11)
link_directories(${TENSORFLOW_DIR}/bazel-bin/tensorflow)

add_executable(demo main.cpp)
#连接libtensorflow_cc.so和libtensorflow_framework库。
target_link_libraries(demo tensorflow_cc tensorflow_framework)
```

* cmake编译
注意这里要使用cmake 3.1以上的版本，我使用了3.9版本
```cpp
#使用cmake构建生成make文件
cmake .
#使用make编译
make
#运行可执行文件
./demo
```

* cmake 升级
```cpp
wget https://cmake.org/files/v3.9/cmake-3.9.2.tar.gz
gunzip cmake-3.9.2.tar.gz
tar xvf cmake-3.9.2.tar
cd cmake-3.9.2
./configure
sudo make 
sudo make install

// 【注】安装完后，执行cmake --version会报如下错误
// CMake Error: Could not find CMAKE_ROOT !!!
// CMake has most likely not been installed correctly.
// Modules directory not found in
// /Applications/CMake 2.8-11.app/Contents/bin
// CMake Error: Error executing cmake::LoadCache(). Aborting.

// 【解决方法】

// 先执行：hash -r

// 然后再执行：cmake --version

```