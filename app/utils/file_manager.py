import PIL.Image
import os

EXTENSIONS = [".png", ".jpg", ".jpeg"]

def remove_ext(filename: str):
    basename, extension = os.path.splitext(filename)
    if not extension in EXTENSIONS: return filename
    return basename
    

def get_image_names():
    directory = './images/'

    if os.path.exists(directory):
        all_names = os.listdir(directory)
        image_names = [file for file in all_names if any(file.endswith(ext) for ext in EXTENSIONS)]
        return image_names
    else:
        print(f"{directory} directory does not exist")

def img_to_ascii(filename: str):
    path = f'./images/{filename}'
    try:
        img = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
        return


    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    filename = remove_ext(filename)

    with open(f'./ascii_art/{filename}.txt', "w") as f:
        f.write(ascii_image)