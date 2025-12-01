import subprocess
import os

def mp4_to_gif(input_path, output_path, fps=15, scale=None):
    """
    将 MP4 转换为 GIF
    :param input_path: 输入 mp4 文件路径
    :param output_path: 输出 gif 文件路径
    :param fps: 转换后 gif 帧率，默认15
    :param scale: 缩放宽度，例如 480。保持宽高比。
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-vf", f"fps={fps}" + (f",scale={scale}:-1" if scale else ""),
        "-y",
        output_path
    ]

    subprocess.run(cmd, check=True)
    print(f"转换完成！GIF 文件已保存到: {output_path}")


# 使用示例
if __name__ == "__main__":
    mp4_to_gif("AlphaPose_output.mp4", "AlphaPose_output.gif", fps=12, scale=480)
