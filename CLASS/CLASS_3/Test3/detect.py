import cv2
import numpy as np

# 读取图像
img_bgr = cv2.imread('image.png')

# 转换为HSV颜色空间（注意OpenCV中H范围为[0,179]，S/V为[0,255]）
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# 分离HSV通道
h, s, v = cv2.split(img_hsv)

# 示例：提取红色区域（H≈0或H≈180附近）
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask_red = cv2.inRange(img_hsv, lower_red1, upper_red1) | cv2.inRange(img_hsv, lower_red2, upper_red2)

# 显示原始图像和红色掩膜
cv2.imshow('Original Image', img_bgr)
cv2.imshow('Red Mask', mask_red)

# 等待按键，然后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
