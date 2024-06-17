from PIL import Image, ImageDraw, ImageFont

def generate_image(text, filename, img_size=(640, 480)):
    img = Image.new('RGB', img_size, color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), text, fill=(255, 255, 255), font=font)
    img.save(filename)
