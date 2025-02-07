# RM_CLASS Homework_2 使用指南

## 项目概述

本项目是机器人学课程（RM_CLASS）的第二次作业，包含了两个任务：Task1和Task2。Task1是一个简单的C++程序，用于打印"Hello RM!"。Task2是一个ROS 2包，包含发布者和监听者节点，用于在ROS 2环境中进行消息发布和订阅。

## 目录结构

```shell
Homework_2/
├── Task1/
│   ├── CMakeLists.txt
│   ├── includes/
│   │   └── hello.hpp
│   ├── src/
│   │   └── cmake.cpp
│   └── tools/
│       └── hello.cpp
└── Task2/
    ├── Publisher2Listener/
    │   ├── CMakeLists.txt
    │   ├── include/
    │   ├── install/
    │   ├── package.xml
    │   └── src/
    │       ├── listener.cpp
    │       └── publisher.cpp
    └── Publisher2Listener_py/
        ├── Publisher2Listener_py/
        │   ├── __init__.py
        │   ├── listener.py
        │   └── publisher.py
        ├── install/
        ├── package.xml
        ├── resource/
        ├── setup.py
        ├── src/
        └── test/
```

## 如何运行

### Task1

1. 打开终端，导航到`Task1`目录：
   ```shell
   cd ./RM_CLASS/Homework/Homework_2/Wang-Zi-Heng/Task1
   ```
2. 使用CMake生成构建文件：
   ```shell
   cmake .
   ```
3. 编译程序：
   ```shell
   mkdir build 
   cd build 
   make
   ```
4. 运行生成的可执行文件：
   ```shell
   ./cmake_exe
   ```

### Task2

#### Publisher2Listener (C++版本)

1. 打开终端，导航到`Publisher2Listener`目录：
   ```shell
   cd ./RM_CLASS/Homework/Homework_2/Wang-Zi-Heng/Task2/Publisher2Listener
   ```
2. 使用colcon构建ROS 2包：
   ```shell
   colcon build
   ```
3. 激活安装环境：
   ```shell
   source install/setup.sh
   ```
4. 运行发布者节点：
   ```shell
   ros2 run Publisher2Listener publisher
   ```
5. 在另一个终端窗口中，运行监听者节点：
   ```shell
   ros2 run Publisher2Listener listener
   ```
    (能附上图片更好)
#### Publisher2Listener_py (Python版本)

1. 打开终端，导航到`Publisher2Listener_py`目录：
   ```shell
   cd ./RM_CLASS/Homework/Homework_2/Wang-Zi-Heng/Task2/Publisher2Listener_py
   ```
2. 安装Python包：
   ```shell
   python3 setup.py install
   ```
3. 激活安装环境：
   ```shell
   source install/setup.sh
   ```
4. 运行Python发布者节点：
   ```shell
   ros2 run Publisher2Listener_py publisher
   ```
5. 在另一个终端窗口中，运行Python监听者节点：
   ```shell
   ros2 run Publisher2Listener_py listener
   ```

## 注意事项

- 请确保在运行Task2之前已经安装了ROS 2。
- 本指南中的命令行步骤可能需要根据您的具体环境进行调整。

## 贡献者

- Wang-Zi-Heng (维护者)

## 许可证

- Task1: TODO: 许可证声明
- Task2: TODO: 许可证声明

---