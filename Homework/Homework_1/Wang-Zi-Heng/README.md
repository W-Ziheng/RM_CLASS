**这是一个示例**
> readme应该详细展示我如何 git 你的项目在我的本地使用

### git clone

```shell
git clone -b Homework https://github.com/W-Ziheng/RM_CLASS.git
# git checkout Homework 
```

failed的话可以试一下这个
```shell
git clone -b Homework git@github.com:W-Ziheng/RM_CLASS.git
```

### 展示运行环境
> Ubuntu22.04 
> ROS2-Humble 
> Python 3.11.4 
> g++ 4.9.2

### 如何运行你的程序

```shell
cd ./Homework1/Wang-Zi-Heng/src/
g++ case1 -o case1
./case1
python case2
```

> 输出示例 见 ***终端演示.png***

### 解释项目结构

> Wang-Zi-Heng-Homework1
├── README.md       # 项目描述文件
├── src             # 源代码目录
│   ├── case1.cpp
│   ├── case2.py   
└── 终端演示.png


> 注意 在 UTF-8 格式下 
> - 符号 **├──** 通过按住 Alt + 43459/43460 释放 Alt 输出  
> - 符号 **└──** 通过按住 Alt + 43456/43460 释放 Alt 输出
> - 符号 **│** 通过按住 Alt + 43443 输出

> 项目名称 (其他示例)

├── README.md       # 项目描述文件
├── LICENSE         # 许可证文件
├── .gitignore      # Git忽略配置文件
├── src             # 源代码目录
│   ├── main.py     # 主程序文件
│   ├── config.py   # 配置文件
│   └── utils       # 工具模块目录
│       ├── __init__.py
│       └── helpers.py
├── tests           # 测试目录
│   ├── __init__.py
│   └── test_main.py
└── docs            # 文档目录
    └── documentation.md








