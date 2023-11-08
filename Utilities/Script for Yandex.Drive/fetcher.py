import os
import progressbar
import parse
import shutil
import subprocess

from ya_disk_utils import *
from token_utils import *

from utilities.img_utils import *
from utilities.pdf_utils import *

token_str = get_secret_token()
y = set_disk_from_token(token_str)

def parse_input(input_s: str): # -> tuple:
    parsed = parse.parse("\"{}\"{}", input_s)
    if parsed:
        command = parsed[0].lower()
    else:
        parsed = parse.parse("\"{}\"", input_s)
        if parsed == None:
            print("{} Try \"help\"".format(input_s))
        elif parsed[0] == "help":
            print()
            print("NOTE!!! All folder names are specified without _tmp_")
            print("\"get\" \"/remote/path/to/folder\" \"destination_folder_name\" - to download remote dir to local")
            print("\"to_pdf\" \"folder_name\" \"filename.pdf\" - to make a pdf from images in downloaded folder")
            print("\"delete\" \"folder_name\" - to delete a folder")
            print("\"open\" \"file_name.pdf\" - to open a pdf")
            print("\"upload\" \"filename.suff\" \"/remote/path/where/to/upload\" - to upload file to remote folder")
            print()
        else:
            print("{} Try \"help\"".format(input_s))
        return

    if command == 'get':
        inp_lst = parse.parse("\"{}\" \"{}\" \"{}\"", input_s)

        path_on_drive = inp_lst[1]
        dest_folder = "_tmp_" + inp_lst[2]
        download_folder(y, path_on_drive, dest_folder)

    elif command == 'to_pdf':
        inp_lst = parse.parse("\"{}\" \"{}\" \"{}\"", input_s)

        folder_name = "_tmp_" + inp_lst[1]
        file_name = inp_lst[2]

        valid = images_in_folder(folder_name)
        if valid:
            print("PDF is being processed")
            pdf_from_folder(file_name, valid)
        else:
            print("No images found, omiting directory {}".format(folder_name))

    elif command == 'delete':
        foldername = "_tmp_" + parse.parse("\"{}\" \"{}\"", input_s)[1]
        print("Removing: {}".format(foldername))
        shutil.rmtree(foldername, ignore_errors=True)

    elif command == "upload":
        inp_lst = parse.parse("\"{}\" \"{}\" \"{}\"", input_s)

        file_name = inp_lst[1]
        folder_name = inp_lst[2]
        
        print("Uploading: {} to {}".format(file_name, folder_name))

        for i in progressbar.progressbar(range(1), redirect_stdout=True):
            y.upload(file_name, folder_name + "/" + file_name)

    elif command == 'open':
        filename = parse.parse("\"{}\" \"{}\"", input_s)[1]
        print("Opening: {}".format(filename))
        subprocess.run(['open', filename], check=True)

    elif command == 'rotate':
        inp_lst = parse.parse("\"{}\" \"{}\" \"{}\"", input_s)

        folder_name = "_tmp_" + inp_lst[1]
        n = int(inp_lst[2])

        valid = images_in_folder(folder_name)
        if valid:
            print("Folder is being processed")
            rotate_folder(n, valid)
        else:
            print("No images found, omiting directory {}".format(folder_name))


    elif command == 'help':
        print("\"get\" \"/remote/path/to/folder\" \"destination_folder_name\" - to download remote dir to local")
        print("\"to_pdf\" \"folder_name\" \"filename.pdf\" - to make a pdf from images in downloaded folder")
        print("\"delete\" \"folder_name\" - to delete a folder")
        print("\"open\" \"file_name.pdf\" - to open a pdf")
        print("\"rotate\" \"folder_name\" \"n\" - rotate all images in a folder for n degrees clockwise")
        print("\"upload\" \"filename.suff\" \"/remote/path/where/to/upload\" - to upload file to remote folder")

    else:
        print("Try \"help\"")

s = input().strip()
while s:
    parse_input(s)
    s = input().strip()

