import os

def alpha():
    list_n = os.listdir(r"D:\Python\Udacity\alphabet")
    print(list_n)
    s = os.getcwd()
    print("The Current Working Dir is :"+s)
    os.chdir(r"D:\Python\Udacity\alphabet")
    for f_name in list_n:
        print("old name- " +f_name)
        print("New name-"+ f_name.translate(None, "0123456789"))
        os.rename(f_name, f_name.translate(None,"0123456789"))
    os.chdir(s)
alpha()
