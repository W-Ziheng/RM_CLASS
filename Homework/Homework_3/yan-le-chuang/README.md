# class_3 openCV

## 文件概况

.
├── 截图 2025-03-29 22-26-04.png
├── 截图 2025-03-29 22-27-25.png
├── 截图 2025-03-29 23-07-33.png
├── build
│   ├── camera_publisher
│   ├── COLCON_IGNORE
│   └── image_processor
├── green_triangle.py
├── install
│   ├── camera_publisher
│   ├── COLCON_IGNORE
│   ├── image_processor
│   ├── local_setup.bash
│   ├── local_setup.ps1
│   ├── local_setup.sh
│   ├── _local_setup_util_ps1.py
│   ├── _local_setup_util_sh.py
│   ├── local_setup.zsh
│   ├── setup.bash
│   ├── setup.ps1
│   ├── setup.sh
│   └── setup.zsh
├── log
│   ├── build_2025-03-29_21-00-00
│   ├── build_2025-03-29_21-02-03
│   ├── build_2025-03-29_22-19-50
│   ├── COLCON_IGNORE
│   ├── latest -> latest_build
│   └── latest_build -> build_2025-03-29_22-19-50
├── README.md
└── workspace
    ├── build
    ├── install
    ├── log
    └── src

​               ├── camera_publisher
​               └── image_processor

## task1 识别绿色三角形

源程序名为 green_triangle.py，根据提供的识别红色圆形程序进行的改动。效果如下图。

![](/home/ylc/RM/yan-le-chuang/截图 2025-03-29 23-07-33.png)

## task2 ros2和openCV的转换

1.图像发布话题 在终端运行 ros2 run camera_publisher camera_publisher_node.

2.图像接受、识别、再发布 在终端运行 ros2 run image_processor image_processor_node.

3.用rviz2显示图像消息 在终端运行 rviz2.

具体效果如下图。

![](/home/ylc/图片/截图/截图 2025-03-29 22-26-04.png)

![](/home/ylc/RM/yan-le-chuang/截图 2025-03-29 22-27-25.png)