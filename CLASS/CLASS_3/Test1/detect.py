import cv2

# 读取图像
image = cv2.imread('armor.png')

# 检查图像是否成功读取
if image is None:
    print("图像读取失败，请检查文件路径")
else:
    # 将图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 显示原始图像和灰度图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Gray Image', gray_image)

    # 等待按键按下，然后关闭所有窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存灰度图像
    cv2.imwrite('armor_gray.png', gray_image)
