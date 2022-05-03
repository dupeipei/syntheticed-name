import random

from PIL import Image, ImageDraw, ImageFont

# 显示的名字
text = "范卓轩"
# 名字的大小
font_size = 660
# 显示的长度
display_width = 2000
# 显示的宽度
display_height = 1080
# 系统文字的路径
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
# 显示的名字数量
name_count = 52014


def generate_mirror_text(text, rotate_angle, size):
    """
        Get the rotated image.

        :param text: Displayed text which is small.
        :param rotate_angle: Angle of rotation.
        :param size: The font size of small text.
        :return: The ratated image.
    """
    font = ImageFont.truetype(font_path, size=size)
    img = Image.new('1', font.getsize(text), (255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, fill=0, font=font)
    rImg = img.rotate(rotate_angle, expand=1, fillcolor=255)
    return rImg

# 计算旋转后的图像（一点点倾斜比较好看）
rImg = generate_mirror_text(text, 20, 10)

# 画布底色
img = Image.new('RGB', (display_width, display_height), (255, 255, 255))

# 可以参照对照原图有没有歪
# draw = ImageDraw.Draw(img)
# draw.text((0, 0), text, fill=(0, 0, 0), font=font)

# 大字系统字体
font = ImageFont.truetype(font_path, size=font_size)
width, height = mask_raw = font.getmask(text, mode='1').size
mask = [x for x in font.getmask(text, mode='1')]

# 获取大字掩码集
pixel_set = set()
for i, val in enumerate(mask):
    if val == 255:
        tmp = (i % width, int(i / width))
        pixel_set.add(tmp)

# 随机取name_count个点，用小字覆盖
pixel_list = random.sample(pixel_set, name_count)
for i, pixel in enumerate(pixel_list):
    width = int(rImg.width/2)
    height = int(rImg.height/2)
    img.paste(rImg, (pixel[0]-width, pixel[1]+2*height, pixel[0]+width, pixel[1]+4*height))
    pixel_set.remove(pixel)
img.show()



