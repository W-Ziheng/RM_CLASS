# 关于ros2的个人学习历程
## 一.对ros2整体框架进行初步理解
- **这一过程主要通过观看B站视频以及在CSDN，github上查阅相关资料所进行学习** 
>b站视频路径：https://www.bilibili.com/video/BV16B4y1Q7jQ?spm_id_from=333.788.videopod.episodes&vd_source=dbc17945aca636bd9433b987661247b2&p=6

- **1.1 工作空间及功能包**
- 首先是对工作空间及功能包的定义产生困惑，后经过不断的查阅资料和思考，最终明白了工作空间即可当作一个目录，在此目录下存有大量的功能包，而功能包中存放了对应的节点，且对应不同的编程语言有不同的功能包，而这样做的目的即是为了在我们运行节点的时候更好的找到对应的功能包

>csdn链接：https://blog.csdn.net/qq_27865227/article/details/131366161?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522510A3E51-5253-4E82-970A-BCE56BC1BDBB%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=510A3E51-5253-4E82-970A-BCE56BC1BDBB&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-131366161-null-null.142^v100^pc_search_result_base1&utm_term=ros2%E5%8A%9F%E8%83%BD%E5%8C%85%E3%80%81&spm=1018.2226.3001.4187
- **1.2 节点**
- 这一块主要是对节点的定义和如何编写运行节点进行学习，学习渠道主要是通过b站以及在CSDN平台上查询相关资料，节点类似于人体中一个个独立的细胞，每个节点负责一个对应的功能，且节点间可进行通信，将信息进行传递，使机器人可以进行完整的动作。
- **针对节点的编写**：1.编辑接口初始化 2.创建节点并初始化 3.实现节点功能 4.销毁节点并关闭接口 
- **运行节点**：ros2 run <所在文件名> <节点名称>
>CSDN链接：https://blog.csdn.net/qq_27865227/article/details/131365956
>b站相关连接：https://www.bilibili.com/video/BV16B4y1Q7jQ/?p=7&spm_id_from=333.880.my_history.page.click&vd_source=dbc17945aca636bd9433b987661247b2
- **1.3 话题及服务**
- **1.3.1** 话题是节点间通信的桥梁，一个节点可以在某一话题上发布信息，另一个节点可以通过订阅该话题，以获取发布信息
>CSDN链接：https://blog.csdn.net/qq_27865227/article/details/131407223
- **1.3.2** ros2的服务中包括了服务器端和客户端，其中客户端向服务器官进行提问而服务器端对此问题进行答复并传输回客户端，客户端可以有多个而服务器端仅有一个
>CSDN链接：https://blog.csdn.net/qq_27865227/article/details/131407432
## 二.视觉组第二次作业的学习完成过程 
**2.1 对作业的分析**
- 本次作业要求编写一个listener和publisher，发布消息为welcome to RM,完成本次任务首先需要创建一个工作空间以及在此工作空间中安装好对应功能包，并在功能包中创建所需节点，编写对应代码。

**2.2 在编写过程中所遇到的问题**
- 在此过程中的前期准备阶段较为顺利，但是在具体运行过程中还是不可避免的出现了一定的错误，比如出现了无法找到功能包，无法找到接入口等问题，这些问题后通过ai查询以及学习更多知识后得以发现为问题存在于set.up的设置之上，发现问题后经过不断的调试最终成功解决了问题

  