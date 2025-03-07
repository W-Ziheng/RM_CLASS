import cv2
import numpy as np

# 初始化摄像头
cap = cv2.VideoCapture(0) # 数字根据自己摄像头确定编号
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取视频帧")
        break

    # 将图像转换为HSV颜色空间（更好的颜色分离）
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 定义绿色的HSV范围（需要根据实际情况调整）
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (9, 9), 2)

    # 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # 近似多边形
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # 如果近似多边形有三个顶点，则认为是三角形
        if len(approx) == 3:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)
            
            # 获取三角形的质心
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # 绘制质心
                cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
                # 在图像上标注坐标
                cv2.putText(frame, f"({cX}, {cY})", (cX - 50, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # 显示结果
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()