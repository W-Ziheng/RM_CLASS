<!-- ---
title: 视觉组培训
tags:
  - Blog
  - Robomaster
  - 视觉组培训
top_img: transparent
date: 2024-10-22 18:06:22
--- -->

> 本文为2024年福州大学robomatser浮舟湿地战队视觉组培训文档,如有错误请联系**2260274457(QQ)**

# 视觉组第一次培训

> 本次培训主要会带大家初识一下linux系统的一些简单配置操作,体验一下ros2的一些自带包,会有小作业,相对来说比较轻松:sunny::sunny:

## 课前预习

> 确保ubuntu正确配置且版本为22.04 , ROS2版本为humble

打开终端(Ctrl+Alt+T),输入以下指令

```shell
cat /etc/os-release && echo $ROS_DISTRO
```
查看输出版本是否为22.04和humble
```shell
VERSION="22.04.5 LTS (Jammy Jellyfish)"
humble
```
<!-- cat是concatenate的缩写,此处用于显示目录文件的内容 -->

## Basic Skills

> **非必须却必须掌握的小技能**

- Github注册    

- Markdown

- python  

- c++      
 
## linux 

why ubuntu ?

### 终端常用命令
```shell
ls # list的缩写
pwd # 显示当前路径
cd # 切换目录
mkdir #新建文件夹
touch <file> #新建文件
rm <file>
rm -r <file>
sudo rm -rf <file> # 谨慎用
cp <file1> <file2_aim>
cp -r <file1> <file2_aim>
mv <old_name> <new_name>
cat <file> # 连接显示文件内容
history
```

### 终端常用技巧

```shell
Ctrl+shift+C/V # 复制粘贴
tab # 自动补全
!! #重复上次命令,常用sudo!!
ctrl+r #补全历史命令
ctrl+c #终止程序
ctrl+z #暂停程序,挂载在后台
```

<!-- ```shell
ps aux # 显示当前运行进程

``` -->


## Hello World.cpp

安装vscode
```shell
sudo apt update
sudo apt install code
```

也可通过小鱼的一键安装进行配置
```shell
wget http://fishros.com/install -O fishros && . fishros
```

安装g++
```shell
sudo apt install g++
```

```shell
code . #打开vscode
```

> 一些常见好用的插件
c/c++


```cpp
#include <iostream>

int main(){
    std::cout <<"hello world!"<<std::endl;
    return 0;
}
```

编译
```shell
g++ hello.cpp -o hello
```

运行
```shell
./hello
```

## Hello World.py

```shell
touch hello.py
code hello.py
```
输入以下内容
```py
print("Hello World!")
```

运行
```shell
python3 hello.py
```

> python 编译型语言，执行速度快、效率高；依靠编译器、跨平台性差些。
> C++ 解释型语言，执行速度慢、效率低；依靠解释器、跨平台性好。

## Terminate

> Terminator 是linux中一个非常实用且开源的终端仿真器

```shell
sudo apt install terminator
```
以后打开终端便会自动是用terminator

> 常见的指令

```shell
Ctrl+Shift+O     #水平分割终端
Ctrl+Shift+E     #垂直分割终端
```

## ros2的一些自带包

> Talker and Listener

倾听者
```shell
ros2 run demo_nodes_py listener
```

说话者
```shell
ros2 run demo_nodes_cpp talker
```

> 海龟

启动海龟节点

```shell
ros2 run turtlesim turtlesim_node
```

启动海龟控制节点

```shell
ros2 run turtlesim turtle_teleop_key
```

接下来就可以控制海龟啦!

## 作业

- 用md语法对今天讲到的一些命令行知识等做总结注释笔记(根据自己情况写,也可添加其余知识)

- 用mkdir等终端命令创建CLASS_1文件夹,在此目录下分别用python 和 c++ 编写两个程序输出 Welcome to RM ! (**需提供histroy终端命令,以及程序源码**)

以压缩包形式发送至邮箱 2260274457@qq.com 压缩包命名为 **视觉组第一次作业+学号+姓名的方式**

:warning: **鼓励用github上传自己的源码,并提供readme的git方式**
































