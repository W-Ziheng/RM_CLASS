import cv2
import numpy as np

def detect_green_triangles(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图像，请检查图像路径。")
        return

    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv_image.png",hsv)

    # 定义绿色的HSV范围
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    # 创建掩码以提取绿色区域
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 进行形态学操作，去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 查找轮廓
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历每个轮廓
    for contour in contours:
        # 近似轮廓为多边形
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # 检查是否为三角形
        if len(approx) == 3:
            # 绘制三角形
            cv2.drawContours(image, [approx], 0, (0, 0, 255), 5)

            M = cv2.moments(approx)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # 在三角形中心绘制一个小圆
                cv2.circle(image, (cX, cY), 5, (255, 0, 0), -1)
                # 显示三角形中心坐标
                cv2.putText(image, f"({cX}, {cY})", (cX - 50, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # 显示结果图像并保存图像
    cv2.imshow("recognise_image", image)
    cv2.imwrite("recognise_image.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "./png/test.png"
detect_green_triangles(image_path)

