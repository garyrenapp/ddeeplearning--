
https://www.bilibili.com/video/av18156598/?p=15
## 文件处理命令
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


