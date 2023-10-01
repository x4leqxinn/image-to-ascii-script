from utils.file_manager import get_image_names,img_to_ascii

if __name__ == '__main__':
    filenames = get_image_names()
    for filename in filenames:
        img_to_ascii(filename=filename)