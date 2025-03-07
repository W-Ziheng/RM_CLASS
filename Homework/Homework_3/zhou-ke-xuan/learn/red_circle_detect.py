import cv2
import numpy as np

# 初始化摄像头
cap = cv2.VideoCapture(0) # 数字根据自己摄像头确定编号

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        print("无法获取视频帧")
        break

    # 将图像转换为HSV颜色空间（更好的颜色分离）
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 定义红色的HSV范围（需要根据实际情况调整）
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # 创建红色掩膜
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # 图像预处理
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (9, 9), 2)

    # 霍夫圆检测
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                              param1=50, param2=30, minRadius=20, maxRadius=200)

    # 如果检测到圆形
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        
        # 遍历所有检测到的圆
        for (x, y, r) in circles:
            # 绘制圆形和中心点
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)
            # 显示圆心坐标
            cv2.putText(frame, f"({x}, {y})", (x-50, y-20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # 显示结果
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()