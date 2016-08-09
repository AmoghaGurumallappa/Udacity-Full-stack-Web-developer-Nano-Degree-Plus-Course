import urllib

def read_txt():
    file_open= open("D:\Python\Udacity\Sample_text.txt")
    content = file_open.read()
    print(content)
    file_open.close()
    chk_pro(content)

def chk_pro(txt_to_chk):
    conn=urllib.urlopen("http://www.wdylike.appspot.com/?q="+txt_to_chk)
    out = conn.read()
    #print(out)
    conn.close()
    if "true" in out:
        print("alert")
    elif "false" in out:
        print("ok")
    else:
         print("error")

read_txt()
