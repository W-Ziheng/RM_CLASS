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
    
    # 定义绿色的HSV范围（需要根据实际情况调整）
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([100, 255, 255])

    # 创建绿色掩膜
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 图像预处理
    mask = cv2.GaussianBlur(mask, (9, 9), 2)

    # 定义结构元素
    kernel = np.ones((5, 5), np.uint8)

    # 膨胀操作
    mask = cv2.dilate(mask, kernel, iterations=1)

    # 侵蚀操作
    mask = cv2.erode(mask, kernel, iterations=1)

    # 边缘检测
    edges = cv2.Canny(mask, 50, 150)

    # 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历每一个轮廓
    for contour in contours:

        # 轮廓近似
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # 如果轮廓近似后的顶点数为3，则绘制三角形
        if len(approx) == 3:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)

    # 显示结果
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放资源
cap.release()
cv2.destroyAllWindows()