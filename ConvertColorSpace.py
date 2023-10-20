import os
import cv2
from tqdm import tqdm
# 输入文件夹路径
visible_image_folder = r"C:\Users\admin\Desktop\Dataset\MSRStestNum\vi"
infrared_image_folder = r"H:\FuseResult\MSRS\test\DIDFuse"

# 输出文件夹路径
output_folder = "output_folder"

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 定义颜色空间名称和亮度通道范围
color_spaces = {
    # "HSV": (cv2.COLOR_BGR2HSV, cv2.COLOR_HSV2BGR, 0, 255),
    # "HSL": (cv2.COLOR_BGR2HLS, cv2.COLOR_HLS2BGR, 0, 100),
    "YCbCr": (cv2.COLOR_BGR2YCrCb, cv2.COLOR_YCrCb2BGR, 0, 255),
    "YUV": (cv2.COLOR_BGR2YUV, cv2.COLOR_YUV2BGR, 0, 255),
    "LAB": (cv2.COLOR_BGR2Lab, cv2.COLOR_Lab2BGR, 0, 255),
    #"LCH": (cv2.COLOR_BGR2Lab, cv2.COLOR_Lab2BGR, 0, 255)
}

# 遍历颜色空间
for color_space, (conversion, reverse_conversion, min_value, max_value) in color_spaces.items():
    # 创建颜色空间文件夹
    color_space_folder = os.path.join(output_folder, color_space)
    os.makedirs(color_space_folder, exist_ok=True)

    # 遍历可见光图像文件
    for visible_image_name in tqdm(os.listdir(visible_image_folder)):
        if visible_image_name.endswith(".jpg") or visible_image_name.endswith(".png"):
            visible_image_path = os.path.join(visible_image_folder, visible_image_name)
            infrared_image_name = visible_image_name  # 使用相同文件名的红外图像
            infrared_image_path = os.path.join(infrared_image_folder, infrared_image_name)

            # 读取可见光图像
            visible_image = cv2.imread(visible_image_path)

            # 读取红外图像并将其转换为灰度图像
            infrared_image = cv2.imread(infrared_image_path, cv2.IMREAD_GRAYSCALE)

            # 将可见光图像转换为指定的颜色空间
            converted_image = cv2.cvtColor(visible_image, conversion)

            # 归一化亮度通道
            converted_image[:, :, 0] = (converted_image[:, :, 0] - min_value) / (max_value - min_value) * 255

            # 将红外图像的灰度通道作为亮度通道的值
            if color_space in ['HSV','HSL'] :
                converted_image[:, :, 2] = infrared_image
            else:
                converted_image[:, :, 0] = infrared_image

            # 反归一化亮度通道
            converted_image[:, :, 0] = (converted_image[:, :, 0] / 255) * (max_value - min_value) + min_value

            # 将转换后的图像从指定的颜色空间转换回RGB模式
            converted_image_rgb = cv2.cvtColor(converted_image, reverse_conversion)

            # 保存转换后的图像
            output_image_path = os.path.join(color_space_folder, visible_image_name)
            cv2.imwrite(output_image_path, converted_image_rgb)
