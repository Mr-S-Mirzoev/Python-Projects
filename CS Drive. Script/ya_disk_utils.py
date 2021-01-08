import yadisk
import os
import progressbar

def set_disk_from_token(token_string: str):
    y = yadisk.YaDisk(token=token_string)

    # Проверяет, валиден ли токен
    if y.check_token():
        print("Token is valid")
    else:
        raise RuntimeError("Token is invalid")

    return y

def directory_contains(y, path_on_drive: str, full_paths=False) -> list:
    directory_contains = list()

    for item in list(y.listdir(path_on_drive)):
        if full_paths:
            file = dict()
            file['full'] = path_on_drive + '/' + item["name"]
            file['name'] = item["name"]
            directory_contains.append(file)
        else:
            directory_contains.append(item["name"])
    
    return directory_contains

def download_folder(y, path_on_drive: str, folder_name: str):
    os.mkdir(folder_name)
    base_dir = os.getcwd()

    os.chdir(folder_name)
    contains = directory_contains(y, path_on_drive, full_paths=True)
    length = len(contains)

    path_on_drive_folder_name = os.path.basename(os.path.normpath(path_on_drive))
    print("Downloading the remote folder {} to local folder {}".format(path_on_drive_folder_name, folder_name))
    print("The full path to femote folder {}".format(path_on_drive))
    
    for i in progressbar.progressbar(range(length), redirect_stdout=True):
        item = contains[i]
        y.download(item['full'], item['name'])
        
    os.chdir(base_dir)