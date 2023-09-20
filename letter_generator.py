from PIL import Image, ImageDraw, ImageFont
import os


def generate_all_alphabet(font_name, alphabet, color=(0, 0, 255, 255)):
    output_dir_name = f"{font_name.split('.ttf')[0].split('/')[-1]}"
    try:
        os.makedirs(output_dir_name)
    except FileExistsError:
        pass
    fontsize = None
    font = None
    for letter in alphabet:
        img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        if not fontsize or font:
            fontsize = 1
            font = ImageFont.truetype(font_name, fontsize)
            while font.getsize(letter)[0] < img.size[0] * 0.9 and font.getsize(letter)[1] < img.size[1] * 0.9:
                fontsize += 1
                font = ImageFont.truetype(font_name, fontsize)
            fontsize -= 1
            font = ImageFont.truetype(font_name, fontsize)

        letter_width, letter_height = font.getsize(letter)
        position = ((img.width - letter_width) // 2, (img.height - letter_height) // 2)
        draw.text(position, letter, fill=color, font=font)
        img.save(f"{output_dir_name}/letter_{letter}.png", "PNG")
