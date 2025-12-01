import cv2
import os
import glob

# 设置参数
image_folder = '.'  # 当前目录
output_video = 'output.mp4'
fps = 30  # 帧率，可根据需要调整

# 获取所有以数字命名的 .png 文件（如 0.png, 1.png, ..., 100.png）
images = []
for file in os.listdir(image_folder):
    if file.endswith('.png'):
        try:
            # 尝试将文件名（不含扩展名）转为整数
            idx = int(os.path.splitext(file)[0])
            images.append((idx, file))
        except ValueError:
            # 如果文件名不是纯数字（如 "frame_1.png"），则跳过
            continue

# 按数字索引排序
images.sort(key=lambda x: x[0])
image_files = [file for _, file in images]

if not image_files:
    print("未找到符合条件的图片（如 0.png, 1.png, ...）")
    exit()

# 读取第一张图以获取尺寸
first_image_path = os.path.join(image_folder, image_files[0])
frame = cv2.imread(first_image_path)
if frame is None:
    raise ValueError(f"无法读取图像: {first_image_path}")
height, width, layers = frame.shape

# 定义视频编码器和 VideoWriter 对象
# 使用 'mp4v' 编码器生成 .mp4 文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# 逐帧写入视频
for image_file in image_files:
    img_path = os.path.join(image_folder, image_file)
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"警告：跳过无法读取的图像 {image_file}")
        continue
    video.write(frame)

# 释放资源
video.release()
print(f"✅ 视频已保存为: {output_video}")
