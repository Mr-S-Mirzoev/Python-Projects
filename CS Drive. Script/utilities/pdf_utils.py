import progressbar
from PIL import Image

def pdf_from_folder(filename: str, imagelist: list):
    # imagelist is the list with all image filenames
    print("Converting a list of {} images to " + filename)

    length = len(imagelist)

    print("ETA: {}:{}".format(length // 120, (length // 2) % 60))

    im_list = list()
    for i in range(1, length):
        im_list.append(Image.open(imagelist[i]))

    for i in progressbar.progressbar(range(1), redirect_stdout=True):
        Image.open(imagelist[0]).save(filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)