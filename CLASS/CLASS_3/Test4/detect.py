import cv2
import matplotlib.pyplot as plt

# 读取图像
img_bgr = cv2.imread("image.png")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 转换为不同颜色空间
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
img_ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)

# 可视化
plt.figure(figsize=(15,10))
plt.subplot(2,2,1), plt.imshow(img_rgb), plt.title("RGB")
plt.subplot(2,2,2), plt.imshow(img_hsv), plt.title("HSV")
plt.subplot(2,2,3), plt.imshow(img_lab), plt.title("LAB")
plt.subplot(2,2,4), plt.imshow(img_ycrcb), plt.title("YCbCr")
plt.show()