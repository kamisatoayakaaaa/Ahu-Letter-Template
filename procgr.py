from PIL import Image

def process_image(input_path, output_path, opacity_factor=1.0):
    """
    将图片的白色背景变为透明，并调整图片整体透明度。
    
    参数:
      input_path: 输入图片路径
      output_path: 输出图片路径（建议使用 PNG 格式以支持透明度）
      opacity_factor: 调整透明度因子，取值范围 (0,1]；1 表示不改变透明度，小于1会使图像整体变得更透明
    """
    # 打开图片并转换为RGBA模式（保证有alpha通道）
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # 判断白色背景（这里设定RGB均大于240认为是白色，可以根据实际情况调整阈值）
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            # 将白色像素设为全透明
            newData.append((255, 255, 255, 0))
        else:
            # 对其他像素，根据原有透明度调整透明度因子
            # 保证透明度不会超过255
            new_alpha = int(item[3] * opacity_factor)
            new_alpha = max(0, min(255, new_alpha))
            newData.append((item[0], item[1], item[2], new_alpha))
    
    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"处理完成，已保存为 {output_path}")

if __name__ == "__main__":
    # 输入图片路径和输出图片路径
    input_path = "pic\\bg.jpg"    # 请替换为你的图片文件路径
    output_path = "output.png"  # 输出文件（请确保文件后缀支持透明度，如 PNG）
    
    # 设置图片透明度因子，例如 0.8 表示整体透明度降低20%
    opacity_factor = 0.3
    
    process_image(input_path, output_path, opacity_factor)
