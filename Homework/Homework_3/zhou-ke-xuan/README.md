# openCV 
## task1 识别绿色三角形  

源文件为`green_triangle_detect.py`  
模仿上课文件`red_circle_detect.py`  
使用笔记本自带摄像头编号0  
主要区别在于
1. 绿色的SHV范围
2. 三角形的识别：使用三角形轮廓及三个顶点  
***运行***  :python3 green_triangle_detect.py
运行结果见green_triangle_detect_frame.png与green_triangle_detect_mask.png
## task2 用ros2订阅摄像头内容并在右上角画正方形
~~大量使用AI调试 doge~~
***运行*** :终端1：ros2 run image_processor image_processo      
            终端2：ros2 run rqt_image_view rqt_image_view  
运行结果见ros_draw.png