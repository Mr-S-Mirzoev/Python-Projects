import os
from PIL import Image
import progressbar
from uuid import uuid1
from pathlib import Path

def rotate_folder(degrees: int, img_list: list):
    length = len(img_list)
    dir_name = "_tmp_" + str(uuid1())
    print("Created a temporary folder {}".format(dir_name))
    os.mkdir(dir_name)

    for i in progressbar.progressbar(range(length), redirect_stdout=True):
        image_name = img_list[i]
        colorImage = Image.open(image_name)
        # Rotate it by 45 degrees
        rotated = colorImage.rotate(360 - (degrees % 360), expand=1)
        
        name = img_list[i][img_list[i].find('/') + 1:img_list[i].rfind('.')]
        rotated.save("{}/{}.jpeg".format(dir_name, name), "JPEG")

def check_image_with_pil(path):
    try:
        Image.open(path)
    except IOError:
        return False
    return True

def images_in_folder(folder_name: str, log=False) -> list:
    paths = sorted(Path(folder_name).iterdir(), key=os.path.getmtime)
    valid = list()
    for path in paths:
        failed = False
        if not check_image_with_pil(path.resolve()):
            os.remove(path.resolve())
            failed = True
        else:
            valid.append("{}/{}".format(folder_name, path.name))
        
        if log:
            print("File: {} is {}".format(path.name, "is not a vailid image and was removed" if failed else "a valid image"))
    
    return valid