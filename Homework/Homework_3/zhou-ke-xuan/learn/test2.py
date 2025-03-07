import cv2
import numpy as np

# 读取图像（OpenCV默认读取为BGR格式）
img_bgr = cv2.imread("image.png")

# # 转换为RGB格式
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 分离RGB通道
r, g, b = cv2.split(img_rgb)

# 合并RGB通道
img_red = cv2.merge([r, g, b])

# 显示图像
cv2.imshow("Original Image", img_bgr)
cv2.imshow("Red Image", img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()