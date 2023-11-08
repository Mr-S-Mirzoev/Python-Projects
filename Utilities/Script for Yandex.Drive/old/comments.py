# Получает общую информацию о диске
#print(y.get_disk_info())

# Выводит содержимое "/some/path"

#path_on_drive = "/CSD_ALL/CSD/Бак/3 курс (2 поток)/5 семестр/Уравнения математической физики/Экзамен/Билеты/1"
#download_folder(path_on_drive, "bilety_umf2")
#images_in_folder("bilety_umf")

#if valid:
#    pdf_from_folder(folder_name + ".pdf", valid)
#else:
#    print("No images found, omiting directory {}".format(folder_name))


#y.download(path_on_drive + "/" + last, last)
"""
# Загружает "file_to_upload.txt" в "/destination.txt"
y.upload("file_to_upload.txt", "/destination.txt")

# То же самое
with open("file_to_upload.txt", "rb") as f:
    y.upload(f, "/destination.txt")

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
y.download("/some-file-to-download.txt", "downloaded.txt")

# Безвозвратно удаляет "/file-to-remove"
y.remove("/file-to-remove", permanently=True)

# Создаёт новую папку "/test-dir"
print(y.mkdir("/test-dir"))
"""