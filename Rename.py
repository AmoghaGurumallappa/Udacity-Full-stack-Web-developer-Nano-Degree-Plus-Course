import os


def rename():
    file_list = os.listdir(r"D:\Python\Udacity\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is:"+saved_path)
    os.chdir(r"D:\Python\Udacity\prank")
    for file_name in file_list:
        print("old name- " +file_name)
        print("New name-"+ file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename()
