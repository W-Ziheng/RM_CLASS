下载名为CLASS_1_2的工作空间后

1.打开一个终端后先输入colcon build
2.输入source install/setup.bash
3.输入ros2 run publisher publisher_node

4.打开另一个终端colcon build 
5.输入source install/setup.bash 
6.输入ros2 run listener listener_node

同时为也说一下此次上传发现的问题：
1.上传的文件无法超过100个，一开始直接上传CLASS_1_2工作空间时是上传失败（我也不清楚为什么会有如此多文件），后来时分成小块上传后再组合起来的。
2.原本有一个log文件夹上传时发生错误（不太清楚什么原因，好像是一个名为latest的文件无法识别）最终尝试了很多次也没成功，但是我在ubuntu上试着移除了该文件夹，发现话题仍然可以正常运行。

本次使用vscode进行上传。
0043